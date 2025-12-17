---
layout: default
title: WildfireX-SLAM: A Large-scale Low-altitude RGB-D Dataset for Wildfire SLAM and Beyond
---

# WildfireX-SLAM: A Large-scale Low-altitude RGB-D Dataset for Wildfire SLAM and Beyond

**arXiv**: [2510.27133v1](https://arxiv.org/abs/2510.27133) | [PDF](https://arxiv.org/pdf/2510.27133.pdf)

**作者**: Zhicong Sun, Jacqueline Lo, Jinxing Hu

---

## 💡 一句话要点

**提出WildfireX-SLAM数据集以支持大规模森林场景SLAM研究**

**关键词**: `合成数据集` `SLAM` `3D高斯泼溅` `野火应急` `森林场景` `无人机数据`

## 📋 核心要点

1. 核心问题：缺乏大规模森林场景的高质量SLAM数据集，阻碍3DGS方法在野火应急等应用中的发展。
2. 方法要点：利用Unreal Engine 5构建合成数据集，提供RGB-D图像、真实相机位姿及环境因素控制。
3. 实验或效果：数据集包含5.5k低空图像，覆盖16平方公里，基准测试揭示森林SLAM挑战与改进方向。

## 📄 摘要（原文）

> 3D Gaussian splatting (3DGS) and its subsequent variants have led to
> remarkable progress in simultaneous localization and mapping (SLAM). While most
> recent 3DGS-based SLAM works focus on small-scale indoor scenes, developing
> 3DGS-based SLAM methods for large-scale forest scenes holds great potential for
> many real-world applications, especially for wildfire emergency response and
> forest management. However, this line of research is impeded by the absence of
> a comprehensive and high-quality dataset, and collecting such a dataset over
> real-world scenes is costly and technically infeasible. To this end, we have
> built a large-scale, comprehensive, and high-quality synthetic dataset for SLAM
> in wildfire and forest environments. Leveraging the Unreal Engine 5 Electric
> Dreams Environment Sample Project, we developed a pipeline to easily collect
> aerial and ground views, including ground-truth camera poses and a range of
> additional data modalities from unmanned aerial vehicle. Our pipeline also
> provides flexible controls on environmental factors such as light, weather, and
> types and conditions of wildfire, supporting the need for various tasks
> covering forest mapping, wildfire emergency response, and beyond. The resulting
> pilot dataset, WildfireX-SLAM, contains 5.5k low-altitude RGB-D aerial images
> from a large-scale forest map with a total size of 16 km2. On top of
> WildfireX-SLAM, a thorough benchmark is also conducted, which not only reveals
> the unique challenges of 3DGS-based SLAM in the forest but also highlights
> potential improvements for future works. The dataset and code will be publicly
> available. Project page: https://zhicongsun.github.io/wildfirexslam.

