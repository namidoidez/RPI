let startB = document.getElementById("start");

startB.addEventListener("click", () => {
    for(let i = 1; i <=3; i++) {
        let input = document.getElementById(`data${i}`);
        let output = document.getElementById(`res${i}`);
    
        let nums = input.value.split(" ").map(el => parseFloat(el));
        let sum = 0;

        for (var j = 0; j < nums.length; j++)
        {
            if (nums[j] % 3 == 0)
                nums[j] *= j;
            sum += nums[j];
        }
        let avgValue = sum / nums.length;

        output.innerText = `${avgValue}`;
    }
});

let showB = document.getElementById("show");
let codeImg = document.getElementById("code");

showB.addEventListener("click", () => {
    codeImg.style.display=codeImg.style.display === "block" ? "none" : "block";
});