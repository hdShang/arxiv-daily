---
layout: default
title: "StructCoh: Structured Contrastive Learning for Context-Aware Text Semantic Matching"
---

# StructCoh: Structured Contrastive Learning for Context-Aware Text Semantic Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02033" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02033v1</a>
  <a href="https://arxiv.org/pdf/2509.02033.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02033v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02033v1', 'StructCoh: Structured Contrastive Learning for Context-Aware Text Semantic Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chao Xue, Ziyuan Gao

**分类**: cs.CL

**发布日期**: 2025-09-02

**备注**: Accepted by PRICAI 2025

---

## 💡 一句话要点

**提出StructCoh以解决文本语义匹配中的结构性与语义细微差异问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `文本语义匹配` `对比学习` `图神经网络` `结构推理` `层次对比目标` `法律文档分析` `学术抄袭检测`

## 📋 核心要点

1. 现有方法在文本语义匹配中难以捕捉层次结构模式和细微语义差异，导致性能不足。
2. 本文提出StructCoh框架，通过双图编码器和层次对比目标，结合结构推理与表示优化。
3. 在法律文档匹配基准测试中，StructCoh实现了86.7%的F1-score，较现有方法提升6.2%。

## 📝 摘要（中文）

文本语义匹配需要对结构关系和细粒度语义差异的细致理解。尽管预训练语言模型在捕捉词元级交互方面表现出色，但往往忽视层次结构模式，并在细微语义区分上存在困难。本文提出了StructCoh，一个图增强的对比学习框架，结合了结构推理与表示空间优化。该方法的两个关键创新点为：一是通过依赖解析和主题建模构建语义图的双图编码器，利用图同构网络传播结构特征；二是采用层次对比目标，在多个粒度上强制一致性，显著提高了法律文档匹配和学术抄袭检测的效果。

## 🔬 方法详解

**问题定义**：本文旨在解决文本语义匹配中对结构关系和细微语义差异的理解不足的问题。现有方法主要依赖于预训练语言模型，难以有效捕捉层次结构和语义细节。

**核心思路**：StructCoh框架通过引入图增强的对比学习，结合结构推理与表示空间优化，旨在提升文本语义匹配的准确性。通过双图编码器和层次对比目标，增强了模型对结构和语义的理解能力。

**技术框架**：该框架主要包括两个模块：双图编码器和层次对比目标。双图编码器通过依赖解析和主题建模构建语义图，利用图同构网络传播结构特征；层次对比目标则在节点级和图级上进行对比学习，确保语义一致性。

**关键创新**：最重要的创新在于双图编码器的设计和层次对比目标的引入。双图编码器通过图同构网络有效传播结构特征，而层次对比目标则在多个粒度上强制一致性，显著提升了模型的表现。

**关键设计**：在技术细节上，采用了图同构网络进行结构特征传播，并设计了节点级和图级的对比损失函数，以确保语义单位和结构语义的一致性。

## 📊 实验亮点

在实验中，StructCoh在法律法规匹配任务中取得了86.7%的F1-score，相较于现有最先进的方法提升了6.2%。此外，该方法在多个法律文档匹配基准和学术抄袭检测数据集上均表现出显著的性能提升，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括法律文档匹配、学术抄袭检测以及其他需要高精度文本语义理解的场景。通过提升文本语义匹配的准确性，StructCoh有助于提高信息检索、法律分析等领域的效率和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Text semantic matching requires nuanced understanding of both structural relationships and fine-grained semantic distinctions. While pre-trained language models excel at capturing token-level interactions, they often overlook hierarchical structural patterns and struggle with subtle semantic discrimination. In this paper, we proposed StructCoh, a graph-enhanced contrastive learning framework that synergistically combines structural reasoning with representation space optimization. Our approach features two key innovations: (1) A dual-graph encoder constructs semantic graphs via dependency parsing and topic modeling, then employs graph isomorphism networks to propagate structural features across syntactic dependencies and cross-document concept nodes. (2) A hierarchical contrastive objective enforces consistency at multiple granularities: node-level contrastive regularization preserves core semantic units, while graph-aware contrastive learning aligns inter-document structural semantics through both explicit and implicit negative sampling strategies. Experiments on three legal document matching benchmarks and academic plagiarism detection datasets demonstrate significant improvements over state-of-the-art methods. Notably, StructCoh achieves 86.7% F1-score (+6.2% absolute gain) on legal statute matching by effectively identifying argument structure similarities.

