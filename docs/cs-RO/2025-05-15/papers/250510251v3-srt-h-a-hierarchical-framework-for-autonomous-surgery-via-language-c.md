---
layout: default
title: SRT-H: A Hierarchical Framework for Autonomous Surgery via Language Conditioned Imitation Learning
---

# SRT-H: A Hierarchical Framework for Autonomous Surgery via Language Conditioned Imitation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.10251" class="toolbar-btn" target="_blank">📄 arXiv: 2505.10251v3</a>
  <a href="https://arxiv.org/pdf/2505.10251.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.10251v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.10251v3', 'SRT-H: A Hierarchical Framework for Autonomous Surgery via Language Conditioned Imitation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ji Woong Kim, Juo-Tung Chen, Pascal Hansen, Lucy X. Shi, Antony Goldenberg, Samuel Schmidgall, Paul Maria Scheikl, Anton Deguet, Brandon M. White, De Ru Tsai, Richard Cha, Jeffrey Jopling, Chelsea Finn, Axel Krieger

**分类**: cs.RO

**发布日期**: 2025-05-15 (更新: 2025-07-08)

---

## 💡 一句话要点

**提出层次化框架以解决自主外科手术中的灵巧操作问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主外科手术` `层次化框架` `任务规划` `机器人轨迹生成` `灵巧操作` `胆囊切除术` `语言条件学习`

## 📋 核心要点

1. 现有的自主外科手术研究主要集中在简单任务的自动化，难以应对复杂的长时间操作和人类组织的变异性。
2. 本文提出了一种层次化框架，结合高层任务规划和低层轨迹生成，以实现灵巧的自主外科手术。
3. 实验结果表明，该方法在胆囊切除术中实现了100%的成功率，展示了其在实际应用中的有效性和可靠性。

## 📝 摘要（中文）

自主外科手术的研究主要集中在控制环境下的简单任务自动化。然而，现实世界的外科应用需要在长时间内进行灵巧操作，并能够适应人类组织的固有变异性。现有的基于逻辑或传统端到端学习的方法难以应对这些挑战。为此，本文提出了一种层次化框架，用于执行灵巧的长时间外科步骤。该方法利用高层策略进行任务规划，低层策略生成机器人轨迹。高层规划器在语言空间中生成任务级或纠正指令，引导机器人完成长时间步骤并纠正低层策略的错误。通过对胆囊切除术的体外实验验证了该框架，结果显示该方法在八个未见的体外胆囊上实现了100%的成功率，完全自主操作，无需人类干预。这项工作展示了外科手术中的步骤级自主性，标志着自主外科系统临床应用的里程碑。

## 🔬 方法详解

**问题定义**：本文旨在解决自主外科手术中灵巧操作的挑战，现有方法在复杂环境下的适应性和长期操作能力不足。

**核心思路**：提出一种层次化框架，通过高层策略进行任务规划，低层策略生成机器人轨迹，以实现长时间的灵巧操作。

**技术框架**：整体架构分为高层规划和低层执行两个模块。高层规划器在语言空间中生成任务指令，低层执行器根据指令生成具体的机器人运动轨迹。

**关键创新**：该框架的创新在于将语言条件与任务规划结合，使机器人能够在复杂的外科环境中进行自主决策和操作，区别于传统的逻辑或端到端学习方法。

**关键设计**：在设计中，采用了特定的损失函数来优化高层和低层策略的协同工作，确保机器人在执行过程中能够及时纠正错误并适应环境变化。具体的网络结构和参数设置在实验中进行了详细的调优。

## 📊 实验亮点

实验结果显示，该方法在胆囊切除术中实现了100%的成功率，且在八个未见的体外胆囊上完全自主操作，未依赖人类干预。这一成果显著提升了自主外科手术的可行性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括自主外科手术系统的开发，尤其是在复杂和动态的手术环境中。其实际价值在于提高手术的安全性和效率，减少对人类外科医生的依赖，未来可能推动自主医疗技术的广泛应用。

## 📄 摘要（原文）

> Research on autonomous surgery has largely focused on simple task automation in controlled environments. However, real-world surgical applications demand dexterous manipulation over extended durations and generalization to the inherent variability of human tissue. These challenges remain difficult to address using existing logic-based or conventional end-to-end learning approaches. To address this gap, we propose a hierarchical framework for performing dexterous, long-horizon surgical steps. Our approach utilizes a high-level policy for task planning and a low-level policy for generating robot trajectories. The high-level planner plans in language space, generating task-level or corrective instructions that guide the robot through the long-horizon steps and correct for the low-level policy's errors. We validate our framework through ex vivo experiments on cholecystectomy, a commonly-practiced minimally invasive procedure, and conduct ablation studies to evaluate key components of the system. Our method achieves a 100\% success rate across eight unseen ex vivo gallbladders, operating fully autonomously without human intervention. This work demonstrates step-level autonomy in a surgical procedure, marking a milestone toward clinical deployment of autonomous surgical systems.

