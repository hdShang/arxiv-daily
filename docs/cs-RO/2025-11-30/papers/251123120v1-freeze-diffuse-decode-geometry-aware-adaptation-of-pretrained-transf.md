---
layout: default
title: Freeze, Diffuse, Decode: Geometry-Aware Adaptation of Pretrained Transformer Embeddings for Antimicrobial Peptide Design
---

# Freeze, Diffuse, Decode: Geometry-Aware Adaptation of Pretrained Transformer Embeddings for Antimicrobial Peptide Design

**arXiv**: [2511.23120v1](https://arxiv.org/abs/2511.23120) | [PDF](https://arxiv.org/pdf/2511.23120.pdf)

**作者**: Pankhil Gawade, Adam Izdebski, Myriam Lizotte, Kevin R. Moon, Jake S. Rhodes, Guy Wolf, Ewa Szczurek

---

## 💡 一句话要点

**提出Freeze, Diffuse, Decode框架，以几何感知方式适应预训练嵌入，用于抗菌肽设计。**

**关键词**: `预训练嵌入适应` `几何感知学习` `扩散模型` `抗菌肽设计` `表示学习`

## 📋 核心要点

1. 核心问题：现有迁移策略在监督数据稀缺时，会扭曲预训练嵌入的几何结构或表达能力不足。
2. 方法要点：通过扩散过程在冻结嵌入的流形上传播监督信号，实现几何感知的嵌入空间适应。
3. 实验或效果：应用于抗菌肽设计，生成低维、可预测、可解释的表示，支持属性预测、检索和插值。

## 📄 摘要（原文）

> Pretrained transformers provide rich, general-purpose embeddings, which are transferred to downstream tasks. However, current transfer strategies: fine-tuning and probing, either distort the pretrained geometric structure of the embeddings or lack sufficient expressivity to capture task-relevant signals. These issues become even more pronounced when supervised data are scarce. Here, we introduce Freeze, Diffuse, Decode (FDD), a novel diffusion-based framework that adapts pre-trained embeddings to downstream tasks while preserving their underlying geometric structure. FDD propagates supervised signal along the intrinsic manifold of frozen embeddings, enabling a geometry-aware adaptation of the embedding space. Applied to antimicrobial peptide design, FDD yields low-dimensional, predictive, and interpretable representations that support property prediction, retrieval, and latent-space interpolation.

