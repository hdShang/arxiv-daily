---
layout: default
title: Breast Cancer VLMs: Clinically Practical Vision-Language Train-Inference Models
---

# Breast Cancer VLMs: Clinically Practical Vision-Language Train-Inference Models

**arXiv**: [2510.25051v1](https://arxiv.org/abs/2510.25051) | [PDF](https://arxiv.org/pdf/2510.25051.pdf)

**作者**: Shunjie-Fabian Zheng, Hyeonjun Lee, Thijs Kooi, Ali Diba

---

## 💡 一句话要点

**提出结合视觉与语言的多模态框架，以提升乳腺癌筛查的临床实用性。**

**关键词**: `乳腺癌筛查` `多模态融合` `视觉语言模型` `计算机辅助诊断` `临床部署`

## 📋 核心要点

1. 核心问题：现有CAD系统难以处理多模态数据和临床历史依赖，影响部署。
2. 方法要点：融合2D乳腺X光片视觉特征与结构化文本描述，使用创新标记化模块。
3. 实验或效果：在多国队列中，癌症检测和钙化识别性能优于单模态基线。

## 📄 摘要（原文）

> Breast cancer remains the most commonly diagnosed malignancy among women in
> the developed world. Early detection through mammography screening plays a
> pivotal role in reducing mortality rates. While computer-aided diagnosis (CAD)
> systems have shown promise in assisting radiologists, existing approaches face
> critical limitations in clinical deployment - particularly in handling the
> nuanced interpretation of multi-modal data and feasibility due to the
> requirement of prior clinical history. This study introduces a novel framework
> that synergistically combines visual features from 2D mammograms with
> structured textual descriptors derived from easily accessible clinical metadata
> and synthesized radiological reports through innovative tokenization modules.
> Our proposed methods in this study demonstrate that strategic integration of
> convolutional neural networks (ConvNets) with language representations achieves
> superior performance to vision transformer-based models while handling
> high-resolution images and enabling practical deployment across diverse
> populations. By evaluating it on multi-national cohort screening mammograms,
> our multi-modal approach achieves superior performance in cancer detection and
> calcification identification compared to unimodal baselines, with particular
> improvements. The proposed method establishes a new paradigm for developing
> clinically viable VLM-based CAD systems that effectively leverage imaging data
> and contextual patient information through effective fusion mechanisms.

