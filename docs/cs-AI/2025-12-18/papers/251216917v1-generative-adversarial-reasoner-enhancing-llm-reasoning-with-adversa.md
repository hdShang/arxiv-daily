---
layout: default
title: "Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning"
---

# Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16917" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16917v1</a>
  <a href="https://arxiv.org/pdf/2512.16917.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16917v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16917v1', 'Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qihao Liu, Luoxin Ye, Wufei Ma, Yu-Cheng Chou, Alan Yuille

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出Generative Adversarial Reasoner，通过对抗强化学习提升LLM的推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `对抗学习` `数学推理` `推理链` `奖励塑造` `知识蒸馏`

## 📋 核心要点

1. 现有LLM在数学推理方面表现出色，但仍存在计算错误、逻辑脆弱和表面合理但无效的步骤等过程性错误。
2. 论文提出Generative Adversarial Reasoner，通过对抗强化学习协同训练LLM推理器和判别器，提升推理的逻辑一致性和准确性。
3. 实验表明，该方法在数学基准测试中优于现有RL微调方法，在AIME24数据集上DeepSeek模型提升高达10个百分点。

## 📝 摘要（中文）

本文提出了一种名为Generative Adversarial Reasoner 的 on-policy 联合训练框架，旨在通过对抗强化学习协同进化 LLM 推理器和基于 LLM 的判别器，从而增强 LLM 的推理能力。该框架采用计算高效的审查机制，将每个推理链划分为逻辑完整的、长度相当的片段，判别器通过简洁、结构化的理由评估每个片段的合理性。学习过程耦合了互补信号：LLM 推理器因产生正确答案的逻辑一致步骤而获得奖励，而判别器因正确检测推理过程中的错误或区分推理轨迹而获得奖励。这产生了密集的、良好校准的、on-policy 的步级奖励，补充了稀疏的精确匹配信号，改善了信用分配，提高了样本效率，并增强了 LLM 的整体推理质量。在各种数学基准测试中，该方法相对于使用标准 RL 后训练的强大基线，实现了持续的收益。特别是在 AIME24 上，我们将 DeepSeek-R1-Distill-Qwen-7B 从 54.0 提高到 61.3 (+7.3)，将 DeepSeek-R1-Distill-Llama-8B 从 43.7 提高到 53.7 (+10.0)。模块化判别器还能够灵活地进行奖励塑造，以实现诸如教师知识蒸馏、偏好对齐和基于数学证明的推理等目标。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在数学推理过程中出现的逻辑错误、计算错误以及推理步骤无效等问题。现有方法通常依赖于稀疏的奖励信号（例如，最终答案是否正确），导致信用分配困难，训练效率低下，难以有效提升LLM的推理能力。

**核心思路**：论文的核心思路是通过对抗强化学习，同时训练一个LLM推理器和一个LLM判别器。推理器负责生成推理步骤，判别器负责评估每个推理步骤的合理性。通过这种对抗的方式，推理器可以学习到更细粒度的奖励信号，从而更好地优化推理过程。

**技术框架**：Generative Adversarial Reasoner (GAR) 包含两个主要模块：LLM推理器和LLM判别器。推理器负责生成推理链，判别器负责评估推理链中每个片段的合理性，并给出结构化的理由。训练过程采用on-policy强化学习，推理器根据判别器的反馈调整策略，判别器根据推理器的输出调整判别能力。整个框架通过对抗的方式，不断提升推理器和判别器的能力。

**关键创新**：该方法最重要的创新点在于引入了对抗强化学习来提升LLM的推理能力。与传统的强化学习方法相比，GAR能够提供更密集、更细粒度的奖励信号，从而更好地指导推理器的训练。此外，GAR的模块化判别器设计使得可以灵活地进行奖励塑造，以适应不同的目标，例如教师知识蒸馏、偏好对齐和基于数学证明的推理。

**关键设计**：GAR的关键设计包括：(1) 计算高效的审查机制，将推理链划分为逻辑完整的片段；(2) 判别器输出的结构化理由，提供更丰富的反馈信息；(3) 基于对抗强化学习的训练策略，协同优化推理器和判别器；(4) 灵活的奖励塑造机制，可以根据不同的目标进行调整。具体参数设置和网络结构等细节未在摘要中详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16917v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16917v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16917v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Generative Adversarial Reasoner 在多个数学基准测试中取得了显著的提升。在 AIME24 数据集上，DeepSeek-R1-Distill-Qwen-7B 模型的准确率从 54.0% 提高到 61.3% (+7.3%)，DeepSeek-R1-Distill-Llama-8B 模型的准确率从 43.7% 提高到 53.7% (+10.0%)。这些结果表明，该方法能够有效提升 LLM 的推理能力。

## 🎯 应用场景

该研究成果可应用于需要复杂推理能力的各种领域，例如数学解题、科学研究、代码生成、逻辑推理等。通过提升LLM的推理能力，可以提高自动化系统的智能化水平，减少人工干预，提高工作效率。未来，该方法有望应用于更广泛的领域，例如医疗诊断、金融分析等。

## 📄 摘要（原文）

> Large language models (LLMs) with explicit reasoning capabilities excel at mathematical reasoning yet still commit process errors, such as incorrect calculations, brittle logic, and superficially plausible but invalid steps. In this paper, we introduce Generative Adversarial Reasoner, an on-policy joint training framework designed to enhance reasoning by co-evolving an LLM reasoner and an LLM-based discriminator through adversarial reinforcement learning. A compute-efficient review schedule partitions each reasoning chain into logically complete slices of comparable length, and the discriminator evaluates each slice's soundness with concise, structured justifications. Learning couples complementary signals: the LLM reasoner is rewarded for logically consistent steps that yield correct answers, while the discriminator earns rewards for correctly detecting errors or distinguishing traces in the reasoning process. This produces dense, well-calibrated, on-policy step-level rewards that supplement sparse exact-match signals, improving credit assignment, increasing sample efficiency, and enhancing overall reasoning quality of LLMs. Across various mathematical benchmarks, the method delivers consistent gains over strong baselines with standard RL post-training. Specifically, on AIME24, we improve DeepSeek-R1-Distill-Qwen-7B from 54.0 to 61.3 (+7.3) and DeepSeek-R1-Distill-Llama-8B from 43.7 to 53.7 (+10.0). The modular discriminator also enables flexible reward shaping for objectives such as teacher distillation, preference alignment, and mathematical proof-based reasoning.

