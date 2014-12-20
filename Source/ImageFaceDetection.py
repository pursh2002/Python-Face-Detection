import cv2
import os
choice="y"
print"------------------------------------------------------------"
print"\t\tPython Face Recognition in Images"
print"------------------------------------------------------------"

while((choice!="n"or choice!="N")and (choice=="y" or choice=="Y")):
    imagex=raw_input("Enter image location:")
    casc=raw_input("Enter cascade path:")
    #create the cascade and initialize it with our face cascade.
    #The face cascade is loaded into memory.
    facecascade=cv2.CascadeClassifier(casc)

    #read the image and convert to gray scale
    image=cv2.imread(imagex)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #thickness=1,linetype=8,shift=0
    #detectMultiScale() that detects objects.
    #First parameter is the grayscale image.
    #Second is the scaleFactor it scales the image's face
    #Third is miniNeighbours defines how many objects are detected
    #near the current one before it declares the face found.
    #Four is minsize which gives the size of each window.
    faces=facecascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(40,40)
        )
    #each face will have its details inside the faces tuple returned
 
    #flags=cv2.cv.CV_HAAR_SCALE_IMAGE for compatibility in old opencv
    #Get number of images and print the number.    
    f=len(faces)
    print"------------------------------------------------------------"
    print "{0} faces found!".format(f)
    print"------------------------------------------------------------"

    #Draw a rectangle around the faces.
    #This function returns 4 values,
    #the x and y location of the rectangle
    #and the rectangle’s width and height (w , h).
    #We use these values to draw a rectangle using the
    #built-in rectangle() function.
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),
                      (255,255,0),2)#image,Vertex of rectangle in relation pt1 and pt2
                                    #,thickness,line type,shift,color=blue
    
    #Displays the faces found.
    cv2.imshow((str(f)+" Faces"),image)

    #Saves the Faces found
    cv2.imwrite(("_"+imagex),image)
    print"------------------------------------------------------------"
    print"Image Saved in %s"%(os.getcwd())
    print"------------------------------------------------------------"
    #period to wait for keypress
    cv2.waitKey(0)
    choice=raw_input("Do you want to continue (y/n):")
    print"------------------------------------------------------------"
    print"------------------------------------------------------------"


print"Goodbye!"    


