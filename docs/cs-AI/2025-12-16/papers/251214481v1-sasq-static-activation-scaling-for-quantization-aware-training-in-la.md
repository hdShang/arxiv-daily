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

**提出SASQ框架以解决大语言模型量化训练中激活量化因子的优化问题，实现高效静态推理。**

**关键词**: `大语言模型` `模型量化` `量化感知训练` `激活量化` `静态推理` `边缘部署` `轻量级框架` `异常值截断`

## 📋 核心要点

1. 现有量化方法面临动态量化计算开销高、静态量化精度低，以及量化感知训练权重成本大的挑战。
2. SASQ框架仅优化激活量化因子，不改变预训练权重，通过自适应截断异常值来降低量化难度。
3. 在LLaMA2-7B上，SASQ在WikiText2上比QuaRot和FP16模型分别降低5.2%和4.7%的困惑度。

## 📝 摘要（中文）

大语言模型（LLMs）在自然语言任务中表现出色，但其规模增长快于GPU内存进步，导致部署挑战。模型量化通过降低权重和激活精度来缓解此问题，但现有方案面临根本性权衡：动态量化计算开销高且在边缘设备上部署困难，而静态量化则牺牲准确性。现有的量化感知训练（QAT）方法还面临权重训练成本问题。我们提出SASQ：一个专门针对激活量化因子的轻量级QAT框架。SASQ仅优化量化因子（不改变预训练权重），实现高精度的静态推理，同时保持部署效率。SASQ自适应地截断一些异常值，从而降低量化难度，同时保留激活的分布特性。SASQ不仅超越了现有SOTA量化方案，还优于对应的FP16模型。在LLaMA2-7B上，它在WikiText2上实现了比QuaRot低5.2%的困惑度和比FP16模型低4.7%的困惑度。

## 🔬 方法详解

SASQ是一个轻量级量化感知训练框架，专注于优化激活量化因子。整体框架基于预训练模型，仅调整量化参数而不更新权重，实现静态推理。关键技术创新包括自适应截断激活中的异常值，以平衡量化精度和分布保留。与现有方法的主要区别在于避免了权重训练成本，同时通过静态量化因子优化提升准确性，解决了动态量化部署困难和静态量化精度不足的问题。

## 📊 实验亮点

在LLaMA2-7B模型上，SASQ在WikiText2数据集上实现比QuaRot低5.2%的困惑度，甚至优于FP16模型4.7%，展示了其在量化精度和部署效率方面的显著优势。

## 🎯 应用场景

该研究适用于大语言模型的边缘部署和资源受限环境，如移动设备、嵌入式系统，能降低内存和计算需求，提升模型在自然语言处理任务中的实际应用效率。

## 📄 摘要（原文）

> Large language models (LLMs) excel at natural language tasks but face deployment challenges due to their growing size outpacing GPU memory advancements. Model quantization mitigates this issue by lowering weight and activation precision, but existing solutions face fundamental trade-offs: dynamic quantization incurs high computational overhead and poses deployment challenges on edge devices, while static quantization sacrifices accuracy. Existing approaches of quantization-aware training (QAT) further suffer from weight training costs. We propose SASQ: a lightweight QAT framework specifically tailored for activation quantization factors. SASQ exclusively optimizes only the quantization factors (without changing pre-trained weights), enabling static inference with high accuracy while maintaining deployment efficiency. SASQ adaptively truncates some outliers, thereby reducing the difficulty of quantization while preserving the distributional characteristics of the activations. SASQ not only surpasses existing SOTA quantization schemes but also outperforms the corresponding FP16 models. On LLaMA2-7B, it achieves 5.2% lower perplexity than QuaRot and 4.7% lower perplexity than the FP16 model on WikiText2.

