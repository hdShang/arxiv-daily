---
layout: default
title: EgoCampus: Egocentric Pedestrian Eye Gaze Model and Dataset
---

# EgoCampus: Egocentric Pedestrian Eye Gaze Model and Dataset

**arXiv**: [2512.07668v1](https://arxiv.org/abs/2512.07668) | [PDF](https://arxiv.org/pdf/2512.07668.pdf)

**作者**: Ronan John, Aditya Kesari, Vincenzo DiMatteo, Kristin Dana

---

## 💡 一句话要点

**提出EgoCampus数据集和EgoCampusNet方法，以预测户外校园环境中行人导航时的视觉注意力。**

**关键词**: `自我中心视觉` `眼动注视预测` `户外导航` `数据集构建` `行人行为分析`

## 📋 核心要点

1. 核心问题：预测真实世界导航中的人类视觉注意力，特别是在户外校园环境下的行人眼动注视。
2. 方法要点：使用Meta's Project Aria眼镜收集数据，开发EgoCampusNet模型预测行人眼动注视。
3. 实验或效果：数据集包含超过80名行人的6公里户外路径视频，提供眼动注释，模型效果未知。

## 📄 摘要（原文）

> We address the challenge of predicting human visual attention during real-world navigation by measuring and modeling egocentric pedestrian eye gaze in an outdoor campus setting. We introduce the EgoCampus dataset, which spans 25 unique outdoor paths over 6 km across a university campus with recordings from more than 80 distinct human pedestrians, resulting in a diverse set of gaze-annotated videos. The system used for collection, Meta's Project Aria glasses, integrates eye tracking, front-facing RGB cameras, inertial sensors, and GPS to provide rich data from the human perspective. Unlike many prior egocentric datasets that focus on indoor tasks or exclude eye gaze information, our work emphasizes visual attention while subjects walk in outdoor campus paths. Using this data, we develop EgoCampusNet, a novel method to predict eye gaze of navigating pedestrians as they move through outdoor environments. Our contributions provide both a new resource for studying real-world attention and a resource for future work in gaze prediction models for navigation. Dataset and code are available upon request, and will be made publicly available at a later date at https://github.com/ComputerVisionRutgers/EgoCampus .

