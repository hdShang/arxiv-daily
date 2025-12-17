---
layout: default
title: Gaussian Blending: Rethinking Alpha Blending in 3D Gaussian Splatting
---

# Gaussian Blending: Rethinking Alpha Blending in 3D Gaussian Splatting

**arXiv**: [2511.15102v1](https://arxiv.org/abs/2511.15102) | [PDF](https://arxiv.org/pdf/2511.15102.pdf)

**作者**: Junseo Koo, Jinseo Jeong, Gunhee Kim

---

## 💡 一句话要点

**提出高斯混合以解决3D高斯溅射中缩放时的视觉伪影问题**

**关键词**: `3D高斯溅射` `新视角合成` `alpha混合` `视觉伪影` `实时渲染` `高斯混合`

## 📋 核心要点

1. 核心问题：3D高斯溅射在训练未见采样率下出现侵蚀模糊和扩张阶梯伪影
2. 方法要点：用高斯混合替代传统alpha混合，将alpha和透射率视为空间分布
3. 实验或效果：在未见和已见采样率下均优于现有模型，保持实时渲染

## 📄 摘要（原文）

> The recent introduction of 3D Gaussian Splatting (3DGS) has significantly advanced novel view synthesis. Several studies have further improved the rendering quality of 3DGS, yet they still exhibit noticeable visual discrepancies when synthesizing views at sampling rates unseen during training. Specifically, they suffer from (i) erosion-induced blurring artifacts when zooming in and (ii) dilation-induced staircase artifacts when zooming out. We speculate that these artifacts arise from the fundamental limitation of the alpha blending adopted in 3DGS methods. Instead of the conventional alpha blending that computes alpha and transmittance as scalar quantities over a pixel, we propose to replace it with our novel Gaussian Blending that treats alpha and transmittance as spatially varying distributions. Thus, transmittances can be updated considering the spatial distribution of alpha values across the pixel area, allowing nearby background splats to contribute to the final rendering. Our Gaussian Blending maintains real-time rendering speed and requires no additional memory cost, while being easily integrated as a drop-in replacement into existing 3DGS-based or other NVS frameworks. Extensive experiments demonstrate that Gaussian Blending effectively captures fine details at various sampling rates unseen during training, consistently outperforming existing novel view synthesis models across both unseen and seen sampling rates.

