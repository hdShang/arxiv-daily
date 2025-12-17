---
layout: default
title: One-to-All Animation: Alignment-Free Character Animation and Image Pose Transfe
---

# One-to-All Animation: Alignment-Free Character Animation and Image Pose Transfe

**arXiv**: [2511.22940v1](https://arxiv.org/abs/2511.22940) | [PDF](https://arxiv.org/pdf/2511.22940.pdf)

**作者**: Shijun Shi, Jing Xu, Zhihang Li, Chunli Peng, Xiaoda Yang, Lijing Lu, Kai Hu, Jiangning Zhang

---

## 💡 一句话要点

**提出One-to-All Animation框架，以解决参考姿态空间不对齐的角色动画与姿态迁移问题。**

**关键词**: `角色动画` `姿态迁移` `扩散模型` `自监督学习` `长视频生成` `参考对齐`

## 📋 核心要点

1. 核心问题：现有方法依赖空间对齐的参考-姿态对，无法处理布局任意或部分可见的参考。
2. 方法要点：通过自监督外绘任务统一输入格式，设计参考提取器与混合融合注意力，并引入身份鲁棒姿态控制。
3. 实验或效果：在广泛实验中优于现有方法，支持高保真动画与长视频生成。

## 📄 摘要（原文）

> Recent advances in diffusion models have greatly improved pose-driven character animation. However, existing methods are limited to spatially aligned reference-pose pairs with matched skeletal structures. Handling reference-pose misalignment remains unsolved. To address this, we present One-to-All Animation, a unified framework for high-fidelity character animation and image pose transfer for references with arbitrary layouts. First, to handle spatially misaligned reference, we reformulate training as a self-supervised outpainting task that transforms diverse-layout reference into a unified occluded-input format. Second, to process partially visible reference, we design a reference extractor for comprehensive identity feature extraction. Further, we integrate hybrid reference fusion attention to handle varying resolutions and dynamic sequence lengths. Finally, from the perspective of generation quality, we introduce identity-robust pose control that decouples appearance from skeletal structure to mitigate pose overfitting, and a token replace strategy for coherent long-video generation. Extensive experiments show that our method outperforms existing approaches. The code and model will be available at https://github.com/ssj9596/One-to-All-Animation.

