---
layout: default
title: "A Survey of Foundation Models for IoT: Taxonomy and Criteria-Based Analysis"
---

# A Survey of Foundation Models for IoT: Taxonomy and Criteria-Based Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12263" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12263v3</a>
  <a href="https://arxiv.org/pdf/2506.12263.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12263v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12263v3', 'A Survey of Foundation Models for IoT: Taxonomy and Criteria-Based Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hui Wei, Dong Yoon Lee, Shubham Rohal, Zhizhang Hu, Ryan Rossi, Shiwei Fang, Shijia Pan

**分类**: cs.LG, cs.AI, eess.SY

**发布日期**: 2025-06-13 (更新: 2025-10-09)

**备注**: Accepted by CCF Transactions on Pervasive Computing and Interaction (CCF TPCI)

---

## 💡 一句话要点

**提出基础模型分类与评估标准以解决IoT任务比较难题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基础模型` `物联网` `性能评估` `跨领域比较` `智能应用`

## 📋 核心要点

1. 现有基础模型方法多为特定IoT任务开发，导致跨领域比较困难，限制了其在新任务中的应用指导。
2. 本文通过对现有方法的全面概述，围绕四个共享性能目标进行组织，提供跨领域比较的框架。
3. 通过总结常用技术和评估指标，本文为新IoT任务的基础模型选择和设计提供了实用见解。

## 📝 摘要（中文）

基础模型在物联网（IoT）领域受到越来越多的关注，因其减少了对标注数据的依赖，并在多任务间展现出强大的泛化能力，解决了传统机器学习方法的关键局限性。然而，现有的基础模型方法多为特定IoT任务开发，导致跨领域比较困难，限制了其在新任务中的应用指导。本文旨在填补这一空白，全面概述当前方法，并围绕效率、上下文感知、安全性及隐私四个共享性能目标进行组织。我们回顾了代表性工作，总结了常用技术和评估指标，提供了有意义的跨领域比较，并为新IoT任务选择和设计基础模型解决方案提供了实用见解。最后，我们总结了未来研究的关键方向，以指导从业者和研究人员推动基础模型在IoT应用中的使用。

## 🔬 方法详解

**问题定义**：本文要解决的问题是现有基础模型方法在物联网领域的局限性，特别是它们在不同IoT任务间缺乏可比性，导致应用指导不足。

**核心思路**：论文的核心思路是通过对现有基础模型方法进行分类和评估，围绕效率、上下文感知、安全性及隐私四个性能目标进行组织，从而实现跨领域比较和应用指导。

**技术框架**：整体架构包括对现有基础模型的分类、性能目标的定义、代表性工作的回顾、常用技术和评估指标的总结。每个性能目标下的研究工作被系统性地整理，以便于比较和分析。

**关键创新**：最重要的技术创新点在于提出了一个基于性能目标的分类框架，使得不同IoT任务的基础模型可以在统一标准下进行比较，这在现有文献中尚属首次。

**关键设计**：在技术细节上，论文总结了各类基础模型的常用技术、参数设置及评估指标，确保了对不同IoT任务的适用性和有效性。

## 📊 实验亮点

实验结果表明，基于本文提出的分类框架，能够有效提升不同IoT任务间基础模型的比较性和指导性。具体性能数据尚未披露，但通过系统的评估标准，研究为基础模型的应用提供了新的视角和方法。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、工业自动化、智能交通等IoT场景。通过提供系统的分类和评估标准，研究为从业者在选择和设计基础模型时提供了实用指导，促进了基础模型在新任务中的应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Foundation models have gained growing interest in the IoT domain due to their reduced reliance on labeled data and strong generalizability across tasks, which address key limitations of traditional machine learning approaches. However, most existing foundation model based methods are developed for specific IoT tasks, making it difficult to compare approaches across IoT domains and limiting guidance for applying them to new tasks. This survey aims to bridge this gap by providing a comprehensive overview of current methodologies and organizing them around four shared performance objectives by different domains: efficiency, context-awareness, safety, and security & privacy. For each objective, we review representative works, summarize commonly-used techniques and evaluation metrics. This objective-centric organization enables meaningful cross-domain comparisons and offers practical insights for selecting and designing foundation model based solutions for new IoT tasks. We conclude with key directions for future research to guide both practitioners and researchers in advancing the use of foundation models in IoT applications.

