exports.plus = function(i, j){
	console.log("module plus(%d, %d)", i, j );
	return i + j;
};

exports.sum = function(){
	var sum = 0;
	for(var i=0; i<arguments.length; i++){
		sum+=arguments[i];
	}
	return sum;
};