# IP-FaceDiff
# Paper is currently under review(codes will be released upon acceptance)

![Overview](Videos/Videos/face_editing.png)

## Setup
```
conda create -n ipfacediff python=3.9
conda activate ipfacediff
pip install -r requirements.txt
```
## Weights and test videos
```
# Download weights from https://drive.google.com/file/d/10sfu8DQAAREGHB22lmRlsmiFSeaYazKl/view?usp=drive_link  and place in weights/
# Place shape extractor models from https://drive.google.com/file/d/10udhYxUdSnT1qbGIm9064YBBszvnJ1U-/view?usp=drive_link and place in weights/
# Place test videos in assets/videos/ 
```

## Inference
```
python inference.py

```
