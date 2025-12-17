---
layout: default
title: BEVDilation: LiDAR-Centric Multi-Modal Fusion for 3D Object Detection
---

# BEVDilation: LiDAR-Centric Multi-Modal Fusion for 3D Object Detection

**arXiv**: [2512.02972v1](https://arxiv.org/abs/2512.02972) | [PDF](https://arxiv.org/pdf/2512.02972.pdf)

**作者**: Guowen Zhang, Chenhang He, Liyi Chen, Lei Zhang

---

## 💡 一句话要点

**提出BEVDilation，以LiDAR为中心的融合框架解决多模态3D检测中的几何错位问题**

**关键词**: `3D目标检测` `多模态融合` `鸟瞰图表示` `LiDAR中心化` `稀疏点云增强` `语义指导`

## 📋 核心要点

1. 核心问题：LiDAR与相机几何精度差异导致直接融合性能下降
2. 方法要点：通过图像BEV特征作为隐式指导，优先LiDAR信息，缓解空间错位
3. 实验或效果：在nuScenes基准上优于现有方法，对深度噪声更鲁棒

## 📄 摘要（原文）

> Integrating LiDAR and camera information in the bird's eye view (BEV) representation has demonstrated its effectiveness in 3D object detection. However, because of the fundamental disparity in geometric accuracy between these sensors, indiscriminate fusion in previous methods often leads to degraded performance. In this paper, we propose BEVDilation, a novel LiDAR-centric framework that prioritizes LiDAR information in the fusion. By formulating image BEV features as implicit guidance rather than naive concatenation, our strategy effectively alleviates the spatial misalignment caused by image depth estimation errors. Furthermore, the image guidance can effectively help the LiDAR-centric paradigm to address the sparsity and semantic limitations of point clouds. Specifically, we propose a Sparse Voxel Dilation Block that mitigates the inherent point sparsity by densifying foreground voxels through image priors. Moreover, we introduce a Semantic-Guided BEV Dilation Block to enhance the LiDAR feature diffusion processing with image semantic guidance and long-range context capture. On the challenging nuScenes benchmark, BEVDilation achieves better performance than state-of-the-art methods while maintaining competitive computational efficiency. Importantly, our LiDAR-centric strategy demonstrates greater robustness to depth noise compared to naive fusion. The source code is available at https://github.com/gwenzhang/BEVDilation.

