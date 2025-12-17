---
layout: default
title: Mistake Attribution: Fine-Grained Mistake Understanding in Egocentric Videos
---

# Mistake Attribution: Fine-Grained Mistake Understanding in Egocentric Videos

**arXiv**: [2511.20525v1](https://arxiv.org/abs/2511.20525) | [PDF](https://arxiv.org/pdf/2511.20525.pdf)

**作者**: Yayuan Li, Aadit Jain, Filippos Bellos, Jason J. Corso

---

## 💡 一句话要点

**提出Mistake Attribution任务和MisFormer模型，用于细粒度理解第一人称视频中的人类错误。**

**关键词**: `第一人称视频理解` `错误归因` `细粒度分析` `数据引擎` `注意力模型` `多模态学习`

## 📋 核心要点

1. 核心问题：现有错误理解方法缺乏细粒度输出，无法将错误归因于指令或视频。
2. 方法要点：开发MisEngine数据引擎自动构建错误样本，并设计MisFormer模型统一处理语义、时间和空间维度。
3. 实验或效果：在EPIC-KITCHENS-M和Ego4D-M数据集上，MisFormer优于多种基线方法。

## 📄 摘要（原文）

> We introduce Mistake Attribution (MATT), a task for fine-grained understanding of human mistakes in egocentric video. Unlike prior mistake understanding work, which lacks fine-grained output, MATT concretely attributes mistakes to the input instruction text or the attempt video. MATT determines what part of the instruction is violated (semantic role), when the deviation becomes irreversible (the Point-of-No-Return, PNR), and where the mistake appears in the PNR frame. We develop MisEngine, a data engine that automatically constructs attribution-rich mistake samples from existing datasets and inherits their annotations. Applied to large egocentric corpora, MisEngine yields EPIC-KITCHENS-M and Ego4D-M, two datasets that are up to two orders of magnitude larger than prior mistake datasets. We then present MisFormer, a unified attention-based model for mistake attribution across semantic (what), temporal (when), and spatial (where) dimensions, trained using MisEngine supervision. Experiments on our new datasets and prior benchmarks show that MisFormer outperforms strong video-language, temporal localization, hand-object interaction, and mistake-detection baselines.

