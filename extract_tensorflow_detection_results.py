# Define classes to extract values from Tensorflow object detection
class BoundingBox:
    def __init__(self, origin_x, origin_y, width, height):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height

class Category:
    def __init__(self, index, score, display_name, category_name):
        self.index = index
        self.score = score
        self.display_name = display_name
        self.category_name = category_name

class Detection:
    def __init__(self, bounding_box, categories):
        self.bounding_box = bounding_box
        self.categories = categories

class DetectionResult:
    def __init__(self, detections):
        self.detections = detections

# Create an instance of DetectionResult with the provided data
detection_output = DetectionResult([
    Detection(BoundingBox(15, -1, 632, 483), [Category(0, 0.9453125, '', 'person')]),
    Detection(BoundingBox(547, 379, 89, 100), [Category(0, 0.45703125, '', 'person')]),
    Detection(BoundingBox(15, -1, 632, 483), [Category(0, 0.45703125, '', 'person')]),
    Detection(BoundingBox(547, 379, 89, 100), [Category(0, 0.45703125, '', 'person')]),
    Detection(BoundingBox(15, -1, 632, 483), [Category(0, 0.45703125, '', 'person')])
])

# Extract and print only the category_name
category_names = [category.category_name for detection in detection_output.detections for category in detection.categories]

# Extract and print bounding box information and category name
for i, detection in enumerate(detection_output.detections, start=1):
    bounding_box_info = detection.bounding_box.__dict__
    category_name = detection.categories[0].category_name  # Assuming one category per detection
    print(f"Detection {i} Bounding Box: {bounding_box_info}, Category: {category_name}")