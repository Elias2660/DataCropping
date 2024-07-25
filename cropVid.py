#%%
import numpy as np
import cv2
#%%
path = "2024-07-07 00:01:39.498363.mp4"
cap = cv2.VideoCapture(path)
fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
print(fps)
print(width)
print(height)
# %%
writer = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (int(width), int(height)))



while True:
    ret, frame = cap.read()
    # set the left part of the frame black
    # set the 
    mask = np.zeros((int(height), int(width), 3), dtype=np.uint8)
    #Flip the mask color to white
    mask.fill(255)
    
    color = (0,0,0)

    start_point_1 = (0,0)
    end_point_1 = (int(width//6), int(height))
    
    mask = cv2.rectangle(mask, start_point_1, end_point_1, color, -1)
    
    
    start_point_2 = (int(width//2), 0)
    end_point_1 = (int(width), int(height))
    mask = cv2.rectangle(mask, start_point_2, end_point_1, color, -1)
    
    result = cv2.bitwise_and(frame,mask)
    if not ret:
        break
    cv2.imshow("Frame", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()