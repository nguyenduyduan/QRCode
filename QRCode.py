import cv2
from pyzbar.pyzbar import decode

def read_qr_code(frame):
    # Decode QR codes in the frame
    decoded_objects = decode(frame)

    # Process each decoded object
    for obj in decoded_objects:
        # Extract data from the QR code
        qr_data = obj.data.decode('utf-8')
        print("QR Code Data:", qr_data)

        # Save information from the QR code to fields or perform desired actions
        save_information(qr_data)

        # Draw a rectangle around the QR code
        points = obj.polygon
        if len(points) == 4:
            hull = cv2.convexHull(points, clockwise=True)
            cv2.polylines(frame, [hull], True, (0, 255, 0), 2)

def save_information(data):
    # Implement your logic to save information from the QR code
    # For example, you can write the data to a file or a database
    with open('qr_data.txt', 'a') as file:
        file.write(data + '\n')

def main():
    # Open the camera (0 is usually the built-in camera)
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Call the function to read and process QR codes
        read_qr_code(frame)

        # Display the frame
        cv2.imshow('QR Code Reader', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
