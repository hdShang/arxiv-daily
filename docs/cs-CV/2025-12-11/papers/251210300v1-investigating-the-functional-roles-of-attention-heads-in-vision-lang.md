---
layout: default
title: Investigating The Functional Roles of Attention Heads in Vision Language Models: Evidence for Reasoning Modules
---

# Investigating The Functional Roles of Attention Heads in Vision Language Models: Evidence for Reasoning Modules

**arXiv**: [2512.10300v1](https://arxiv.org/abs/2512.10300) | [PDF](https://arxiv.org/pdf/2512.10300.pdf)

**作者**: Yanbei Jiang, Xueqi Ma, Shu Liu, Sarah Monazam Erfani, Tongliang Liu, James Bailey, Jey Han Lau, Krista A. Ehinger

---

## 💡 一句话要点

**提出CogVision数据集与探测方法，分析视觉语言模型中注意力头的功能角色，揭示其在多模态推理中的模块化组织。**

**关键词**: `视觉语言模型` `注意力头分析` `多模态推理` `可解释性框架` `CogVision数据集` `功能头探测`

## 📋 核心要点

1. 核心问题：视觉语言模型内部机制不透明，缺乏对注意力头在多模态推理中功能角色的理解。
2. 方法要点：引入CogVision数据集，将复杂问题分解为子问题，通过探测方法识别与特定认知功能相关的功能头。
3. 实验或效果：发现功能头稀疏且分布不均，干预实验显示其移除导致性能下降，强调则提升准确性。

## 📄 摘要（原文）

> Despite excelling on multimodal benchmarks, vision-language models (VLMs) largely remain a black box. In this paper, we propose a novel interpretability framework to systematically analyze the internal mechanisms of VLMs, focusing on the functional roles of attention heads in multimodal reasoning. To this end, we introduce CogVision, a dataset that decomposes complex multimodal questions into step-by-step subquestions designed to simulate human reasoning through a chain-of-thought paradigm, with each subquestion associated with specific receptive or cognitive functions such as high-level visual reception and inference. Using a probing-based methodology, we identify attention heads that specialize in these functions and characterize them as functional heads. Our analysis across diverse VLM families reveals that these functional heads are universally sparse, vary in number and distribution across functions, and mediate interactions and hierarchical organization. Furthermore, intervention experiments demonstrate their critical role in multimodal reasoning: removing functional heads leads to performance degradation, while emphasizing them enhances accuracy. These findings provide new insights into the cognitive organization of VLMs and suggest promising directions for designing models with more human-aligned perceptual and reasoning abilities.

