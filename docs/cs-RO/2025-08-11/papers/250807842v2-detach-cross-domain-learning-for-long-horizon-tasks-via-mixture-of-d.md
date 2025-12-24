---
layout: default
title: "DETACH: Cross-domain Learning for Long-Horizon Tasks via Mixture of Disentangled Experts"
---

# DETACH: Cross-domain Learning for Long-Horizon Tasks via Mixture of Disentangled Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07842" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07842v2</a>
  <a href="https://arxiv.org/pdf/2508.07842.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07842v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07842v2', 'DETACH: Cross-domain Learning for Long-Horizon Tasks via Mixture of Disentangled Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yutong Shen, Hangxu Liu, Lei Zhang, Penghui Liu, Ruizhe Xia, Tianyi Yao, Tongtong Feng

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-11 (更新: 2025-09-22)

**备注**: 14 pages,8 figures. Submitted to ICRA'26

---

## 💡 一句话要点

**提出DETACH以解决长时间任务跨域学习问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `长时间任务` `跨域学习` `生物启发` `技能解耦` `环境理解` `任务执行` `人机交互` `机器人技术`

## 📋 核心要点

1. 现有方法依赖技能链，无法有效泛化到新环境和技能组合，导致长时间任务的完成率低。
2. DETACH框架通过双流解耦机制，分别处理环境理解和技能执行，实现跨域和跨技能的学习。
3. 在多种LH任务实验中，DETACH的子任务成功率平均提高23%，执行效率提升29%，表现优于现有方法。

## 📝 摘要（中文）

长时间任务（LH任务）在人与场景交互中是复杂的多步骤任务，需要持续规划、顺序决策和跨域执行以实现最终目标。然而，现有方法过于依赖技能链，通过连接预训练的子任务，导致环境观察与自我状态紧密耦合，缺乏对新环境和技能组合的泛化能力。为了解决这一问题，本文提出了DETACH，一个通过生物启发的双流解耦框架进行LH任务的跨域学习。DETACH包含两个核心模块：环境学习模块和技能学习模块，分别实现空间理解和任务执行。实验结果表明，DETACH在LH任务的子任务成功率上平均提高了23%，执行效率提高了29%。

## 🔬 方法详解

**问题定义**：本文旨在解决长时间任务在跨域学习中的泛化能力不足的问题。现有方法通过技能链连接子任务，导致环境观察与自我状态紧密耦合，无法适应新环境和技能组合。

**核心思路**：DETACH框架受大脑“何处-何物”双通道机制启发，采用双流解耦设计，分别处理环境信息和技能信息，从而实现更好的跨域和跨技能学习能力。

**技术框架**：DETACH由两个主要模块组成：环境学习模块用于空间理解，捕捉对象功能、空间关系和场景语义；技能学习模块用于任务执行，处理自我状态信息，包括关节自由度和运动模式。

**关键创新**：DETACH的核心创新在于通过环境-自我解耦实现跨域转移，以及通过独立运动模式编码实现跨技能转移，这与现有方法的紧密耦合设计形成鲜明对比。

**关键设计**：在环境学习模块中，采用了特定的损失函数以优化空间关系的捕捉；技能学习模块则通过独立编码运动模式，确保不同技能之间的有效转移。

## 📊 实验亮点

DETACH在多种长时间任务的实验中表现出色，子任务成功率平均提高了23%，执行效率提升29%。与现有方法相比，DETACH显著提升了跨域和跨技能的学习能力，展现了其在复杂任务中的实际应用潜力。

## 🎯 应用场景

DETACH框架在复杂的长时间任务中具有广泛的应用潜力，特别是在机器人操作、自动驾驶和人机交互等领域。其跨域学习能力可以帮助系统更好地适应不同环境，提高任务执行的灵活性和效率，未来可能推动智能系统的自主学习与决策能力的发展。

## 📄 摘要（原文）

> Long-Horizon (LH) tasks in Human-Scene Interaction (HSI) are complex multi-step tasks that require continuous planning, sequential decision-making, and extended execution across domains to achieve the final goal. However, existing methods heavily rely on skill chaining by concatenating pre-trained subtasks, with environment observations and self-state tightly coupled, lacking the ability to generalize to new combinations of environments and skills, failing to complete various LH tasks across domains. To solve this problem, this paper presents DETACH, a cross-domain learning framework for LH tasks via biologically inspired dual-stream disentanglement. Inspired by the brain's "where-what" dual pathway mechanism, DETACH comprises two core modules: i) an environment learning module for spatial understanding, which captures object functions, spatial relationships, and scene semantics, achieving cross-domain transfer through complete environment-self disentanglement; ii) a skill learning module for task execution, which processes self-state information including joint degrees of freedom and motor patterns, enabling cross-skill transfer through independent motor pattern encoding. We conducted extensive experiments on various LH tasks in HSI scenes. Compared with existing methods, DETACH can achieve an average subtasks success rate improvement of 23% and average execution efficiency improvement of 29%.

