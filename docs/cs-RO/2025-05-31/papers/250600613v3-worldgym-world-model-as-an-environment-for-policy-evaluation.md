---
layout: default
title: WorldGym: World Model as An Environment for Policy Evaluation
---

# WorldGym: World Model as An Environment for Policy Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00613" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00613v3</a>
  <a href="https://arxiv.org/pdf/2506.00613.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00613v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00613v3', 'WorldGym: World Model as An Environment for Policy Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Julian Quevedo, Ansh Kumar Sharma, Yixiang Sun, Varad Suryavanshi, Percy Liang, Sherry Yang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-31 (更新: 2025-09-30)

**备注**: https://world-model-eval.github.io

---

## 💡 一句话要点

**提出WorldGym以解决机器人控制策略评估难题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人控制` `策略评估` `世界模型` `视频生成` `视觉-语言模型` `蒙特卡洛回滚` `泛化能力`

## 📋 核心要点

1. 现有的机器人控制策略评估方法面临高成本和低通用性的问题，手工模拟器的改进需要大量的人工干预。
2. 本文提出WorldGym，一个基于世界模型的环境，通过自回归视频生成模型实现高效的策略评估，利用视觉-语言模型提供奖励。
3. 实验结果显示，WorldGym中的策略成功率与现实世界高度相关，并能有效评估策略的泛化能力，保持相对排名一致性。

## 📝 摘要（中文）

评估机器人控制策略是一项困难的任务：现实世界测试成本高昂，而手工制作的模拟器需要大量手动努力来提高其真实性和通用性。本文提出了一种基于世界模型的策略评估环境（WorldGym），该环境是一个自回归的、动作条件的视频生成模型，作为现实世界环境的代理。通过在世界模型中进行蒙特卡洛回滚评估策略，并利用视觉-语言模型提供奖励。我们在世界模型中评估了一组基于VLA的真实机器人策略，仅使用真实机器人的初始帧，结果表明，世界模型中的策略成功率与现实世界的成功率高度相关。此外，WorldGym能够保持不同策略版本、规模和训练检查点之间的相对策略排名。由于仅需一个起始帧作为输入，世界模型进一步支持对机器人策略在新任务和环境中的泛化能力进行高效评估。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人控制策略评估中的高成本和低通用性问题。现有方法依赖于昂贵的现实世界测试和手工制作的模拟器，难以实现高效评估。

**核心思路**：论文提出WorldGym，利用自回归的、动作条件的视频生成模型作为现实环境的代理，通过蒙特卡洛回滚评估策略，结合视觉-语言模型提供奖励，从而实现高效的策略评估。

**技术框架**：WorldGym的整体架构包括视频生成模型、策略评估模块和奖励计算模块。视频生成模型根据输入的初始帧生成模拟环境，策略评估模块执行蒙特卡洛回滚，奖励计算模块则通过视觉-语言模型评估策略的表现。

**关键创新**：WorldGym的主要创新在于其能够在仅使用单一初始帧的情况下，进行高效的策略评估，并保持不同策略版本之间的相对排名一致性。这与传统方法相比，显著降低了评估成本和复杂性。

**关键设计**：在技术细节上，WorldGym采用了自回归生成模型，设计了适应性强的损失函数，并优化了网络结构以提高生成视频的真实性和策略评估的准确性。

## 📊 实验亮点

实验结果表明，WorldGym中策略的成功率与现实世界的成功率高度相关，且能够有效保持不同策略版本之间的相对排名一致性。这一方法为机器人策略的泛化能力评估提供了新的视角，具有重要的实际应用价值。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、智能制造等。通过提供一个高效、安全的策略评估环境，WorldGym能够帮助研究人员和工程师在部署前进行更可靠的策略测试，从而降低实际应用中的风险和成本。

## 📄 摘要（原文）

> Evaluating robot control policies is difficult: real-world testing is costly, and handcrafted simulators require manual effort to improve in realism and generality. We propose a world-model-based policy evaluation environment (WorldGym), an autoregressive, action-conditioned video generation model which serves as a proxy to real world environments. Policies are evaluated via Monte Carlo rollouts in the world model, with a vision-language model providing rewards. We evaluate a set of VLA-based real-robot policies in the world model using only initial frames from real robots, and show that policy success rates within the world model highly correlate with real-world success rates. Moreoever, we show that WorldGym is able to preserve relative policy rankings across different policy versions, sizes, and training checkpoints. Due to requiring only a single start frame as input, the world model further enables efficient evaluation of robot policies' generalization ability on novel tasks and environments. We find that modern VLA-based robot policies still struggle to distinguish object shapes and can become distracted by adversarial facades of objects. While generating highly realistic object interaction remains challenging, WorldGym faithfully emulates robot motions and offers a practical starting point for safe and reproducible policy evaluation before deployment.

