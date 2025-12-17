---
layout: default
title: MEGConformer: Conformer-Based MEG Decoder for Robust Speech and Phoneme Classification
---

# MEGConformer: Conformer-Based MEG Decoder for Robust Speech and Phoneme Classification

**arXiv**: [2512.01443v1](https://arxiv.org/abs/2512.01443) | [PDF](https://arxiv.org/pdf/2512.01443.pdf)

**作者**: Xabier de Zuazo, Ibon Saratxaga, Eva Navas

---

## 💡 一句话要点

**提出基于Conformer的MEG解码器，用于鲁棒的语音和音素分类任务。**

**关键词**: `脑磁图解码` `Conformer模型` `语音分类` `音素分类` `数据增强` `信号处理`

## 📋 核心要点

1. 核心问题：解决脑磁图信号在语音检测和音素分类中的解码挑战。
2. 方法要点：采用紧凑Conformer处理原始MEG信号，结合任务特定头和MEG增强技术。
3. 实验或效果：在官方评估中，语音检测达88.9%，音素分类达65.8%，超越基线并进入前十。

## 📄 摘要（原文）

> We present Conformer-based decoders for the LibriBrain 2025 PNPL competition, targeting two foundational MEG tasks: Speech Detection and Phoneme Classification. Our approach adapts a compact Conformer to raw 306-channel MEG signals, with a lightweight convolutional projection layer and task-specific heads. For Speech Detection, a MEG-oriented SpecAugment provided a first exploration of MEG-specific augmentation. For Phoneme Classification, we used inverse-square-root class weighting and a dynamic grouping loader to handle 100-sample averaged examples. In addition, a simple instance-level normalization proved critical to mitigate distribution shifts on the holdout split. Using the official Standard track splits and F1-macro for model selection, our best systems achieved 88.9% (Speech) and 65.8% (Phoneme) on the leaderboard, surpassing the competition baselines and ranking within the top-10 in both tasks. For further implementation details, the technical documentation, source code, and checkpoints are available at https://github.com/neural2speech/libribrain-experiments.

