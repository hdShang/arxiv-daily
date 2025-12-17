---
layout: default
title: SceneMaker: Open-set 3D Scene Generation with Decoupled De-occlusion and Pose Estimation Model
---

# SceneMaker: Open-set 3D Scene Generation with Decoupled De-occlusion and Pose Estimation Model

**arXiv**: [2512.10957v1](https://arxiv.org/abs/2512.10957) | [PDF](https://arxiv.org/pdf/2512.10957.pdf)

**作者**: Yukai Shi, Weiyu Li, Zihao Wang, Hongyang Li, Xingyu Chen, Ping Tan, Lei Zhang

---

## 💡 一句话要点

**提出SceneMaker框架，通过解耦去遮挡与姿态估计解决开放集3D场景生成问题。**

**关键词**: `3D场景生成` `去遮挡模型` `姿态估计` `开放集学习` `注意力机制`

## 📋 核心要点

1. 现有方法在严重遮挡和开放集下难以同时生成高质量几何与准确姿态。
2. 解耦去遮挡模型，利用图像和去遮挡数据集增强开放集遮挡处理能力。
3. 构建统一姿态估计模型，结合全局与局部注意力机制，并在开放集场景数据集上验证。

## 📄 摘要（原文）

> We propose a decoupled 3D scene generation framework called SceneMaker in this work. Due to the lack of sufficient open-set de-occlusion and pose estimation priors, existing methods struggle to simultaneously produce high-quality geometry and accurate poses under severe occlusion and open-set settings. To address these issues, we first decouple the de-occlusion model from 3D object generation, and enhance it by leveraging image datasets and collected de-occlusion datasets for much more diverse open-set occlusion patterns. Then, we propose a unified pose estimation model that integrates global and local mechanisms for both self-attention and cross-attention to improve accuracy. Besides, we construct an open-set 3D scene dataset to further extend the generalization of the pose estimation model. Comprehensive experiments demonstrate the superiority of our decoupled framework on both indoor and open-set scenes. Our codes and datasets is released at https://idea-research.github.io/SceneMaker/.

