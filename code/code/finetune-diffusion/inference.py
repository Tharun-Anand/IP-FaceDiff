from diffusers import StableDiffusionPipeline
from PIL import Image
import torch
import numpy as np

init_image=np.array(Image.open('/mnt/data/tarun/celeba_hq_256/00002.jpg'))
model_path = "/mnt/data/tarun/finetune/epoch_5"
print('hi')
pipe = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16)
print('hi')
pipe.to("cuda:1")
print('hi')
prompt = "same face,add curly hair"
init_image=init_image+init_image
image = pipe(prompt=prompt,image=init_image,num_inference_steps=50).images[0]
image.save("yoda-pokemon.png")