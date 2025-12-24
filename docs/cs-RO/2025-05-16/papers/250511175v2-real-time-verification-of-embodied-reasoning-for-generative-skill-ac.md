---
layout: default
title: Real-Time Verification of Embodied Reasoning for Generative Skill Acquisition
---

# Real-Time Verification of Embodied Reasoning for Generative Skill Acquisition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11175" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11175v2</a>
  <a href="https://arxiv.org/pdf/2505.11175.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11175v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11175v2', 'Real-Time Verification of Embodied Reasoning for Generative Skill Acquisition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bo Yue, Shuqi Guo, Kaiyu Hu, Chujiao Wang, Benyou Wang, Kui Jia, Guiliang Liu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-16 (更新: 2025-05-19)

---

## 💡 一句话要点

**提出VERGSA框架以解决复杂3D环境中的技能学习效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成技能获取` `具身智能体` `实时验证` `复杂环境` `奖励标记` `自动化学习` `决策模型`

## 📋 核心要点

1. 现有方法依赖于通用智能体的监督信号，导致在复杂3D环境中的有效性不明确，且评估成本高。
2. 提出VERGSA框架，通过实时验证原则提升具身技能学习的效率，动态整合相关任务和成功指标。
3. 实验结果显示，示例任务池提高了21%的平均任务成功率，验证模型对新任务成功率提升24%，对已遇任务提升36%。

## 📝 摘要（中文）

生成技能获取使得具身智能体能够主动学习可扩展和不断演变的控制技能，这对大型决策模型的进步至关重要。现有方法通常依赖于通用智能体（如大型语言模型）的监督信号，但在复杂3D环境中的有效性尚不明确，且全面评估会产生巨大的计算成本，显著影响技能学习效率。为此，本文提出了VERGSA（验证具身推理的生成技能获取），该框架系统地将实时验证原则整合到具身技能学习中。VERGSA实现了数学推理验证向具身学习的无缝扩展，并提出了一种自动化、可扩展的奖励标记方案。实验结果表明，所提方法在任务成功率上有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有生成技能获取方法在复杂3D环境中效率低下的问题，尤其是依赖通用智能体的监督信号导致的有效性不确定性和高计算成本。

**核心思路**：提出VERGSA框架，通过实时验证原则，动态整合上下文相关任务，定义子任务和整体任务的成功指标，从而提升技能学习的效率和准确性。

**技术框架**：VERGSA框架包括两个主要模块：1) 验证模块，负责动态整合任务和成功指标；2) 奖励标记模块，自动化生成密集奖励信号，评估场景配置和子任务学习对整体技能获取的贡献。

**关键创新**：本文首次提出了基于验证驱动的生成技能获取的全面训练数据集，消除了繁琐的手动奖励工程，显著提升了技能学习的效率。

**关键设计**：在奖励标记方案中，采用了迭代优化的方法来综合场景配置和子任务的贡献，确保奖励信号的密集性和准确性。

## 📊 实验亮点

实验结果表明，示例任务池使得平均任务成功率提高了21%，而验证模型在新任务和已遇任务上的成功率分别提升了24%和36%。此外，VERGSA在验证质量上超越了以LLM为评判基线的方法，显示出其优越性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动化决策系统和智能代理的技能学习等。通过提高技能获取的效率，VERGSA框架能够加速智能体在复杂环境中的适应能力，推动智能体在实际应用中的广泛使用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Generative skill acquisition enables embodied agents to actively learn a scalable and evolving repertoire of control skills, crucial for the advancement of large decision models. While prior approaches often rely on supervision signals from generalist agents (e.g., LLMs), their effectiveness in complex 3D environments remains unclear; exhaustive evaluation incurs substantial computational costs, significantly hindering the efficiency of skill learning. Inspired by recent successes in verification models for mathematical reasoning, we propose VERGSA (Verifying Embodied Reasoning in Generative Skill Acquisition), a framework that systematically integrates real-time verification principles into embodied skill learning. VERGSA establishes 1) a seamless extension from verification of mathematical reasoning into embodied learning by dynamically incorporating contextually relevant tasks into prompts and defining success metrics for both subtasks and overall tasks, and 2) an automated, scalable reward labeling scheme that synthesizes dense reward signals by iteratively finalizing the contribution of scene configuration and subtask learning to overall skill acquisition. To the best of our knowledge, this approach constitutes the first comprehensive training dataset for verification-driven generative skill acquisition, eliminating arduous manual reward engineering. Experiments validate the efficacy of our approach: 1) the exemplar task pool improves the average task success rates by 21%, 2) our verification model boosts success rates by 24% for novel tasks and 36% for encountered tasks, and 3) outperforms LLM-as-a-Judge baselines in verification quality.

