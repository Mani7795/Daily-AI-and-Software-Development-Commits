# 📘 Diffusion Models: From Theory to Implementation
# Author: Mani Meka
# Goal: Explore and implement key components of Denoising Diffusion Probabilistic Models (DDPM)

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import torch
import torch.nn as nn
import torch.nn.functional as F

device = "cuda" if torch.cuda.is_available() else "cpu"
image_size = 28
timesteps = 200  # Total diffusion steps
beta_start = 1e-4
beta_end = 0.02

betas = torch.linspace(beta_start, beta_end, timesteps).to(device)
alphas = 1.0 - betas
alphas_cumprod = torch.cumprod(alphas, dim=0)

def forward_diffusion_sample(x_0, t, noise=None):
    if noise is None:
        noise = torch.randn_like(x_0)
    sqrt_alphas_cumprod = torch.sqrt(alphas_cumprod[t])[:, None, None, None]
    sqrt_one_minus_alphas_cumprod = torch.sqrt(1 - alphas_cumprod[t])[:, None, None, None]
    return sqrt_alphas_cumprod * x_0 + sqrt_one_minus_alphas_cumprod * noise, noise


from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([transforms.ToTensor(), transforms.Lambda(lambda x: x * 2 - 1)])
mnist = MNIST(root=".", download=True, train=True, transform=transform)
loader = DataLoader(mnist, batch_size=8, shuffle=True)

x, _ = next(iter(loader))
x = x.to(device)

plt.figure(figsize=(12, 2))
for idx, t in enumerate([0, 50, 100, 150, 199]):
    noisy, _ = forward_diffusion_sample(x, torch.tensor([t]*x.shape[0]).to(device))
    plt.subplot(1, 5, idx+1)
    plt.imshow(noisy[0].cpu().squeeze(), cmap="gray")
    plt.title(f"t={t}")
    plt.axis("off")
plt.show()


