---
layout: default
title: ChipMind: Retrieval-Augmented Reasoning for Long-Context Circuit Design Specifications
---

# ChipMind: Retrieval-Augmented Reasoning for Long-Context Circuit Design Specifications

**arXiv**: [2512.05371v1](https://arxiv.org/abs/2512.05371) | [PDF](https://arxiv.org/pdf/2512.05371.pdf)

**作者**: Changwen Xing, SamZaak Wong, Xinlai Wan, Yanfeng Lu, Mengli Zhang, Zebin Ma, Lei Qi, Zhengxiong Li, Nan Guan, Zhe Jiang, Xi Wang, Jun Yang

---

## 💡 一句话要点

**提出ChipMind框架，通过知识图谱增强推理解决长上下文电路设计规范处理问题**

**关键词**: `长上下文处理` `知识图谱增强` `电路设计规范` `自适应检索` `多跳推理` `LLM辅助硬件设计`

## 📋 核心要点

1. 核心问题：LLMs在集成电路开发中受限于上下文窗口，难以对复杂长规范进行语义建模和多跳推理
2. 方法要点：构建电路知识图谱ChipKG，结合自适应检索和语义过滤实现动态推理
3. 实验或效果：在工业基准上平均提升34.59%，最高达72.73%，优于现有方法

## 📄 摘要（原文）

> While Large Language Models (LLMs) demonstrate immense potential for automating integrated circuit (IC) development, their practical deployment is fundamentally limited by restricted context windows. Existing context-extension methods struggle to achieve effective semantic modeling and thorough multi-hop reasoning over extensive, intricate circuit specifications. To address this, we introduce ChipMind, a novel knowledge graph-augmented reasoning framework specifically designed for lengthy IC specifications. ChipMind first transforms circuit specifications into a domain-specific knowledge graph ChipKG through the Circuit Semantic-Aware Knowledge Graph Construction methodology. It then leverages the ChipKG-Augmented Reasoning mechanism, combining information-theoretic adaptive retrieval to dynamically trace logical dependencies with intent-aware semantic filtering to prune irrelevant noise, effectively balancing retrieval completeness and precision. Evaluated on an industrial-scale specification reasoning benchmark, ChipMind significantly outperforms state-of-the-art baselines, achieving an average improvement of 34.59% (up to 72.73%). Our framework bridges a critical gap between academic research and practical industrial deployment of LLM-aided Hardware Design (LAD).

