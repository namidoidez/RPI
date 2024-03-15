let startB = document.getElementById("start");

startB.addEventListener("click", () => {
    for(let i = 1; i <=3; i++) {
        let input = document.getElementById(`data${i}`);
        let output = document.getElementById(`res${i}`);
		output.innerText = '';
    
        let words = input.value.split(" ");
		let max = 0;
		
		for (var j = 0; j < words.length; j++)
		{
			if (words[j].length > max)
				max = words[j].length;
		}
			
		for (var j = 0; j < words.length; j++)
		{
			if (words[j].length == max)
				output.innerText += `${j}; `;
		}
    }
});

let showB = document.getElementById("show");
let codeImg = document.getElementById("code");

showB.addEventListener("click", () => {
    codeImg.style.display=codeImg.style.display === "block" ? "none" : "block";
});