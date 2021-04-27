let btnRandom = document.querySelector('button');
let result = document.querySelector('h1');

let users = ['Blues', 'Hip-Hop', 'Hip-Hop', 'Hip-Hop', 'Hip-Hop', 'Classical', 'Blues', 'Blues', 'Blues', 'Hip-Hop', 'Country', 'Hip-Hop', 'Disco', 'Pop', 'Pop', 'Pop', 'Pop', 'Pop', 'Hip-Hop', 'Pop',  'Jazz', 'Metal', 'Pop', 'Rock', 'Pop', 'Pop', 'Hip-Hop', 'Hip-Hop'];

function getRandomNumber(min, max) {
    let step1 = max - min + 1;
    let step2 = Math.random() * step1;
    let result = Math.floor(step2) + min;

    return result;
}

btnRandom.addEventListener('click', () => {
    let index = getRandomNumber(0, users.length-1);
    result.innerText = users[index];
});