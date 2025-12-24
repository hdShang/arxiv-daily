---
layout: default
title: JEDI: Latent End-to-end Diffusion Mitigates Agent-Human Performance Asymmetry in Model-Based Reinforcement Learning
---

# JEDI: Latent End-to-end Diffusion Mitigates Agent-Human Performance Asymmetry in Model-Based Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19698" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19698v2</a>
  <a href="https://arxiv.org/pdf/2505.19698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19698v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19698v2', 'JEDI: Latent End-to-end Diffusion Mitigates Agent-Human Performance Asymmetry in Model-Based Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jing Yu Lim, Zarif Ikram, Samson Yu, Haozhe Ma, Tze-Yun Leong, Dianbo Liu

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-05-26 (更新: 2025-05-28)

**备注**: Preprint

---

## 💡 一句话要点

**提出JEDI以解决模型基础强化学习中的人机性能不对称问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模型基础强化学习` `扩散模型` `人机性能对称性` `潜在空间` `自一致性目标`

## 📋 核心要点

1. 现有的基于模型的强化学习方法在不同任务中表现不均，导致人机性能不对称，影响整体评估。
2. 本文提出JEDI，通过端到端训练的潜在扩散模型，旨在解决像素基础代理中的时间结构缺失问题。
3. 实验结果表明，JEDI在人类最优任务中表现优异，同时在Atari100k基准测试中保持竞争力，显著提高了效率。

## 📝 摘要（中文）

近年来，基于模型的强化学习（MBRL）在Atari100k基准测试中取得了超人类水平的表现，得益于强大的扩散世界模型。然而，我们发现当前的聚合指标掩盖了一个主要的性能不对称性：在某些任务中，MBRL代理显著超越人类，而在其他任务中却表现不佳。本文通过将任务划分为代理最优和人类最优，提出了Joint Embedding DIffusion（JEDI），一种端到端训练的潜在扩散世界模型，旨在缓解这种不对称性。JEDI在人类最优任务中超越了最新的模型，同时在Atari100k基准测试中保持竞争力，且运行速度提高了三倍，内存使用降低了43%。

## 🔬 方法详解

**问题定义**：当前基于模型的强化学习方法在不同任务中表现差异显著，尤其是像素基础的代理在某些任务中表现优于人类，而在其他任务中则远不及人类，导致性能评估的偏差。

**核心思路**：本文提出的JEDI模型通过引入端到端的潜在扩散训练，旨在建立一个具有时间结构的潜在空间，以更好地适应不同类型的任务，从而减少人机性能的不对称性。

**技术框架**：JEDI模型的整体架构包括潜在空间的构建、扩散过程的优化和自一致性目标的实现。模型通过自一致性目标进行训练，确保生成的潜在表示能够有效捕捉任务的动态特征。

**关键创新**：JEDI的主要创新在于其端到端的训练方式和自一致性目标的引入，这与传统的分阶段训练方法有本质区别，能够更有效地处理任务中的时间依赖性。

**关键设计**：在模型设计中，JEDI使用了特定的损失函数来优化潜在空间的结构，并通过调整网络结构和参数设置来提高模型的训练效率和性能表现。

## 📊 实验亮点

实验结果显示，JEDI在多个任务中超越了最新的基线模型，在人类最优任务中表现尤为突出。同时，JEDI的运行速度提高了三倍，内存使用降低了43%，在Atari100k基准测试中保持了竞争力，显示出其在效率和性能上的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI、机器人控制和人机交互等。通过改善人机性能的对称性，JEDI可以在更广泛的任务中实现更高效的学习和决策，推动智能体在复杂环境中的应用。未来，JEDI的设计理念也可能被应用于其他领域的模型训练中，提升模型的适应性和性能。

## 📄 摘要（原文）

> Recent advances in model-based reinforcement learning (MBRL) have achieved super-human level performance on the Atari100k benchmark, driven by reinforcement learning agents trained on powerful diffusion world models. However, we identify that the current aggregates mask a major performance asymmetry: MBRL agents dramatically outperform humans in some tasks despite drastically underperforming in others, with the former inflating the aggregate metrics. This is especially pronounced in pixel-based agents trained with diffusion world models. In this work, we address the pronounced asymmetry observed in pixel-based agents as an initial attempt to reverse the worrying upward trend observed in them. We address the problematic aggregates by delineating all tasks as Agent-Optimal or Human-Optimal and advocate for equal importance on metrics from both sets. Next, we hypothesize this pronounced asymmetry is due to the lack of temporally-structured latent space trained with the World Model objective in pixel-based methods. Lastly, to address this issue, we propose Joint Embedding DIffusion (JEDI), a novel latent diffusion world model trained end-to-end with the self-consistency objective. JEDI outperforms SOTA models in human-optimal tasks while staying competitive across the Atari100k benchmark, and runs 3 times faster with 43% lower memory than the latest pixel-based diffusion baseline. Overall, our work rethinks what it truly means to cross human-level performance in Atari100k.

