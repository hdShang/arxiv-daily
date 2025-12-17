---
layout: default
title: SASQ: Static Activation Scaling for Quantization-Aware Training in Large Language Models
---

# SASQ: Static Activation Scaling for Quantization-Aware Training in Large Language Models

**arXiv**: [2512.14481v1](https://arxiv.org/abs/2512.14481) | [PDF](https://arxiv.org/pdf/2512.14481.pdf)

**作者**: Shizhuo Mao, Song Chen, Yi Kang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出SASQ静态激活缩放框架，以解决大语言模型量化训练中精度与效率的权衡问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `大语言模型` `模型量化` `量化感知训练` `激活量化` `静态推理` `边缘部署` `轻量级框架` `精度提升`

## 📋 核心要点

1. 现有量化方法面临动态量化计算开销高、静态量化精度低的根本性权衡，且量化感知训练成本高。
2. SASQ框架仅优化激活量化因子，不改变预训练权重，通过自适应截断异常值实现轻量级训练。
3. 在LLaMA2-7B上，SASQ超越SOTA量化方案，甚至优于FP16模型，显著降低困惑度。

## 📝 摘要（中文）

大语言模型（LLMs）在自然语言任务中表现出色，但其规模增长超过了GPU内存的进步，导致部署面临挑战。模型量化通过降低权重和激活的精度来缓解这一问题，但现有解决方案存在根本性权衡：动态量化计算开销高且在边缘设备上部署困难，而静态量化则牺牲了精度。现有的量化感知训练（QAT）方法还面临权重训练成本高的问题。我们提出了SASQ：一个专门针对激活量化因子设计的轻量级QAT框架。SASQ仅优化量化因子（不改变预训练权重），实现了高精度的静态推理，同时保持了部署效率。SASQ自适应地截断一些异常值，从而降低了量化的难度，同时保留了激活的分布特性。SASQ不仅超越了现有的SOTA量化方案，还优于相应的FP16模型。在LLaMA2-7B上，它在WikiText2上实现了比QuaRot低5.2%的困惑度，比FP16模型低4.7%的困惑度。

## 🔬 方法详解

SASQ是一个轻量级的量化感知训练框架，专注于优化激活量化因子。整体框架基于预训练的大语言模型，通过静态方式调整激活的量化参数，而不修改权重。关键技术创新点包括：自适应截断激活中的异常值，以简化量化过程并保持分布特性；仅训练量化因子，避免了权重更新的高成本。与现有方法的主要区别在于：相比动态量化，SASQ实现了静态推理，减少了计算开销；相比传统静态量化，它通过训练提升了精度；相比全量QAT，它大幅降低了训练负担。

## 📊 实验亮点

在LLaMA2-7B模型上，SASQ在WikiText2数据集上实现了比QuaRot量化方案低5.2%的困惑度，甚至比原始FP16模型低4.7%的困惑度，展示了显著的性能提升。

## 🎯 应用场景

该研究适用于大语言模型的边缘部署和资源受限环境，如移动设备、嵌入式系统，能提升模型效率并保持高精度，具有实际部署价值。

## 📄 摘要（原文）

> Large language models (LLMs) excel at natural language tasks but face deployment challenges due to their growing size outpacing GPU memory advancements. Model quantization mitigates this issue by lowering weight and activation precision, but existing solutions face fundamental trade-offs: dynamic quantization incurs high computational overhead and poses deployment challenges on edge devices, while static quantization sacrifices accuracy. Existing approaches of quantization-aware training (QAT) further suffer from weight training costs. We propose SASQ: a lightweight QAT framework specifically tailored for activation quantization factors. SASQ exclusively optimizes only the quantization factors (without changing pre-trained weights), enabling static inference with high accuracy while maintaining deployment efficiency. SASQ adaptively truncates some outliers, thereby reducing the difficulty of quantization while preserving the distributional characteristics of the activations. SASQ not only surpasses existing SOTA quantization schemes but also outperforms the corresponding FP16 models. On LLaMA2-7B, it achieves 5.2% lower perplexity than QuaRot and 4.7% lower perplexity than the FP16 model on WikiText2.

