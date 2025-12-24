---
layout: default
title: "A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings"
---

# A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24550" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24550v2</a>
  <a href="https://arxiv.org/pdf/2505.24550.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24550v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24550v2', 'A*-Thought: Efficient Reasoning via Bidirectional Compression for Low-Resource Settings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoang Xu, Shuo Wang, Xu Han, Zhenghao Liu, Huijia Wu, Peipei Li, Zhiyuan Liu, Maosong Sun, Zhaofeng He

**分类**: cs.CL

**发布日期**: 2025-05-30 (更新: 2025-10-19)

**备注**: Accepted by NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/AI9Stars/AStar-Thought)

---

## 💡 一句话要点

**提出A*-Thought以解决低资源环境下推理效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理模型` `树搜索` `A*算法` `效率提升` `双向评估` `数学任务` `低资源环境`

## 📋 核心要点

1. 现有方法在推理效率上存在不足，过长的思考链导致性能下降。
2. A*-Thought通过树搜索框架识别重要思维，结合A*算法和成本函数实现高效推理。
3. 实验表明，A*-Thought在低预算下提升QwQ-32B性能2.39倍，并在高预算下减少近50%的输出token长度。

## 📝 摘要（中文）

大型推理模型（LRMs）通过延长思考长度实现了卓越的性能，但过长的思考轨迹导致效率降低。现有方法往往假设过度思考，并试图通过压缩思维链来提高推理效率，但这通常会导致性能下降。为了解决这一问题，本文提出了A*-Thought，这是一种基于高效树搜索的统一框架，旨在从这些模型生成的广泛推理链中识别和隔离最重要的思维。该方法将LRMs的推理过程形式化为搜索树，通过结合A*搜索算法和特定于推理路径的成本函数，能够高效压缩思维链并确定高信息密度和低成本的推理路径。实验结果表明，A*-Thought在多个高级数学任务上有效平衡了性能和效率。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型在低资源环境下推理效率低下的问题。现有方法往往假设过度思考，导致推理链冗长，影响性能。

**核心思路**：A*-Thought通过将推理过程视为搜索树，利用A*搜索算法和特定成本函数来高效压缩思维链，提取最重要的推理信息，从而提高推理效率。

**技术框架**：整体架构包括推理树的构建、A*搜索算法的应用和双向重要性评估机制。推理树的每个节点代表一个推理跨度，算法通过评估路径成本来选择最优推理路径。

**关键创新**：A*-Thought的主要创新在于引入了双向重要性评估机制，进一步优化了搜索过程，相较于传统方法，能够在更大的搜索空间中实现更高的效率和性能。

**关键设计**：在参数设置上，成本函数的设计是关键，确保能够有效评估推理路径的价值。此外，算法的实现兼容多种大型推理模型，展示了其广泛的适用性。

## 📊 实验亮点

实验结果显示，A*-Thought在低预算条件下提升了QwQ-32B模型的性能2.39倍，同时在高预算条件下将输出token长度减少近50%。该方法在多个高级数学任务上表现出色，证明了其在性能与效率之间的有效平衡。

## 🎯 应用场景

A*-Thought的研究成果具有广泛的应用潜力，尤其在需要高效推理的低资源环境中，如移动设备、边缘计算和实时决策系统等领域。其高效的推理能力可以为智能助手、自动化系统和教育工具等提供更优质的服务，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Large Reasoning Models (LRMs) achieve superior performance by extending the thought length. However, a lengthy thinking trajectory leads to reduced efficiency. Most of the existing methods are stuck in the assumption of overthinking and attempt to reason efficiently by compressing the Chain-of-Thought, but this often leads to performance degradation. To address this problem, we introduce A*-Thought, an efficient tree search-based unified framework designed to identify and isolate the most essential thoughts from the extensive reasoning chains produced by these models. It formulates the reasoning process of LRMs as a search tree, where each node represents a reasoning span in the giant reasoning space. By combining the A* search algorithm with a cost function specific to the reasoning path, it can efficiently compress the chain of thought and determine a reasoning path with high information density and low cost. In addition, we also propose a bidirectional importance estimation mechanism, which further refines this search process and enhances its efficiency beyond uniform sampling. Extensive experiments on several advanced math tasks show that A*-Thought effectively balances performance and efficiency over a huge search space. Specifically, A*-Thought can improve the performance of QwQ-32B by 2.39$\times$ with low-budget and reduce the length of the output token by nearly 50% with high-budget. The proposed method is also compatible with several other LRMs, demonstrating its generalization capability. The code can be accessed at: https://github.com/AI9Stars/AStar-Thought.

