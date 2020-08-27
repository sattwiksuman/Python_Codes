import cv2

img = cv2.imread("galaxy.jpg", 0)

print(img)
print(type(img))
print(img.shape)

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWondows()



"""
import glob 

files=glob.glob("*.jpg")
for f in files:
	print(f)
	im=cv2.imread(f,0)
	re=cv2.resize(im, (100,100))
	cv2.imwrite("resized_"+f, re)
	cv2.imshow("IMAGE", re)
	cv2.waitKey(500)
	cv2.destroyAllWindows()

newfiles = glob.glob("*.jpg")
for nf in newfiles:
	print(nf)
"""