---
layout: default
title: Rethinking Visual Intelligence: Insights from Video Pretraining
---

# Rethinking Visual Intelligence: Insights from Video Pretraining

**arXiv**: [2510.24448v1](https://arxiv.org/abs/2510.24448) | [PDF](https://arxiv.org/pdf/2510.24448.pdf)

**作者**: Pablo Acuaviva, Aram Davtyan, Mariam Hassan, Sebastian Stapf, Ahmad Rahimi, Alexandre Alahi, Paolo Favaro

---

## 💡 一句话要点

**提出视频扩散模型预训练以提升视觉智能的数据效率和泛化能力**

**关键词**: `视频扩散模型` `视觉预训练` `归纳偏置` `数据效率` `时空数据` `视觉基础模型`

## 📋 核心要点

1. 核心问题：视觉模型在组合理解、样本效率和通用问题解决方面落后于语言模型
2. 方法要点：利用视频扩散模型预训练，引入时空数据的归纳偏置
3. 实验或效果：在多个基准测试中，视频模型比语言模型数据效率更高

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated that large-scale pretraining
> enables systems to adapt rapidly to new problems with little supervision in the
> language domain. This success, however, has not translated as effectively to
> the visual domain, where models, including LLMs, continue to struggle with
> compositional understanding, sample efficiency, and general-purpose
> problem-solving. We investigate Video Diffusion Models (VDMs) as a promising
> direction for bridging this gap. Pretraining on spatiotemporal data endows
> these models with strong inductive biases for structure and dynamics, which we
> hypothesize can support broad task adaptability. To test this, we design a
> controlled evaluation in which both a pretrained LLM and a pretrained VDM are
> equipped with lightweight adapters and presented with tasks in their natural
> modalities. Across benchmarks including ARC-AGI, ConceptARC, visual games,
> route planning, and cellular automata, VDMs demonstrate higher data efficiency
> than their language counterparts. Taken together, our results indicate that
> video pretraining offers inductive biases that support progress toward visual
> foundation models.

