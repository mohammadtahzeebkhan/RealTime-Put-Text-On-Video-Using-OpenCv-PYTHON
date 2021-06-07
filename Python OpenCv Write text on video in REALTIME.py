# Python program to write 
# text on video 
import cv2
import pyautogui
  
font_size=1.5
x=0
y=0
cap = cv2.VideoCapture('video.mp4')
while(True): 
      
    # Capture frames in the video 
    ret, frame = cap.read() 
  
    # describe the type of font 
    # to be used. 
    font = cv2.FONT_HERSHEY_SIMPLEX 
  
    # Use putText() method for 
    # inserting text on video 
    cv2.putText(frame,  
                       'paradise_hope',  
                                       (x, y),  #loctoin of text
                                     font,# font famliy
                                    font_size,#font size
                             (0, 255, 255),  #color of font
                              5,#thikness of font  
                             cv2.LINE_4) 
  
    # Display the resulting frame 
    cv2.imshow('video', frame)
    
   
    
    # creating 'q' as the quit  
    # button for the video

    #zoom texting press z in 
    if cv2.waitKey(1) & 0xFF == ord('z'):
        font_size=font_size+1
   
   #zoom texting press O out
    if cv2.waitKey(1) & 0xFF == ord('o'):
        font_size=font_size-1    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
##    p,x=pyautogui.position()
##    print(p)
##    print(x)

    # position text press p and move mouse
    if cv2.waitKey(1) & 0xFF == ord('p'):
        x,y=pyautogui.position()
        print(x)
        print(y)
    
  
# release the cap object 
cap.release() 
# close all windows 
cv2.destroyAllWindows() 
