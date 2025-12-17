---
layout: default
title: G-SHARP: Gaussian Surgical Hardware Accelerated Real-time Pipeline
---

# G-SHARP: Gaussian Surgical Hardware Accelerated Real-time Pipeline

**arXiv**: [2512.02482v1](https://arxiv.org/abs/2512.02482) | [PDF](https://arxiv.org/pdf/2512.02482.pdf)

**作者**: Vishwesh Nath, Javier G. Tejero, Ruilong Li, Filippo Filicori, Mahdi Azizian, Sean D. Huver

---

## 💡 一句话要点

**提出G-SHARP，基于开源GSplat构建实时手术场景重建框架，适用于微创手术中的可变形组织建模。**

**关键词**: `手术场景重建` `高斯溅射` `实时渲染` `可变形组织建模` `边缘计算` `微创手术`

## 📋 核心要点

1. 核心问题：现有高斯溅射方法依赖非商业衍生工具，限制了手术场景重建的部署能力。
2. 方法要点：基于Apache-2.0许可的GSplat可微分高斯光栅化器，实现原理性变形建模和鲁棒遮挡处理。
3. 实验或效果：在EndoNeRF基准上达到先进重建质量，提供Holoscan SDK应用支持NVIDIA边缘硬件实时可视化。

## 📄 摘要（原文）

> We propose G-SHARP, a commercially compatible, real-time surgical scene reconstruction framework designed for minimally invasive procedures that require fast and accurate 3D modeling of deformable tissue. While recent Gaussian splatting approaches have advanced real-time endoscopic reconstruction, existing implementations often depend on non-commercial derivatives, limiting deployability. G-SHARP overcomes these constraints by being the first surgical pipeline built natively on the GSplat (Apache-2.0) differentiable Gaussian rasterizer, enabling principled deformation modeling, robust occlusion handling, and high-fidelity reconstructions on the EndoNeRF pulling benchmark. Our results demonstrate state-of-the-art reconstruction quality with strong speed-accuracy trade-offs suitable for intra-operative use. Finally, we provide a Holoscan SDK application that deploys G-SHARP on NVIDIA IGX Orin and Thor edge hardware, enabling real-time surgical visualization in practical operating-room settings.

