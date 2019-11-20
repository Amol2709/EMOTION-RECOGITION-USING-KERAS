
# coding: utf-8

# In[4]:


#args={'cascade':'haarcascade_frontalface_default.xml','image':'R1.jpg','model':'checkpoints/epoch_60.hdf5'}


# In[24]:



# coding: utf-8

# In[2]:


# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2


# In[ ]:


# construct the argument parse and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,help="path to where the face cascade resides")
ap.add_argument("-m", "--model", required=True,help="path to pre-trained emotion detector CNN")

ap.add_argument("-i", "--image",help="path to the (optional) image")
args = vars(ap.parse_args())


# In[ ]:


# load the face detector cascade, emotion detection CNN, then define
# the list of emotion labels
detector = cv2.CascadeClassifier(args["cascade"])
model = load_model(args["model"])
EMOTIONS = ["angry", "scared", "happy", "sad", "surprised","neutral"]


frame= cv2.imread(args["image"])

# resize the frame and convert it to grayscale
frame = imutils.resize(frame, width=300)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# initialize the canvas for the visualization, then clone
# the frame so we can draw on it
canvas = np.zeros((220, 300, 3), dtype="uint8")
frameClone = frame.copy()
# detect faces in the input frame, then clone the frame so that
# we can draw on it
rects = detector.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=5, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
    # ensure at least one face was found before continuing
for i in range(0,len(rects)):
    # determine the largest face area
    #rect = sorted(rects, reverse=True,key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
    (fX, fY, fW, fH) = rects[i]
    # extract the face ROI from the image, then pre-process
    # it for the network
    roi = gray[fY:fY + fH, fX:fX + fW]
    roi = cv2.resize(roi, (48, 48))
    roi = roi.astype("float") / 255.0
    roi = img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)
    # make a prediction on the ROI, then lookup the class# label
    preds = model.predict(roi)[0]
    label = EMOTIONS[preds.argmax()]
    # loop over the labels + probabilities and draw them
    for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
        # construct the label text
        text = "{}: {:.2f}%".format(emotion, prob * 100)
        # draw the label + probability bar on the canvas
        w = int(prob * 300)
        cv2.rectangle(canvas, (5, (i * 35) + 5),(w, (i * 35) + 35), (40, 50, 155), -1)
        cv2.putText(canvas, text, (10, (i * 35) + 23),cv2.FONT_HERSHEY_SIMPLEX, 0.45,(55, 25, 5), 2)
    cv2.putText(frameClone, label, (fX, fY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (40, 50, 155), 2)
    cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),(140, 50, 155), 2)
    # show our classifications + probabilities
cv2.imshow("Face", frameClone)
cv2.imshow("Probabilities", canvas)
# cleanup the camera and close any open windows
cv2.waitKey(0)
cv2.destroyAllWindows()

