from threading import Thread
import time
from vidgear.gears import CamGear



class VideoRetriever:
    """
    Class that continuously get frames from the rtmp url
    with a dedicated thread.
    """

    # 133.41.117.94 IP address for the other interface
    def __init__(self):
        self._start_time = time.time()
        self.frame_num = 0

        # CamGear is the library I use to get the frames from the livestream
        self.rtmp_url = "rtmp://172.16.0.13:1935/live/stream" 
        self.stream = CamGear(source=self.rtmp_url).start()
        self.frame = self.stream.read()

        self.stopped = False

    # start thread function here
    def start(self):    
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        
        # get the frames in here
        while not self.stopped:
            
            frame = self.stream.read()
            self.frame = frame

            # Here I am just enumarating the number of frames received
            self.frame_num += 1
            
            if self.stopped:
                break

    def stop(self):
        self.stopped = True