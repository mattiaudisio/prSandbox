console.log('frontend code running')

const title = document.getElementById('title');
const button = document.getElementById('button');

if(button){
    button.onclick = () => {
        if(title){
            title.innerText ='Titolo cambiato da TypeScript';
        }    
    };
}

