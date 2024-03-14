let startB = document.getElementById("start");

startB.addEventListener("click", () => {
	for(let i = 1; i <=3; i++) {
        let input = document.getElementById(`data${i}`);
        let output = document.getElementById(`res${i}`);
		
		points = input.value.split(";");
		pointA = points[0].split(",").map(el => parseInt(el));
		pointB = points[1].split(",").map(el => parseInt(el));;
		length = Math.sqrt(Math.pow(pointA[0] - pointB[0], 2) + Math.pow(pointA[1] - pointB[1], 2));
    
        output.innerText = `${length}`;
    }
});

let showB = document.getElementById("show");
let codeImg = document.getElementById("code");

showB.addEventListener("click", () => {
    codeImg.style.display=codeImg.style.display === "block" ? "none" : "block";
});