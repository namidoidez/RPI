let startB = document.getElementById("start");

startB.addEventListener("click", () => {
    for(let i = 1; i <=3; i++) {
        let input = document.getElementById(`data${i}`);
        let output = document.getElementById(`res${i}`);
    
        coefficients = input.value.split(" ").map(el => parseFloat(el));
        
        output.innerText = `${uTest(coefficients[0], coefficients[1], coefficients[2])}`;
    }
});

function uTest(x, y, z) {
    return (Math.max(x, y) + Math.max(x + y, z)) / (Math.pow(Math.max(0.5, x + z), 2));
}

let showB = document.getElementById("show");
let codeImg = document.getElementById("code");

showB.addEventListener("click", () => {
    codeImg.style.display=codeImg.style.display === "block" ? "none" : "block";
});