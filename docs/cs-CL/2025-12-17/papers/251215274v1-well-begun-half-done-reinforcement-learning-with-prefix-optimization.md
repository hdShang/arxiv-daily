---
layout: default
title: Well Begun, Half Done: Reinforcement Learning with Prefix Optimization for LLM Reasoning
---

# Well Begun, Half Done: Reinforcement Learning with Prefix Optimization for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15274" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15274v1</a>
  <a href="https://arxiv.org/pdf/2512.15274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15274v1" onclick="toggleFavorite(this, '2512.15274v1', 'Well Begun, Half Done: Reinforcement Learning with Prefix Optimization for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiliu Sun, Zicheng Zhao, Yang Wei, Yanfang Zhang, Chen Gong

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-17

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**提出PPPO方法，通过优化LLM推理前缀token策略，提升强化学习推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `推理能力` `前缀优化` `策略优化`

## 📋 核心要点

1. 现有基于可验证奖励的强化学习方法在训练LLM推理时，忽略了前缀token的重要性，导致训练效率低下。
2. PPPO方法受到路径依赖理论启发，关注LLM推理的“起始锁定效应”，优化前缀token策略，提升推理能力。
3. 实验结果表明，PPPO方法优于现有RLVR方法，仅使用少量训练token即可显著提升推理准确率。

## 📝 摘要（中文）

本文提出了一种新的基于可验证奖励的强化学习方法，称为渐进式前缀token策略优化（PPPO），旨在提升大型语言模型（LLM）的推理能力。现有方法通常在所有生成的token上进行训练，忽略了哪些token（例如，前缀token）真正有助于推理。这种统一的训练策略在优化低回报token上花费了大量精力，从而阻碍了高回报token的潜在改进，并降低了整体训练效率。PPPO通过突出生成输出的前缀部分的重要性来解决这个问题。受到路径依赖理论的启发，PPPO发现LLM推理中存在“起始锁定效应”（BLE）。PPPO利用这一发现，将其优化目标集中在LLM的前缀推理过程上。这种有针对性的优化策略可以积极影响后续的推理过程，并最终提高最终结果。为了提高LLM高质量推理起始的学习效率，PPPO引入了两种训练策略：（a）渐进式前缀保留，通过在训练期间增加保留的前缀token的比例来形成渐进式学习过程；（b）连续累积奖励，通过为一个前缀token序列采样多个延续，并累积它们的分数作为奖励信号，来减轻奖励偏差。在各种推理任务上的大量实验结果表明，我们提出的PPPO优于代表性的RLVR方法，仅使用26.17%的训练token，准确率就提高了18.02%。

## 🔬 方法详解

**问题定义**：现有基于可验证奖励的强化学习（RLVR）方法在训练大型语言模型（LLM）进行推理时，通常对所有生成的token进行统一训练。这种方法忽略了不同token对推理过程的贡献差异，特别是前缀token的重要性。由于大量计算资源被用于优化对推理贡献较小的token，导致训练效率低下，并限制了模型性能的进一步提升。现有方法的痛点在于未能有效利用LLM推理过程中的“起始锁定效应”，即初始token对后续推理轨迹的强烈影响。

**核心思路**：PPPO的核心思路是借鉴人类思维中的路径依赖理论，强调LLM推理过程中前缀token的重要性。通过观察发现LLM推理存在“起始锁定效应”（Beginning Lock-in Effect, BLE），即初始生成的前缀token会显著影响后续的推理路径和最终结果。因此，PPPO将优化重点放在前缀token的策略学习上，旨在通过优化初始推理步骤来改善整体推理性能。这种有针对性的优化策略能够更有效地利用训练资源，并引导LLM朝着更正确的推理方向发展。

