const parent = document.querySelector(".parent");
const children = parent.querySelectorAll(".child");


console.log(children[0]);

for (var i=0; i<children.length; i++) {
    children[i].classList.add("red");
}

son1.textContent = "저는 사실 딸입니다.";
son2.textContent = "저는 아들2 입니다.";
son1.innerHTML = "<b>저는</b>아들입니다.";

const sj = document.createElement("div");
const yena = document.createTextNode("저는 예나입니다.");

Sj.appendChild(yena);
document.body.appendChild(sj);
sj.setAttribute("id", "sj");
sj.setAttribute("class", "parent");
yena.setAttribute("id", "yena");


