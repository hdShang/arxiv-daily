---
layout: default
title: Rethinking Driving World Model as Synthetic Data Generator for Perception Tasks
---

# Rethinking Driving World Model as Synthetic Data Generator for Perception Tasks

**arXiv**: [2510.19195v1](https://arxiv.org/abs/2510.19195) | [PDF](https://arxiv.org/pdf/2510.19195.pdf)

**作者**: Kai Zeng, Zhanqian Wu, Kaixin Xiong, Xiaobao Wei, Xiangyu Guo, Zhenxin Zhu, Kalok Ho, Lijun Zhou, Bohan Zeng, Ming Lu, Haiyang Sun, Bing Wang, Guang Chen, Hangjun Ye, Wentao Zhang

---

## 💡 一句话要点

**提出Dream4Drive框架作为合成数据生成器，以增强自动驾驶感知任务性能**

**关键词**: `驾驶世界模型` `合成数据生成` `3D感知引导` `多视角视频编辑` `自动驾驶感知` `角落案例增强`

## 📋 核心要点

1. 现有驾驶世界模型忽视下游感知任务评估，导致合成数据益处不明显
2. Dream4Drive分解视频为3D感知引导图，渲染3D资产并微调模型生成多视角视频
3. 实验显示Dream4Drive在各种训练轮次下有效提升下游感知模型性能

## 📄 摘要（原文）

> Recent advancements in driving world models enable controllable generation of
> high-quality RGB videos or multimodal videos. Existing methods primarily focus
> on metrics related to generation quality and controllability. However, they
> often overlook the evaluation of downstream perception tasks, which are
> $\mathbf{really\ crucial}$ for the performance of autonomous driving. Existing
> methods usually leverage a training strategy that first pretrains on synthetic
> data and finetunes on real data, resulting in twice the epochs compared to the
> baseline (real data only). When we double the epochs in the baseline, the
> benefit of synthetic data becomes negligible. To thoroughly demonstrate the
> benefit of synthetic data, we introduce Dream4Drive, a novel synthetic data
> generation framework designed for enhancing the downstream perception tasks.
> Dream4Drive first decomposes the input video into several 3D-aware guidance
> maps and subsequently renders the 3D assets onto these guidance maps. Finally,
> the driving world model is fine-tuned to produce the edited, multi-view
> photorealistic videos, which can be used to train the downstream perception
> models. Dream4Drive enables unprecedented flexibility in generating multi-view
> corner cases at scale, significantly boosting corner case perception in
> autonomous driving. To facilitate future research, we also contribute a
> large-scale 3D asset dataset named DriveObj3D, covering the typical categories
> in driving scenarios and enabling diverse 3D-aware video editing. We conduct
> comprehensive experiments to show that Dream4Drive can effectively boost the
> performance of downstream perception models under various training epochs.
> Project: $\href{https://wm-research.github.io/Dream4Drive/}{this\ https\ URL}$

