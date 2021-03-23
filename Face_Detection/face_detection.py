import cv2
import numpy as np

class Face_Detect:
    def __init__(self,src):         # constructor with parameter image location
        self.img = cv2.imread(src,cv2.IMREAD_UNCHANGED)
    def show_image(self):           # function to show the image
        print('Dimensions : ',self.img.shape)
        cv2.imshow("Face Detection",self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    # def resize_image(self):       # function to resize the image
    #     scale_percent = 5 # percent of the original image
    #     width = int(self.img.shape[1] * scale_percent /100)
    #     height = int(self.img.shape[0] * scale_percent /100)
    #     dim = (width, height)
    #     # resize image
    #     self.resized = cv2.resize(self.img, dim, interpolation=cv2.INTER_AREA)

    def face_detection(self):       # function to detect facein the image using haarcascade
        face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)      # convert image into grayscale for processing
        faces = face_classifier.detectMultiScale(self.gray, 1.0485258, 6)
        if faces == ():
            print("No faces found")
        for (x,y,w,h) in faces:
            cv2.rectangle(self.img, (x,y), (x+w,y+h), (130,0,15), 3)

    def rotate_image(self):     # function to rotate image 90 degree
        self.img = cv2.rotate(self.img,cv2.ROTATE_90_CLOCKWISE)

    def save_image(self):       # function to save image in the disk
        cv2.imwrite("NewImage.jpg",self.img)



def main():
    obj = Face_Detect('C:/Users/User/Desktop/Internship/Face_Detection/sample.jpg')
    # obj.resize_image()
    obj.face_detection()
    obj.rotate_image()
    obj.show_image()
    obj.save_image()

main()
