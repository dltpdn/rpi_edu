var cv = require('opencv');

var camera = new cv.VideoCapture(0);
camera.setWidth(320);
camera.setHeight(240);

console.log('press any key to capture.');
process.stdin.on('data', function(){
    camera.read(function(err, im) {
        if (err) throw err;
        im.save('capture.jpg')
        console.log('captured successfully.');
        console.log('press any key to capture.');
      });
});
