---
layout: default
title: MUSE: Manipulating Unified Framework for Synthesizing Emotions in Images via Test-Time Optimization
---

# MUSE: Manipulating Unified Framework for Synthesizing Emotions in Images via Test-Time Optimization

**arXiv**: [2511.21051v1](https://arxiv.org/abs/2511.21051) | [PDF](https://arxiv.org/pdf/2511.21051.pdf)

**作者**: Yingjie Xia, Xi Wang, Jinglei Shi, Vicky Kalogeiton, Jian Yang

---

## 💡 一句话要点

**提出MUSE统一框架，通过测试时优化实现图像情感生成与编辑，提升情感准确性和语义多样性。**

**关键词**: `图像情感合成` `测试时优化` `扩散模型` `情感分类器` `多情感损失`

## 📋 核心要点

1. 核心问题：现有方法分离生成与编辑任务，导致效率低下，限制如治疗干预等应用。
2. 方法要点：利用现成情感分类器，基于梯度优化情感令牌，并引入语义相似性指导时机。
3. 实验效果：在生成和编辑任务中优于所有方法，平衡内容、文本提示和情感表达。

## 📄 摘要（原文）

> Images evoke emotions that profoundly influence perception, often prioritized over content. Current Image Emotional Synthesis (IES) approaches artificially separate generation and editing tasks, creating inefficiencies and limiting applications where these tasks naturally intertwine, such as therapeutic interventions or storytelling. In this work, we introduce MUSE, the first unified framework capable of both emotional generation and editing. By adopting a strategy conceptually aligned with Test-Time Scaling (TTS) that widely used in both LLM and diffusion model communities, it avoids the requirement for additional updating diffusion model and specialized emotional synthesis datasets. More specifically, MUSE addresses three key questions in emotional synthesis: (1) HOW to stably guide synthesis by leveraging an off-the-shelf emotion classifier with gradient-based optimization of emotional tokens; (2) WHEN to introduce emotional guidance by identifying the optimal timing using semantic similarity as a supervisory signal; and (3) WHICH emotion to guide synthesis through a multi-emotion loss that reduces interference from inherent and similar emotions. Experimental results show that MUSE performs favorably against all methods for both generation and editing, improving emotional accuracy and semantic diversity while maintaining an optimal balance between desired content, adherence to text prompts, and realistic emotional expression. It establishes a new paradigm for emotion synthesis.

