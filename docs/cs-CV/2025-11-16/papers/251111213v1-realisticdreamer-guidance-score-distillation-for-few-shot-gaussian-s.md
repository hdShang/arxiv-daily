---
layout: default
title: RealisticDreamer: Guidance Score Distillation for Few-shot Gaussian Splatting
---

# RealisticDreamer: Guidance Score Distillation for Few-shot Gaussian Splatting

**arXiv**: [2511.11213v1](https://arxiv.org/abs/2511.11213) | [PDF](https://arxiv.org/pdf/2511.11213.pdf)

**作者**: Ruocheng Wu, Haolan He, Yufei Wang, Zhihao Li, Bihan Wen

---

## 💡 一句话要点

**提出引导分数蒸馏以解决稀疏视图下3D高斯溅射过拟合问题**

**关键词**: `3D高斯溅射` `分数蒸馏采样` `视频扩散模型` `多视图一致性` `稀疏视图重建`

## 📋 核心要点

1. 核心问题：稀疏训练视图导致3D高斯溅射过拟合，缺乏中间视图监督。
2. 方法要点：从预训练视频扩散模型提取多视图一致性先验，通过统一引导形式校正噪声预测。
3. 实验或效果：在多个数据集上优于现有方法，提升几何准确性和相机姿态对齐。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has recently gained great attention in the 3D scene representation for its high-quality real-time rendering capabilities. However, when the input comprises sparse training views, 3DGS is prone to overfitting, primarily due to the lack of intermediate-view supervision. Inspired by the recent success of Video Diffusion Models (VDM), we propose a framework called Guidance Score Distillation (GSD) to extract the rich multi-view consistency priors from pretrained VDMs. Building on the insights from Score Distillation Sampling (SDS), GSD supervises rendered images from multiple neighboring views, guiding the Gaussian splatting representation towards the generative direction of VDM. However, the generative direction often involves object motion and random camera trajectories, making it challenging for direct supervision in the optimization process. To address this problem, we introduce an unified guidance form to correct the noise prediction result of VDM. Specifically, we incorporate both a depth warp guidance based on real depth maps and a guidance based on semantic image features, ensuring that the score update direction from VDM aligns with the correct camera pose and accurate geometry. Experimental results show that our method outperforms existing approaches across multiple datasets.

