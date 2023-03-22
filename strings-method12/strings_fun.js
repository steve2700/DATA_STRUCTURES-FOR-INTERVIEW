// return the word banana in this string 
let txt = "I can eat bananas all day";
let startindex = txt.indexof("banana");
let endindex = startindex + "banana".length;
let banana  = txt.slice(startindex, endindex);
alert(banana);