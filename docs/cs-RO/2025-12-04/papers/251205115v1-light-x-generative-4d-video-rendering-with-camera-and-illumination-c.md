---
layout: default
title: Light-X: Generative 4D Video Rendering with Camera and Illumination Control
---

# Light-X: Generative 4D Video Rendering with Camera and Illumination Control

**arXiv**: [2512.05115v1](https://arxiv.org/abs/2512.05115) | [PDF](https://arxiv.org/pdf/2512.05115.pdf)

**作者**: Tianqi Liu, Zhaoxi Chen, Zihao Huang, Shaocong Xu, Saining Zhang, Chongjie Ye, Bohan Li, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu

---

## 💡 一句话要点

**提出Light-X框架，实现单目视频的相机轨迹与光照联合可控生成渲染**

**关键词**: `4D视频生成` `相机轨迹控制` `光照控制` `解耦渲染` `合成数据集` `单目视频处理`

## 📋 核心要点

1. 核心问题：现有视频光照控制方法在光照保真度与时间一致性间存在权衡，且缺乏相机与光照的联合控制
2. 方法要点：通过解耦几何与光照信号，利用动态点云和重光照帧提供显式细粒度线索，并引入Light-Syn合成训练数据
3. 实验或效果：在联合相机-光照控制上优于基线方法，在文本和背景条件下超越先前视频重光照方法

## 📄 摘要（原文）

> Recent advances in illumination control extend image-based methods to video, yet still facing a trade-off between lighting fidelity and temporal consistency. Moving beyond relighting, a key step toward generative modeling of real-world scenes is the joint control of camera trajectory and illumination, since visual dynamics are inherently shaped by both geometry and lighting. To this end, we present Light-X, a video generation framework that enables controllable rendering from monocular videos with both viewpoint and illumination control. 1) We propose a disentangled design that decouples geometry and lighting signals: geometry and motion are captured via dynamic point clouds projected along user-defined camera trajectories, while illumination cues are provided by a relit frame consistently projected into the same geometry. These explicit, fine-grained cues enable effective disentanglement and guide high-quality illumination. 2) To address the lack of paired multi-view and multi-illumination videos, we introduce Light-Syn, a degradation-based pipeline with inverse-mapping that synthesizes training pairs from in-the-wild monocular footage. This strategy yields a dataset covering static, dynamic, and AI-generated scenes, ensuring robust training. Extensive experiments show that Light-X outperforms baseline methods in joint camera-illumination control and surpasses prior video relighting methods under both text- and background-conditioned settings.

