let Cars  = new Map();

let dataEnter = document.getElementById("dataEnter");
dataEnter.addEventListener("click", () => {
    Cars.set(document.getElementById(`carBrand`).value, 'Фамилия: ' + document.getElementById(`ownerSurname`).value + ', Номер: ' + document.getElementById(`carNumber`).value + '; ');
});

let carsClear = document.getElementById("carsClear");
carsClear.addEventListener("click", () => {
    Cars.clear();
});

let startB = document.getElementById("start");
startB.addEventListener("click", () => {
    for(let i = 1; i <=3; i++) {
        let input = document.getElementById(`data${i}`);
        let output = document.getElementById(`res${i}`);
    
        let carBrand = input.value;
        let value = Cars.get(carBrand);
        if (value != undefined)
            output.innerText = `${value}`;
        else
            output.innerText = ``;
    }
});

let showB = document.getElementById("show");
let codeImg = document.getElementById("code");
showB.addEventListener("click", () => {
    codeImg.style.display=codeImg.style.display === "block" ? "none" : "block";
});

