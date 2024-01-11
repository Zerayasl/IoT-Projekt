"""Main script to run image classification."""

import requests
import base64 # Your data to be sent (replace this with your actual data)
import argparse
import sys
import time
import requests
import numpy as np
from PIL import Image, ImageDraw, ImageFont


import cv2
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision

# Visualization parameters
_ROW_SIZE = 20  # pixels
_LEFT_MARGIN = 5  # pixels
_TEXT_COLOR = (255, 255, 255)  # red
_FONT_SIZE = 1.2
_FONT_THICKNESS = 2
#panel_width = 400
#panel_color = (255, 255, 255)  # White panel

# Creating two lists
first_list = ["cardigan", "sweatshirt", "suit", "pyjama", "fur", "fur coat", "wool", "stole"]
second_list = ["jersey", "maillot"]

# Combining the lists into a Python array
combined_array = [first_list, second_list]

def run(model: str, max_results: int, score_threshold: float, num_threads: int,
        enable_edgetpu: bool, camera_id: int, width: int, height: int) -> None:

  # Initialize the image classification model
  base_options = core.BaseOptions(
      file_name=model, use_coral=enable_edgetpu, num_threads=num_threads)

  # Enable Coral by this setting
  classification_options = processor.ClassificationOptions(
      max_results=max_results, score_threshold=score_threshold)
  options = vision.ImageClassifierOptions(
      base_options=base_options, classification_options=classification_options)

  classifier = vision.ImageClassifier.create_from_options(options)

  
  # Start capturing video input from the camera
  cap = cv2.VideoCapture(camera_id)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

  # Continuously capture images from the camera and run inference
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      sys.exit(
          'ERROR: Unable to read from webcam. Please verify your webcam settings.'
      )

    image = cv2.flip(image, 1)
    image = cv2.resize(image, (1550, 1080))
    image_height, image_width, _ = image.shape
    
    # Use Pillow's ImageDraw to add weather information to the panel
    font = ImageFont.load_default()

    # Convert the image from BGR to RGB as required by the TFLite model.
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create TensorImage from the RGB image
    tensor_image = vision.TensorImage.create_from_array(rgb_image)
    # List classification results
    categories = classifier.classify(tensor_image)

    # Store the temperature in a variable to avoid redundant API calls
    temperature = get_temperature()
    
    #manuelle wetterangabe
    #temperature = 4.9

    category_name = ''

    # Show classification results on the image
    for idx, category in enumerate(categories.classifications[0].categories):


        if category.category_name in combined_array[0]:
            print('yes')
            print(temperature)
            if temperature > 15:
                category_name = 'Too warm :('.format(temperature)
                response = requests.get(f'http://127.0.0.1:1880/red')
                 
            else:
                category_name = 'Accordingly!'.format(temperature)
                response = requests.get(f'http://127.0.0.1:1880/green')
                 
              
        elif category.category_name in combined_array[1]:
            if temperature < 15:
                category_name = 'Too cold :('.format(temperature)
                response = requests.get(f'http://127.0.0.1:1880/red')
                 
            else:
                category_name = 'Accordingly!'.format(temperature)
                response = requests.get(f'http://127.0.0.1:1880/green')
              

      #  score = round(category.score, 2)
       # result_text = '{}'.format(category_name)
        #text_location = (_LEFT_MARGIN, (idx + 2) * _ROW_SIZE)
        #cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
           #         _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS)

    # Stop the program if the ESC key is pressed.
    if cv2.waitKey(1) == 27:
      response = requests.get(f'http://127.0.0.1:1880/off')
      break
    
    # Get the height of the existing image
    height = image.shape[0]

    # Create a new panel (right side)
    panel_width = 300
    
    # Iconpfad
    sun_icon_path = '/home/pi/examples/lite/examples/image_classification/raspberry_pi/iconsonne.jpg'
    cloud_icon_path = '/home/pi/examples/lite/examples/image_classification/raspberry_pi/iconwolke.jpg'
    snow_icon_path = '/home/pi/examples/lite/examples/image_classification/raspberry_pi/iconschnee.jpg'
    new_panel = np.full((height, panel_width, 3), (0, 0, 0), dtype=np.uint8)
    weather_panel = draw_weather_panel(temperature, new_panel, sun_icon_path, cloud_icon_path, snow_icon_path, category_name)

    # Combine the existing image and the new panel
    combined_image = np.hstack((image, weather_panel))

    # Save the image to the Node-RED endpoint
    img = Image.fromarray(combined_image)
    img.save('/home/pi/.node-red/image/snapshot.jpg')
    
    # cv2.imshow('Combined Image', combined_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imshow('image_classification', combined_image)

  cap.release()
  cv2.destroyAllWindows()
  response = requests.get(f'http://127.0.0.1:1880/off')



def main():

    
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Name of image classification model.',
      required=False,
      default='efficientnet_lite0.tflite')
  parser.add_argument(
      '--maxResults',
      help='Max of classification results.',
      required=False,
      default=1)
  parser.add_argument(
      '--scoreThreshold',
      help='The score threshold of classification results.',
      required=False,
      type=float,
      default=0.0)
  parser.add_argument(
      '--numThreads',
      help='Number of CPU threads to run the model.',
      required=False,
      default=4)
  parser.add_argument(
      '--enableEdgeTPU',
      help='Whether to run the model on EdgeTPU.',
      action='store_true',
      required=False,
      default=False)
  parser.add_argument(
      '--cameraId', help='Id of camera.', required=False, default=0)
  parser.add_argument(
      '--frameWidth',
      help='Width of frame to capture from camera.',
      required=False,
      default=1920)
  parser.add_argument(
      '--frameHeight',
      help='Height of frame to capture from camera.',
      required=False,
      default=1080)
  args = parser.parse_args()

  run(args.model, int(args.maxResults),
      args.scoreThreshold, int(args.numThreads), bool(args.enableEdgeTPU),
      int(args.cameraId), args.frameWidth, args.frameHeight)



def get_temperature():
    try:
        # Make a GET request to the API
        response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude=47.3769&longitude=8.5417&current=temperature_2m')

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and print the temperature
            temperature = data['current']['temperature_2m']
            return temperature
            print(f'The current temperature is: {temperature} °C')
        else:
            print(f'Error: Unable to retrieve data. Status code: {response.status_code}')

    except Exception as e:
        print(f'An error occurred: {e}')



def draw_weather_panel(value, panel, sun_icon_path, cloud_icon_path, snow_icon_path, category_name):

    #Icons laden
    if value > 15:
        # Sonne
        icon = cv2.imread(sun_icon_path)
    elif value > 5:
        # Wolke
        icon = cv2.imread(cloud_icon_path)
    else:
        # Wolke mit Schnee
        icon = cv2.imread(snow_icon_path)

    #Icon überprüen
    if icon is None:
        print("Icon nicht geladen")
        return panel
    
    #Icon Skalierung
    icon = cv2.resize(icon, (180, 180))

    #Icon einfügen
    x_offset, y_offset = 70, 50
    panel[y_offset:y_offset+icon.shape[0], x_offset:x_offset+icon.shape[1]]= icon
    
    #Eingabewert
    text = f"{value} Celsius"
    cv2.putText(panel, text, (70, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    
    #Detector Text
    #result_text = '{}'.format(category_name)
    cv2.putText(panel, category_name, (70, 420), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)

    #Trennlinie
    cv2.line(panel, (70, 340), (panel.shape[1]-70, 340), (255,255,255), 5)
   
   
   
    return panel
    
    
    
if __name__ == '__main__':
  main()
