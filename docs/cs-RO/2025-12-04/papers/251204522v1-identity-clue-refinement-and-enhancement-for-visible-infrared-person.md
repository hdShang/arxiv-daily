---
layout: default
title: Identity Clue Refinement and Enhancement for Visible-Infrared Person Re-Identification
---

# Identity Clue Refinement and Enhancement for Visible-Infrared Person Re-Identification

**arXiv**: [2512.04522v1](https://arxiv.org/abs/2512.04522) | [PDF](https://arxiv.org/pdf/2512.04522.pdf)

**作者**: Guoqing Zhang, Zhun Wang, Hairui Wang, Zhonglin Ye, Yuhui Zheng

---

## 💡 一句话要点

**提出ICRE网络以解决可见光-红外行人重识别中的模态差异问题**

**关键词**: `可见光-红外行人重识别` `模态特定属性` `身份知识蒸馏` `跨模态匹配` `特征增强`

## 📋 核心要点

1. 核心问题：现有方法忽视模态特定身份知识，导致跨模态匹配困难
2. 方法要点：设计MPFR模块捕获模态特定属性，SDCE模块蒸馏身份知识指导特征学习
3. 实验或效果：在多个公开数据集上超越现有SOTA方法

## 📄 摘要（原文）

> Visible-Infrared Person Re-Identification (VI-ReID) is a challenging cross-modal matching task due to significant modality discrepancies. While current methods mainly focus on learning modality-invariant features through unified embedding spaces, they often focus solely on the common discriminative semantics across modalities while disregarding the critical role of modality-specific identity-aware knowledge in discriminative feature learning. To bridge this gap, we propose a novel Identity Clue Refinement and Enhancement (ICRE) network to mine and utilize the implicit discriminative knowledge inherent in modality-specific attributes. Initially, we design a Multi-Perception Feature Refinement (MPFR) module that aggregates shallow features from shared branches, aiming to capture modality-specific attributes that are easily overlooked. Then, we propose a Semantic Distillation Cascade Enhancement (SDCE) module, which distills identity-aware knowledge from the aggregated shallow features and guide the learning of modality-invariant features. Finally, an Identity Clues Guided (ICG) Loss is proposed to alleviate the modality discrepancies within the enhanced features and promote the learning of a diverse representation space. Extensive experiments across multiple public datasets clearly show that our proposed ICRE outperforms existing SOTA methods.

