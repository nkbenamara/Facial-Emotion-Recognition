import numpy as np
from keras.models import load_model
import cv2 as cv
import time

num_frames=1
font = cv.FONT_HERSHEY_SIMPLEX

emotions=['Angry', 'Disgust','Afraid', 'Happy', 'Sad', 'Surprise', 'Neutral']
modelA=load_model('./pretrained_models/fer_best_models/ModelA_66,39_-1,06val_68,68_-1,02test.h5')
modelB=load_model('./pretrained_models/fer_best_models/ModelB_65,75_-1,07val_67,48_-1,00test.h5')
modelC=load_model('./pretrained_models/fer_best_models/ModelC_65,51_-1,03val_68,15_-0.97test.h5')
modelD=load_model('./pretrained_models/fer_best_models/ModelD_67,26_-1,07val_68,15_-0.99test.h5')

faceCascade = cv.CascadeClassifier('./pretrained_models/face_detection/haarcascade_frontalface_default.xml')

video_capture = cv.VideoCapture(0)

while True:
    
    start = time.time()
    ret, frame = video_capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        
        roi_gray = gray[y:y + h, x:x + w]
        
        emotion_to_predict= cv.resize(roi_gray,(48,48),interpolation=cv.INTER_AREA)
        emotion_to_predict = emotion_to_predict/ 255.0
        emotion_to_predict =np.expand_dims(np.array(emotion_to_predict),-1)
        emotion_to_predict =np.expand_dims(np.array(emotion_to_predict),0)
        emotion=modelA.predict(emotion_to_predict)
        index_emotion=np.argmax(emotion[0], axis=0)
        
        

        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 4)
        cv.putText(frame, "Emotion :"+emotions[index_emotion], (7, 70), font, 1, (200, 0, 0), 1, cv.LINE_AA)

    end = time.time()
    seconds = end - start
    fps  = num_frames / seconds
    
    cv.putText(frame, "FPS: " + str(round(fps)), (7,50), font, 1, (200, 0, 0))
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break