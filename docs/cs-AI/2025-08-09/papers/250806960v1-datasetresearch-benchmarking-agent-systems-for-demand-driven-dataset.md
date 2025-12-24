---
layout: default
title: "DatasetResearch: Benchmarking Agent Systems for Demand-Driven Dataset Discovery"
---

# DatasetResearch: Benchmarking Agent Systems for Demand-Driven Dataset Discovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06960" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06960v1</a>
  <a href="https://arxiv.org/pdf/2508.06960.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06960v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06960v1', 'DatasetResearch: Benchmarking Agent Systems for Demand-Driven Dataset Discovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keyu Li, Mohan Jiang, Dayuan Fu, Yunze Wu, Xiangkun Hu, Dequan Wang, Pengfei Liu

**分类**: cs.AI, cs.CL

**发布日期**: 2025-08-09

**🔗 代码/项目**: [GITHUB](https://github.com/GAIR-NLP/DatasetResearch)

---

## 💡 一句话要点

**提出DatasetResearch以解决数据集发现的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据集发现` `AI代理` `基准评估` `深度学习` `知识管理`

## 📋 核心要点

1. 现有方法在数据集发现上面临挑战，许多有价值的数据集未被有效利用。
2. 本文提出DatasetResearch基准，评估AI代理在满足特定用户需求下发现和合成数据集的能力。
3. 实验结果显示，尽管深度研究系统表现良好，但在复杂任务上仅获得22%的得分，揭示了当前技术的不足。

## 📝 摘要（中文）

随着大语言模型的快速发展，AI发展的瓶颈已从计算能力转向数据可用性，许多有价值的数据集隐藏在专业库和研究附录中。本文提出DatasetResearch，这是第一个全面的基准，评估AI代理发现和合成数据集的能力，涵盖208个真实世界需求。我们的三维评估框架揭示了当前系统的局限性，尽管深度研究系统表现出色，但在挑战性任务上仅获得22%的得分，显示出现有能力与理想数据集发现之间的巨大差距。我们的分析表明，搜索代理在知识任务中表现优异，而合成代理在推理挑战中占据优势，但在“边缘案例”中均表现不佳。该基准为数据集发现代理建立了严格的基线，并为未来自我改进的AI系统奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决AI代理在数据集发现中的局限性，尤其是在满足特定用户需求时的有效性和准确性。现有方法在处理复杂和边缘案例时表现不佳，导致数据集的可用性未能充分发挥。

**核心思路**：论文提出DatasetResearch基准，旨在通过系统性评估AI代理的能力，推动其在数据集发现中的应用。通过构建一个包含真实世界需求的多维评估框架，旨在揭示当前技术的不足并推动未来发展。

**技术框架**：整体架构包括数据集需求的定义、AI代理的搜索与合成能力评估，以及基于真实任务的性能测试。主要模块包括需求分析、数据集检索、合成生成和性能评估。

**关键创新**：最重要的创新在于建立了一个全面的基准，首次系统性地评估AI代理在数据集发现中的表现，并揭示了搜索与合成代理在不同任务中的优势与不足。

**关键设计**：在设计中，采用了多维度评估指标，结合了检索广度与生成结构化内容的能力，确保能够全面反映AI代理的性能。

## 📊 实验亮点

实验结果显示，尽管当前深度研究系统在知识任务中表现良好，但在DatasetResearch-pro子集上仅获得22%的得分，揭示了现有技术与理想数据集发现之间的显著差距。这一发现为未来的研究提供了重要的方向。

## 🎯 应用场景

该研究的潜在应用领域包括数据科学、机器学习模型训练、知识管理等。通过提高数据集发现的效率，能够帮助研究人员和开发者更快地获取所需数据，推动AI系统的自我改进和智能化发展。

## 📄 摘要（原文）

> The rapid advancement of large language models has fundamentally shifted the bottleneck in AI development from computational power to data availability-with countless valuable datasets remaining hidden across specialized repositories, research appendices, and domain platforms. As reasoning capabilities and deep research methodologies continue to evolve, a critical question emerges: can AI agents transcend conventional search to systematically discover any dataset that meets specific user requirements, enabling truly autonomous demand-driven data curation? We introduce DatasetResearch, the first comprehensive benchmark evaluating AI agents' ability to discover and synthesize datasets from 208 real-world demands across knowledge-intensive and reasoning-intensive tasks. Our tri-dimensional evaluation framework reveals a stark reality: even advanced deep research systems achieve only 22% score on our challenging DatasetResearch-pro subset, exposing the vast gap between current capabilities and perfect dataset discovery. Our analysis uncovers a fundamental dichotomy-search agents excel at knowledge tasks through retrieval breadth, while synthesis agents dominate reasoning challenges via structured generation-yet both catastrophically fail on "corner cases" outside existing distributions. These findings establish the first rigorous baseline for dataset discovery agents and illuminate the path toward AI systems capable of finding any dataset in the digital universe. Our benchmark and comprehensive analysis provide the foundation for the next generation of self-improving AI systems and are publicly available at https://github.com/GAIR-NLP/DatasetResearch.

