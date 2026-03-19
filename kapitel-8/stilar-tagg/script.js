// Körs direkt!
document.querySelector('img').style.visibility = "hidden"
document.querySelector('img').style.width = "100px"

// Körs när man klickar!
function styla() {
    document.body.style.backgroundColor = "lightgreen"
    document.querySelector('h1').style.color = "red"
    document.querySelector('h1').style.fontFamily = "courier"
    document.querySelector('h2').style.marginLeft = "300px"
    document.querySelector('p').style.border = "1px solid"
}
// Körs när man klickar!
function fixa() {
    document.querySelector('img').style.visibility = "visible"
}