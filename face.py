import cv2

# Loading pre-trained face detection cascade (Haar cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image): #to detect faces in an image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Function to recognize faces using OpenCV's built-in methods
def recognize_faces(image, faces):
    for (x, y, w, h) in faces:
        # Extracting the face region
        face_roi = image[y:y+h, x:x+w]
        # Converting the face region to grayscale
        face_gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
        # Here, we are just drawing a rectangle around the detected face
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(image, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    return image


def process_image(image_path): #function to detect faces in image
    # Load the image
    image = cv2.imread(r"image_path")
    faces = detect_faces(image)
    # Recognize faces
    image_with_faces = recognize_faces(image, faces)
    # Display the image with detected and recognized faces
    cv2.imshow("Face Detection and Recognition", image_with_faces)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path =(r"image_path") #to Process the given image
process_image(image_path)
