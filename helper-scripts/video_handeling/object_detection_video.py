from detecto.core import Model
from detecto.visualize import detect_video

model = Model()  # Initialize a pre-trained model
detect_video(model, "Arxiepiskopi_flock.avi", "output3.avi")  # Run inference on a video
