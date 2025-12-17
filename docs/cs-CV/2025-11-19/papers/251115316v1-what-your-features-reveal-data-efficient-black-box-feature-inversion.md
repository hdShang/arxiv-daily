---
layout: default
title: What Your Features Reveal: Data-Efficient Black-Box Feature Inversion Attack for Split DNNs
---

# What Your Features Reveal: Data-Efficient Black-Box Feature Inversion Attack for Split DNNs

**arXiv**: [2511.15316v1](https://arxiv.org/abs/2511.15316) | [PDF](https://arxiv.org/pdf/2511.15316.pdf)

**作者**: Zhihan Ren, Lijun He, Jiaxi Liang, Xinzhu Fu, Haixia Bi, Fan Li

---

## 💡 一句话要点

**提出FIA-Flow框架以解决分割DNN中特征反演攻击的隐私泄露问题**

**关键词**: `特征反演攻击` `分割DNN` `隐私保护` `黑盒攻击` `语义对齐` `分布匹配`

## 📋 核心要点

1. 分割DNN中中间特征易被利用重构私有输入，现有方法重建质量有限
2. 设计LFSAM和DIFM模块，桥接语义差距并纠正分布不匹配，实现高保真反演
3. 实验在多种模型和层上验证，反演更忠实，揭示更严重隐私威胁

## 📄 摘要（原文）

> Split DNNs enable edge devices by offloading intensive computation to a cloud server, but this paradigm exposes privacy vulnerabilities, as the intermediate features can be exploited to reconstruct the private inputs via Feature Inversion Attack (FIA). Existing FIA methods often produce limited reconstruction quality, making it difficult to assess the true extent of privacy leakage. To reveal the privacy risk of the leaked features, we introduce FIA-Flow, a black-box FIA framework that achieves high-fidelity image reconstruction from intermediate features. To exploit the semantic information within intermediate features, we design a Latent Feature Space Alignment Module (LFSAM) to bridge the semantic gap between the intermediate feature space and the latent space. Furthermore, to rectify distributional mismatch, we develop Deterministic Inversion Flow Matching (DIFM), which projects off-manifold features onto the target manifold with one-step inference. This decoupled design simplifies learning and enables effective training with few image-feature pairs. To quantify privacy leakage from a human perspective, we also propose two metrics based on a large vision-language model. Experiments show that FIA-Flow achieves more faithful and semantically aligned feature inversion across various models (AlexNet, ResNet, Swin Transformer, DINO, and YOLO11) and layers, revealing a more severe privacy threat in Split DNNs than previously recognized.

