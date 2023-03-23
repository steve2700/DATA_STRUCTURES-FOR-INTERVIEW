let numbers = [1, 2, 6, 7, 8, 9, 6, 10,];
numbers.sort((a, b) => a - b); // sorting in ascending order
console.log(`This is the ascending of ${numbers}`);

numbers.sort((a, b) => b - a);
console.log(numbers); // sorting in descending order