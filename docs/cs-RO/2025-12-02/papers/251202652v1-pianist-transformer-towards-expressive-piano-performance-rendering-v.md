---
layout: default
title: Pianist Transformer: Towards Expressive Piano Performance Rendering via Scalable Self-Supervised Pre-Training
---

# Pianist Transformer: Towards Expressive Piano Performance Rendering via Scalable Self-Supervised Pre-Training

**arXiv**: [2512.02652v1](https://arxiv.org/abs/2512.02652) | [PDF](https://arxiv.org/pdf/2512.02652.pdf)

**作者**: Hong-Jie You, Jie-Jing Shao, Xiao-Wen Yang, Lin-Han Jia, Lan-Zhe Guo, Yu-Feng Li

---

## 💡 一句话要点

**提出Pianist Transformer，通过可扩展的自监督预训练解决钢琴表现力渲染的数据和模型规模限制。**

**关键词**: `钢琴表现力渲染` `自监督预训练` `MIDI数据表示` `不对称架构` `可扩展模型`

## 📋 核心要点

1. 核心问题：现有方法依赖小规模标注数据，限制了数据和模型规模扩展。
2. 方法要点：采用统一MIDI表示和不对称架构，实现自监督预训练，提升渲染效率和质量。
3. 实验或效果：在10B token预训练后，模型达到先进性能，客观指标和主观评分接近人类水平。

## 📄 摘要（原文）

> Existing methods for expressive music performance rendering rely on supervised learning over small labeled datasets, which limits scaling of both data volume and model size, despite the availability of vast unlabeled music, as in vision and language. To address this gap, we introduce Pianist Transformer, with four key contributions: 1) a unified Musical Instrument Digital Interface (MIDI) data representation for learning the shared principles of musical structure and expression without explicit annotation; 2) an efficient asymmetric architecture, enabling longer contexts and faster inference without sacrificing rendering quality; 3) a self-supervised pre-training pipeline with 10B tokens and 135M-parameter model, unlocking data and model scaling advantages for expressive performance rendering; 4) a state-of-the-art performance model, which achieves strong objective metrics and human-level subjective ratings. Overall, Pianist Transformer establishes a scalable path toward human-like performance synthesis in the music domain.

