let vinkel = 0
//document.querySelector("audio").play()
function roteraBild() {
    vinkel += 90
    document.querySelector("img").style.transform = "rotate(" + vinkel + "deg)"
}
function spelaLjud() {
    document.querySelector("audio").pause()
}
function visaVideo() {
    document.querySelector(".video-lada").style.display = "block"
}
function aktivera() {
    document.querySelector("h1").textContent = "Sille Walks aktiverad!"
}