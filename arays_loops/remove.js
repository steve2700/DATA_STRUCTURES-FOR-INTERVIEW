let numbers = [10, 20, 30, 40, 50];
numbers.splice(2, 1)// the splice method remove 0ne number from index 2
console.log(numbers);
// using the filter 
numbers = numbers.filter(num => num !==50);
console.log(numbers);
numbers = [...numbers.slice(0, 2), ...numbers.slice(3)];
console.log(numbers);  // output: [10, 20, 40, 50]

numbers = numbers.filter(num => num!==20);
console.log(numbers);
numbers = numbers.splice(3, 2);
console.log(numbers);