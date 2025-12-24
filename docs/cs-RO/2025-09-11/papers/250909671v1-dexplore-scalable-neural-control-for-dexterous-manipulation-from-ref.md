---
layout: default
title: "Dexplore: Scalable Neural Control for Dexterous Manipulation from Reference-Scoped Exploration"
---

# Dexplore: Scalable Neural Control for Dexterous Manipulation from Reference-Scoped Exploration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09671" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09671v1</a>
  <a href="https://arxiv.org/pdf/2509.09671.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09671v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09671v1', 'Dexplore: Scalable Neural Control for Dexterous Manipulation from Reference-Scoped Exploration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sirui Xu, Yu-Wei Chao, Liuyu Bian, Arsalan Mousavian, Yu-Xiong Wang, Liang-Yan Gui, Wei Yang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-11

**备注**: CoRL 2025

---

## 💡 一句话要点

**Dexplore：基于参考范围探索的可扩展神经控制，用于灵巧操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `灵巧操作` `机器人控制` `强化学习` `运动捕捉` `策略蒸馏`

## 📋 核心要点

1. 现有灵巧操作方法依赖三阶段流程，易累积误差且未充分利用演示数据。
2. Dexplore提出统一的单循环优化，联合重定向和跟踪，从MoCap数据学习控制策略。
3. Dexplore通过自适应空间范围和强化学习，提升策略鲁棒性，并泛化到真实场景。

## 📝 摘要（中文）

手部-物体运动捕捉(MoCap)库提供了大规模、富含接触的演示数据，为扩展灵巧机器人操作提供了可能。然而，演示数据的不准确性以及人类和机器人手之间的差异限制了这些数据的直接使用。现有方法通常采用三阶段工作流程，包括重定向、跟踪和残差校正，这往往导致演示数据未被充分利用，并在各个阶段累积误差。我们提出了Dexplore，一种统一的单循环优化方法，它联合执行重定向和跟踪，从而直接从大规模MoCap数据中学习机器人控制策略。我们不将演示数据视为真值，而是将其用作软指导。从原始轨迹中，我们推导出自适应空间范围，并使用强化学习进行训练，以使策略保持在范围内，同时最小化控制工作量并完成任务。这种统一的公式保留了演示意图，使机器人特定的策略得以涌现，提高了对噪声的鲁棒性，并可扩展到大型演示语料库。我们将缩放后的跟踪策略提炼成一个基于视觉、技能条件生成控制器，该控制器在丰富的潜在表示中编码了各种操作技能，支持跨对象的泛化和真实世界的部署。总而言之，这些贡献使Dexplore成为一座原则性的桥梁，将不完美的演示转化为灵巧操作的有效训练信号。

## 🔬 方法详解

**问题定义**：现有灵巧操作方法通常采用三阶段流程：重定向（retargeting）、跟踪（tracking）和残差校正。这种方法存在几个痛点：一是演示数据本身可能存在不准确性；二是人类手和机器人手之间存在结构差异，导致重定向过程引入误差；三是各个阶段的误差会累积，最终影响控制策略的性能；四是演示数据没有被充分利用，机器人难以学习到自身的优势策略。

**核心思路**：Dexplore的核心思路是将重定向和跟踪两个阶段融合到一个统一的优化循环中，直接从MoCap数据学习机器人控制策略。不将演示数据视为绝对真值，而是将其作为一种软指导，允许机器人根据自身特性学习最优策略。通过引入自适应空间范围，约束策略在合理范围内探索，避免无效学习。

**技术框架**：Dexplore的整体框架包含以下几个主要模块：1) **数据预处理**：从MoCap数据中提取原始轨迹。2) **自适应空间范围生成**：根据原始轨迹，动态生成策略探索的空间范围。3) **强化学习训练**：使用强化学习算法，训练机器人控制策略，目标是保持在空间范围内，同时最小化控制成本并完成任务。4) **策略蒸馏**：将训练好的跟踪策略蒸馏成一个基于视觉的、技能条件生成控制器。

**关键创新**：Dexplore的关键创新在于其统一的单循环优化框架，它避免了传统三阶段流程中的误差累积问题，并允许机器人根据自身特性学习最优策略。此外，自适应空间范围的引入，提高了训练效率和策略的鲁棒性。将策略蒸馏成技能条件生成控制器，实现了跨对象的泛化能力。

**关键设计**：Dexplore的关键设计包括：1) **自适应空间范围**：根据演示轨迹动态调整，允许策略在合理范围内探索。2) **强化学习奖励函数**：设计奖励函数，鼓励策略保持在空间范围内，同时最小化控制成本并完成任务。3) **技能条件生成控制器**：使用变分自编码器（VAE）等技术，将不同的操作技能编码到潜在空间中，实现技能的泛化和组合。

## 📊 实验亮点

Dexplore在灵巧操作任务上取得了显著的性能提升。实验结果表明，Dexplore能够有效地从大规模MoCap数据中学习到鲁棒的控制策略，并在真实机器人上成功部署。相较于传统的三阶段方法，Dexplore在操作成功率和效率方面均有明显提升，并且能够更好地泛化到新的对象和场景。

## 🎯 应用场景

Dexplore在机器人灵巧操作领域具有广泛的应用前景，例如自动化装配、医疗手术机器人、家庭服务机器人等。通过学习人类的灵巧操作技能，机器人可以更好地适应复杂环境，完成各种精细操作任务。该研究有助于推动机器人技术的发展，提高机器人的智能化水平，并最终实现机器人在各个领域的广泛应用。

## 📄 摘要（原文）

> Hand-object motion-capture (MoCap) repositories offer large-scale, contact-rich demonstrations and hold promise for scaling dexterous robotic manipulation. Yet demonstration inaccuracies and embodiment gaps between human and robot hands limit the straightforward use of these data. Existing methods adopt a three-stage workflow, including retargeting, tracking, and residual correction, which often leaves demonstrations underused and compound errors across stages. We introduce Dexplore, a unified single-loop optimization that jointly performs retargeting and tracking to learn robot control policies directly from MoCap at scale. Rather than treating demonstrations as ground truth, we use them as soft guidance. From raw trajectories, we derive adaptive spatial scopes, and train with reinforcement learning to keep the policy in-scope while minimizing control effort and accomplishing the task. This unified formulation preserves demonstration intent, enables robot-specific strategies to emerge, improves robustness to noise, and scales to large demonstration corpora. We distill the scaled tracking policy into a vision-based, skill-conditioned generative controller that encodes diverse manipulation skills in a rich latent representation, supporting generalization across objects and real-world deployment. Taken together, these contributions position Dexplore as a principled bridge that transforms imperfect demonstrations into effective training signals for dexterous manipulation.

