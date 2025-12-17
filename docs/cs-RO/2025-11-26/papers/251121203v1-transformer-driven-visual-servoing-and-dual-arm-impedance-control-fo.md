---
layout: default
title: Transformer Driven Visual Servoing and Dual Arm Impedance Control for Fabric Texture Matching
---

# Transformer Driven Visual Servoing and Dual Arm Impedance Control for Fabric Texture Matching

**arXiv**: [2511.21203v1](https://arxiv.org/abs/2511.21203) | [PDF](https://arxiv.org/pdf/2511.21203.pdf)

**作者**: Fuyuki Tokuda, Akira Seino, Akinari Kobayashi, Kai Tang, Kazuhiro Kosuge

---

## 💡 一句话要点

**提出Transformer视觉伺服与双臂阻抗控制方法，用于织物纹理匹配对齐**

**关键词**: `视觉伺服` `双臂机器人控制` `织物纹理匹配` `Transformer网络` `零样本学习`

## 📋 核心要点

1. 核心问题：如何精确对齐和放置织物片，使其表面纹理匹配，避免褶皱。
2. 方法要点：结合Transformer视觉伺服和双臂阻抗控制，实现姿态控制和张力施加。
3. 实验或效果：在真实世界实验中，系统能零样本部署，准确对齐不同纹理织物。

## 📄 摘要（原文）

> In this paper, we propose a method to align and place a fabric piece on top of another using a dual-arm manipulator and a grayscale camera, so that their surface textures are accurately matched. We propose a novel control scheme that combines Transformer-driven visual servoing with dualarm impedance control. This approach enables the system to simultaneously control the pose of the fabric piece and place it onto the underlying one while applying tension to keep the fabric piece flat. Our transformer-based network incorporates pretrained backbones and a newly introduced Difference Extraction Attention Module (DEAM), which significantly enhances pose difference prediction accuracy. Trained entirely on synthetic images generated using rendering software, the network enables zero-shot deployment in real-world scenarios without requiring prior training on specific fabric textures. Real-world experiments demonstrate that the proposed system accurately aligns fabric pieces with different textures.

