---
layout: default
title: ELVIS: Enhance Low-Light for Video Instance Segmentation in the Dark
---

# ELVIS: Enhance Low-Light for Video Instance Segmentation in the Dark

**arXiv**: [2512.01495v1](https://arxiv.org/abs/2512.01495) | [PDF](https://arxiv.org/pdf/2512.01495.pdf)

**作者**: Joanne Lin, Ruirui Lin, Yini Li, David Bull, Nantheera Anantrasirichai

---

## 💡 一句话要点

**提出ELVIS框架，通过无监督合成低光视频和增强解码器，提升低光视频实例分割性能。**

**关键词**: `低光视频实例分割` `无监督合成` `域适应` `增强解码器` `VDP-Net` `YouTube-VIS`

## 📋 核心要点

1. 核心问题：低光视频实例分割因噪声、模糊和低对比度等退化而困难，缺乏大规模标注数据和有效合成方法。
2. 方法要点：ELVIS包括无监督合成低光视频管道、VDP-Net和增强解码器头，以解耦退化与内容特征。
3. 实验或效果：在合成低光YouTube-VIS 2019数据集上，性能提升高达+3.7AP。

## 📄 摘要（原文）

> Video instance segmentation (VIS) for low-light content remains highly challenging for both humans and machines alike, due to adverse imaging conditions including noise, blur and low-contrast. The lack of large-scale annotated datasets and the limitations of current synthetic pipelines, particularly in modeling temporal degradations, further hinder progress. Moreover, existing VIS methods are not robust to the degradations found in low-light videos and, as a result, perform poorly even when finetuned on low-light data. In this paper, we introduce \textbf{ELVIS} (\textbf{E}nhance \textbf{L}ow-light for \textbf{V}ideo \textbf{I}nstance \textbf{S}egmentation), a novel framework that enables effective domain adaptation of state-of-the-art VIS models to low-light scenarios. ELVIS comprises an unsupervised synthetic low-light video pipeline that models both spatial and temporal degradations, a calibration-free degradation profile synthesis network (VDP-Net) and an enhancement decoder head that disentangles degradations from content features. ELVIS improves performances by up to \textbf{+3.7AP} on the synthetic low-light YouTube-VIS 2019 dataset. Code will be released upon acceptance.

