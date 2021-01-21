colors = {
    button_1: 'green',
    button_2: 'red',
    button_3: 'black'
}

for (let prop in colors) {
    document.getElementById(prop).addEventListener('click',
     function() {
    document.getElementById('nav_menu').style.backgroundColor = colors[prop];
    });
}

let username = document.getElementById('id_username');

let elem = document.getElementsByClassName('form-group row')[0]
    .getElementsByClassName('col-md-9')[0]
    .appendChild(
        document.createElement('p')
        );

function change(value, elem) {
    elem.style.backgroundColor = "green";
    elem.innerText = value.replaceAll(/[.,'"\/:;\s\\%|]/g, '');
}

username.addEventListener('keyup',
    function() {
    let username = document.getElementById('id_username');
    change(username.value, elem);
    },
);