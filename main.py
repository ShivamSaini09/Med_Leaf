import tkinter as tk
from tkinter import filedialog
import requests
from PIL import Image, ImageTk

class CustomVisionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medleaf")

        self.image_path = None
        self.predicted_tag = tk.StringVar()
        self.confidence = tk.StringVar()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Image display area
        self.image_label = tk.Label(self.root, text="Uploaded Image:")
        self.image_label.pack()

        self.canvas = tk.Canvas(self.root, width=600, height=200)
        self.canvas.pack()

        # Buttons
        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.predict_button = tk.Button(self.root, text="Make Prediction", command=self.make_prediction)
        self.predict_button.pack(pady=10)

        # Prediction result
        self.result_label = tk.Label(self.root, text="Prediction Result:")
        self.result_label.pack()

        self.predicted_label = tk.Label(self.root, textvariable=self.predicted_tag)
        self.predicted_label.pack()

        self.confidence_label = tk.Label(self.root, textvariable=self.confidence)
        self.confidence_label.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path = file_path
            self.show_image(file_path)

    def show_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((600, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        self.canvas.config(width=photo.width(), height=photo.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def make_prediction(self):
        if self.image_path:
            with open(self.image_path, 'rb') as image_file:
                prediction_url = 'https://violence-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/8bbd3e68-2be6-4624-810b-c04c90becd3d/classify/iterations/Leaf%20detection/image'
                prediction_key = '1a6a334e28b743718ccf4f558f7553a4'
                content_type = 'application/octet-stream'

                # Prepare headers and data for the request
                headers = {
                    'Prediction-Key': prediction_key,
                    'Content-Type': content_type
                }
                data = image_file.read()

                # Make a prediction
                response = requests.post(prediction_url, headers=headers, data=data)

                # Parse and display the results
                results = response.json()
                if 'predictions' in results:
                    predictions = results['predictions']
                    if predictions:
                        best_prediction = max(predictions, key=lambda x: x['probability'])
                        predicted_tag = best_prediction['tagName']
                        confidence = best_prediction['probability']
                        self.predicted_tag.set(f'Predicted Tag: {predicted_tag}')
                        self.confidence.set(f'Confidence: {confidence:.2f}')
                    else:
                        self.predicted_tag.set('No predictions were made.')
                        self.confidence.set('')
                else:
                    self.predicted_tag.set('No predictions were made.')
                    self.confidence.set('')


if __name__ == "__main__":
    root = tk.Tk()
    app = CustomVisionApp(root)
    root.mainloop()
