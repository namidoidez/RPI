let startB = document.getElementById("start");

startB.addEventListener("click", () => {
    for(let i = 1; i <=3; i++) {
        let input = document.getElementById(`data${i}`);
        let output = document.getElementById(`res${i}`);

        n = parseInt(input.value);

        output.innerText = `${FibonacciNumbers(0, 1, n)}`;
    }
});

function FibonacciNumbers(num1, num2, n)
{
    if (n != 0)     
    {
        [num1, num2] = [num2, num1 + num2];
        return FibonacciNumbers(num1, num2, n - 1);
    }
    else
        return num1;
}

let showB = document.getElementById("show");
let codeImg = document.getElementById("code");

showB.addEventListener("click", () => {
    codeImg.style.display=codeImg.style.display === "block" ? "none" : "block";
});

