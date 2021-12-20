import picamera
import time

path = '/home/pi/src3/06_multimedia'

camera = picamera.PiCamera()

try:
  camera.resolution = (640, 480)
  camera.start_preview()
  time.sleep(3)
  camera.rotation = 0
  while True:
    now_str = time.strftime("%Y%m%d_%H%M%S")
    print("photo:1, video:2, exit:9")
    cmd = input()
    if cmd == '1':
      camera.capture('%s/photo_%s.jpg' % (path, now_str))
    elif cmd == '2':
      camera.start_recording('%s/video_%s.h264' % (path, now_str))
      time.sleep(5)
      camera.stop_recording()
    elif cmd == '9':
      break
    else:
      print("It's wrong command")

finally:
  camera.stop_preview()