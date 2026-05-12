import os
import subprocess
import json
import requests
import datetime

# Konfigurera DeepSeek
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    print("Inget DEEPSEEK_API_KEY hittades. Avbryter.")
    exit(1)

DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-pro")

def get_git_info():
    # Hämta commit-meddelande och diff för senaste commiten
    commit_msg = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8')
    diff = subprocess.check_output(['git', 'diff', 'HEAD~1', 'HEAD']).decode('utf-8', errors='ignore')
    files_changed = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD']).decode('utf-8').splitlines()
    
    # Identifiera vilka mappar som ändrats (ignorera rot-filer och .github-mappen)
    folders = set()
    for f in files_changed:
        parts = f.split('/')
        # Ignorera filer i roten, filer i .github, och filer i mappar vars namn börjar med '.'
        if '/' in f and not any(part.startswith('.') for part in parts[:-1]):
            folders.add(os.path.dirname(f))
    return commit_msg, diff, list(folders)

def read_file(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def write_file(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def call_deepseek(prompt):
    """Anropa DeepSeek v4 Pro API"""
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95
    }
    
    response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)
    response.raise_for_status()
    
    return response.json()["choices"][0]["message"]["content"]

def main():
    commit_msg, diff, folders = get_git_info()
    
    if not folders:
        print("Inga lektionsmappar ändrades. Behöver inte generera dagböcker.")
        # Vi kan ändå vilja uppdatera history.md om rotfiler ändrats, men oftast är de kopplade.
        if not diff:
            return

    history_content = read_file('history.md')
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
    Du är en pedagogisk assistent för en gymnasielärare i webbutveckling/programmering.
    Din uppgift är att skriva dokumentation baserat på lärarens senaste kod-commit. Svara ENDAST med ett giltigt JSON-objekt, ingen annan text runtom.

    Här är dagens datum: {today}
    Här är commit-meddelandet: {commit_msg}
    Här är kod-ändringarna (git diff):
    {diff}

    Här är nuvarande innehåll i history.md:
    {history_content}

    Dina uppgifter för JSON-objektet som ska returneras:
    1. "dagbok_updates": En array av objekt med "folder" och "content". För varje mapp som ändrats, skriv en dagbok.md. 
       - Ton: Neutral och pedagogisk ("I den här lektionen gick vi igenom...").
       - Format: Markdown
       - Fokus på lärande och innehål, inte tekniska detaljer
    2. "history_update": Ett stycke som sammanfattar dagens arbete och lägger till det i history.md.

    Här är mapparna som ändrats: {', '.join(folders)}

    Returnera ENDAST JSON utan formatering runtom.
    """

    try:
        response = call_deepseek(prompt)
        result = json.loads(response)
        
        # Uppdatera dagböcker
        for update in result.get("dagbok_updates", []):
            dagbok_path = f"{update['folder']}/dagbok.md"
            write_file(dagbok_path, update["content"])
            print(f"✓ Uppdaterad: {dagbok_path}")
        
        # Uppdatera history.md
        if result.get("history_update"):
            new_history = history_content + f"\n\n## {today}\n{result['history_update']}"
            write_file('history.md', new_history)
            print("✓ Uppdaterad: history.md")
        
        print("Dokumentation genererad med DeepSeek v4 Pro!")
    
    except json.JSONDecodeError as e:
        print(f"Fel vid JSON-tolkning: {e}")
        print(f"Svar från DeepSeek: {response}")
        exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Fel vid anrop till DeepSeek API: {e}")
        exit(1)

if __name__ == "__main__":
    main()
