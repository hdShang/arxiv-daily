---
layout: default
title: Test-Time Preference Optimization for Image Restoration
---

# Test-Time Preference Optimization for Image Restoration

**arXiv**: [2511.19169v1](https://arxiv.org/abs/2511.19169) | [PDF](https://arxiv.org/pdf/2511.19169.pdf)

**作者**: Bingchen Li, Xin Li, Jiaqi Xu, Jiaming Guo, Wenbo Li, Renjing Pei, Zhibo Chen

---

## 💡 一句话要点

**提出测试时偏好优化范式以提升图像恢复质量并适应多种任务**

**关键词**: `图像恢复` `测试时优化` `偏好对齐` `扩散模型` `无训练方法` `感知质量`

## 📋 核心要点

1. 现有图像恢复方法常与人类偏好不一致，导致恢复图像质量不佳
2. 设计无训练三阶段流程：在线生成候选图像、选择偏好图像、指导扩散去噪优化
3. 实验证明在多种图像恢复任务和模型中有效提升感知质量与灵活性

## 📄 摘要（原文）

> Image restoration (IR) models are typically trained to recover high-quality images using L1 or LPIPS loss. To handle diverse unknown degradations, zero-shot IR methods have also been introduced. However, existing pre-trained and zero-shot IR approaches often fail to align with human preferences, resulting in restored images that may not be favored. This highlights the critical need to enhance restoration quality and adapt flexibly to various image restoration tasks or backbones without requiring model retraining and ideally without labor-intensive preference data collection. In this paper, we propose the first Test-Time Preference Optimization (TTPO) paradigm for image restoration, which enhances perceptual quality, generates preference data on-the-fly, and is compatible with any IR model backbone. Specifically, we design a training-free, three-stage pipeline: (i) generate candidate preference images online using diffusion inversion and denoising based on the initially restored image; (ii) select preferred and dispreferred images using automated preference-aligned metrics or human feedback; and (iii) use the selected preference images as reward signals to guide the diffusion denoising process, optimizing the restored image to better align with human preferences. Extensive experiments across various image restoration tasks and models demonstrate the effectiveness and flexibility of the proposed pipeline.

