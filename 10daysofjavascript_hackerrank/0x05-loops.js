'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    let consonants = '';

    // Loop through each character of the string
    for (let i = 0; i < s.length; i++) {
        const char = s[i].toLowerCase();

        // Check if the character is a vowel or a consonant
        if (vowels.includes(char)) {
            console.log(char);
        } else {
            consonants += char;
        }
    }

    // Print the consonants
    for (let i = 0; i < consonants.length; i++) {
        console.log(consonants[i]);
    }
}



function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
