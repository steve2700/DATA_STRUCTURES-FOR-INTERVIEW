/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {
        
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
 var compose = function(functions) {
  return function(x) {
    if (functions.length === 0) {
      return x; // identifying the function
    }

    var result = functions[functions.length - 1](x); // Start with the rightmost function

    for (var i = functions.length - 2; i >= 0; i--) {
      result = functions[i](result);
    }

    return result;
  };
};
