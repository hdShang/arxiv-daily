---
layout: default
title: Inversion-Free Style Transfer with Dual Rectified Flows
---

# Inversion-Free Style Transfer with Dual Rectified Flows

**arXiv**: [2511.20986v1](https://arxiv.org/abs/2511.20986) | [PDF](https://arxiv.org/pdf/2511.20986.pdf)

**作者**: Yingying Deng, Xiangyu He, Fan Tang, Weiming Dong, Xucheng Yin

---

## 💡 一句话要点

**提出基于双整流流的免反演风格迁移框架，以提升图像风格迁移的效率与视觉质量。**

**关键词**: `风格迁移` `整流流` `免反演方法` `图像合成` `动态插值` `注意力注入`

## 📋 核心要点

1. 主流免训练扩散方法依赖计算密集型反演过程，导致效率低下和视觉失真。
2. 采用双整流流并行预测内容和风格轨迹，通过动态中点插值融合，仅需前向传播。
3. 实验验证了方法在多样风格和内容上的泛化能力，实现高效且高质量的迁移。

## 📄 摘要（原文）

> Style transfer, a pivotal task in image processing, synthesizes visually compelling images by seamlessly blending realistic content with artistic styles, enabling applications in photo editing and creative design. While mainstream training-free diffusion-based methods have greatly advanced style transfer in recent years, their reliance on computationally inversion processes compromises efficiency and introduces visual distortions when inversion is inaccurate. To address these limitations, we propose a novel \textit{inversion-free} style transfer framework based on dual rectified flows, which tackles the challenge of finding an unknown stylized distribution from two distinct inputs (content and style images), \textit{only with forward pass}. Our approach predicts content and style trajectories in parallel, then fuses them through a dynamic midpoint interpolation that integrates velocities from both paths while adapting to the evolving stylized image. By jointly modeling the content, style, and stylized distributions, our velocity field design achieves robust fusion and avoids the shortcomings of naive overlays. Attention injection further guides style integration, enhancing visual fidelity, content preservation, and computational efficiency. Extensive experiments demonstrate generalization across diverse styles and content, providing an effective and efficient pipeline for style transfer.

