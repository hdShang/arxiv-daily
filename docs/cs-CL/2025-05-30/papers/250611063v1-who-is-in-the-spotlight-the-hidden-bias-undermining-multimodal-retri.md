---
layout: default
title: Who is in the Spotlight: The Hidden Bias Undermining Multimodal Retrieval-Augmented Generation
---

# Who is in the Spotlight: The Hidden Bias Undermining Multimodal Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11063" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11063v1</a>
  <a href="https://arxiv.org/pdf/2506.11063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11063v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11063v1', 'Who is in the Spotlight: The Hidden Bias Undermining Multimodal Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayu Yao, Shenghua Liu, Yiwei Wang, Lingrui Mei, Baolong Bi, Yuyao Ge, Zhecheng Li, Xueqi Cheng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出位置敏感性指数以解决多模态RAG系统中的偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `生成模型` `位置偏见` `公平性` `知识密集型任务` `可视化分析` `模型优化`

## 📋 核心要点

1. 现有的多模态RAG系统对证据顺序的敏感性导致了不稳定的性能和偏见推理，尤其是在检索项数量或模态多样性增加时。
2. 本文通过引入位置敏感性指数（PSI_p）和可视化框架，系统性地分析了证据位置对多模态RAG性能的影响。
3. 实验结果显示，位置偏见在多模态设置中比单模态设置更为严重，并且随着检索范围的增加，偏见呈对数增长。

## 📝 摘要（中文）

多模态检索增强生成（RAG）系统在知识密集型和开放领域任务中至关重要。然而，现有RAG模型对证据呈现顺序高度敏感，导致性能不稳定和推理偏见。本文首次全面研究了多模态RAG系统中的位置偏见，通过控制实验观察到证据位置与准确率之间的U型曲线。为量化这种偏见，提出了位置敏感性指数（PSI_p），并开发了可视化框架追踪解码器层的注意力分配模式。研究结果表明，多模态交互加剧了位置偏见，并且偏见随检索范围的增加而对数增长。这些发现为RAG中的位置感知分析提供了理论和实证基础，强调了证据重排序或去偏策略的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态RAG系统中由于证据呈现顺序导致的性能不稳定和偏见推理问题。现有方法未能有效处理这一挑战，导致生成结果的公平性和可靠性下降。

**核心思路**：论文提出通过引入位置敏感性指数（PSI_p）来量化位置偏见，并利用可视化工具分析解码器层的注意力分配，从而深入理解证据位置对生成结果的影响。

**技术框架**：研究采用控制实验设计，涵盖文本、图像和混合模态任务。通过不同位置的证据进行实验，观察准确率的变化，并使用PSI_p进行偏见量化。

**关键创新**：最重要的创新在于首次系统性地研究了多模态RAG中的位置偏见，并提出了量化和可视化的工具，这与现有方法的单一模态分析形成鲜明对比。

**关键设计**：在实验中，设计了不同的证据位置组合，并通过对比分析不同模态下的性能变化，使用特定的损失函数来优化模型的生成能力。

## 📊 实验亮点

实验结果表明，随着证据位置的变化，准确率呈现U型曲线，且在多模态交互中位置偏见显著加剧。通过引入PSI_p，研究量化了这一偏见，并为后续的去偏策略提供了理论依据。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、信息检索和多模态内容生成等。通过提高多模态RAG系统的公平性和可靠性，能够在实际应用中提供更准确和公正的生成结果，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Multimodal Retrieval-Augmented Generation (RAG) systems have become essential in knowledge-intensive and open-domain tasks. As retrieval complexity increases, ensuring the robustness of these systems is critical. However, current RAG models are highly sensitive to the order in which evidence is presented, often resulting in unstable performance and biased reasoning, particularly as the number of retrieved items or modality diversity grows. This raises a central question: How does the position of retrieved evidence affect multimodal RAG performance? To answer this, we present the first comprehensive study of position bias in multimodal RAG systems. Through controlled experiments across text-only, image-only, and mixed-modality tasks, we observe a consistent U-shaped accuracy curve with respect to evidence position. To quantify this bias, we introduce the Position Sensitivity Index ($PSI_p$) and develop a visualization framework to trace attention allocation patterns across decoder layers. Our results reveal that multimodal interactions intensify position bias compared to unimodal settings, and that this bias increases logarithmically with retrieval range. These findings offer both theoretical and empirical foundations for position-aware analysis in RAG, highlighting the need for evidence reordering or debiasing strategies to build more reliable and equitable generation systems.

