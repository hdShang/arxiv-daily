---
layout: default
title: Some Modalities are More Equal Than Others: Decoding and Architecting Multimodal Integration in MLLMs
---

# Some Modalities are More Equal Than Others: Decoding and Architecting Multimodal Integration in MLLMs

**arXiv**: [2511.22826v1](https://arxiv.org/abs/2511.22826) | [PDF](https://arxiv.org/pdf/2511.22826.pdf)

**作者**: Tianle Chen, Chaitanya Chakka, Arjun Reddy Akula, Xavier Thomas, Deepti Ghadiyaram

---

## 💡 一句话要点

**提出模态对齐调优策略以增强多模态大语言模型在矛盾模态下的鲁棒性**

**关键词**: `多模态大语言模型` `模态对齐` `可解释性分析` `鲁棒性评估` `音频-视觉矛盾`

## 📋 核心要点

1. 核心问题：多模态大语言模型在矛盾模态下缺乏鲁棒推理能力
2. 方法要点：引入MMA-Bench基准，结合黑盒与白盒可解释性技术分析模型脆弱性
3. 实验或效果：通过模态对齐调优提升模型的多模态基础能力，代码与数据集将公开

## 📄 摘要（原文）

> Despite remarkable advancements in Multimodal Large Language Models (MLLMs), a fundamental question remains: are MLLMs robust to contradicting modalities? To rigorously study this, we introduce MMA-Bench comprising videos and tasks that probe a model's reliance on specific modalities. Using black-box and white-box interpretability techniques, we provide a critical analysis of the brittleness of both open- and closed-sourced MLLMs. We show that current MLLMs struggle under misaligned audio-visual pairs and simple misleading text, thereby lacking robust multi-modal reasoning. Building on these findings, we propose a modality alignment tuning strategy to teach the model when to prioritize, leverage, or ignore specific modality cues. Through extensive experiments and analysis, we show that our alignment tuning yields demonstrably stronger multimodal grounding. This work provides both interpretability tools and a clear path toward developing MLLMs with intrinsically reliable cross-modal reasoning. Code and dataset will be publicly available.

