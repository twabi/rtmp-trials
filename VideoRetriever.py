from threading import Thread
import time
from vidgear.gears import CamGear
from turbojpeg import TurboJPEG, TJFLAG_PROGRESSIVE


jpeg = TurboJPEG()



class VideoRetriever:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    # 133.41.117.94
    def __init__(self):
        self._start_time = time.time()
        self.frame_num = 0
        self.rtmp_url = "rtmp://172.16.0.13:1935/live/stream" 
        self.stream = CamGear(source=self.rtmp_url).start()
        self.frame = self.stream.read()
        self.stopped = False

    def start(self):    
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        
        while not self.stopped:
            
            frame = self.stream.read()
            #buffer = jpeg.decode(frame)
            self.frame = frame
            self.frame_num += 1
            
            if self.stopped:
                break

    def stop(self):
        self.stopped = True