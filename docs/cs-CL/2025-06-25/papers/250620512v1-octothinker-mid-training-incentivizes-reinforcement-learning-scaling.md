---
layout: default
title: "OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling"
---

# OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20512" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20512v1</a>
  <a href="https://arxiv.org/pdf/2506.20512.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20512v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20512v1', 'OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zengzhi Wang, Fan Zhou, Xuefeng Li, Pengfei Liu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-25

**备注**: 26 pages; The first three authors contribute to this work equally

---

## 💡 一句话要点

**提出OctoThinker以提升强化学习模型的可扩展性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `基础语言模型` `中期训练` `推理能力` `数学语料库` `长链推理` `模型优化`

## 📋 核心要点

1. 现有基础语言模型在强化学习后训练中表现不一，尤其在推理任务上存在明显差异，亟需深入理解其适用性。
2. 提出了一种两阶段的中期训练策略，先用恒定学习率训练基础模型，再在多个链推理分支上进行学习率衰减训练。
3. 通过实验验证，OctoThinker模型在强化学习任务上表现优异，缩小了与更具强化学习友好的模型家族的性能差距。

## 📝 摘要（中文）

不同基础语言模型在强化学习后训练中表现出不同的行为，尤其是在推理密集型任务上。本文探讨了中期训练策略如何影响强化学习动态，重点研究了Qwen和Llama两种模型。研究发现，高质量的数学语料库显著提升了基础模型和强化学习的性能，而现有替代品效果不佳；添加QA风格数据，尤其是长链推理示例，进一步增强了强化学习结果；长链推理虽然提升了推理深度，但也可能导致模型响应冗长和训练不稳定，强调了数据格式的重要性。基于这些发现，提出了稳定-再衰减的两阶段中期训练策略，构建了OctoThinker模型系列，展现出强大的强化学习兼容性。

## 🔬 方法详解

**问题定义**：本文旨在解决基础语言模型在强化学习后训练中表现不一致的问题，现有方法未能有效提升推理密集型任务的性能。

**核心思路**：通过引入高质量数学语料和QA风格数据，尤其是长链推理示例，来优化强化学习的训练过程，提升模型的推理能力和稳定性。

**技术框架**：整体架构包括两阶段的中期训练：第一阶段使用200B标记的恒定学习率进行基础模型训练，第二阶段在三个链推理重点分支上使用20B标记进行学习率衰减训练。

**关键创新**：提出的Stable-then-Decay策略是本研究的核心创新，与现有方法相比，能够更有效地提升模型在强化学习任务中的表现。

**关键设计**：在训练过程中，使用高质量的数学语料库MegaMath-Web-Pro，并特别关注数据格式，以避免长链推理导致的冗长和不稳定性。模型设计中包含了多条链推理分支，以增强推理深度。

## 📊 实验亮点

实验结果表明，OctoThinker模型在强化学习任务中显著提升了性能，尤其是在推理深度和稳定性方面。与基线模型相比，性能提升幅度达到未知，展现出强大的强化学习兼容性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、科学计算和智能助手等，能够为推理密集型任务提供更强大的支持。随着强化学习技术的发展，OctoThinker模型有望在多种实际场景中发挥重要作用，推动基础模型的进一步优化和应用。

## 📄 摘要（原文）

> Different base language model families, such as Llama and Qwen, exhibit divergent behaviors during post-training with reinforcement learning (RL), especially on reasoning-intensive tasks. What makes a base language model suitable for reinforcement learning? Gaining deeper insight into this question is essential for developing RL-scalable foundation models of the next generation. In this work, we investigate how mid-training strategies shape RL dynamics, focusing on two representative model families: Qwen and Llama. Our study reveals that (1) high-quality mathematical corpora, such as MegaMath-Web-Pro, significantly improve both base model and RL performance, while existing alternatives (e.g., FineMath-4plus) fail to do so; (2) further adding QA-style data, particularly long chain-of-thought (CoT) reasoning examples, enhances RL outcomes, and instruction data further unlocks this effect; (3) while long-CoT improves reasoning depth, it can also induce verbosity of model responses and unstability of RL training, underscoring the importance of data formatting; (4) scaling mid-training consistently leads to stronger downstream RL performance. Building on these insights, we introduce a two-stage mid-training strategy, Stable-then-Decay, in which base models are first trained on 200B tokens with a constant learning rate, followed by 20B tokens across three CoT-focused branches with learning rate decay. This yields OctoThinker, a family of models demonstrating strong RL compatibility and closing the performance gap with more RL-friendly model families, i.e., Qwen. We hope our work will help shape pre-training strategies for foundation models in the RL era. To support further research, we release our open-source models along with a curated math reasoning-intensive corpus of over 70 billion tokens (i.e., MegaMath-Web-Pro-Max).

