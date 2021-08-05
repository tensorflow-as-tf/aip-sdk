import time

import utils
from model import InferenceModel

FROZEN_GRAPH_PATH = "/jetson_4.3_processor/synthetic_truck_detector_graph_tf1.15.pb"
IMAGE_PATH = "/jetson_4.3_processor/0-325658917-325658917.png"

model = InferenceModel(FROZEN_GRAPH_PATH)
image = utils.read_png_or_tiff(IMAGE_PATH)

logs = []
for i in range(5):
  start = time.time()
  output = model.run_inference(image)
  end = time.time()
  logs.append("Inference %d completed in %s secs (%s ms)." % (i+1, end-start, int((end-start)*1000)))

print("Inference results:")
print(output)
print("=============================================================================")

for log in logs:
  print(log)

print("Note: If the first inference took a LOT of time, that's expected. Inferences 2 onwards are a better estimate of the speed.")
