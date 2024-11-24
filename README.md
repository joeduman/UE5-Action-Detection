# 678 Project: UE5-Action-Detection

## Overview
This project generates a synthetic dataset for training an LSTM-based action recognition model. The dataset is created using Unreal Engine with UnrealCV for automated data capture. It includes variations in camera angles, lighting conditions, backgrounds, and six predefined human actions.

## Dataset Composition
## Actions: Waving, jumping, pointing, limping, running, holding something in pain.
## Camera Profiles:
- Front view
- Side view
- Top-down view
## Lighting Conditions:
- Day
- Night
- Foggy
- Dim
## Backgrounds:
- Plain-colored environment
- Grassy area
- Rural area

Dataset/
├── Waving/
│   ├── waving_day_front_plain.mp4
│   ├── waving_night_side_grassy.mp4
│   ...
├── Jumping/
│   ├── jumping_foggy_top_rural.mp4
│   ...
├── Pointing/
│   ├── pointing_dim_side_plain.mp4
│   ...
