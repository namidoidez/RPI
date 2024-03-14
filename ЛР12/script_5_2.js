let startB = document.getElementById("start");

startB.addEventListener("click", () => {
    for(let i = 1; i <=3; i++) {
        let input = document.getElementById(`data${i}`);
        let output = document.getElementById(`res${i}`);
    
        let matrix = input.value.split(";").map(els => els.split(",").map(el => parseFloat(el)));
        let n = matrix.length;
        let mainDiagonalMax = 0;
        let mainDiagonalMin = Number.MAX_VALUE;
        let antiDiagonalMax = 0;
        let antiDiagonalMin = Number.MAX_VALUE;

        for (var j = 0; j < n; j++)
        {
            if (matrix[j][j] > mainDiagonalMax)
                mainDiagonalMax = matrix[j][j];
            if (matrix[j][j] < mainDiagonalMin)
                mainDiagonalMin = matrix[j][j];

            if (matrix[j][n - j - 1] > antiDiagonalMax)
                antiDiagonalMax = matrix[j][n - j - 1];
            if (matrix[j][n - j - 1] < antiDiagonalMin)
                antiDiagonalMin = matrix[j][n - j - 1];
        }

        for (var j = 0; j < n; j++) {
            if ((matrix[j][j] != mainDiagonalMax) && (matrix[j][j] != mainDiagonalMin))
                matrix[j][j] = 0;

            if ((matrix[j][n - j - 1] != antiDiagonalMax) && (matrix[j][n - j - 1] != antiDiagonalMin))
                matrix[j][n - j - 1] = 0;
        }

        output.innerText = `${[matrix.map(el => "[" + el.join(", ") + "]")].join(";")}`;
    }
});

let showB = document.getElementById("show");
let codeImg = document.getElementById("code");

showB.addEventListener("click", () => {
    codeImg.style.display=codeImg.style.display === "block" ? "none" : "block";
});
