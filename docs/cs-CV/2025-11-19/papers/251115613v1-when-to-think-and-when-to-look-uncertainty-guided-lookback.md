---
layout: default
title: When to Think and When to Look: Uncertainty-Guided Lookback
---

# When to Think and When to Look: Uncertainty-Guided Lookback

**arXiv**: [2511.15613v1](https://arxiv.org/abs/2511.15613) | [PDF](https://arxiv.org/pdf/2511.15613.pdf)

**作者**: Jing Bi, Filippos Bellos, Junjia Guo, Yayuan Li, Chao Huang, Yunlong, Tang, Luchuan Song, Susan Liang, Zhongfei, Zhang, Jason J. Corso, Chenliang Xu

---

## 💡 一句话要点

**提出不确定性引导回看方法，以提升大型视觉语言模型的视觉推理性能。**

**关键词**: `大型视觉语言模型` `视觉推理` `不确定性引导` `解码策略` `多模态基准`

## 📋 核心要点

1. 核心问题：长推理链易忽略图像，导致视觉推理性能下降。
2. 方法要点：结合不确定性信号与自适应回看提示，无需训练。
3. 实验效果：在MMMU等基准上提升性能，优于多种解码基线。

## 📄 摘要（原文）

> Test-time thinking (that is, generating explicit intermediate reasoning chains) is known to boost performance in large language models and has recently shown strong gains for large vision language models (LVLMs). However, despite these promising results, there is still no systematic analysis of how thinking actually affects visual reasoning. We provide the first such analysis with a large scale, controlled comparison of thinking for LVLMs, evaluating ten variants from the InternVL3.5 and Qwen3-VL families on MMMU-val under generous token budgets and multi pass decoding. We show that more thinking is not always better; long chains often yield long wrong trajectories that ignore the image and underperform the same models run in standard instruct mode. A deeper analysis reveals that certain short lookback phrases, which explicitly refer back to the image, are strongly enriched in successful trajectories and correlate with better visual grounding. Building on this insight, we propose uncertainty guided lookback, a training free decoding strategy that combines an uncertainty signal with adaptive lookback prompts and breadth search. Our method improves overall MMMU performance, delivers the largest gains in categories where standard thinking is weak, and outperforms several strong decoding baselines, setting a new state of the art under fixed model families and token budgets. We further show that this decoding strategy generalizes, yielding consistent improvements on five additional benchmarks, including two broad multimodal suites and math focused visual reasoning datasets.

