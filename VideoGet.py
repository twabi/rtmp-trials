from threading import Thread
import time
from vidgear.gears import CamGear
from turbojpeg import TurboJPEG


jpeg = TurboJPEG()

class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, src=0):
        self._start_time = time.time()
        self.frame_num = 0

        # these are options for the webcam. You can change resolution and other variables from here. Check the CamGear docs for more
        self.options = {
                "THREADED_QUEUE_MODE": True,
                "CAP_PROP_FRAME_WIDTH": 640, # resolution 320x240
                "CAP_PROP_FRAME_HEIGHT": 360,
                "CAP_PROP_FPS": 30, # framerate 60fps
            }
        self.stream = CamGear(source=0, logging=True, **self.options).start()
        self.frame = self.stream.read()
        self.stopped = False

    def start(self):    
        Thread(target=self.get, args=()).start()
        return self

    # get the frames here
    def get(self):
        
        while not self.stopped:
            
            frame = self.stream.read()
            self.frame = frame
            self.frame_num += 1
            
            if self.stopped:
                break

    def stop(self):
        self.stopped = True