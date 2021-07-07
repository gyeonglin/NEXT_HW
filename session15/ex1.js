let $ulElement = document.querySelector('ul');
let $modal = document.getElementById('myModal');
let $modalBtn = document.getElementById('myModalBtn');
let $modalClose = document.getElementsByClassName('modal-close')[0];

$modalBtn.onclick = (event) => {
    $modal.style.display = "block";
}

$modalClose.onclick = () => {
    $modal.style.display = "none";
}

$ulElement.addEventListener("click", (event) => {
    let $target = event.target;
    if($target.classList.contains('close')){
        let $parentTarget = $target.parentElement;
        $parentTarget.style.display = "none";
        console.dir($parentTarget)
        console.log($parentTarget.childNodes)
        let $value = $parentTarget.childNodes[0].textContent
        console.log($value)
        deleteTodoList("todo", $value)
    }
    $target.classList.toggle('checked');
})



function newElement() {
    //let $liElement = document.createElement("li");
    const inputValue = document.getElementById("myInput").value;
    if (inputValue === '') {
        alert("You must write something!");
    } else {
        $ulElement.insertAdjacentHTML('Beforeend', `<li><span>${inputValue}</span><span class = "close">\u00D7</span></li>`);
        console.log(inputValue);
        addTodoList("todo", inputValue);
    }
    document.getElementById("myInput").value = "";
}

function init() {
    let todolist = getTodoList("todo");
    for (let i=0; i< todolist.length ; i++){
        $ulElement.insertAdjacentHTML('Beforeend', `<li><span>${todolist[i]}</span><span class = "close">\u00D7</span></li>`);
    }

}

function getTodoList(key) {    
    if (localStorage.getItem(key)){
        return localStorage.getItem(key).split(',')
    }
    else {
        return []
    }
    
}

function addTodoList(key, value) {
    let todolist = getTodoList(key);
    todolist.push(value);
    localStorage.setItem(key, todolist);
}

function deleteTodoList(key,value) {
    let todolist = getTodoList(key);
    for (i = 0; i < todolist.length; i++){
        if (todolist[i] === value) {
            todolist.splice(i, 1);
            break;
        }
    }
    localStorage.setItem(key, todolist);
}

init()

