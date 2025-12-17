---
layout: default
title: Diagnosing Visual Reasoning: Challenges, Insights, and a Path Forward
---

# Diagnosing Visual Reasoning: Challenges, Insights, and a Path Forward

**arXiv**: [2510.20696v1](https://arxiv.org/abs/2510.20696) | [PDF](https://arxiv.org/pdf/2510.20696.pdf)

**作者**: Jing Bi, Guangyu Sun, Ali Vosoughi, Chen Chen, Chenliang Xu

---

## 💡 一句话要点

**提出基于代理的架构以解决多模态大语言模型的视觉幻觉和文本依赖问题**

**关键词**: `多模态大语言模型` `视觉推理诊断` `代理架构` `推理链优化` `视觉幻觉` `基准评估`

## 📋 核心要点

1. 多模态大语言模型在视觉推理中存在视觉幻觉和过度依赖文本先验的问题
2. 采用代理架构结合LLM推理与轻量视觉模块，实现细粒度分析和推理链迭代优化
3. 在MMMU和MathVista基准上显著提升性能，超越更大模型基线

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) that integrate visual and textual
> reasoning leverage chain-of-thought (CoT) prompting to tackle complex visual
> tasks, yet continue to exhibit visual hallucinations and an over-reliance on
> textual priors. We present a systematic diagnosis of state-of-the-art
> vision-language models using a three-stage evaluation framework, uncovering key
> failure modes. To address these, we propose an agent-based architecture that
> combines LLM reasoning with lightweight visual modules, enabling fine-grained
> analysis and iterative refinement of reasoning chains. Our results highlight
> future visual reasoning models should focus on integrating a broader set of
> specialized tools for analyzing visual content. Our system achieves significant
> gains (+10.3 on MMMU, +6.0 on MathVista over a 7B baseline), matching or
> surpassing much larger models. We will release our framework and evaluation
> suite to facilitate future research.

