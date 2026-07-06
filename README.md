# Egg Candling & Fertility Detection - Live Prototype

This project is a real-time computer vision application designed to detect and classify egg fertility using live webcam feeds. It leverages the **YOLOv8** (You Only Look Once) object detection architecture via the Ultralytics library and **OpenCV** for video stream processing.

---

## Project Status: Testing & Prototyping Phase

**Please Note:** The current implementation and model are **solely for testing the technical capabilities** of live object detection and classification. 

The model currently in use (`best.pt`) was trained on a public, generalized dataset to verify that the pipeline (webcam capture ➡️ YOLOv8 inference ➡️ UI rendering) works flawlessly. 

**Next Steps:** We will soon be collecting, annotating, and training a **custom, proprietary dataset** specific to our exact lighting, egg types, and candling equipment to achieve production-grade accuracy. This repository will be updated with the new custom-trained model once available.

---

## Project Structure

For the script to run correctly, your folder structure must look exactly like this:

```text
egg_detection/
│
├── mainh.py          # The main Python script for live inference
├── README.md         # This file
└── weights/
    └── best.pt       # The trained YOLOv8 model weights
```

---

## Setup Instructions

### 1. Prerequisites
* **Python 3.8 or higher** installed on your machine.
* A working **Webcam** (Built-in or USB).
* *(Optional but recommended)* **NVIDIA GPU** with CUDA installed for faster inference, though CPU works perfectly fine for testing.

### 2. Install Dependencies
Open your terminal or command prompt, navigate to the project folder, and install the required Python packages:

```bash
pip install ultralytics opencv-python
```
*(Note: If you are using a virtual environment like `venv` or `conda`, make sure it is activated before running this command).*

### 3. Add the Model Weights
1. Obtain the `best.pt` file (currently using the public test model).
2. Create a folder named `weights` in the root of this project.
3. Place the `best.pt` file inside the `weights` folder.

---

## Usage Instructions

### Running the Live Feed
1. Open your terminal in the project directory.
2. Run the main script:
   ```bash
   python mainh.py
   ```
3. A new window titled **"Egg Fertility Detection"** will pop up, displaying your live webcam feed.
4. Point your camera at an egg candling setup. The model will draw bounding boxes and label the eggs (e.g., `FER` for Fertile, `INF` for Infertile).
5. **To quit the application:** Simply press the **`q`** key on your keyboard while the video window is in focus.

### Configuring Your Camera
The script is currently configured to use camera index `1` (typically a USB external camera). 
* If the screen is black or throws an error, you may need to change the camera index.
* Open `mainh.py` and find this line:
  ```python
  cap = cv2.VideoCapture(1)
  ```
* Change `1` to `0` (for built-in laptop cameras) or `2` (if you have multiple USB cameras plugged in).

---

## Troubleshooting

* **`ModuleNotFoundError: No module named 'cv2'`**
  You are missing OpenCV. Run `pip install opencv-python`.
* **`FileNotFoundError: [Errno 2] No such file or directory: 'weights/best.pt'`**
  Ensure you created the `weights` folder and placed the `best.pt` file inside it, exactly as shown in the Project Structure section.
* **Camera is not turning on / Black Screen**
  Make sure no other applications (Zoom, Teams, Discord, Windows Camera app) are currently using the webcam. Windows only allows one app to access the camera at a time.

---

## Future Roadmap

- [x] Setup live webcam inference pipeline using YOLOv8.
- [x] Test classification and detection capabilities using a public dataset.
- [ ] **Collect proprietary dataset** using our specific candling hardware and lighting.
- [ ] **Annotate and train** a custom YOLOv8 model on the proprietary dataset.
- [ ] Optimize model using ONNX Runtime / TensorRT for edge-device deployment.
- [ ] Integrate with physical sorting hardware / IoT dashboard.

---

## License & Credits
* **Object Detection Framework:** [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* **Video Processing:** [OpenCV](https://opencv.org/)