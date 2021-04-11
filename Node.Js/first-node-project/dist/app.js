"use strict";
console.log('frontend code running');
var title = document.getElementById('title');
var button = document.getElementById('button');
if (button) {
    button.onclick = function () {
        if (title) {
            title.innerText = 'Titolo cambiato da TypeScript';
        }
    };
}
