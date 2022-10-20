import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import os
from scipy.stats import kurtosis
from scipy.stats import skew

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

import statistics

label=[]
landmarks11xS = []
landmarks11yS = []
landmarks12xS = []
landmarks12yS = []
landmarks14xS = []
landmarks14yS = []
landmarks16xS = []
landmarks16yS = []
maxlistxS = []
minlistxS = []
meanlistxS = []
medianlistxS = []
stdevlistxS = []
modelistxS = []
coefvarxS = []
peakpeakxS =[]
skewxS = []
interquartilexS = []
kurtosisxS = []
sqrtxS = []
powerxS = []

maxlistyS = []
minlistyS = []
meanlistyS = []
medianlistyS = []
stdevlistyS = []
modelistyS = []
coefvaryS = []
peakpeakyS =[]
skewyS = []
interquartileyS = []
kurtosisyS = []
sqrtyS = []
poweryS = []

activities = ['test']
def getlandmarks(activity,path):
        cap = cv2.VideoCapture(path)
        landmarks11xS = []
        landmarks11yS = []
        landmarks12xS = []
        landmarks12yS = []
        landmarks14xS = []
        landmarks14yS = []
        landmarks16xS = []
        landmarks16yS = []
        print(path)
        while True:
            success, img = cap.read()
            success, frames = cap.read()
            try:
                imgRGB = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
            except:
                break
            results = pose.process(imgRGB)
            if results.pose_landmarks:
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    if id == 28:
                        landmarks11xS.append(lm.x)
                        landmarks11yS.append(lm.y)
                    if id == 26:
                        landmarks12xS.append(lm.x)
                        landmarks12yS.append(lm.y)
                    if id == 27:
                        landmarks14xS.append(lm.x)
                        landmarks14yS.append(lm.y)
                    if id == 31:
                        landmarks16xS.append(lm.x)
                        landmarks16yS.append(lm.y)
            # cv2.imshow("Image", img)
            # cv2.waitKey(1)
        cap.release()
        cv2.destroyAllWindows()
        maxlistxS.extend([max(landmarks11xS), max(landmarks12xS), max(landmarks14xS), max(landmarks16xS)])
        maxlistyS.extend([max(landmarks11yS), max(landmarks12yS), max(landmarks14yS), max(landmarks16yS)])
        meanlistxS.extend(
            [statistics.mean(landmarks11xS), statistics.mean(landmarks12xS), statistics.mean(landmarks14xS),
             statistics.mean(landmarks16xS)])
        meanlistyS.extend(
            [statistics.mean(landmarks11yS), statistics.mean(landmarks12yS), statistics.mean(landmarks14yS),
             statistics.mean(landmarks16yS)])
        minlistxS.extend([min(landmarks11xS), min(landmarks12xS), min(landmarks14xS), min(landmarks16xS)])
        minlistyS.extend([min(landmarks11yS), min(landmarks12yS), min(landmarks14yS), min(landmarks16yS)])
        medianlistxS.extend(
            [statistics.median(landmarks11xS), statistics.median(landmarks12xS), statistics.median(landmarks14xS),
             statistics.median(landmarks16xS)])
        medianlistyS.extend(
            [statistics.median(landmarks11yS), statistics.median(landmarks12yS), statistics.median(landmarks14yS),
             statistics.median(landmarks16yS)])
        stdevlistxS.extend(
            [statistics.stdev(landmarks11xS), statistics.stdev(landmarks12xS), statistics.stdev(landmarks14xS),
             statistics.stdev(landmarks16xS)])
        stdevlistyS.extend(
            [statistics.stdev(landmarks11yS), statistics.stdev(landmarks12yS), statistics.stdev(landmarks14yS),
             statistics.stdev(landmarks16yS)])
        modelistxS.extend(
            [statistics.mode(landmarks11xS), statistics.mode(landmarks12xS), statistics.mode(landmarks14xS),
             statistics.mode(landmarks16xS)])
        modelistyS.extend(
            [statistics.mode(landmarks11yS), statistics.mode(landmarks12yS), statistics.mode(landmarks14yS),
             statistics.mode(landmarks16yS)])
        interquartilexS.extend([np.percentile(landmarks11xS, 75) - np.percentile(landmarks11xS, 25),
                                np.percentile(landmarks12xS, 75) - np.percentile(landmarks12xS, 25),
                                np.percentile(landmarks14xS, 75) - np.percentile(landmarks14xS, 25),
                                np.percentile(landmarks16xS, 75) - np.percentile(landmarks16xS, 25)])
        interquartileyS.extend([np.percentile(landmarks11yS, 75) - np.percentile(landmarks11yS, 25),
                                np.percentile(landmarks12yS, 75) - np.percentile(landmarks12yS, 25),
                                np.percentile(landmarks14yS, 75) - np.percentile(landmarks14yS, 25),
                                np.percentile(landmarks16yS, 75) - np.percentile(landmarks16yS, 25)])
        peakpeakxS.extend([max(landmarks11xS) - min(landmarks11xS), max(landmarks12xS) - min(landmarks12xS),
                           max(landmarks14xS) - min(landmarks14xS), max(landmarks16xS) - min(landmarks16xS)])
        peakpeakyS.extend([max(landmarks11yS) - min(landmarks11yS), max(landmarks12yS) - min(landmarks12yS),
                           max(landmarks14yS) - min(landmarks14yS), max(landmarks16yS) - min(landmarks16yS)])
        kurtosisxS.extend(
            [kurtosis(landmarks11xS), kurtosis(landmarks12xS), kurtosis(landmarks14xS), kurtosis(landmarks16xS)])
        kurtosisyS.extend(
            [kurtosis(landmarks11yS), kurtosis(landmarks12yS), kurtosis(landmarks14yS), kurtosis(landmarks16yS)])



for i in range(len(activities)):
    for file in os.listdir("test"):
        path = "test" + '/' + file
        landmarks11xS = []
        landmarks11yS = []
        landmarks12xS = []
        landmarks12yS = []
        landmarks14xS = []
        landmarks14yS = []
        landmarks16xS = []
        landmarks16yS = []
        getlandmarks(activities[i],path)
label.extend(['juggle','juggle','juggle','juggle','pass','pass','pass','pass','drill','drill','drill','drill'])

df = pd.DataFrame({
'max-xS':maxlistxS,
'max-yS':maxlistyS,
'min-xS':minlistxS,
'min-yS': minlistyS,
'mean-xS':meanlistxS,
'mean-yS':meanlistyS,
'median-xS':medianlistxS,
'median-yS':medianlistyS,
'mode-xS':modelistxS,
'mode-yS':modelistyS,
'stdv-xS':stdevlistxS,
'stdv-yS':stdevlistyS,
'peaktopeak-xS': peakpeakxS,
'peaktopeak-yS': peakpeakyS,
'interquart-xS': interquartilexS,
'interquart-yS': interquartileyS,
'kurtosis-xS': kurtosisxS,
'kurtosis-yS': kurtosisyS,
'Label': label
})
df.to_csv('Test.csv')

#bbleef or dbleef