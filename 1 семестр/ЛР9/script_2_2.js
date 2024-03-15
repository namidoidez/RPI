let startB = document.getElementById("start");

startB.addEventListener("click", () => {
    for(let i = 1; i <=3; i++) {
        let input = document.getElementById(`data${i}`);
        let output = document.getElementById(`res${i}`);

        let words = input.value.split(" ");
        let a = parseFloat(words[0]);
        let b = parseFloat(words[1]);
        let n = parseInt(words[2]);
        let h = (b - a) / n;
        let res = "";

        if (a < b)
        {
            var j = 0;
            while (j < n)
            {
                x = a + j * h;
                y = x * Math.abs(x + 1);
                res += (`(${x}; ${y}), `);
                j++;
            }
        }

        output.innerText = `${res}`;
    }
});

let showB = document.getElementById("show");
let codeImg = document.getElementById("code");

showB.addEventListener("click", () => {
    codeImg.style.display=codeImg.style.display === "block" ? "none" : "block";
});

