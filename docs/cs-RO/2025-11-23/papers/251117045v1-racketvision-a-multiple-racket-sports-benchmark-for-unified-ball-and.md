---
layout: default
title: RacketVision: A Multiple Racket Sports Benchmark for Unified Ball and Racket Analysis
---

# RacketVision: A Multiple Racket Sports Benchmark for Unified Ball and Racket Analysis

**arXiv**: [2511.17045v1](https://arxiv.org/abs/2511.17045) | [PDF](https://arxiv.org/pdf/2511.17045.pdf)

**作者**: Linfeng Dong, Yuchen Yang, Hao Wu, Wei Wang, Yuenan HouZhihang Zhong, Xiao Sun

---

## 💡 一句话要点

**提出RacketVision数据集与基准，以统一分析球拍类运动中的球和球拍。**

**关键词**: `球拍姿态估计` `球轨迹预测` `多模态融合` `运动分析数据集` `计算机视觉基准`

## 📋 核心要点

1. 核心问题：球拍类运动中球跟踪、球拍姿态估计和轨迹预测的复杂交互问题。
2. 方法要点：引入大规模细粒度球拍姿态标注，采用CrossAttention机制融合多模态特征。
3. 实验或效果：CrossAttention提升轨迹预测性能，优于单模态基线。

## 📄 摘要（原文）

> We introduce RacketVision, a novel dataset and benchmark for advancing computer vision in sports analytics, covering table tennis, tennis, and badminton. The dataset is the first to provide large-scale, fine-grained annotations for racket pose alongside traditional ball positions, enabling research into complex human-object interactions. It is designed to tackle three interconnected tasks: fine-grained ball tracking, articulated racket pose estimation, and predictive ball trajectory forecasting. Our evaluation of established baselines reveals a critical insight for multi-modal fusion: while naively concatenating racket pose features degrades performance, a CrossAttention mechanism is essential to unlock their value, leading to trajectory prediction results that surpass strong unimodal baselines. RacketVision provides a versatile resource and a strong starting point for future research in dynamic object tracking, conditional motion forecasting, and multimodal analysis in sports. Project page at https://github.com/OrcustD/RacketVision

