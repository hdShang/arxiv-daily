---
layout: default
title: "Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR"
---

# Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14029" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14029v4</a>
  <a href="https://arxiv.org/pdf/2508.14029.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14029v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14029v4', 'Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Liang, Zhongzhi Li, Yeyun Gong, Yelong Shen, Ying Nian Wu, Zhijiang Guo, Weizhu Chen

**分类**: cs.CL

**发布日期**: 2025-08-19 (更新: 2025-12-13)

---

## 💡 一句话要点

**提出自我博弈与变分问题合成以提升RLVR性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `可验证奖励` `自我博弈` `变分问题合成` `生成多样性` `推理任务` `大型语言模型`

## 📋 核心要点

1. 现有的RLVR训练方法在提高Pass@1性能的同时，导致策略熵降低，生成多样性受限。
2. 本文提出的SvS策略通过自我博弈合成变分问题，保持策略熵，提升生成多样性。
3. 在多个基准测试中，SvS策略在Pass@32性能上实现了显著提升，证明了其有效性和鲁棒性。

## 📝 摘要（中文）

强化学习与可验证奖励（RLVR）最近成为后训练大型语言模型（LLMs）的关键范式，尤其在复杂推理任务中。然而，传统的RLVR训练虽然提高了Pass@1性能，却牺牲了策略熵，导致生成多样性降低，限制了Pass@k性能。本文系统分析了训练问题对策略生成多样性的影响，发现增强和更新训练问题有助于缓解训练过程中的熵崩溃。基于此，提出了一种在线自我博弈与变分问题合成（SvS）策略，利用策略的正确解合成变分问题，同时确保参考答案与原始问题一致。该策略有效维持训练过程中的策略熵，显著提升Pass@k性能，在AIME24和AIME25基准上分别实现了18.3%和22.8%的绝对提升，并在代码生成任务中也表现出色。12个推理基准的实验结果表明SvS的普适性和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决传统RLVR训练中策略熵降低导致生成多样性不足的问题。现有方法在提高Pass@1性能时，往往牺牲了生成的多样性，限制了模型的推理能力。

**核心思路**：提出的SvS策略通过自我博弈的方式，利用策略的正确解合成新的变分问题，确保生成问题的参考答案与原始问题一致，从而维持策略的多样性和熵。

**技术框架**：SvS策略的整体架构包括问题合成模块和自我博弈模块。问题合成模块负责生成变分问题，自我博弈模块则利用当前策略进行训练，确保生成问题的有效性。

**关键创新**：SvS策略的核心创新在于通过自我博弈与变分问题合成的结合，有效避免了传统RLVR训练中的熵崩溃现象。这一方法与现有方法的本质区别在于其动态生成训练问题的能力。

**关键设计**：在SvS策略中，关键设计包括动态更新训练问题的机制、保持参考答案一致性的策略，以及在训练过程中对策略熵的监控和调整。这些设计确保了模型在训练过程中的稳定性和生成多样性。

## 📊 实验亮点

实验结果显示，SvS策略在AIME24和AIME25基准上分别实现了18.3%和22.8%的绝对提升，且在12个推理基准上表现出色，验证了其普适性和鲁棒性。这些结果表明，SvS策略显著优于传统RLVR方法。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的复杂推理任务、代码生成以及其他需要高生成多样性的场景。通过提升模型的推理能力和生成多样性，SvS策略能够在实际应用中提供更为准确和多样化的输出，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has recently emerged as a key paradigm for post-training Large Language Models (LLMs), particularly for complex reasoning tasks. However, vanilla RLVR training has been shown to improve Pass@1 performance at the expense of policy entropy, leading to reduced generation diversity and limiting the Pass@k performance, which typically represents the upper bound of LLM reasoning capability. In this paper, we systematically analyze the policy's generation diversity from the perspective of training problems and find that augmenting and updating training problems helps mitigate entropy collapse during training. Based on these observations, we propose an online Self-play with Variational problem Synthesis (SvS) strategy for RLVR training, which uses the policy's correct solutions to synthesize variational problems while ensuring their reference answers remain identical to the originals. This self-improving strategy effectively maintains policy entropy during training and substantially improves Pass@k compared with standard RLVR, sustaining prolonged improvements and achieving absolute gains of 18.3% and 22.8% in Pass@32 performance on the competition-level AIME24 and AIME25 benchmarks, as well as on code generation tasks. Experiments on 12 reasoning benchmarks across varying model sizes from 3B to 32B consistently demonstrate the generalizability and robustness of SvS.

