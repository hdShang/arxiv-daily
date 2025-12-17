---
layout: default
title: AlignSAE: Concept-Aligned Sparse Autoencoders
---

# AlignSAE: Concept-Aligned Sparse Autoencoders

**arXiv**: [2512.02004v1](https://arxiv.org/abs/2512.02004) | [PDF](https://arxiv.org/pdf/2512.02004.pdf)

**作者**: Minglai Yang, Xinyu Guo, Mihai Surdeanu, Liangming Pan

---

## 💡 一句话要点

**提出AlignSAE方法，通过预训练后训练课程对齐稀疏自编码器特征与概念，以解决大语言模型隐藏参数空间难以解释和控制的问题。**

**关键词**: `稀疏自编码器` `概念对齐` `大语言模型` `可解释性` `因果干预`

## 📋 核心要点

1. 核心问题：稀疏自编码器特征与人类定义概念对齐困难，导致特征纠缠和分布表示。
2. 方法要点：采用预训练后训练课程，先无监督训练，后监督后训练，将特定概念绑定到专用潜在槽。
3. 实验或效果：实现精确因果干预，如可靠概念交换，通过针对语义对齐的单个槽。

## 📄 摘要（原文）

> Large Language Models (LLMs) encode factual knowledge within hidden parametric spaces that are difficult to inspect or control. While Sparse Autoencoders (SAEs) can decompose hidden activations into more fine-grained, interpretable features, they often struggle to reliably align these features with human-defined concepts, resulting in entangled and distributed feature representations. To address this, we introduce AlignSAE, a method that aligns SAE features with a defined ontology through a "pre-train, then post-train" curriculum. After an initial unsupervised training phase, we apply supervised post-training to bind specific concepts to dedicated latent slots while preserving the remaining capacity for general reconstruction. This separation creates an interpretable interface where specific relations can be inspected and controlled without interference from unrelated features. Empirical results demonstrate that AlignSAE enables precise causal interventions, such as reliable "concept swaps", by targeting single, semantically aligned slots.

