---
layout: default
title: "ProST: Progressive Sub-task Training for Pareto-Optimal Multi-agent Systems Using Small Language Models"
---

# ProST: Progressive Sub-task Training for Pareto-Optimal Multi-agent Systems Using Small Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04508" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04508v2</a>
  <a href="https://arxiv.org/pdf/2509.04508.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04508v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04508v2', 'ProST: Progressive Sub-task Training for Pareto-Optimal Multi-agent Systems Using Small Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Biddut Sarker Bijoy, Mohammad Saqib Hasan, Pegah Alipoormolabashi, Avirup Sil, Aruna Balasubramanian, Niranjan Balasubramanian

**分类**: cs.CL

**发布日期**: 2025-09-02 (更新: 2025-11-11)

---

## 💡 一句话要点

**提出ProST渐进式子任务训练方法，提升小型语言模型多智能体系统在复杂任务中的效率和效果。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `小型语言模型` `渐进式训练` `课程学习` `强化学习` `子任务分解` `AppWorld环境`

## 📋 核心要点

1. 小型语言模型在复杂任务中面临长轨迹学习困难，导致多智能体系统性能受限。
2. 提出渐进式子任务训练（ProST）策略，类似于课程学习，逐步引入子任务以提升学习效果。
3. 实验表明，ProST能有效提升多智能体系统性能，实现更好的有效性-效率权衡。

## 📝 摘要（中文）

本文研究了使用小型语言模型（SLM）的多智能体系统与使用大型语言模型（LLM）的单智能体系统在解决复杂问题时的有效性和效率对比。研究发现，SLM在长轨迹学习方面的困难限制了其性能，即使经过专门的角色训练，SLM也无法有效地学习所有子任务。为了解决这个问题，本文提出了一种简单的渐进式子任务训练策略，该策略在每个训练周期中逐步引入新的子任务。实验结果表明，这种类似于实例级别课程学习的策略，能够持续提高多智能体系统在各种配置下的有效性。帕累托分析表明，微调后的多智能体系统能够实现更好的有效性-效率权衡。额外的消融实验和分析表明了渐进式训练策略的重要性及其降低子任务错误率的能力。

## 🔬 方法详解

**问题定义**：论文旨在解决小型语言模型（SLM）在复杂多智能体任务中表现不佳的问题。现有方法直接训练SLM完成所有子任务，但由于SLM的容量限制和长轨迹学习的困难，导致其无法有效学习所有子任务，从而限制了整体性能。尤其是在AppWorld这种需要长期规划和多步骤交互的环境中，问题更加突出。

**核心思路**：论文的核心思路是采用渐进式子任务训练（Progressive Sub-task Training, ProST）。类似于课程学习，ProST从简单的子任务开始训练SLM，然后逐步引入更复杂的子任务。这种方式有助于SLM逐步掌握各个子任务，避免一开始就面临过于复杂的学习目标，从而提高学习效率和最终性能。

**技术框架**：ProST的整体框架是在多智能体强化学习训练循环中，对每个训练epoch的训练数据进行调整。具体来说，在每个epoch开始时，根据预定义的子任务难度顺序，选择一部分子任务进行训练。随着epoch的进行，逐步增加训练的子任务数量，直到所有子任务都被包含在训练集中。这种渐进式的训练方式使得SLM能够逐步适应复杂任务。

**关键创新**：ProST的关键创新在于将课程学习的思想应用到多智能体系统的子任务训练中。与传统的直接训练所有子任务的方法相比，ProST能够更好地利用SLM的有限容量，使其能够更有效地学习各个子任务。此外，ProST的实现方式简单，易于集成到现有的多智能体训练框架中。

**关键设计**：ProST的关键设计包括子任务的划分和难度排序。论文中，子任务的划分基于AppWorld环境中的不同操作和目标。难度排序可以根据经验或通过实验确定。此外，ProST还需要确定每个epoch中引入新子任务的策略，例如线性增加或指数增加。具体的损失函数和网络结构与底层使用的多智能体强化学习算法相关，ProST本身并不引入新的损失函数或网络结构。

## 📊 实验亮点

实验结果表明，ProST能够显著提升多智能体系统的性能。在AppWorld环境中，使用ProST训练的SLM多智能体系统在各种配置下都取得了更好的效果，并且在有效性-效率权衡方面优于传统的训练方法。消融实验表明，渐进式训练策略对于降低子任务错误率至关重要。帕累托分析进一步验证了ProST在提升系统整体性能方面的优势。

## 🎯 应用场景

该研究成果可应用于各种需要多智能体协作完成复杂任务的场景，例如机器人协作、自动驾驶、智能交通管理、以及分布式计算等。通过使用小型语言模型和渐进式训练策略，可以在资源受限的环境中实现高效的多智能体系统，降低部署成本和计算需求，并为边缘计算设备上的复杂任务提供解决方案。

## 📄 摘要（原文）

> Multi-agent systems with smaller language models (SLMs) present a viable alternative to single agent systems powered by large language models (LLMs) for addressing complex problems. In this work, we study how these alternatives compare in terms of both effectiveness and efficiency. To study this trade-off, we instantiate single and multi-agent systems for the complex problems in the AppWorld environment using different sized language models.
>   We find that difficulties with long-trajectory learning in smaller language models (SLMs) limit their performance. Even when trained for specialized roles, SLMs fail to learn all subtasks effectively. To address this issue, we introduce a simple progressive sub-task training strategy, which introduces new sub-tasks progressively in each training epoch. We find that this novel strategy, analogous to instance level curriculum learning, consistently improves the effectiveness of multi-agents at all configurations. Our Pareto analysis shows that fine-tuned multi-agent systems yield better effectiveness-efficiency trade-offs. Additional ablations and analyses shows the importance of our progressive training strategy and its ability to reduce subtask error rates.

