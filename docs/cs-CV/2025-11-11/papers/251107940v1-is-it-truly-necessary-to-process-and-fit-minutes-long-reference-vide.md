---
layout: default
title: Is It Truly Necessary to Process and Fit Minutes-Long Reference Videos for Personalized Talking Face Generation?
---

# Is It Truly Necessary to Process and Fit Minutes-Long Reference Videos for Personalized Talking Face Generation?

**arXiv**: [2511.07940v1](https://arxiv.org/abs/2511.07940) | [PDF](https://arxiv.org/pdf/2511.07940.pdf)

**作者**: Rui-Qing Sun, Ang Li, Zhijing Wu, Tian Lan, Qianyu Lu, Xingshan Yao, Chen Xu, Xian-Ling Mao

---

## 💡 一句话要点

**提出ISExplore策略，通过选择信息丰富短视频段，提升个性化说话人脸生成效率。**

**关键词**: `说话人脸生成` `参考视频选择` `信息丰富段` `NeRF方法` `3D高斯溅射` `效率优化`

## 📋 核心要点

1. 核心问题：传统方法需处理数分钟参考视频，计算负担大，限制实际应用。
2. 方法要点：基于音频多样性、唇动幅度和相机视角，自动选择5秒信息丰富视频段。
3. 实验或效果：在NeRF和3DGS方法中，数据处理和训练速度提升5倍以上，保持高保真输出。

## 📄 摘要（原文）

> Talking Face Generation (TFG) aims to produce realistic and dynamic talking portraits, with broad applications in fields such as digital education, film and television production, e-commerce live streaming, and other related areas. Currently, TFG methods based on Neural Radiated Field (NeRF) or 3D Gaussian sputtering (3DGS) are received widespread attention. They learn and store personalized features from reference videos of each target individual to generate realistic speaking videos. To ensure models can capture sufficient 3D information and successfully learns the lip-audio mapping, previous studies usually require meticulous processing and fitting several minutes of reference video, which always takes hours. The computational burden of processing and fitting long reference videos severely limits the practical application value of these methods.However, is it really necessary to fit such minutes of reference video? Our exploratory case studies show that using some informative reference video segments of just a few seconds can achieve performance comparable to or even better than the full reference video. This indicates that video informative quality is much more important than its length. Inspired by this observation, we propose the ISExplore (short for Informative Segment Explore), a simple-yet-effective segment selection strategy that automatically identifies the informative 5-second reference video segment based on three key data quality dimensions: audio feature diversity, lip movement amplitude, and number of camera views. Extensive experiments demonstrate that our approach increases data processing and training speed by more than 5x for NeRF and 3DGS methods, while maintaining high-fidelity output. Project resources are available at xx.

