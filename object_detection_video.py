from detecto.core import Model
from detecto.visualize import detect_video

model = Model()  # Initialize a pre-trained model
detect_video(model, 'students003.avi', 'output2.avi')  # Run inference on a video