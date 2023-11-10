'''
This python script combines the two threads to get frames from webcam and send them to rtmp
VideoGet and VideoSend classes are used to get and send
'''

from VideoGet import VideoGet
from VideoSend import VideoSend
import csv
import time


# This function I just wrote it. It takes a list of dictionaries and makes a csv from that
def save_csv(list):
    keys = list[0].keys()
    with open('sinet-sender-async-1080-30-150.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)


def sinetSend():

    # start the timer and the threads here
    start_time = time.time()
    video_getter = VideoGet(0).start()
    video_sender = VideoSend(video_getter.frame, video_getter.options["CAP_PROP_FRAME_WIDTH"], video_getter.options["CAP_PROP_FRAME_HEIGHT"]).start()
    while True:
        frame = video_getter.frame
        video_sender.frame = frame

        time_now = time.time()
        if time_now - start_time > 150:
            print(video_sender.metrics)
            #save_csv(video_sender.metrics)
            video_getter.stop()
            video_sender.stop()
            break

def main() :
    sinetSend()
        

if __name__ == "__main__":
    main()

