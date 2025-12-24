---
layout: default
title: Deep Reinforcement Learning Agents are not even close to Human Intelligence
---

# Deep Reinforcement Learning Agents are not even close to Human Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21731" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21731v1</a>
  <a href="https://arxiv.org/pdf/2505.21731.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21731v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21731v1', 'Deep Reinforcement Learning Agents are not even close to Human Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Quentin Delfosse, Jannis Blüml, Fabian Tatai, Théo Vincent, Bjarne Gregori, Elisabeth Dillies, Jan Peters, Constantin Rothkopf, Kristian Kersting

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-27

**备注**: 49 pages in total, 5 main figures, 14 figures total

---

## 💡 一句话要点

**提出HackAtari以解决深度强化学习智能不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `零-shot 适应` `任务简化` `HackAtari` `智能评估` `人类智能` `性能下降`

## 📋 核心要点

1. 现有深度强化学习代理在任务简化时表现出显著的性能下降，缺乏人类的零-shot 适应能力。
2. 本文提出HackAtari，通过一系列任务变体评估RL代理在简化任务中的表现，揭示其对捷径的依赖。
3. 实验结果显示，RL代理在简化任务上系统性地表现不佳，强调了与人类智能的差距，呼吁新的评估标准。

## 📝 摘要（中文）

深度强化学习（RL）代理在多种任务中取得了显著成果，但缺乏零-shot 适应能力。现有的鲁棒性评估主要集中在任务复杂化上，而对任务简化的评估尚未进行。为了解决这一问题，本文引入了HackAtari，一个基于街机学习环境的任务变体集合。研究表明，与人类不同，RL代理在训练任务的简化版本上表现出显著的性能下降，揭示了代理对捷径的依赖。通过对多种算法和架构的分析，强调了RL代理与人类行为智能之间的持续差距，呼吁建立新的基准和方法，以强制进行系统性的泛化测试，而不仅仅依赖静态评估协议。仅在同一环境中训练和测试不足以培养具有人类智能的代理。

## 🔬 方法详解

**问题定义**：本文旨在解决深度强化学习代理在任务简化时表现不佳的问题。现有方法主要关注任务复杂化，未能评估代理在简化任务中的适应能力。

**核心思路**：通过引入HackAtari，研究者能够系统性地评估RL代理在简化任务中的表现，揭示其对捷径的依赖，进而强调与人类智能的差距。

**技术框架**：HackAtari是基于街机学习环境的任务变体集合，包含多种简化任务。研究通过对比不同算法和架构的表现，分析其在简化任务中的适应能力。

**关键创新**：最重要的创新在于提出了HackAtari这一新评估框架，系统性地揭示了RL代理在任务简化时的性能下降，与现有方法相比，提供了新的视角来理解代理的智能局限性。

**关键设计**：实验中使用了多种RL算法和网络架构，评估其在HackAtari任务集上的表现，重点关注性能下降的幅度和原因。

## 📊 实验亮点

实验结果显示，RL代理在HackAtari任务集的简化版本上表现出高达50%的性能下降，明显低于人类的适应能力。这一发现强调了现有RL方法在智能泛化方面的不足，呼吁新的评估和训练方法。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI、机器人控制和自动驾驶等领域，能够帮助研究者更好地理解和提升RL代理的智能水平。通过建立新的评估标准，未来可能推动更具人类智能特征的AI系统的开发。

## 📄 摘要（原文）

> Deep reinforcement learning (RL) agents achieve impressive results in a wide variety of tasks, but they lack zero-shot adaptation capabilities. While most robustness evaluations focus on tasks complexifications, for which human also struggle to maintain performances, no evaluation has been performed on tasks simplifications. To tackle this issue, we introduce HackAtari, a set of task variations of the Arcade Learning Environments. We use it to demonstrate that, contrary to humans, RL agents systematically exhibit huge performance drops on simpler versions of their training tasks, uncovering agents' consistent reliance on shortcuts. Our analysis across multiple algorithms and architectures highlights the persistent gap between RL agents and human behavioral intelligence, underscoring the need for new benchmarks and methodologies that enforce systematic generalization testing beyond static evaluation protocols. Training and testing in the same environment is not enough to obtain agents equipped with human-like intelligence.

