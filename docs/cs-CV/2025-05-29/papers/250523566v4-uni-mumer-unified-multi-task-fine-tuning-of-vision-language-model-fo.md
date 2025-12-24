---
layout: default
title: "Uni-MuMER: Unified Multi-Task Fine-Tuning of Vision-Language Model for Handwritten Mathematical Expression Recognition"
---

# Uni-MuMER: Unified Multi-Task Fine-Tuning of Vision-Language Model for Handwritten Mathematical Expression Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23566" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23566v4</a>
  <a href="https://arxiv.org/pdf/2505.23566.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23566v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23566v4', 'Uni-MuMER: Unified Multi-Task Fine-Tuning of Vision-Language Model for Handwritten Mathematical Expression Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Li, Jin Jiang, Jianhua Zhu, Shuai Peng, Baole Wei, Yuxuan Zhou, Liangcai Gao

**分类**: cs.CV

**发布日期**: 2025-05-29 (更新: 2025-10-25)

**备注**: Accepted by NeurIPS 2025 as a spotlight

**🔗 代码/项目**: [GITHUB](https://github.com/BFlameSwift/Uni-MuMER)

---

## 💡 一句话要点

**提出Uni-MuMER以解决手写数学表达式识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手写数学识别` `视觉-语言模型` `多任务学习` `错误驱动学习` `树状链式思维` `符号计数` `光学字符识别`

## 📋 核心要点

1. 手写数学表达式识别面临符号布局自由度高和书写风格多样性的问题，现有方法难以有效整合。
2. Uni-MuMER通过全面微调视觉-语言模型，结合多个数据驱动任务，注入领域知识以提升识别性能。
3. 在CROHME和HME100K数据集上，Uni-MuMER的性能超越了现有最佳模型，显示出显著的提升效果。

## 📝 摘要（中文）

手写数学表达式识别（HMER）在光学字符识别（OCR）中仍然面临挑战，主要由于符号布局的自由度和书写风格的多样性。以往方法通过孤立的架构修改面临性能瓶颈，难以整合成统一框架。本文提出Uni-MuMER，全面微调视觉-语言模型（VLM）以应对HMER任务，而不修改其架构，有效地将领域特定知识注入通用框架。该方法整合了三个数据驱动任务：树状链式思维（Tree-CoT）用于结构化空间推理，错误驱动学习（EDL）用于减少视觉相似字符之间的混淆，以及符号计数（SC）以提高长表达式的识别一致性。实验结果表明，Uni-MuMER在CROHME和HME100K数据集上实现了超越最优轻量级专用模型SSAN 16.31%的性能提升，以及超越顶级VLM Gemini2.5-flash 24.42%的表现。

## 🔬 方法详解

**问题定义**：本文旨在解决手写数学表达式识别（HMER）中的性能瓶颈，现有方法通过孤立的架构修改难以形成统一的解决方案，导致识别效果不佳。

**核心思路**：Uni-MuMER的核心思路是全面微调一个预训练的视觉-语言模型（VLM），而不改变其架构，从而有效地将领域特定知识融入通用框架中。

**技术框架**：该方法整合了三个主要模块：树状链式思维（Tree-CoT）用于结构化空间推理，错误驱动学习（EDL）用于减少视觉相似字符的混淆，以及符号计数（SC）用于提高长表达式的识别一致性。

**关键创新**：Uni-MuMER的关键创新在于其通过微调VLM来实现跨任务的通用性，避免了以往方法的架构限制，使得模型能够在多个任务上表现出色。

**关键设计**：在模型设计中，采用了特定的损失函数以优化每个任务的学习效果，同时在数据预处理阶段进行了针对性的符号布局和书写风格的增强，以提高模型的鲁棒性。

## 📊 实验亮点

实验结果显示，Uni-MuMER在CROHME和HME100K数据集上取得了超越最佳轻量级专用模型SSAN 16.31%的性能提升，以及超越顶级VLM Gemini2.5-flash 24.42%的表现，展现了其在零-shot设置下的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括教育、科学计算和自动化文档处理等。通过提升手写数学表达式的识别准确性，Uni-MuMER能够在教育技术和智能文档分析中发挥重要作用，未来可能推动更多基于手写输入的智能应用的发展。

## 📄 摘要（原文）

> Handwritten Mathematical Expression Recognition (HMER) remains a persistent challenge in Optical Character Recognition (OCR) due to the inherent freedom of symbol layouts and variability in handwriting styles. Prior methods have faced performance bottlenecks by proposing isolated architectural modifications, making them difficult to integrate coherently into a unified framework. Meanwhile, recent advances in pretrained vision-language models (VLMs) have demonstrated strong cross-task generalization, offering a promising foundation for developing unified solutions. In this paper, we introduce Uni-MuMER, which fully fine-tunes a VLM for the HMER task without modifying its architecture, effectively injecting domain-specific knowledge into a generalist framework. Our method integrates three data-driven tasks: Tree-Aware Chain-of-Thought (Tree-CoT) for structured spatial reasoning, Error-Driven Learning (EDL) for reducing confusion among visually similar characters, and Symbol Counting (SC) for improving recognition consistency in long expressions. Experiments on the CROHME and HME100K datasets show that Uni-MuMER achieves super state-of-the-art performance, outperforming the best lightweight specialized model SSAN by 16.31\% and the top-performing VLM Gemini2.5-flash by 24.42\% under zero-shot setting. Our datasets, models, and code are open-sourced at: {https://github.com/BFlameSwift/Uni-MuMER

