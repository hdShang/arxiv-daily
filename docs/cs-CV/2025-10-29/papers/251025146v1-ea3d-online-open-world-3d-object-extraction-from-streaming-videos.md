---
layout: default
title: EA3D: Online Open-World 3D Object Extraction from Streaming Videos
---

# EA3D: Online Open-World 3D Object Extraction from Streaming Videos

**arXiv**: [2510.25146v1](https://arxiv.org/abs/2510.25146) | [PDF](https://arxiv.org/pdf/2510.25146.pdf)

**作者**: Xiaoyu Zhou, Jingqi Wang, Yuang Jia, Yongtao Wang, Deqing Sun, Ming-Hsuan Yang

---

## 💡 一句话要点

**提出EA3D在线框架，从流视频中动态提取开放世界3D对象，实现联合几何重建与场景理解。**

**关键词**: `在线3D重建` `开放世界对象提取` `高斯特征图` `视觉语言模型` `流视频处理` `联合优化`

## 📋 核心要点

1. 当前3D场景理解依赖离线多视图数据或预建几何，限制了实时应用。
2. EA3D使用视觉语言和2D视觉编码器动态提取对象知识，通过在线更新策略嵌入高斯特征图。
3. 实验在渲染、分割、3D框估计等任务中验证了方法的有效性和统一性。

## 📄 摘要（原文）

> Current 3D scene understanding methods are limited by offline-collected
> multi-view data or pre-constructed 3D geometry. In this paper, we present
> ExtractAnything3D (EA3D), a unified online framework for open-world 3D object
> extraction that enables simultaneous geometric reconstruction and holistic
> scene understanding. Given a streaming video, EA3D dynamically interprets each
> frame using vision-language and 2D vision foundation encoders to extract
> object-level knowledge. This knowledge is integrated and embedded into a
> Gaussian feature map via a feed-forward online update strategy. We then
> iteratively estimate visual odometry from historical frames and incrementally
> update online Gaussian features with new observations. A recurrent joint
> optimization module directs the model's attention to regions of interest,
> simultaneously enhancing both geometric reconstruction and semantic
> understanding. Extensive experiments across diverse benchmarks and tasks,
> including photo-realistic rendering, semantic and instance segmentation, 3D
> bounding box and semantic occupancy estimation, and 3D mesh generation,
> demonstrate the effectiveness of EA3D. Our method establishes a unified and
> efficient framework for joint online 3D reconstruction and holistic scene
> understanding, enabling a broad range of downstream tasks.

