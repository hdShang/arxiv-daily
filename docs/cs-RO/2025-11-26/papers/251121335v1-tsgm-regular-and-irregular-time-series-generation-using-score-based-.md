---
layout: default
title: TSGM: Regular and Irregular Time-series Generation using Score-based Generative Models
---

# TSGM: Regular and Irregular Time-series Generation using Score-based Generative Models

**arXiv**: [2511.21335v1](https://arxiv.org/abs/2511.21335) | [PDF](https://arxiv.org/pdf/2511.21335.pdf)

**作者**: Haksoo Lim, Jaehoon Lee, Sewon Park, Minjung Kim, Noseong Park

---

## 💡 一句话要点

**提出TSGM框架，基于分数生成模型合成规则与不规则时间序列。**

**关键词**: `分数生成模型` `时间序列合成` `条件分数网络` `去噪分数匹配` `规则时间序列` `不规则时间序列`

## 📋 核心要点

1. 核心问题：时间序列合成中采样质量和多样性不足。
2. 方法要点：设计条件分数网络，使用条件去噪分数匹配损失。
3. 实验或效果：在多个数据集上实现最先进的合成性能。

## 📄 摘要（原文）

> Score-based generative models (SGMs) have demonstrated unparalleled sampling quality and diversity in numerous fields, such as image generation, voice synthesis, and tabular data synthesis, etc. Inspired by those outstanding results, we apply SGMs to synthesize time-series by learning its conditional score function. To this end, we present a conditional score network for time-series synthesis, deriving a denoising score matching loss tailored for our purposes. In particular, our presented denoising score matching loss is the conditional denoising score matching loss for time-series synthesis. In addition, our framework is such flexible that both regular and irregular time-series can be synthesized with minimal changes to our model design. Finally, we obtain exceptional synthesis performance on various time-series datasets, achieving state-of-the-art sampling diversity and quality.

