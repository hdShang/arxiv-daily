---
layout: default
title: Understanding the Performance Gap in Preference Learning: A Dichotomy of RLHF and DPO
---

# Understanding the Performance Gap in Preference Learning: A Dichotomy of RLHF and DPO

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19770" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19770v2</a>
  <a href="https://arxiv.org/pdf/2505.19770.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19770v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19770v2', 'Understanding the Performance Gap in Preference Learning: A Dichotomy of RLHF and DPO')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruizhe Shi, Minhak Song, Runlong Zhou, Zihan Zhang, Maryam Fazel, Simon S. Du

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-26 (更新: 2025-10-03)

**备注**: 30 pages, 5 figures. Improved proofs, and typo fixes

---

## 💡 一句话要点

**提出细致理论分析以理解RLHF与DPO间的性能差距**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `人类反馈强化学习` `直接偏好优化` `性能差距` `表示差距` `样本效率`

## 📋 核心要点

1. 现有方法在处理人类反馈强化学习与直接偏好优化时存在性能差距，尤其是在表示差距的影响下。
2. 论文通过理论分析将性能差距分解为显式和隐式表示差距，并探讨不同模型指定对策略质量的影响。
3. 研究结果显示，在特定条件下，在线DPO能够超越RLHF和标准DPO，且RLHF在样本效率上具有优势。

## 📝 摘要（中文）

本文对人类反馈强化学习（RLHF）与直接偏好优化（DPO）在表示差距下的性能差距进行了细致的理论分析。研究将这一差距分解为两个来源：在精确优化下的显式表示差距和在有限样本下的隐式表示差距。在精确优化设置中，论文表征了奖励模型和策略模型类别的相对能力如何影响最终策略质量。研究表明，RLHF、DPO或在线DPO的表现取决于模型的错误指定类型。值得注意的是，当奖励和策略模型类别同构且均被错误指定时，在线DPO可以超越RLHF和标准DPO。在近似优化设置中，论文提供了一个具体构造，表明RLHF在恢复有效奖励模型时所需的样本显著少于DPO，突显了两阶段学习的统计优势。这些结果为理解RLHF与DPO间的性能差距提供了全面的视角，并为选择合适的方法提供了实用的见解。

## 🔬 方法详解

**问题定义**：本文旨在解决人类反馈强化学习（RLHF）与直接偏好优化（DPO）之间的性能差距，尤其是在表示差距的影响下，现有方法在不同模型指定情况下的表现不尽相同。

**核心思路**：论文通过细致的理论分析，将性能差距分解为显式和隐式表示差距，探讨如何通过优化模型类别的相对能力来改善策略质量。

**技术框架**：研究首先定义了精确优化和近似优化的设置，分析了奖励模型和策略模型的相对能力，然后通过构造示例展示了RLHF和DPO在样本效率上的差异。

**关键创新**：最重要的创新在于将性能差距细分为两种类型的表示差距，并揭示了在线DPO在特定条件下的优越性，这与现有方法的单一视角形成鲜明对比。

**关键设计**：论文中设计了具体的奖励模型和策略模型类别，并通过理论推导和构造示例验证了RLHF在样本效率上的优势，强调了两阶段学习的统计优势。

## 📊 实验亮点

实验结果表明，在特定条件下，在线DPO的性能超越了RLHF和标准DPO，尤其是在奖励和策略模型同构且均被错误指定的情况下。此外，RLHF在样本效率上显著优于DPO，展示了在恢复有效奖励模型时所需样本数量的显著减少。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、推荐系统和自动化决策等。通过理解不同学习方法的性能差距，研究者和工程师可以更有效地选择合适的算法来优化模型性能，从而提升实际应用的效果和效率。未来，该研究可能推动更智能的学习系统的发展，改善人类与机器的协作。

## 📄 摘要（原文）

> We present a fine-grained theoretical analysis of the performance gap between reinforcement learning from human feedback (RLHF) and direct preference optimization (DPO) under a representation gap. Our study decomposes this gap into two sources: an explicit representation gap under exact optimization and an implicit representation gap under finite samples. In the exact optimization setting, we characterize how the relative capacities of the reward and policy model classes influence the final policy qualities. We show that RLHF, DPO, or online DPO can outperform one another depending on type of model mis-specifications. Notably, online DPO can outperform both RLHF and standard DPO when the reward and policy model classes are isomorphic and both mis-specified. In the approximate optimization setting, we provide a concrete construction where the ground-truth reward is implicitly sparse and show that RLHF requires significantly fewer samples than DPO to recover an effective reward model -- highlighting a statistical advantage of two-stage learning. Together, these results provide a comprehensive understanding of the performance gap between RLHF and DPO under various settings, and offer practical insights into when each method is preferred.

