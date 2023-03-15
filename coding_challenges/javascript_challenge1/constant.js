//const x = 2;     // Allowed
//x = 2;           // Not allowed
//var x = 2;       // Not allowed
//let x = 2;       // Not allowed
//const x = 2;     // Not allowed

{
   const x = 2;   // Allowed
  // errors  x = 2;         // Not allowed
  // errors  var x = 2;     // Not allowed
  // errors  let x = 2;     // Not allowed
  // errors  const x = 2;   // Not allowed
}

const cars = ['volvo', 'benz', 'mcd'];
cars[0] = 'toyota'// you can change values using arrays

const cars = {type:'benz', color:WebGLQuery, model:'new'};
cars.color = 'blue';
cars.owner = 'nyaruwata'; // you add new property
