---
layout: default
title: WarNav: An Autonomous Driving Benchmark for Segmentation of Navigable Zones in War Scenes
---

# WarNav: An Autonomous Driving Benchmark for Segmentation of Navigable Zones in War Scenes

**arXiv**: [2511.15429v1](https://arxiv.org/abs/2511.15429) | [PDF](https://arxiv.org/pdf/2511.15429.pdf)

**作者**: Marc-Emmanuel Coupvent des Graviers, Hejer Ammar, Christophe Guettier, Yann Dumortier, Romaric Audigier

---

## 💡 一句话要点

**提出WarNav数据集以解决战争场景中自主车辆导航区域分割问题**

**关键词**: `语义分割` `自主驾驶` `战争场景数据集` `非结构化环境` `基准测试`

## 📋 核心要点

1. 核心问题：现有数据集无法覆盖战争等高风险非结构化环境，导致自主车辆导航模型鲁棒性不足
2. 方法要点：基于开源DATTALION图像构建真实数据集，支持语义分割模型开发与基准测试
3. 实验或效果：使用城市场景预训练模型进行基线评估，分析训练数据环境影响，探索无标注图像导航方法

## 📄 摘要（原文）

> We introduce WarNav, a novel real-world dataset constructed from images of the open-source DATTALION repository, specifically tailored to enable the development and benchmarking of semantic segmentation models for autonomous ground vehicle navigation in unstructured, conflict-affected environments. This dataset addresses a critical gap between conventional urban driving resources and the unique operational scenarios encountered by unmanned systems in hazardous and damaged war-zones. We detail the methodological challenges encountered, ranging from data heterogeneity to ethical considerations, providing guidance for future efforts that target extreme operational contexts. To establish performance references, we report baseline results on WarNav using several state-of-the-art semantic segmentation models trained on structured urban scenes. We further analyse the impact of training data environments and propose a first step towards effective navigability in challenging environments with the constraint of having no annotation of the targeted images. Our goal is to foster impactful research that enhances the robustness and safety of autonomous vehicles in high-risk scenarios while being frugal in annotated data.

