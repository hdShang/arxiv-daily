---
layout: default
title: GeoWorld: Unlocking the Potential of Geometry Models to Facilitate High-Fidelity 3D Scene Generation
---

# GeoWorld: Unlocking the Potential of Geometry Models to Facilitate High-Fidelity 3D Scene Generation

**arXiv**: [2511.23191v1](https://arxiv.org/abs/2511.23191) | [PDF](https://arxiv.org/pdf/2511.23191.pdf)

**作者**: Yuhao Wan, Lijuan Liu, Jingzhi Zhou, Zihan Zhou, Xuying Zhang, Dongbo Zhang, Shaohui Jiao, Qibin Hou, Ming-Ming Cheng

---

## 💡 一句话要点

**提出GeoWorld，利用几何模型增强视频生成，实现单图像到高保真3D场景生成。**

**关键词**: `3D场景生成` `几何模型` `视频生成` `几何特征` `图像到3D`

## 📋 核心要点

1. 核心问题：现有基于视频模型的图像到3D场景生成方法存在几何失真和内容模糊问题。
2. 方法要点：先生成连续视频帧，再通过几何模型提取全帧几何特征作为条件，并引入几何对齐损失和适应模块增强一致性。
3. 实验或效果：实验表明GeoWorld在单图像和给定相机轨迹下生成高保真3D场景，定性和定量优于先前方法。

## 📄 摘要（原文）

> Previous works leveraging video models for image-to-3D scene generation tend to suffer from geometric distortions and blurry content. In this paper, we renovate the pipeline of image-to-3D scene generation by unlocking the potential of geometry models and present our GeoWorld. Instead of exploiting geometric information obtained from a single-frame input, we propose to first generate consecutive video frames and then take advantage of the geometry model to provide full-frame geometry features, which contain richer information than single-frame depth maps or camera embeddings used in previous methods, and use these geometry features as geometrical conditions to aid the video generation model. To enhance the consistency of geometric structures, we further propose a geometry alignment loss to provide the model with real-world geometric constraints and a geometry adaptation module to ensure the effective utilization of geometry features. Extensive experiments show that our GeoWorld can generate high-fidelity 3D scenes from a single image and a given camera trajectory, outperforming prior methods both qualitatively and quantitatively. Project Page: https://peaes.github.io/GeoWorld/.

