window.onload = function onLoad() {
    document.getElementById('button_1').onclick = function() {
        document.getElementById('nav_menu').style.backgroundColor = 'green';
    };

    document.getElementById('button_2').onclick = function() {
        document.getElementById('nav_menu').style.backgroundColor = 'red';
    };

    document.getElementById('button_3').onclick = function() {
        document.getElementById('nav_menu').style.backgroundColor = 'black';
    };

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

    username.onkeyup = function() {
        let username = document.getElementById('id_username');
        change(username.value, elem);
    };
};