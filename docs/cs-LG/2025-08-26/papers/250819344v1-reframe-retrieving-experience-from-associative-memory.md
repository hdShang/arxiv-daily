---
layout: default
title: "Re:Frame -- Retrieving Experience From Associative Memory"
---

# Re:Frame -- Retrieving Experience From Associative Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19344" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19344v1</a>
  <a href="https://arxiv.org/pdf/2508.19344.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19344v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19344v1', 'Re:Frame -- Retrieving Experience From Associative Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniil Zelezetsky, Egor Cherepanov, Alexey K. Kovalev, Aleksandr I. Panov

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-26

**备注**: 11 pages, 3 figures

---

## 💡 一句话要点

**提出Re:Frame以解决离线强化学习中的专家数据稀缺问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `专家数据` `关联记忆` `决策变换器` `性能提升`

## 📋 核心要点

1. 现有的离线强化学习方法在数据稀缺的情况下，难以从低质量数据中有效学习，导致性能受限。
2. Re:Frame通过引入外部的关联记忆缓冲区，允许策略在训练和评估阶段检索专家轨迹，从而提升决策质量。
3. 在D4RL MuJoCo任务中，使用少量专家数据，Re:Frame在多个设置上超越了强基线，显示出显著的性能提升。

## 📝 摘要（中文）

离线强化学习（RL）通常面临收集大型专家数据集的困难，导致代理在学习时只能依赖于不完美或不一致的轨迹。本文提出Re:Frame（从关联记忆中检索经验），这是一个插件模块，能够将少量专家轨迹与标准离线RL策略（如决策变换器）结合。在低质量数据的训练过程中，策略通过内容关联从外部的关联记忆缓冲区（AMB）检索专家数据，并将其整合到决策中。实验结果表明，使用仅60条专家轨迹，Re:Frame在D4RL MuJoCo任务中在三个设置上均显著提升了性能，最高提升达10.7个标准化点。

## 🔬 方法详解

**问题定义**：本文旨在解决离线强化学习中专家数据稀缺的问题。现有方法在缺乏高质量专家数据时，代理的学习效果受到限制，难以实现高性能。

**核心思路**：Re:Frame的核心思路是通过引入一个小型的关联记忆缓冲区（AMB），使得策略能够在训练过程中检索并利用少量专家经验，从而改善决策过程。

**技术框架**：Re:Frame的整体架构包括一个标准的离线RL策略（如决策变换器）和一个外部的AMB。在训练阶段，策略通过内容关联从AMB中检索专家轨迹，并将其整合到决策中；在评估阶段，AMB同样被查询以增强决策质量。

**关键创新**：Re:Frame的主要创新在于其无需与环境交互，且不需要对基础架构进行修改，就能有效利用稀缺的专家知识。这一设计与传统的强化学习方法形成了鲜明对比。

**关键设计**：在技术细节上，Re:Frame设定了AMB的大小和专家轨迹的数量，实验中使用了仅60条专家轨迹（占6000条数据集的0.1%），并通过内容关联机制实现了高效的数据检索。具体的损失函数和网络结构设计未在摘要中详细说明，需参考原文获取更多信息。

## 📊 实验亮点

在D4RL MuJoCo任务中，Re:Frame在三个设置上均超越了强基线，使用仅60条专家轨迹实现了最高10.7个标准化点的性能提升，展示了其在低质量数据环境下的有效性和数据效率。

## 🎯 应用场景

Re:Frame的研究成果在多个领域具有广泛的应用潜力，尤其是在机器人控制、自动驾驶和游戏AI等需要高效学习的场景中。通过有效利用有限的专家数据，该方法能够显著提升智能体的学习效率和决策能力，推动离线强化学习技术的实际应用。

## 📄 摘要（原文）

> Offline reinforcement learning (RL) often deals with suboptimal data when collecting large expert datasets is unavailable or impractical. This limitation makes it difficult for agents to generalize and achieve high performance, as they must learn primarily from imperfect or inconsistent trajectories. A central challenge is therefore how to best leverage scarce expert demonstrations alongside abundant but lower-quality data. We demonstrate that incorporating even a tiny amount of expert experience can substantially improve RL agent performance. We introduce Re:Frame (Retrieving Experience From Associative Memory), a plug-in module that augments a standard offline RL policy (e.g., Decision Transformer) with a small external Associative Memory Buffer (AMB) populated by expert trajectories drawn from a separate dataset. During training on low-quality data, the policy learns to retrieve expert data from the Associative Memory Buffer (AMB) via content-based associations and integrate them into decision-making; the same AMB is queried at evaluation. This requires no environment interaction and no modifications to the backbone architecture. On D4RL MuJoCo tasks, using as few as 60 expert trajectories (0.1% of a 6000-trajectory dataset), Re:Frame consistently improves over a strong Decision Transformer baseline in three of four settings, with gains up to +10.7 normalized points. These results show that Re:Frame offers a simple and data-efficient way to inject scarce expert knowledge and substantially improve offline RL from low-quality datasets.

