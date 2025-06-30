from PIL import Image
from realesrgan import RealESRGANer
import torch

# cuda gpu 사용 여부 확인
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = RealESRGANer(device, scale=4)
model.load_weights('RealESRGAN_x4.pth')

