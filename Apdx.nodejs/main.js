var module = require('./module1');
module();

var module2 = require('./module2');
console.log(module2.msg);
console.log(module2.sum(2, 4));
console.log(module2.avg(2, 4));
