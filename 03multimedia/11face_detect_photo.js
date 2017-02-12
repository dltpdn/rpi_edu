var cv = require('opencv');

cv.readImage("children.jpg", function(err, im){
  im.detectObject('haarcascade_frontalface_default.xml', {}, function(err, faces){
    for (var i=0;i<faces.length; i++){
      var face = faces[i]
      im.rectangle([face.x, face.y], [face.width, face.height], [0,255,0], 2);
    }
    im.save('./children_detect.jpg');
  });
})