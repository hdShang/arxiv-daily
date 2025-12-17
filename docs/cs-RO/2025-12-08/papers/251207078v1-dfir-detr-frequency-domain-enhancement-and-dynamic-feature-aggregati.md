---
layout: default
title: DFIR-DETR: Frequency Domain Enhancement and Dynamic Feature Aggregation for Cross-Scene Small Object Detection
---

# DFIR-DETR: Frequency Domain Enhancement and Dynamic Feature Aggregation for Cross-Scene Small Object Detection

**arXiv**: [2512.07078v1](https://arxiv.org/abs/2512.07078) | [PDF](https://arxiv.org/pdf/2512.07078.pdf)

**作者**: Bo Gao, Jingcheng Tong, Xingsheng Chen, Han Yu, Zichen Li

---

## 💡 一句话要点

**提出DFIR-DETR，结合频域增强与动态特征聚合，用于跨场景小目标检测。**

**关键词**: `小目标检测` `Transformer检测器` `频域处理` `动态特征聚合` `轻量模型` `跨场景检测`

## 📋 核心要点

1. 核心问题：小目标特征稀疏、背景杂乱、尺度多变，现有Transformer检测器存在特征退化、长程依赖不足和特征图膨胀问题。
2. 方法要点：引入DCFA模块降低注意力复杂度，DFPN模块防止特征膨胀，FIRC3模块在频域实现全局感受野。
3. 实验或效果：在NEU-DET和VisDrone数据集上达到SOTA，模型轻量，参数11.7M，GFLOPs 41.2，跨场景泛化能力强。

## 📄 摘要（原文）

> Detecting small objects in UAV remote sensing images and identifying surface defects in industrial inspection remain difficult tasks. These applications face common obstacles: features are sparse and weak, backgrounds are cluttered, and object scales vary dramatically. Current transformer-based detectors, while powerful, struggle with three critical issues. First, features degrade severely as networks downsample progressively. Second, spatial convolutions cannot capture long-range dependencies effectively. Third, standard upsampling methods inflate feature maps unnecessarily.
>   We introduce DFIR-DETR to tackle these problems through dynamic feature aggregation combined with frequency-domain processing. Our architecture builds on three novel components. The DCFA module uses dynamic K-sparse attention, cutting complexity from O(N2) down to O(NK), and employs spatial gated linear units for better nonlinear modeling. The DFPN module applies amplitude-normalized upsampling to prevent feature inflation and uses dual-path shuffle convolution to retain spatial details across scales. The FIRC3 module operates in the frequency domain, achieving global receptive fields without sacrificing efficiency.
>   We tested our method extensively on NEU-DET and VisDrone datasets. Results show mAP50 scores of 92.9% and 51.6% respectively-both state-of-the-art. The model stays lightweight with just 11.7M parameters and 41.2 GFLOPs. Strong performance across two very different domains confirms that DFIR-DETR generalizes well and works effectively in resource-limited settings for cross-scene small object detection.