**技术框架**：PPPO的整体框架包括以下几个主要阶段：1) **前缀选择**：从输入问题出发，生成一系列候选的前缀token序列。2) **策略优化**：使用强化学习算法，根据奖励信号优化前缀token的生成策略。3) **渐进式前缀保留**：在训练过程中，逐步增加保留的前缀token的比例，引导模型学习更长的有效推理路径。4) **连续累积奖励**：对每个前缀token序列，采样多个后续的token序列，并将这些序列的奖励累加作为该前缀token序列的奖励信号，以减少奖励偏差。5) **模型更新**：使用优化后的策略更新LLM的参数。

**关键创新**：PPPO的关键创新在于：1) **关注前缀token**：首次明确提出并验证了LLM推理过程中前缀token的重要性，并将其作为优化的重点。2) **渐进式前缀保留**：通过逐步增加保留的前缀token的比例，引导模型学习更长的有效推理路径，避免了早期训练阶段的过度探索。3) **连续累积奖励**：通过对每个前缀token序列采样多个后续序列并累加奖励，有效缓解了奖励稀疏和偏差问题。与现有方法的本质区别在于，PPPO不再对所有token进行无差别训练，而是有针对性地优化对推理过程影响最大的前缀token。

**关键设计**：PPPO的关键设计包括：1) **奖励函数**：奖励函数的设计需要能够准确反映LLM推理的正确性。可以使用外部知识库或人工标注来验证推理结果的正确性，并给予相应的奖励。2) **策略梯度算法**：可以使用常见的策略梯度算法，如PPO或TRPO，来优化前缀token的生成策略。3) **前缀保留比例**：需要仔细调整前缀保留比例的增加速度，以平衡探索和利用之间的关系。4) **采样数量**：需要选择合适的采样数量，以保证奖励信号的准确性和稳定性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15274v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15274v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15274v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PPPO方法在多个推理任务上取得了显著的性能提升。实验结果表明，PPPO在仅使用26.17%的训练token的情况下，推理准确率提升了18.02%，显著优于现有的RLVR方法。这一结果表明，PPPO能够更有效地利用训练资源，并显著提升LLM的推理能力。此外，实验还验证了渐进式前缀保留和连续累积奖励两种训练策略的有效性。

## 🎯 应用场景

PPPO方法具有广泛的应用前景，可以应用于各种需要LLM进行复杂推理的任务，例如数学问题求解、代码生成、知识图谱推理等。该方法能够有效提升LLM的推理能力和准确性，降低计算成本，并有望推动LLM在实际应用中的普及。未来，PPPO可以与其他技术相结合，例如知识增强、多模态融合等，进一步提升LLM的推理性能。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) significantly enhances the reasoning capability of Large Language Models (LLMs). Current RLVR approaches typically conduct training across all generated tokens, but neglect to explore which tokens (e.g., prefix tokens) actually contribute to reasoning. This uniform training strategy spends substantial effort on optimizing low-return tokens, which in turn impedes the potential improvement from high-return tokens and reduces overall training effectiveness. To address this issue, we propose a novel RLVR approach called Progressive Prefix-token Policy Optimization (PPPO), which highlights the significance of the prefix segment of generated outputs. Specifically, inspired by the well-established human thinking theory of Path Dependence, where early-stage thoughts substantially constrain subsequent thinking trajectory, we identify an analogous phenomenon in LLM reasoning termed Beginning Lock-in Effect (BLE). PPPO leverages this finding by focusing its optimization objective on the prefix reasoning process of LLMs. This targeted optimization strategy can positively influence subsequent reasoning processes, and ultimately improve final results. To improve the learning effectiveness of LLMs on how to start reasoning with high quality, PPPO introduces two training strategies: (a) Progressive Prefix Retention, which shapes a progressive learning process by increasing the proportion of retained prefix tokens during training; (b) Continuation Accumulated Reward, which mitigates reward bias by sampling multiple continuations for one prefix token sequence, and accumulating their scores as the reward signal. Extensive experimental results on various reasoning tasks demonstrate that our proposed PPPO outperforms representative RLVR methods, with the accuracy improvements of 18.02% on only 26.17% training tokens.

