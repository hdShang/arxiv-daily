---
layout: default
title: Reconstruction as a Bridge for Event-Based Visual Question Answering
---

# Reconstruction as a Bridge for Event-Based Visual Question Answering

**arXiv**: [2512.11510v1](https://arxiv.org/abs/2512.11510) | [PDF](https://arxiv.org/pdf/2512.11510.pdf)

**作者**: Hanyue Lou, Jiayi Zhou, Yang Zhang, Boyu Li, Yi Wang, Guangnan Ye, Boxin Shi

---

## 💡 一句话要点

**提出基于重建的方法以解决事件相机与多模态大语言模型融合中的权衡问题**

**关键词**: `事件相机` `多模态大语言模型` `视觉问答` `重建方法` `稀疏性利用` `基准评测`

## 📋 核心要点

1. 核心问题：事件相机与帧基模型融合需平衡事件数据优势与兼容性
2. 方法要点：设计FRT和ART方法，利用重建作为桥梁，ART利用事件稀疏性提升效率
3. 实验或效果：在EvQA基准上实现最优性能，验证MLLMs在事件视觉中的潜力

## 📄 摘要（原文）

> Integrating event cameras with Multimodal Large Language Models (MLLMs) promises general scene understanding in challenging visual conditions, yet requires navigating a trade-off between preserving the unique advantages of event data and ensuring compatibility with frame-based models. We address this challenge by using reconstruction as a bridge, proposing a straightforward Frame-based Reconstruction and Tokenization (FRT) method and designing an efficient Adaptive Reconstruction and Tokenization (ART) method that leverages event sparsity. For robust evaluation, we introduce EvQA, the first objective, real-world benchmark for event-based MLLMs, comprising 1,000 event-Q&A pairs from 22 public datasets. Our experiments demonstrate that our methods achieve state-of-the-art performance on EvQA, highlighting the significant potential of MLLMs in event-based vision.

