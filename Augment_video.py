import cv2
import numpy as np
from PIL import Image, ImageEnhance
import random

def random_erasing(frame, max_erasing_area=0.2):
    """Applies random erasing to a frame."""
    h, w, _ = frame.shape
    area = h * w
    target_area = random.uniform(0.02, max_erasing_area) * area
    aspect_ratio = random.uniform(0.3, 3.0)

    erase_h = int(round(np.sqrt(target_area * aspect_ratio)))
    erase_w = int(round(np.sqrt(target_area / aspect_ratio)))

    if erase_h < h and erase_w < w:
        top = random.randint(0, h - erase_h)
        left = random.randint(0, w - erase_w)
        frame[top:top + erase_h, left:left + erase_w] = random.randint(0, 255)
    return frame

def add_gaussian_noise(frame, mean=0, std=25):
    """Adds Gaussian noise to a frame."""
    noise = np.random.normal(mean, std, frame.shape).astype(np.uint8)
    noisy_frame = np.clip(frame + noise, 0, 255).astype(np.uint8)
    return noisy_frame

def adjust_saturation(frame, saturation_factor=1.5):
    """Adjusts saturation using PIL."""
    pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    enhancer = ImageEnhance.Color(pil_frame)
    saturated_frame = enhancer.enhance(saturation_factor)
    return cv2.cvtColor(np.array(saturated_frame), cv2.COLOR_RGB2BGR)

def process_video(input_path, output_path, apply_erasing=True, apply_noise=True, apply_saturation=True):
    """Processes a video file with specified transformations."""
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for saving
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Apply transformations
        if apply_erasing:
            frame = random_erasing(frame)
        if apply_noise:
            frame = add_gaussian_noise(frame)
        if apply_saturation:
            frame = adjust_saturation(frame)
        
        out.write(frame)
    
    cap.release()
    out.release()


process_video(
    input_path="Holding_Something_In_Pain_Day_Grassy_front_30fps.mkv",
    output_path="Holding_Something_In_Pain_Day_Grassy_front_30fps_erasing.mkv",
    apply_erasing=True,
    apply_noise=False,
    apply_saturation=False
)
