# 678 Project: UE5-Action-Detection

## Overview

This project is focused on distress-related action recognition in a variety of environmental and weather conditions.
We automate the generation of synthetic video data using Unreal Engine 5 (UE5) and UnrealCV, performing simulations of six distress-related
human actions: injured waving, jumping, pointing, limping, running, and holding something in pain.

We pass this data through a convolutional neural network to perform feature extraction, and follow this up by utilising 
a Long Short-Term Memory network to analyze patterns within the time series data. We utilise fully connected layers to
then map our learned representations to one of the six distress-related actions, which we may use for action classification.

## Dataset Composition

### Mixamo Actions: 

#### Waving
![Waving Animation](/readme_assets/waving.gif)

#### Jumping:
![Jumping Animation](/readme_assets/jumping.gif)

#### Pointing:
![Pointing Animation](/readme_assets/pointing.gif)

#### Limping:
![Limping Animation](/readme_assets/limping.gif)

#### Running:
![Running Animation](/readme_assets/running.gif)

#### Holding something in pain:
![Holding Animation](/readme_assets/holding.gif)


### Camera Profiles:
- Front view
- Side view
  - Left
  - Right
- Top-down view

### Lighting Conditions:
- Day
- Night
- Foggy
- Dim

## Backgrounds:
- Neutral environment
- Grassy environment
- Rural environment

### File Structure:

```
dataset/
├── holding/
│   ├── holding_day_front_plain.mp4
│   ├── holding_night_side_grassy.mp4
│   ...
├── jumping/
│   ├── jumping_foggy_top_rural.mp4
│   ...
├── limping/
│   ├── limping_dim_side_plain.mp4
│   ...
...
```

## Model Architecture

The model architecture combines convolutional neural networks (CNNs) 
and Long Short-Term Memory (LSTM) to classify our synthetic video data of distress-related actions.
Our data is of the form of 30fps video segments of animations in various environments and conditions.

We pass our data through CNN to extract spatial features from individual frames, which helps the model learn visual patterns.

We then utilise these learned features by passing them through an LSTM model, which are better equipped to handle the time
series data from videos, and can interpret the features across each time step.

Finally, we utilise a fully connected layer to then map our learned representations to each of the labels associated with
the six distress-related actions.

![](/readme_assets/architecture.png)
