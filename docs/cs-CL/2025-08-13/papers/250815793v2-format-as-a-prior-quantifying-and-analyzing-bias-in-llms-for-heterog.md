---
layout: default
title: "Format as a Prior: Quantifying and Analyzing Bias in LLMs for Heterogeneous Data"
---

# Format as a Prior: Quantifying and Analyzing Bias in LLMs for Heterogeneous Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15793" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15793v2</a>
  <a href="https://arxiv.org/pdf/2508.15793.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15793v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15793v2', 'Format as a Prior: Quantifying and Analyzing Bias in LLMs for Heterogeneous Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiacheng Liu, Mayi Xu, Qiankun Pi, Wenli Li, Ming Zhong, Yuanyuan Zhu, Mengchi Liu, Tieyun Qian

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-13 (更新: 2025-11-14)

**备注**: Accepted by AAAI 2026, camera ready version

---

## 💡 一句话要点

**提出格式偏见分析方法以解决LLMs在异构数据处理中的偏差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `格式偏见` `异构数据` `注意力机制` `数据预处理` `公平性` `鲁棒性`

## 📋 核心要点

1. 现有LLMs在处理异构数据时存在系统性格式偏见，影响其推理能力和下游任务的安全性。
2. 本文提出通过三阶段实证分析，系统量化和分析LLMs中的格式偏见及其影响因素。
3. 研究发现格式偏见在不同模型中普遍存在，并提出数据预处理和推理干预等未来研究方向。

## 📝 摘要（中文）

大型语言模型（LLMs）在处理异构格式信息（如文本、表格、信息框和知识图谱）时，可能存在系统性偏见，这会影响其公正整合异构数据的能力，导致推理错误和下游任务风险增加。本文通过三阶段实证分析，首次全面研究LLMs中的格式偏见，探讨偏见的存在及方向、数据层面因素的影响以及偏见在注意力模式中的表现。研究结果表明，格式偏见在不同模型家族中一致存在，受信息丰富度、结构质量和表示类型驱动，并与LLMs内部的注意力失衡密切相关。基于此，提出了三条未来研究方向，以减少格式偏见。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在处理异构数据时的格式偏见问题。现有方法未能系统性分析偏见的来源及其对模型性能的影响。

**核心思路**：通过三阶段实证分析，探索不同LLMs中的格式偏见及其驱动因素，分析注意力模式中的偏见表现，并测试轻量级干预的有效性。

**技术框架**：研究分为三个阶段：第一阶段评估不同LLMs中的偏见存在及方向；第二阶段分析数据层面因素对偏见的影响；第三阶段探讨注意力模式中的偏见及干预效果。

**关键创新**：首次系统性研究LLMs中的格式偏见，揭示其在不同模型中的一致性及驱动因素，提出了针对格式偏见的干预措施。

**关键设计**：研究中关注信息丰富度、结构质量和表示类型等因素，并通过注意力重加权等方法进行干预，旨在提升模型在异构数据处理中的公平性和鲁棒性。

## 📊 实验亮点

实验结果显示，格式偏见在不同模型家族中普遍存在，且与信息丰富度、结构质量和表示类型密切相关。通过注意力模式分析，发现注意力失衡是偏见的重要表现，提出的干预措施在一定程度上有效改善了模型的表现。

## 🎯 应用场景

该研究为大型语言模型在异构数据处理中的应用提供了重要的理论基础和实践指导，尤其在信息检索、自动问答和数据集成等领域具有广泛的应用潜力。通过减少格式偏见，能够提升模型的公正性和可靠性，促进更安全的人工智能系统的开发。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly employed in applications that require processing information from heterogeneous formats, including texts, tables, infoboxes, and knowledge graphs. However, systematic biases toward particular formats may undermine LLMs' ability to integrate heterogeneous data impartially, potentially resulting in reasoning errors and increased risks in downstream tasks. Yet it remains unclear whether such biases are systematic, which data-level factors drive them, and what internal mechanisms underlie their emergence.
>   In this paper, we present the first comprehensive study of format bias in LLMs through a three-stage empirical analysis. The first stage explores the presence and direction of bias across a diverse range of LLMs. The second stage examines how key data-level factors influence these biases. The third stage analyzes how format bias emerges within LLMs' attention patterns and evaluates a lightweight intervention to test its effectiveness. Our results show that format bias is consistent across model families, driven by information richness, structure quality, and representation type, and is closely associated with attention imbalance within the LLMs. Based on these investigations, we identify three future research directions to reduce format bias: enhancing data pre-processing through format repair and normalization, introducing inference-time interventions such as attention re-weighting, and developing format-balanced training corpora. These directions will support the design of more robust and fair heterogeneous data processing systems.

