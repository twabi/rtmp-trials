from VideoShow import VideoShow
from VideoRetriever import VideoRetriever
import csv
import time


# This function I just wrote it. It takes a list of dictionaries and makes a csv from that
def save_csv(list):
    keys = list[0].keys()
    with open('sinet-receiver-async-1080-30-150.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)

def main():
    start_time = time.time() # start the clock time - You can use another library if you feel like so

    # start the thread to get frames and then subsequently show them
    video_retriever = VideoRetriever().start()
    video_shower = VideoShow(video_retriever.frame).start()

    # main loop to continously update thread variables
    while True:
        if video_retriever.stopped or video_shower.stopped:
            video_shower.stop()
            video_retriever.stop()
            break

        image = video_retriever.frame
        time_now = time.time() # a new timestamp to compare with the initial one outside the loop

        # stop the loop after the required number of seconds has elapsed
        if time_now - start_time > 150:
            #save_csv(video_retriever.metrics)
            video_retriever.stop()
            video_shower.stop()
            break

        if image is not None:
            video_shower.image = image
                
            

if __name__ == "__main__":
    main()