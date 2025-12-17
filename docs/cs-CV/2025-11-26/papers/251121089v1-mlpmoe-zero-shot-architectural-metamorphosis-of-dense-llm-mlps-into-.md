---
layout: default
title: MLPMoE: Zero-Shot Architectural Metamorphosis of Dense LLM MLPs into Static Mixture-of-Experts
---

# MLPMoE: Zero-Shot Architectural Metamorphosis of Dense LLM MLPs into Static Mixture-of-Experts

**arXiv**: [2511.21089v1](https://arxiv.org/abs/2511.21089) | [PDF](https://arxiv.org/pdf/2511.21089.pdf)

**作者**: Ivan Novikov

---

## 💡 一句话要点

**提出MLPMoE方法，将稠密LLM MLPs零样本转换为静态MoE以提升计算效率。**

**关键词**: `零样本转换` `混合专家` `结构化稀疏` `推理优化` `张量并行`

## 📋 核心要点

1. 核心问题：稠密LLM推理计算成本高，参数激活冗余。
2. 方法要点：使用张量切片和求和，无需训练或校准数据。
3. 实验效果：在8B模型上，稀疏化移除20%参数，困惑度变化小于2%。

## 📄 摘要（原文）

> Large Language Models (LLMs) are predominantly deployed as dense transformers, where every parameter in every feed-forward block is activated for every token. While architecturally simple, this is computationally inefficient, since inference costs scale linearly with parameter count. Recent upcycling methods such as MoEfication, CMoE, ToMoE, and MoORE reveal that much of the useful computation lives in sparse, semi-modular substructures inside dense feed-forward networks, but these approaches typically rely on clustering, activation profiling, singular value decomposition, or custom routing that requires calibration data. This paper introduces MLPMoE (MLP Mixture-of-Experts), a training-free, deterministic transformation that restructures the dense MLP in transformer blocks into a static, high-cardinality mixture of experts. The transformation uses simple tensor slicing and summation, reinterpreting the algebra of tensor parallelism as a topological conversion rather than a distributed training pattern. We further introduce Fractal Fade (differential branch sparsity) and Compensated Pruning (variance-preserving branch reduction) as lightweight mechanisms for structured sparsity. On Qwen2.5-0.5B-Instruct and DeepSeek-R1-Distill-Llama-8B, the zero-shot MLPMoE transform changes a proxy perplexity metric by less than 0.05 percent while keeping the parameter count effectively constant. On the 8B model, differential sparsity removes about 20 percent of MLP parameters while keeping perplexity within about 2 percent of the dense baseline. The method operates entirely post hoc on existing checkpoints and does not require gradients, calibration sets, or router training. Code is available at https://gist.github.com/iwallarm/fc2ef1eddf226ca7814f9e5e2ae9bad1

