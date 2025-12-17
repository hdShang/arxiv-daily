---
layout: default
title: StereoDETR: Stereo-based Transformer for 3D Object Detection
---

# StereoDETR: Stereo-based Transformer for 3D Object Detection

**arXiv**: [2511.18788v1](https://arxiv.org/abs/2511.18788) | [PDF](https://arxiv.org/pdf/2511.18788.pdf)

**作者**: Shiyi Mu, Zichong Gu, Zhiqi Ai, Anqi Liu, Yilin Gao, Shugong Xu

---

## 💡 一句话要点

**提出StereoDETR以高效实现基于立体视觉的3D物体检测**

**关键词**: `立体视觉` `3D物体检测` `Transformer` `实时推理` `深度采样` `KITTI基准`

## 📋 核心要点

1. 立体3D检测精度高但计算开销大，推理速度慢于单目方法
2. 结合单目DETR分支和立体分支，通过可微分深度采样耦合
3. 在KITTI基准上实现实时推理，精度竞争领先，速度超越单目方法

## 📄 摘要（原文）

> Compared to monocular 3D object detection, stereo-based 3D methods offer significantly higher accuracy but still suffer from high computational overhead and latency. The state-of-the-art stereo 3D detection method achieves twice the accuracy of monocular approaches, yet its inference speed is only half as fast. In this paper, we propose StereoDETR, an efficient stereo 3D object detection framework based on DETR. StereoDETR consists of two branches: a monocular DETR branch and a stereo branch. The DETR branch is built upon 2D DETR with additional channels for predicting object scale, orientation, and sampling points. The stereo branch leverages low-cost multi-scale disparity features to predict object-level depth maps. These two branches are coupled solely through a differentiable depth sampling strategy. To handle occlusion, we introduce a constrained supervision strategy for sampling points without requiring extra annotations. StereoDETR achieves real-time inference and is the first stereo-based method to surpass monocular approaches in speed. It also achieves competitive accuracy on the public KITTI benchmark, setting new state-of-the-art results on pedestrian and cyclist subsets. The code is available at https://github.com/shiyi-mu/StereoDETR-OPEN.

