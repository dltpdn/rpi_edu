import cv2

video_file = "./BigBuck.m4v" 

cap = cv2.VideoCapture(video_file) 
fps = cap.get(cv2.CAP_PROP_FPS) 
delay = int(1000/fps)

while cap.isOpened():           
    ret, img = cap.read()      
    if ret:                    
        cv2.imshow(video_file, img) 
        if cv2.waitKey(delay) == 27: #esc to exit
            break
    else:
        print('no frame.')
        break                   
else:
    print("can't open video.")  
cap.release()                   
cv2.destroyAllWindows()