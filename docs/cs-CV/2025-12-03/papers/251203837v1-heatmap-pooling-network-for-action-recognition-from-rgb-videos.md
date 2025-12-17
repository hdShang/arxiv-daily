---
layout: default
title: Heatmap Pooling Network for Action Recognition from RGB Videos
---

# Heatmap Pooling Network for Action Recognition from RGB Videos

**arXiv**: [2512.03837v1](https://arxiv.org/abs/2512.03837) | [PDF](https://arxiv.org/pdf/2512.03837.pdf)

**作者**: Mengyuan Liu, Jinfu Liu, Yongkang Jiang, Bin He

---

## 💡 一句话要点

**提出热图池化网络以解决RGB视频动作识别中的信息冗余和噪声问题。**

**关键词**: `动作识别` `RGB视频` `热图池化` `多模态融合` `反馈池化`

## 📋 核心要点

1. 核心问题：RGB视频动作识别存在信息冗余、噪声敏感和高存储成本。
2. 方法要点：通过反馈池化模块提取信息丰富、鲁棒且简洁的人体池化特征。
3. 实验或效果：在多个基准数据集上验证有效性，优于现有方法。

## 📄 摘要（原文）

> Human action recognition (HAR) in videos has garnered widespread attention due to the rich information in RGB videos. Nevertheless, existing methods for extracting deep features from RGB videos face challenges such as information redundancy, susceptibility to noise and high storage costs. To address these issues and fully harness the useful information in videos, we propose a novel heatmap pooling network (HP-Net) for action recognition from videos, which extracts information-rich, robust and concise pooled features of the human body in videos through a feedback pooling module. The extracted pooled features demonstrate obvious performance advantages over the previously obtained pose data and heatmap features from videos. In addition, we design a spatial-motion co-learning module and a text refinement modulation module to integrate the extracted pooled features with other multimodal data, enabling more robust action recognition. Extensive experiments on several benchmarks namely NTU RGB+D 60, NTU RGB+D 120, Toyota-Smarthome and UAV-Human consistently verify the effectiveness of our HP-Net, which outperforms the existing human action recognition methods. Our code is publicly available at: https://github.com/liujf69/HPNet-Action.

