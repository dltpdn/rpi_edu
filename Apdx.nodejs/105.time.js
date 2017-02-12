console.time('check');

var i = 10;
for(var i = 1; i <=10000; i++){
	i*=i;
}
console.log('result : %d', i);
console.timeEnd('check');