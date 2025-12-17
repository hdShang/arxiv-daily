---
layout: default
title: From Detection to Anticipation: Online Understanding of Struggles across Various Tasks and Activities
---

# From Detection to Anticipation: Online Understanding of Struggles across Various Tasks and Activities

**arXiv**: [2512.09847v1](https://arxiv.org/abs/2512.09847) | [PDF](https://arxiv.org/pdf/2512.09847.pdf)

**作者**: Shijia Feng, Michael Wray, Walterio Mayol-Cuevas

---

## 💡 一句话要点

**提出在线检测与预测模型，以实时识别和预测用户在任务中的困难，适用于智能辅助系统。**

**关键词**: `在线困难检测` `困难预测` `智能辅助系统` `实时应用` `跨任务泛化`

## 📋 核心要点

1. 核心问题：现有研究多关注离线困难分类与定位，但实时应用需在线检测与预测困难。
2. 方法要点：将困难定位重构为在线检测任务，并扩展至预测，采用现成模型作为基线。
3. 实验或效果：在线检测达到70-80%每帧mAP，预测性能略有下降，模型在跨任务泛化中优于随机基线4-20%。

## 📄 摘要（原文）

> Understanding human skill performance is essential for intelligent assistive systems, with struggle recognition offering a natural cue for identifying user difficulties. While prior work focuses on offline struggle classification and localization, real-time applications require models capable of detecting and anticipating struggle online. We reformulate struggle localization as an online detection task and further extend it to anticipation, predicting struggle moments before they occur. We adapt two off-the-shelf models as baselines for online struggle detection and anticipation. Online struggle detection achieves 70-80% per-frame mAP, while struggle anticipation up to 2 seconds ahead yields comparable performance with slight drops. We further examine generalization across tasks and activities and analyse the impact of skill evolution. Despite larger domain gaps in activity-level generalization, models still outperform random baselines by 4-20%. Our feature-based models run at up to 143 FPS, and the whole pipeline, including feature extraction, operates at around 20 FPS, sufficient for real-time assistive applications.

