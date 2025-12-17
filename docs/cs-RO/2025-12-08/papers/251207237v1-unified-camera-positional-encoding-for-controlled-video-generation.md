---
layout: default
title: Unified Camera Positional Encoding for Controlled Video Generation
---

# Unified Camera Positional Encoding for Controlled Video Generation

**arXiv**: [2512.07237v1](https://arxiv.org/abs/2512.07237) | [PDF](https://arxiv.org/pdf/2512.07237.pdf)

**作者**: Cheng Zhang, Boying Li, Meng Wei, Yan-Pei Cao, Camilo Cruz Gambardella, Dinh Phung, Jianfei Cai

---

## 💡 一句话要点

**提出统一相机位置编码UCPE，通过相对射线编码和绝对方向编码增强相机可控视频生成。**

**关键词**: `相机可控视频生成` `统一相机编码` `相对射线编码` `扩散变换器` `多视图任务` `镜头畸变建模`

## 📋 核心要点

1. 现有相机编码依赖简化针孔模型，限制了对真实相机多样内参和镜头畸变的泛化能力。
2. 引入相对射线编码统一相机6自由度位姿、内参和镜头畸变，并识别俯仰和横滚作为绝对方向编码的关键组件。
3. 在相机可控文本到视频生成任务中，UCPE以少于1%可训练参数实现最先进的相机控制性和视觉保真度。

## 📄 摘要（原文）

> Transformers have emerged as a universal backbone across 3D perception, video generation, and world models for autonomous driving and embodied AI, where understanding camera geometry is essential for grounding visual observations in three-dimensional space. However, existing camera encoding methods often rely on simplified pinhole assumptions, restricting generalization across the diverse intrinsics and lens distortions in real-world cameras. We introduce Relative Ray Encoding, a geometry-consistent representation that unifies complete camera information, including 6-DoF poses, intrinsics, and lens distortions. To evaluate its capability under diverse controllability demands, we adopt camera-controlled text-to-video generation as a testbed task. Within this setting, we further identify pitch and roll as two components effective for Absolute Orientation Encoding, enabling full control over the initial camera orientation. Together, these designs form UCPE (Unified Camera Positional Encoding), which integrates into a pretrained video Diffusion Transformer through a lightweight spatial attention adapter, adding less than 1% trainable parameters while achieving state-of-the-art camera controllability and visual fidelity. To facilitate systematic training and evaluation, we construct a large video dataset covering a wide range of camera motions and lens types. Extensive experiments validate the effectiveness of UCPE in camera-controllable video generation and highlight its potential as a general camera representation for Transformers across future multi-view, video, and 3D tasks. Code will be available at https://github.com/chengzhag/UCPE.

