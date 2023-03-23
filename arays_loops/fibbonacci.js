// Write a JavaScript program to print the Fibonacci sequence up to a given number using a for loop.
function Fibonacci(n) {
    let fibo = [0, 1];

    for (let x = 2; x <= n; x++) {
        fibo[x] = fibo[x - 1] + fibo[x- 2];
    }
    return fibo;

}
console.log(Fibonacci(100));