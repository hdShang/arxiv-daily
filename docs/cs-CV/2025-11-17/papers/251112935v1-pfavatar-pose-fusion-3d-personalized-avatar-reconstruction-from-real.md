---
layout: default
title: PFAvatar: Pose-Fusion 3D Personalized Avatar Reconstruction from Real-World Outfit-of-the-Day Photos
---

# PFAvatar: Pose-Fusion 3D Personalized Avatar Reconstruction from Real-World Outfit-of-the-Day Photos

**arXiv**: [2511.12935v1](https://arxiv.org/abs/2511.12935) | [PDF](https://arxiv.org/pdf/2511.12935.pdf)

**作者**: Dianbing Xi, Guoyuan An, Jingsen Zhu, Zhijian Liu, Yuan Liu, Ruiyuan Zhang, Jiayuan Lu, Rui Wang, Yuchi Huo

---

## 💡 一句话要点

**提出PFAvatar方法，从日常穿搭照片重建高质量3D虚拟化身**

**关键词**: `3D虚拟化身重建` `神经辐射场` `姿态融合` `少样本学习` `日常穿搭照片` `扩散模型`

## 📋 核心要点

1. 核心问题：从多样姿态、遮挡和复杂背景的日常穿搭照片中重建3D化身，避免传统分解方法的不一致性问题。
2. 方法要点：采用两阶段方法，先微调姿态感知扩散模型，再蒸馏NeRF表示，结合ControlNet和CPPL损失优化细节。
3. 实验效果：在重建保真度、细节保留和遮挡鲁棒性上优于现有方法，支持虚拟试穿等下游应用。

## 📄 摘要（原文）

> We propose PFAvatar (Pose-Fusion Avatar), a new method that reconstructs high-quality 3D avatars from ``Outfit of the Day'' (OOTD) photos, which exhibit diverse poses, occlusions, and complex backgrounds. Our method consists of two stages: (1) fine-tuning a pose-aware diffusion model from few-shot OOTD examples and (2) distilling a 3D avatar represented by a neural radiance field (NeRF). In the first stage, unlike previous methods that segment images into assets (e.g., garments, accessories) for 3D assembly, which is prone to inconsistency, we avoid decomposition and directly model the full-body appearance. By integrating a pre-trained ControlNet for pose estimation and a novel Condition Prior Preservation Loss (CPPL), our method enables end-to-end learning of fine details while mitigating language drift in few-shot training. Our method completes personalization in just 5 minutes, achieving a 48$\times$ speed-up compared to previous approaches. In the second stage, we introduce a NeRF-based avatar representation optimized by canonical SMPL-X space sampling and Multi-Resolution 3D-SDS. Compared to mesh-based representations that suffer from resolution-dependent discretization and erroneous occluded geometry, our continuous radiance field can preserve high-frequency textures (e.g., hair) and handle occlusions correctly through transmittance. Experiments demonstrate that PFAvatar outperforms state-of-the-art methods in terms of reconstruction fidelity, detail preservation, and robustness to occlusions/truncations, advancing practical 3D avatar generation from real-world OOTD albums. In addition, the reconstructed 3D avatar supports downstream applications such as virtual try-on, animation, and human video reenactment, further demonstrating the versatility and practical value of our approach.

