import os
import datetime
import time
import subprocess

def video_rec():
    file_path = "Video/"
    file_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S.mp4')
    live_video = subprocess.Popen("ffmpeg -rtsp_transport tcp -i \"rtsp://fms:fms12345@192.168.1.250:554/cam/realmonitor?channel=1&subtype=0\" -an -vcodec copy {}".format(os.path.join(file_path,file_name)),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    time.sleep(11)
    live_video.stdin.write('q'.encode("GBK"))
    live_video.communicate()

def take_image():
    file_path = "Image/"
    file_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S.jpeg')
    img = subprocess.Popen("ffmpeg -rtsp_transport tcp -i \"rtsp://fms:fms12345@192.168.1.250:554/cam/realmonitor?channel=1&subtype=0\" -vframes 1 {}".format(os.path.join(file_path,file_name)) )

if __name__ == "__main__":
    hours = datetime.datetime.now().time().hour
    print(hours)
    previousHr = 0
    while True:
        hours = datetime.datetime.now().time().hour
        if int(hours) >= 6 and int(hours) <= 18:
            # if int(hours - previousHr) >= 1:
            #     previousHr = hours
            #     print("Start Recording")
            #     video_rec()
            #     print("Stop recording")
            print("taking a Snapshot")
            take_image()
            print("Sleeping **********************************")
        else:
            print("Morning yet? Nope- ", hours)
        time.sleep(1 * 60)

