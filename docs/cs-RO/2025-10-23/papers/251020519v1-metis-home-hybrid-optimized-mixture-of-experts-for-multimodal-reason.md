---
layout: default
title: Metis-HOME: Hybrid Optimized Mixture-of-Experts for Multimodal Reasoning
---

# Metis-HOME: Hybrid Optimized Mixture-of-Experts for Multimodal Reasoning

**arXiv**: [2510.20519v1](https://arxiv.org/abs/2510.20519) | [PDF](https://arxiv.org/pdf/2510.20519.pdf)

**作者**: Xiaohan Lan, Fanfan Liu, Haibo Qiu, Siqi Yang, Delian Ruan, Peng Shi, Lin Ma

---

## 💡 一句话要点

**提出混合优化专家框架以解决多模态推理中的效率与泛化权衡问题**

**关键词**: `多模态推理` `混合专家模型` `动态路由` `效率优化` `泛化能力` `Qwen2.5-VL-7B`

## 📋 核心要点

1. 当前多模态大模型在简单查询上计算成本高，且推理专业化损害泛化能力
2. 采用双分支专家结构：思考分支处理复杂推理，非思考分支优化快速推断
3. 实验显示模型在复杂推理和一般能力上均有提升，逆转退化趋势

## 📄 摘要（原文）

> Inspired by recent advancements in LLM reasoning, the field of multimodal
> reasoning has seen remarkable progress, achieving significant performance gains
> on intricate tasks such as mathematical problem-solving. Despite this progress,
> current multimodal large reasoning models exhibit two key limitations. They
> tend to employ computationally expensive reasoning even for simple queries,
> leading to inefficiency. Furthermore, this focus on specialized reasoning often
> impairs their broader, more general understanding capabilities. In this paper,
> we propose Metis-HOME: a Hybrid Optimized Mixture-of-Experts framework designed
> to address this trade-off. Metis-HOME enables a ''Hybrid Thinking'' paradigm by
> structuring the original dense model into two distinct expert branches: a
> thinking branch tailored for complex, multi-step reasoning, and a non-thinking
> branch optimized for rapid, direct inference on tasks like general VQA and OCR.
> A lightweight, trainable router dynamically allocates queries to the most
> suitable expert. We instantiate Metis-HOME by adapting the Qwen2.5-VL-7B into
> an MoE architecture. Comprehensive evaluations reveal that our approach not
> only substantially enhances complex reasoning abilities but also improves the
> model's general capabilities, reversing the degradation trend observed in other
> reasoning-specialized models. Our work establishes a new paradigm for building
> powerful and versatile MLLMs, effectively resolving the prevalent
> reasoning-vs-generalization dilemma.

