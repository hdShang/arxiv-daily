---
layout: default
title: Optimizing DINOv2 with Registers for Face Anti-Spoofing
---

# Optimizing DINOv2 with Registers for Face Anti-Spoofing

**arXiv**: [2510.17201v1](https://arxiv.org/abs/2510.17201) | [PDF](https://arxiv.org/pdf/2510.17201.pdf)

**作者**: Mika Feng, Pierre Gallin-Martel, Koichi Ito, Takafumi Aoki

---

## 💡 一句话要点

**提出基于DINOv2与寄存器的面部反欺骗方法，以检测活体与欺骗图像的细微差异。**

**关键词**: `面部反欺骗` `DINOv2` `注意力机制` `寄存器优化` `活体检测`

## 📋 核心要点

1. 核心问题：面部识别系统易受照片欺骗攻击，需在识别前检测活体与欺骗图像。
2. 方法要点：使用DINOv2与寄存器提取泛化特征，抑制注意力机制中的扰动。
3. 实验或效果：在ICCV2025工作坊数据集和SiW数据集上验证方法有效性。

## 📄 摘要（原文）

> Face recognition systems are designed to be robust against variations in head
> pose, illumination, and image blur during capture. However, malicious actors
> can exploit these systems by presenting a face photo of a registered user,
> potentially bypassing the authentication process. Such spoofing attacks must be
> detected prior to face recognition. In this paper, we propose a DINOv2-based
> spoofing attack detection method to discern minute differences between live and
> spoofed face images. Specifically, we employ DINOv2 with registers to extract
> generalizable features and to suppress perturbations in the attention
> mechanism, which enables focused attention on essential and minute features. We
> demonstrate the effectiveness of the proposed method through experiments
> conducted on the dataset provided by ``The 6th Face Anti-Spoofing Workshop:
> Unified Physical-Digital Attacks Detection@ICCV2025'' and SiW dataset.

