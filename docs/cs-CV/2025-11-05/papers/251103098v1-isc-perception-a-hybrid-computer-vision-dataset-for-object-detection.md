---
layout: default
title: ISC-Perception: A Hybrid Computer Vision Dataset for Object Detection in Novel Steel Assembly
---

# ISC-Perception: A Hybrid Computer Vision Dataset for Object Detection in Novel Steel Assembly

**arXiv**: [2511.03098v1](https://arxiv.org/abs/2511.03098) | [PDF](https://arxiv.org/pdf/2511.03098.pdf)

**作者**: Miftahur Rahman, Samuel Adebayo, Dorian A. Acevedo-Mejia, David Hester, Daniel McPolin, Karen Rafferty, Debra F. Laefer

---

## 💡 一句话要点

**提出ISC-Perception混合数据集以解决建筑机器人中钢构件检测的数据缺失问题**

**关键词**: `对象检测` `混合数据集` `建筑机器人` `钢构件识别` `合成数据生成`

## 📋 核心要点

1. 核心问题：建筑工地图像采集困难，缺乏专用数据集阻碍钢构件检测
2. 方法要点：结合CAD渲染、游戏引擎合成图像和少量真实照片，实现自动标注
3. 实验或效果：训练检测器mAP@0.50达0.756，优于纯合成或真实数据模型

## 📄 摘要（原文）

> The Intermeshed Steel Connection (ISC) system, when paired with robotic
> manipulators, can accelerate steel-frame assembly and improve worker safety by
> eliminating manual assembly. Dependable perception is one of the initial stages
> for ISC-aware robots. However, this is hampered by the absence of a dedicated
> image corpus, as collecting photographs on active construction sites is
> logistically difficult and raises safety and privacy concerns. In response, we
> introduce ISC-Perception, the first hybrid dataset expressly designed for ISC
> component detection. It blends procedurally rendered CAD images, game-engine
> photorealistic scenes, and a limited, curated set of real photographs, enabling
> fully automatic labelling of the synthetic portion. We explicitly account for
> all human effort to produce the dataset, including simulation engine and scene
> setup, asset preparation, post-processing scripts and quality checks; our total
> human time to generate a 10,000-image dataset was 30.5,h versus 166.7,h for
> manual labelling at 60,s per image (-81.7%). A manual pilot on a representative
> image with five instances of ISC members took 60,s (maximum 80,s), anchoring
> the manual baseline. Detectors trained on ISC-Perception achieved a mean
> Average Precision at IoU 0.50 of 0.756, substantially surpassing models trained
> on synthetic-only or photorealistic-only data. On a 1,200-frame bench test, we
> report mAP@0.50/mAP@[0.50:0.95] of 0.943/0.823. By bridging the data gap for
> construction-robotics perception, ISC-Perception facilitates rapid development
> of custom object detectors and is freely available for research and industrial
> use upon request.

