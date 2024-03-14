let startB = document.getElementById("start");

startB.addEventListener("click", () => {
    for(let i = 1; i <=3; i++) {
        let input = document.getElementById(`data${i}`);
        let output = document.getElementById(`res${i}`);
		
        let cathets = input.value.split(",").map(el => parseFloat(el));
		
		if (cathets[0]/cathets[2] == cathets[1]/cathets[3] || cathets[0]/cathets[3] == cathets[1]/cathets[2] && cathets.length != 4)
			output.innerText = 'Треугольники являются подобными';
		else
			output.innerText = 'Треугольники не являются подобными';
    }
});

let showB = document.getElementById("show");
let codeImg = document.getElementById("code");

showB.addEventListener("click", () => {
    codeImg.style.display=codeImg.style.display === "block" ? "none" : "block";
});

