---
layout: default
title: "Triple-S: A Collaborative Multi-LLM Framework for Solving Long-Horizon Implicative Tasks in Robotics"
---

# Triple-S: A Collaborative Multi-LLM Framework for Solving Long-Horizon Implicative Tasks in Robotics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07421" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07421v1</a>
  <a href="https://arxiv.org/pdf/2508.07421.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07421v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07421v1', 'Triple-S: A Collaborative Multi-LLM Framework for Solving Long-Horizon Implicative Tasks in Robotics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixi Jia, Hongbin Gao, Fashe Li, Jiqiang Liu, Hexiao Li, Qinghua Liu

**分类**: cs.RO

**发布日期**: 2025-08-10

**备注**: Accepted to IROS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Ghbbbbb/Triple-S)

---

## 💡 一句话要点

**提出Triple-S框架以解决机器人长时间隐含任务中的错误问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `机器人控制` `长时间任务` `协作框架` `任务成功率` `演示库更新` `上下文学习`

## 📋 核心要点

1. 现有方法在长时间隐含任务中容易出现API参数、注释和顺序错误，导致任务失败。
2. 本文提出的Triple-S框架通过多个LLM的协作，采用简化-解决-总结的闭环过程，提升任务成功率。
3. 实验结果显示，Triple-S在LDIP数据集上成功执行了89%的任务，验证了其在模拟和真实环境中的有效性。

## 📝 摘要（中文）

利用大型语言模型（LLMs）编写机器人控制策略代码的研究引起了广泛关注。然而，在长时间隐含任务中，这种方法常常导致API参数、注释和顺序错误，从而导致任务失败。为了解决这一问题，本文提出了一种协作的Triple-S框架，涉及多个LLM。通过上下文学习，不同的LLM在闭环的简化-解决-总结过程中承担特定角色，有效提高了长时间隐含任务的成功率和鲁棒性。此外，本文还提出了一种新的演示库更新机制，通过成功案例学习，使其能够推广到之前失败的任务。我们在长时间桌面隐含放置（LDIP）数据集上验证了该框架，在各种基线模型中，Triple-S在可观察和部分可观察场景中成功执行了89%的任务。模拟和真实机器人环境中的实验进一步验证了Triple-S的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决在长时间隐含任务中，利用大型语言模型（LLMs）编写策略代码时出现的API参数、注释和顺序错误等问题，这些问题常导致任务失败。

**核心思路**：Triple-S框架通过协作多个LLM，利用上下文学习，使不同的LLM在任务执行中承担特定角色，从而在简化、解决和总结的闭环过程中提高任务的成功率和鲁棒性。

**技术框架**：Triple-S框架包括三个主要模块：简化模块负责将任务简化为可处理的子任务，解决模块利用LLMs生成解决方案，最后总结模块整合结果并更新演示库。

**关键创新**：本文的关键创新在于引入了协作的多LLM框架和新的演示库更新机制，使得系统能够从成功案例中学习并推广到之前失败的任务，这一设计显著提高了任务的成功率。

**关键设计**：在框架中，LLMs的角色分配和任务简化策略是关键设计要素，此外，演示库的更新机制通过成功案例的反馈进行动态调整，以增强系统的适应性和泛化能力。

## 📊 实验亮点

实验结果表明，Triple-S框架在长时间桌面隐含放置（LDIP）数据集上成功执行了89%的任务，较基线模型有显著提升，尤其在可观察和部分可观察场景中均表现出色，验证了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动化任务执行和人机协作等。通过提高机器人在复杂任务中的成功率，Triple-S框架能够在工业、服务和家庭等多个场景中发挥重要作用，未来可能推动智能机器人技术的进一步发展。

## 📄 摘要（原文）

> Leveraging Large Language Models (LLMs) to write policy code for controlling robots has gained significant attention. However, in long-horizon implicative tasks, this approach often results in API parameter, comments and sequencing errors, leading to task failure. To address this problem, we propose a collaborative Triple-S framework that involves multiple LLMs. Through In-Context Learning, different LLMs assume specific roles in a closed-loop Simplification-Solution-Summary process, effectively improving success rates and robustness in long-horizon implicative tasks. Additionally, a novel demonstration library update mechanism which learned from success allows it to generalize to previously failed tasks. We validate the framework in the Long-horizon Desktop Implicative Placement (LDIP) dataset across various baseline models, where Triple-S successfully executes 89% of tasks in both observable and partially observable scenarios. Experiments in both simulation and real-world robot settings further validated the effectiveness of Triple-S. Our code and dataset is available at: https://github.com/Ghbbbbb/Triple-S.

