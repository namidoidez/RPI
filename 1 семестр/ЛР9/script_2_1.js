let startB = document.getElementById("start");

startB.addEventListener("click", () => {
    for(let i = 1; i <=3; i++) {
        let input = document.getElementById(`data${i}`);
        let output = document.getElementById(`res${i}`); 

        let precision = parseFloat(input.value);
                
        let k = 1;
        let sum = 0;

        for (var term = 1 / (k * k); term > precision; k++, term = 1 / (k * k))
            sum += term;
        
        output.innerText = `Σ = ${sum}, k = ${k}`;
    }
});

let showB = document.getElementById("show");
let codeImg = document.getElementById("code");

showB.addEventListener("click", () => {
    codeImg.style.display=codeImg.style.display === "block" ? "none" : "block";
});