---
layout: default
title: "Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning"
---

# Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21589" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21589v5</a>
  <a href="https://arxiv.org/pdf/2508.21589.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21589v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21589v5', 'Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zinan Tang, Xin Gao, Qizhi Pei, Zhuoshi Pan, Mengzhang Cai, Jiang Wu, Conghui He, Lijun Wu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-29 (更新: 2025-10-22)

**备注**: Accepted by EMNLP 2025 (Main)

**🔗 代码/项目**: [GITHUB](https://github.com/Word2VecT/Middo)

---

## 💡 一句话要点

**提出Middo框架以解决LLM训练数据优化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `动态数据优化` `闭环学习` `模型微调` `数据选择` `数据精炼` `自我演化` `机器学习`

## 📋 核心要点

1. 现有的微调方法在数据选择和合成上存在局限，无法适应模型能力的动态变化。
2. Middo框架通过模型感知的数据选择和上下文保留的数据精炼，建立了闭环优化系统。
3. 实验结果显示，Middo在多个基准上提升了LLM的性能，平均提高了7.15%的准确率。

## 📝 摘要（中文）

监督微调（SFT）大型语言模型（LLM）本质上依赖于高质量的训练数据。尽管数据选择和数据合成是提高数据质量的常用策略，但现有方法在静态数据集策划方面存在局限，无法适应模型能力的演变。本文提出了Middo，一个自我演化的模型信息动态数据优化框架，采用模型感知的数据选择和上下文保留的数据精炼。与传统的一次性过滤/合成方法不同，我们的框架建立了一个闭环优化系统，能够持续提升数据质量和模型性能。实验表明，Middo在多个基准测试中平均提高了7.15%的准确率，同时保持了原始数据集的规模。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLM）训练中数据质量不足的问题。现有方法在数据选择和合成上往往是静态的，无法适应模型能力的变化，导致训练效果不佳。

**核心思路**：Middo框架通过建立一个自我演化的动态数据优化系统，利用模型感知的方式选择和精炼数据，从而提升训练数据的质量和模型的性能。

**技术框架**：Middo框架主要包括三个模块：自我诊断模块、适应性优化引擎和动态学习机制。自我诊断模块通过三轴模型信号（损失模式、嵌入聚类动态和自对齐分数）识别次优样本，适应性优化引擎则将这些样本转化为有价值的训练点。

**关键创新**：Middo的创新在于其闭环优化系统，能够根据模型能力的演变动态调整数据选择和优化策略，这与传统的一次性数据处理方法有本质区别。

**关键设计**：在设计上，Middo采用了三轴信号分析方法，结合损失函数和自对齐评分来评估样本质量，并通过上下文保留技术确保数据的语义完整性。

## 📊 实验亮点

在多个基准测试中，Middo框架显著提高了LLM的性能，平均准确率提升了7.15%。这一结果表明，Middo在保持原始数据集规模的同时，能够有效优化训练数据质量，展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

Middo框架在大型语言模型的训练中具有广泛的应用潜力，能够有效提升模型的性能和适应性。其动态数据优化机制不仅适用于自然语言处理领域，还可以扩展到其他需要高质量数据的机器学习任务，如图像识别和语音处理等。未来，Middo可能推动人机协作的进一步发展，实现更智能的训练过程。

## 📄 摘要（原文）

> Supervised Fine-Tuning (SFT) Large Language Models (LLM) fundamentally rely on high-quality training data. While data selection and data synthesis are two common strategies to improve data quality, existing approaches often face limitations in static dataset curation that fail to adapt to evolving model capabilities. In this paper, we introduce Middo, a self-evolving Model-informed dynamic data optimization framework that uses model-aware data selection and context-preserving data refinement. Unlike conventional one-off filtering/synthesis methods, our framework establishes a closed-loop optimization system: (1) A self-referential diagnostic module proactively identifies suboptimal samples through tri-axial model signals - loss patterns (complexity), embedding cluster dynamics (diversity), and self-alignment scores (quality); (2) An adaptive optimization engine then transforms suboptimal samples into pedagogically valuable training points while preserving semantic integrity; (3) This optimization process continuously evolves with model capability through dynamic learning principles. Experiments on multiple benchmarks demonstrate that our Middo consistently enhances the quality of seed data and boosts LLM's performance with improving accuracy by 7.15% on average while maintaining the original dataset scale. This work establishes a new paradigm for sustainable LLM training through dynamic human-AI co-evolution of data and models. Our datasets, models, and code are publicly available at https://github.com/Word2VecT/Middo.

