---
layout: default
title: Granular Computing-driven SAM: From Coarse-to-Fine Guidance for Prompt-Free Segmentation
---

# Granular Computing-driven SAM: From Coarse-to-Fine Guidance for Prompt-Free Segmentation

**arXiv**: [2511.19062v1](https://arxiv.org/abs/2511.19062) | [PDF](https://arxiv.org/pdf/2511.19062.pdf)

**作者**: Qiyang Yu, Yu Fang, Tianrui Li, Xuemei Cao, Yan Chen, Jianghao Li, Fan Min, Yi Zhang

---

## 💡 一句话要点

**提出Grc-SAM框架以解决无提示图像分割中的定位和细节建模问题**

**关键词**: `无提示图像分割` `粒度计算` `粗到细框架` `多粒度注意力` `高分辨率分割`

## 📋 核心要点

1. 核心问题：SAM模型缺乏自主区域定位机制和在高分辨率下精细建模能力
2. 方法要点：采用粗到细框架，结合粒度计算和多粒度注意力实现自动分割
3. 实验或效果：实验显示Grc-SAM在准确性和可扩展性上优于基线方法

## 📄 摘要（原文）

> Prompt-free image segmentation aims to generate accurate masks without manual guidance. Typical pre-trained models, notably Segmentation Anything Model (SAM), generate prompts directly at a single granularity level. However, this approach has two limitations: (1) Localizability, lacking mechanisms for autonomous region localization; (2) Scalability, limited fine-grained modeling at high resolution. To address these challenges, we introduce Granular Computing-driven SAM (Grc-SAM), a coarse-to-fine framework motivated by Granular Computing (GrC). First, the coarse stage adaptively extracts high-response regions from features to achieve precise foreground localization and reduce reliance on external prompts. Second, the fine stage applies finer patch partitioning with sparse local swin-style attention to enhance detail modeling and enable high-resolution segmentation. Third, refined masks are encoded as latent prompt embeddings for the SAM decoder, replacing handcrafted prompts with an automated reasoning process. By integrating multi-granularity attention, Grc-SAM bridges granular computing with vision transformers. Extensive experimental results demonstrate Grc-SAM outperforms baseline methods in both accuracy and scalability. It offers a unique granular computational perspective for prompt-free segmentation.

