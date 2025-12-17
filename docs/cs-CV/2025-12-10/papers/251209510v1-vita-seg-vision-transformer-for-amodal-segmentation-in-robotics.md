---
layout: default
title: ViTA-Seg: Vision Transformer for Amodal Segmentation in Robotics
---

# ViTA-Seg: Vision Transformer for Amodal Segmentation in Robotics

**arXiv**: [2512.09510v1](https://arxiv.org/abs/2512.09510) | [PDF](https://arxiv.org/pdf/2512.09510.pdf)

**作者**: Donato Caramia, Florian T. Pokorny, Giuseppe Triggiani, Denis Ruffino, David Naso, Paolo Roberto Massenio

---

## 💡 一句话要点

**提出ViTA-Seg视觉Transformer框架，用于机器人遮挡场景的实时全模态分割。**

**关键词**: `全模态分割` `视觉Transformer` `机器人抓取` `遮挡处理` `实时分割` `合成数据集`

## 📋 核心要点

1. 核心问题：机器人箱体拾取中的遮挡影响抓取规划准确性。
2. 方法要点：基于全局注意力的类无关视觉Transformer，支持单头全模态和双头全模态加遮挡掩码预测。
3. 实验或效果：在COOCA和KINS基准上验证了高精度与计算效率，并引入ViTA-SimData合成数据集。

## 📄 摘要（原文）

> Occlusions in robotic bin picking compromise accurate and reliable grasp planning. We present ViTA-Seg, a class-agnostic Vision Transformer framework for real-time amodal segmentation that leverages global attention to recover complete object masks, including hidden regions. We proposte two architectures: a) Single-Head for amodal mask prediction; b) Dual-Head for amodal and occluded mask prediction. We also introduce ViTA-SimData, a photo-realistic synthetic dataset tailored to industrial bin-picking scenario. Extensive experiments on two amodal benchmarks, COOCA and KINS, demonstrate that ViTA-Seg Dual Head achieves strong amodal and occlusion segmentation accuracy with computational efficiency, enabling robust, real-time robotic manipulation.

