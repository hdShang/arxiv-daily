---
layout: default
title: MindCross: Fast New Subject Adaptation with Limited Data for Cross-subject Video Reconstruction from Brain Signals
---

# MindCross: Fast New Subject Adaptation with Limited Data for Cross-subject Video Reconstruction from Brain Signals

**arXiv**: [2511.14196v1](https://arxiv.org/abs/2511.14196) | [PDF](https://arxiv.org/pdf/2511.14196.pdf)

**作者**: Xuan-Hao Liu, Yan-Kai Liu, Tianyi Zhou, Bao-Liang Lu, Wei-Long Zheng

---

## 💡 一句话要点

**提出MindCross框架，通过多编码器与Top-K协作实现快速少数据跨被试视频重建**

**关键词**: `脑信号解码` `跨被试适应` `视频重建` `多编码器框架` `Top-K协作`

## 📋 核心要点

1. 核心问题：跨被试脑信号视频重建数据稀缺，现有方法忽略被试特异性信息，适应慢
2. 方法要点：设计N个特定编码器提取被试特异性信息，共享编码器提取不变信息，Top-K模块协作增强解码
3. 实验或效果：在fMRI/EEG基准上验证，仅需一个模型实现高效跨被试解码与新被试快速适应

## 📄 摘要（原文）

> Reconstructing video from brain signals is an important brain decoding task. Existing brain decoding frameworks are primarily built on a subject-dependent paradigm, which requires large amounts of brain data for each subject. However, the expensive cost of collecting brain-video data causes severe data scarcity. Although some cross-subject methods being introduced, they often overfocus with subject-invariant information while neglecting subject-specific information, resulting in slow fine-tune-based adaptation strategy. To achieve fast and data-efficient new subject adaptation, we propose MindCross, a novel cross-subject framework. MindCross's N specific encoders and one shared encoder are designed to extract subject-specific and subject-invariant information, respectively. Additionally, a Top-K collaboration module is adopted to enhance new subject decoding with the knowledge learned from previous subjects' encoders. Extensive experiments on fMRI/EEG-to-video benchmarks demonstrate MindCross's efficacy and efficiency of cross-subject decoding and new subject adaptation using only one model.

