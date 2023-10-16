#!/usr/bin/node

exports.callMeMoby = function (number, theFunction) {
  for (let d = 0; d < number; d++) {
	  theFunction();
  }
};
