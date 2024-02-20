import torch
import  streamlit as st
from PIL import Image
from diffusers  import DiffusionPipeline as DP
h = st.header('Diffusion.AI')
s = st.subheader('เว็บไซต์สำหรับเเปลงข้อความเป็นภาพ')
p = st.write('เว็บไซต์นี้เเลกมาด้วยหยาดเหงื่อเเละความอดทน')
text = st.text_input('prompt:')
if text:
   dq = DP.from_pretrained("runwayml/stable-diffusion-v1-5"
                           torch_dtype=torch.float16)
   image_data = dp(text).images[0]
   image = image.frommarray(image_data)
   image.show()
   #st.image('http://picsum.photos/400/200'
   b = st.button('จะไปต่อหรือ...')