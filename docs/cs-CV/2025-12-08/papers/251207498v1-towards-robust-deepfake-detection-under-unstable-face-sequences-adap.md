---
layout: default
title: Towards Robust DeepFake Detection under Unstable Face Sequences: Adaptive Sparse Graph Embedding with Order-Free Representation and Explicit Laplacian Spectral Prior
---

# Towards Robust DeepFake Detection under Unstable Face Sequences: Adaptive Sparse Graph Embedding with Order-Free Representation and Explicit Laplacian Spectral Prior

**arXiv**: [2512.07498v1](https://arxiv.org/abs/2512.07498) | [PDF](https://arxiv.org/pdf/2512.07498.pdf)

**作者**: Chih-Chung Hsu, Shao-Ning Chen, Chia-Ming Lee, Yi-Fang Wang, Yi-Shiuan Chou

---

## 💡 一句话要点

**提出拉普拉斯正则化图卷积网络以解决不稳定人脸序列下的DeepFake检测问题**

**关键词**: `DeepFake检测` `图卷积网络` `无序时序表示` `拉普拉斯谱先验` `鲁棒性增强`

## 📋 核心要点

1. 核心问题：现有检测器依赖时序一致且干净的人脸序列，但实际场景中压缩、遮挡和对抗攻击导致人脸检测不稳定
2. 方法要点：构建无序时序图嵌入，基于语义亲和度自适应稀疏图，并引入显式图拉普拉斯谱先验作为高通滤波器
3. 实验或效果：在FF++、Celeb-DFv2和DFDC数据集上实现SOTA性能，显著提升在缺失、遮挡和对抗扰动下的鲁棒性

## 📄 摘要（原文）

> Ensuring the authenticity of video content remains challenging as DeepFake generation becomes increasingly realistic and robust against detection. Most existing detectors implicitly assume temporally consistent and clean facial sequences, an assumption that rarely holds in real-world scenarios where compression artifacts, occlusions, and adversarial attacks destabilize face detection and often lead to invalid or misdetected faces. To address these challenges, we propose a Laplacian-Regularized Graph Convolutional Network (LR-GCN) that robustly detects DeepFakes from noisy or unordered face sequences, while being trained only on clean facial data. Our method constructs an Order-Free Temporal Graph Embedding (OF-TGE) that organizes frame-wise CNN features into an adaptive sparse graph based on semantic affinities. Unlike traditional methods constrained by strict temporal continuity, OF-TGE captures intrinsic feature consistency across frames, making it resilient to shuffled, missing, or heavily corrupted inputs. We further impose a dual-level sparsity mechanism on both graph structure and node features to suppress the influence of invalid faces. Crucially, we introduce an explicit Graph Laplacian Spectral Prior that acts as a high-pass operator in the graph spectral domain, highlighting structural anomalies and forgery artifacts, which are then consolidated by a low-pass GCN aggregation. This sequential design effectively realizes a task-driven spectral band-pass mechanism that suppresses background information and random noise while preserving manipulation cues. Extensive experiments on FF++, Celeb-DFv2, and DFDC demonstrate that LR-GCN achieves state-of-the-art performance and significantly improved robustness under severe global and local disruptions, including missing faces, occlusions, and adversarially perturbed face detections.

