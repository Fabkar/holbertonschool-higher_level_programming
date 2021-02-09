#!/usr/bin/ node
/* function that returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  let clons = 0;
  for (let i = 0; i < list.length; i++) { // check all list
    if (list[i] === searchElement) clons += 1; // fetching the clon
  }
  return (clons);
};
