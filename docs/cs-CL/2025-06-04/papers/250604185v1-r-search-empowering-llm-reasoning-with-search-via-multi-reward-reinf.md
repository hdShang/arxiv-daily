---
layout: default
title: "R-Search: Empowering LLM Reasoning with Search via Multi-Reward Reinforcement Learning"
---

# R-Search: Empowering LLM Reasoning with Search via Multi-Reward Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04185" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04185v1</a>
  <a href="https://arxiv.org/pdf/2506.04185.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04185v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04185v1', 'R-Search: Empowering LLM Reasoning with Search via Multi-Reward Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingfei Zhao, Ruobing Wang, Dingling Xu, Daren Zha, Limin Liu

**分类**: cs.CL

**发布日期**: 2025-06-04

**备注**: 16 pages, 3 figures

**🔗 代码/项目**: [GITHUB](https://github.com/QingFei1/R-Search)

---

## 💡 一句话要点

**提出R-Search以解决LLM推理与搜索交互不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `推理与搜索` `多重奖励` `知识检索` `智能问答` `逻辑推理`

## 📋 核心要点

1. 现有方法在推理与搜索的交互上存在不足，导致LLMs无法有效识别最佳的推理-搜索轨迹，影响响应质量。
2. 本文提出R-Search框架，通过强化学习实现推理与搜索的深度集成，动态决定何时检索或推理，优化交互轨迹。
3. 实验结果显示，R-Search在七个数据集上的性能显著优于现有RAG基线，领域内提升最高达32.2%，领域外提升达25.1%。

## 📝 摘要（中文）

大型语言模型（LLMs）在多步骤和长链推理方面取得了显著进展。然而，将其推理能力扩展到与搜索的深度交互仍然是一个非平凡的挑战，因为模型往往无法识别最佳的推理-搜索交互轨迹，导致响应质量不佳。为此，本文提出了R-Search，一个新颖的强化学习框架，旨在实现推理与搜索的集成，使LLMs能够自主执行多步骤推理并与搜索深度交互，通过多重奖励信号学习最佳的推理搜索交互轨迹，从而提高复杂逻辑和知识密集型任务的响应质量。实验结果表明，R-Search在七个数据集上的表现优于先进的RAG基线，提升幅度最高可达32.2%（领域内）和25.1%（领域外）。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在推理与搜索交互中的不足，现有方法无法有效识别最佳的推理-搜索交互轨迹，导致响应质量不佳。

**核心思路**：R-Search框架通过强化学习实现推理与搜索的深度集成，允许模型自主决定何时进行检索或推理，并通过多重奖励信号优化交互轨迹。

**技术框架**：R-Search的整体架构包括多个模块，首先是推理模块和搜索模块的集成，其次是动态决策机制，最后是多阶段、多类型奖励的设计，以优化推理-搜索轨迹。

**关键创新**：R-Search的主要创新在于通过多重奖励信号联合优化推理与搜索的交互轨迹，这一方法与传统的单一奖励机制显著不同，能够更好地引导模型学习。

**关键设计**：在设计上，R-Search采用了多阶段的奖励机制，结合了不同类型的奖励信号，以确保模型在推理与搜索之间的平衡，同时在损失函数和网络结构上进行了优化，以提升整体性能。

## 📊 实验亮点

在七个数据集上的实验结果表明，R-Search在领域内的性能提升最高可达32.2%，在领域外的提升幅度达到25.1%。这些结果显示出R-Search在推理与搜索集成方面的显著优势，超越了现有的RAG基线，证明了其有效性和实用性。

## 🎯 应用场景

R-Search的研究成果具有广泛的应用潜力，尤其在需要复杂逻辑推理和知识检索的领域，如智能问答系统、知识图谱构建和自动化客服等。通过提升LLMs的推理与搜索能力，该框架能够显著改善用户体验和系统效率，未来可能推动更智能的对话系统和信息检索技术的发展。

## 📄 摘要（原文）

> Large language models (LLMs) have notably progressed in multi-step and long-chain reasoning. However, extending their reasoning capabilities to encompass deep interactions with search remains a non-trivial challenge, as models often fail to identify optimal reasoning-search interaction trajectories, resulting in suboptimal responses. We propose R-Search, a novel reinforcement learning framework for Reasoning-Search integration, designed to enable LLMs to autonomously execute multi-step reasoning with deep search interaction, and learn optimal reasoning search interaction trajectories via multi-reward signals, improving response quality in complex logic- and knowledge-intensive tasks. R-Search guides the LLM to dynamically decide when to retrieve or reason, while globally integrating key evidence to enhance deep knowledge interaction between reasoning and search. During RL training, R-Search provides multi-stage, multi-type rewards to jointly optimize the reasoning-search trajectory. Experiments on seven datasets show that R-Search outperforms advanced RAG baselines by up to 32.2% (in-domain) and 25.1% (out-of-domain). The code and data are available at https://github.com/QingFei1/R-Search.

