from threading import Thread
import cv2
import numpy as np
import threading


class VideoShow:
    '''
    This class shows captured frames using cv2. Nothing extreme here.
    '''
    def __init__(self, image=None):
        self.image = image
        self.stopped = False
        self.lock = threading.Lock()

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def update_image(self, image):
        with self.lock:
            self.image = image

    def show(self):
        window_name = "Live video"

        while not self.stopped:
            with self.lock:
                if isinstance(self.image, np.ndarray):
                    cv2.imshow(window_name, self.image)
                    
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

            if self.stopped:
                break
    
    def stop(self):
        self.stopped = True
        cv2.destroyAllWindows()
