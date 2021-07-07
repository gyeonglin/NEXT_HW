const title = document.getElementById("title");
title.innerText = '자스 어려워요';
const divs = document.querySelectorAll('div');

for (let i = 0; i<divs.length; i++) {
    divs[i].innerText = '앙뇽하슈?';
    divs[i].style.color = 'blue';
    divs[i].style.fontSize = `${(i+1)*10}px`;
}

console.log(divs)
