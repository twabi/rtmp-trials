from threading import Thread
import cv2
from turbojpeg import TurboJPEG
from vidgear.gears import WriteGear

jpeg = TurboJPEG()

class VideoSend:
    """
    Class that continuously sends a frame to rtmp url using a dedicated thread.
    """

    def __init__(self, frame=None, width=0, height=0):
        self.frame = frame
        self.metrics = []
        self.rtmp_url = "rtmp://172.16.0.13:1935/live/stream"
        self.stopped = False
        self.width = width
        self.height = height

    def start(self):
        Thread(target=self.send, args=()).start()
        return self

    def send(self):

        # params for the writer object
        output_params = {
            "-preset:v": "veryfast",
            "-g": 60,
            "-keyint_min": 60,
            "-sc_threshold": 0,
            "-bufsize": "2500k",
            "-f": "flv",
        }

        # The writer object from WriteGear writes frames to a given server. here we initialize the writer
        writer = WriteGear(
            output=self.rtmp_url,
            compression_mode=True,
            logging=True,
            **output_params
        )

        # loop and keep sending frames
        while (not self.stopped) and (self.frame is not None):
            writer.write(self.frame)
            print("Sent")


            if self.stopped:
                break

            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True