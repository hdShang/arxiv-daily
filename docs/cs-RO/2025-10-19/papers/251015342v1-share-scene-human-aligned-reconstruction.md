---
layout: default
title: SHARE: Scene-Human Aligned Reconstruction
---

# SHARE: Scene-Human Aligned Reconstruction

**arXiv**: [2510.15342v1](https://arxiv.org/abs/2510.15342) | [PDF](https://arxiv.org/pdf/2510.15342.pdf)

**作者**: Joshua Li, Brendan Chharawala, Chang Shu, Xue Bin Peng, Pengcheng Xi

---

## 💡 一句话要点

**提出SHARE方法，利用场景几何线索提升单目视频中3D人体运动重建的准确性。**

**关键词**: `3D人体重建` `场景几何对齐` `单目视频处理` `运动优化` `虚拟环境交互`

## 📋 核心要点

1. 核心问题：现有方法难以在3D空间中准确定位人体，影响虚拟角色与环境的交互。
2. 方法要点：通过迭代优化关键帧人体网格与场景点云对齐，并保持非关键帧相对位置一致性。
3. 实验或效果：在数据集和野外视频中，SHARE优于现有方法，实现更精确的3D人体放置。

## 📄 摘要（原文）

> Animating realistic character interactions with the surrounding environment
> is important for autonomous agents in gaming, AR/VR, and robotics. However,
> current methods for human motion reconstruction struggle with accurately
> placing humans in 3D space. We introduce Scene-Human Aligned REconstruction
> (SHARE), a technique that leverages the scene geometry's inherent spatial cues
> to accurately ground human motion reconstruction. Each reconstruction relies
> solely on a monocular RGB video from a stationary camera. SHARE first estimates
> a human mesh and segmentation mask for every frame, alongside a scene point map
> at keyframes. It iteratively refines the human's positions at these keyframes
> by comparing the human mesh against the human point map extracted from the
> scene using the mask. Crucially, we also ensure that non-keyframe human meshes
> remain consistent by preserving their relative root joint positions to keyframe
> root joints during optimization. Our approach enables more accurate 3D human
> placement while reconstructing the surrounding scene, facilitating use cases on
> both curated datasets and in-the-wild web videos. Extensive experiments
> demonstrate that SHARE outperforms existing methods.

