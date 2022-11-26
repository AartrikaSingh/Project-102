import cv2
import dropbox
import time
import random
start_time=time.time()
def takesnapshot():
    number=random.randint(0,100)
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=VideoCaptureObject.read()
        imgname="img"+str(number)+".png"
        cv2.imwrite(imgname,frame)
        start_time=time.time
        result=False
        return imgname
    print("SNAPSHOT TAKEN")
    VideoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadphoto(imgname):
    access_token="sl.BE47rJ4LVqPdfqKHEceJ3PcyJd2W_O2qzwjWuxTyr_13pVl0xc3QxBHGJVoA1xRsKjhJ-pAG0U_45aQJwDeybWkheS51en3JMJlPXPyINJMOrRPrHY9sgp4uI6gIx7cQN5700_Yjdfk"
    file=imgname     
    file_from=file
    file_to="/Testfolder/"+(imgname)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("IMAGE UPLOADED")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=takesnapshot()   
            uploadphoto(name)
main()                 
