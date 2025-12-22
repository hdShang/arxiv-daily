---
layout: default
title: Cooperative Energy Scheduling of Multi-Microgrids Based on Risk-Sensitive Reinforcement Learning
---

# Cooperative Energy Scheduling of Multi-Microgrids Based on Risk-Sensitive Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17246" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17246v1</a>
  <a href="https://arxiv.org/pdf/2512.17246.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17246v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17246v1', 'Cooperative Energy Scheduling of Multi-Microgrids Based on Risk-Sensitive Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rongxiang Zhang, Bo Li, Jinghua Li, Yuguang Song, Ziqing Zhu, Wentao Yang, Zhengmao Li, Edris Pouresmaeil, Joshua Y. Kim

**分类**: eess.SY

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出风险敏感强化学习框架以优化多微电网的能量调度**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `风险敏感强化学习` `多微电网` `能量调度` `共享记忆` `可再生能源管理`

## 📋 核心要点

1. 现有方法未能明确量化个体与联合风险值之间的关系，导致信用分配模糊。
2. 提出了一种风险敏感强化学习框架RRL-SM，通过共享记忆机制提升多微电网调度效率。
3. 实验结果显示，RRL-SM将负荷削减风险降低了84.5%，在可靠性与经济性之间取得了良好平衡。

## 📝 摘要（中文）

随着分布式可再生能源的快速发展，多微电网在提高能源供应的灵活性和可靠性方面发挥着越来越重要的作用。强化学习因其无模型特性在协调策略中展现出巨大潜力。然而，现有方法缺乏对个体与联合风险值关系的明确量化，导致信用分配不清。此外，随着系统复杂性的增加，显式通信的效率也受到影响。为了解决这些挑战，本文提出了一种基于共享记忆的风险敏感强化学习框架（RRL-SM）用于多微电网调度。通过分布式建模和基于注意力的表示，提出了一种风险敏感值因子分解方案，以量化个体与联合风险值之间的关系，从而使局部决策与全球风险目标对齐。实验结果表明，RRL-SM将负荷削减风险降低了84.5%，在可再生能源不确定性下提供了更可靠的合作调度。

## 🔬 方法详解

**问题定义**：本文旨在解决多微电网调度中的风险管理问题，现有方法在个体与联合风险值的量化上存在不足，导致决策效率低下。

**核心思路**：提出风险敏感强化学习框架RRL-SM，通过共享记忆机制和风险敏感值因子分解，提升局部决策与全球目标的一致性，从而优化调度策略。

**技术框架**：RRL-SM框架包括三个主要模块：风险敏感值因子分解模块、共享记忆协调机制和强化学习决策模块。通过全局记忆空间实现隐式协调，增强去中心化决策的整体效率。

**关键创新**：本研究的核心创新在于引入风险敏感值因子分解方案，利用分布式建模和注意力机制量化个体与联合风险值的关系，显著提升了决策的准确性和效率。

**关键设计**：在模型设计中，采用了特定的损失函数以平衡风险与收益，同时在网络结构中引入了注意力机制，以便更好地捕捉风险信息和决策相关性。通过这些设计，RRL-SM能够在复杂环境中实现高效的能量调度。

## 📊 实验亮点

实验结果表明，RRL-SM框架在负荷削减风险方面表现优异，降低幅度达到84.5%。与传统方法相比，该框架在可靠性和经济性之间实现了良好的平衡，显示出其在复杂能源管理场景中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能电网、可再生能源管理和分布式能源系统。通过优化多微电网的调度策略，能够有效提高能源利用效率，降低运营成本，增强系统的灵活性和可靠性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> With the rapid development of distributed renewable energy, multi-microgrids play an increasingly important role in improving the flexibility and reliability of energy supply. Reinforcement learning has shown great potential in coordination strategies due to its model-free nature. Current methods lack explicit quantification of the relationship between individual and joint risk values, resulting in obscured credit assignment. Moreover, they often depend on explicit communication, which becomes inefficient as system complexity grows. To address these challenges, this paper proposes a risk-sensitive reinforcement learning framework with shared memory (RRL-SM) for multi-microgrid scheduling. Specifically, a risk-sensitive value factorization scheme is proposed to quantify the relationship between individual and joint risk values by leveraging distributional modeling and attention-based representations, thereby aligning local decisions with global risk objectives. An implicit shared-memory coordination mechanism is implemented through a global memory space to enhance the overall efficiency of decentralized decision-making. Collectively, the integrated approach delivers more reliable cooperative scheduling under renewable energy uncertainty. Simulation results show that RRL-SM reduces load-shedding risk by 84.5%, demonstrating a favorable balance between reliability and economic performance.

