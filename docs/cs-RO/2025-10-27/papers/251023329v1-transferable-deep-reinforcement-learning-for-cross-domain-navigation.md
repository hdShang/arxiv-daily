---
layout: default
title: Transferable Deep Reinforcement Learning for Cross-Domain Navigation: from Farmland to the Moon
---

# Transferable Deep Reinforcement Learning for Cross-Domain Navigation: from Farmland to the Moon

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23329" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23329v1</a>
  <a href="https://arxiv.org/pdf/2510.23329.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23329v1" onclick="toggleFavorite(this, '2510.23329v1', 'Transferable Deep Reinforcement Learning for Cross-Domain Navigation: from Farmland to the Moon')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shreya Santra, Thomas Robbins, Kazuya Yoshida

**分类**: cs.RO

**发布日期**: 2025-10-27

**备注**: 6 pages, 7 figures. Accepted at IEEE iSpaRo 2025

---

## 💡 一句话要点

**提出基于DRL的跨域迁移导航方法，实现从农田到月球的零样本泛化**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `跨域迁移` `自主导航` `机器人` `行星探索`

## 📋 核心要点

1. 传统导航算法需要针对特定环境进行大量调整，限制了其在新领域的扩展性，是当前面临的核心问题。
2. 论文提出利用深度强化学习，使机器人在与环境的直接交互中学习导航策略，并研究其跨域泛化能力。
3. 实验结果表明，在陆地环境训练的策略在月球环境中无需额外训练即可达到接近50%的成功率。

## 📝 摘要（中文）

本文研究了深度强化学习(DRL)策略在视觉和地形上截然不同的模拟环境中的泛化能力，策略在陆地环境中训练，并在外星环境中以零样本方式进行验证。开发了一个农业漫游车的3D模拟环境，并使用近端策略优化(PPO)进行训练，以实现在农田环境中进行目标导向导航和避障。然后，在类似月球的模拟环境中评估学习到的策略，以评估迁移性能。结果表明，在陆地条件下训练的策略保持了较高的有效性，在月球模拟中无需额外训练和微调即可达到接近50%的成功率。这突显了基于DRL的跨域策略迁移作为一种有前途的方法的潜力，可以为未来的行星探索任务开发适应性强且高效的自主导航，并具有最大限度地降低再训练成本的额外优势。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人自主导航在不同环境下的泛化问题。现有算法通常需要针对特定环境进行大量调整，难以直接应用于新的、未知的环境，例如从地球农田到月球表面。这种环境适应性差的问题限制了机器人技术在行星探索等领域的应用。

**核心思路**：论文的核心思路是利用深度强化学习（DRL）训练一个通用的导航策略，使其能够适应不同的视觉和地形环境。通过在模拟的陆地环境中训练，使机器人学习到通用的导航规则和避障策略，然后将这些策略直接迁移到模拟的月球环境中，无需进行额外的训练或微调。这种方法旨在减少对环境特定信息的依赖，提高策略的泛化能力。

**技术框架**：整体框架包括以下几个主要步骤：1) 构建一个农业漫游车的3D模拟环境，用于训练DRL策略。2) 使用近端策略优化（PPO）算法训练漫游车在农田环境中进行目标导向导航和避障。3) 构建一个类似月球的模拟环境，用于评估训练好的策略的迁移性能。4) 在月球环境中，使用零样本迁移的方式，直接应用在农田环境中训练的策略，评估其导航成功率和效率。

**关键创新**：论文的关键创新在于验证了DRL策略在视觉和地形差异显著的环境之间的零样本迁移能力。以往的DRL研究通常关注于在同一环境或相似环境中的策略迁移，而本文则探索了在完全不同的环境（农田 vs. 月球）下的策略泛化能力。这种跨域迁移能力可以显著降低机器人部署到新环境时的训练成本和时间。

**关键设计**：论文使用了Proximal Policy Optimization (PPO)算法进行策略训练。PPO是一种常用的策略梯度算法，具有较好的稳定性和收敛性。具体的技术细节包括：奖励函数的设计，用于鼓励机器人到达目标并避免碰撞；状态空间和动作空间的设计，需要能够有效地描述机器人的状态和控制机器人的运动；以及神经网络结构的选择，需要能够有效地学习到导航策略。

## 📊 实验亮点

实验结果表明，在农田环境中训练的DRL策略在月球模拟环境中实现了接近50%的导航成功率，而无需进行任何额外的训练或微调。这表明DRL策略具有较强的跨域泛化能力，可以在视觉和地形差异显著的环境中有效工作。这一结果验证了基于DRL的跨域策略迁移方法的可行性，为未来的行星探索任务提供了新的思路。

## 🎯 应用场景

该研究成果可应用于行星探测、农业机器人、搜救机器人等领域。通过在模拟环境中训练通用的导航策略，可以降低机器人在新环境中的部署成本和时间，提高机器人的自主性和适应性。未来，该技术有望应用于火星探测、深海勘探等复杂环境，实现更高效、更智能的机器人自主导航。

## 📄 摘要（原文）

> Autonomous navigation in unstructured environments is essential for field and planetary robotics, where robots must efficiently reach goals while avoiding obstacles under uncertain conditions. Conventional algorithmic approaches often require extensive environment-specific tuning, limiting scalability to new domains. Deep Reinforcement Learning (DRL) provides a data-driven alternative, allowing robots to acquire navigation strategies through direct interactions with their environment. This work investigates the feasibility of DRL policy generalization across visually and topographically distinct simulated domains, where policies are trained in terrestrial settings and validated in a zero-shot manner in extraterrestrial environments. A 3D simulation of an agricultural rover is developed and trained using Proximal Policy Optimization (PPO) to achieve goal-directed navigation and obstacle avoidance in farmland settings. The learned policy is then evaluated in a lunar-like simulated environment to assess transfer performance. The results indicate that policies trained under terrestrial conditions retain a high level of effectiveness, achieving close to 50\% success in lunar simulations without the need for additional training and fine-tuning. This underscores the potential of cross-domain DRL-based policy transfer as a promising approach to developing adaptable and efficient autonomous navigation for future planetary exploration missions, with the added benefit of minimizing retraining costs.

