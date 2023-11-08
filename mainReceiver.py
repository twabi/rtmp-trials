import cv2
import threading
import sys
import numpy as np
from VideoShow import VideoShow
from VideoRetriever import VideoRetriever
from sinetstream import MessageReader, AsyncMessageReader
import csv
import time
import os
import pickle
import sys


def save_csv(list):
    keys = list[0].keys()
    with open('sinet-receiver-async-1080-30-150.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)

def main():
    start_time = time.time()
    video_retriever = VideoRetriever().start()
    video_shower = VideoShow(video_retriever.frame).start()
    while True:
        if video_retriever.stopped or video_shower.stopped:
            video_shower.stop()
            video_retriever.stop()
            break

        image = video_retriever.frame
        time_now = time.time()
        if time_now - start_time > 150:
            #save_csv(video_retriever.metrics)
            video_retriever.stop()
            video_shower.stop()
            break

        if image is not None:
            video_shower.image = image
                
            

if __name__ == "__main__":
    main()