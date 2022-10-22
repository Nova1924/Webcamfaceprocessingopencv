from multiprocessing import Process
import time
from itertools import count
from multiprocessing import Process

import cv2

# Opens the inbuilt camera of laptop to capture video.
webCam = cv2.VideoCapture(0)
currentframe = 0

while (True):
    success, frame = webCam.read()

    # Save Frame by Frame into disk using imwrite method
    cv2.imshow("Output", frame)
    cv2.imwrite('Frame' + str(currentframe) + '.jpg', frame)
    currentframe += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



def inc_forever():
    print('Starting function inc_forever()...')
    while True:
        time.sleep(1)
        print(next(counter))
def return_zero():
    print('Starting function return_zero()...')
    return 0
if __name__ == '__main__':
    # counter is an infinite iterator
    counter = count(0)
    p2 = Process(target=return_zero, name='Process_return_zero')
    p2.start()
    p2.join(timeout=2)
    p2.terminate()

if p2.exitcode == 0:
        print(f'{p2} is luck and finishes in 5 seconds!')
        webCam.release()
        cv2.destroyAllWindows()

webCam.release()
cv2.destroyAllWindows()
