window.onload=function(){
    const b = document.querySelector(".vertical-menu-button");
    const k = document.querySelector(".X");

    b.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        document.querySelector(".vertical-menu").classList.toggle("activate");
    });

    k.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        document.querySelector(".vertical-menu").classList.toggle("activate");
    });
}