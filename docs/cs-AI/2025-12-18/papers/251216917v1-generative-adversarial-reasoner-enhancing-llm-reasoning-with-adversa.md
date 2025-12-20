---
layout: default
title: Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning
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

**提出生成对抗推理器，通过对抗强化学习提升LLM的推理能力，尤其在数学问题上。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `对抗学习` `数学推理` `推理器` `判别器` `奖励塑造` `在线学习`

## 📋 核心要点

1. 现有具备显式推理能力的大型语言模型在数学推理方面表现出色，但仍存在过程错误，如不正确的计算和脆弱的逻辑。
2. 论文提出生成对抗推理器，通过对抗强化学习协同训练LLM推理器和判别器，利用判别器对推理过程进行细粒度评估。
3. 实验结果表明，该方法在多个数学基准测试中，相较于标准强化学习后训练的基线模型，性能得到显著提升。

## 📝 摘要（中文）

本文提出了一种名为生成对抗推理器(Generative Adversarial Reasoner)的在线联合训练框架，旨在通过对抗强化学习协同进化LLM推理器和基于LLM的判别器，从而增强推理能力。该框架采用计算高效的审查机制，将每个推理链划分为逻辑完整的、长度相当的片段，判别器使用简洁、结构化的理由评估每个片段的合理性。学习过程耦合了互补信号：LLM推理器因产生逻辑一致且能得出正确答案的步骤而获得奖励，而判别器因正确检测到推理过程中的错误或区分推理轨迹而获得奖励。这产生了密集的、良好校准的、在线的步骤级别奖励，补充了稀疏的精确匹配信号，改善了信用分配，提高了样本效率，并增强了LLM的整体推理质量。在各种数学基准测试中，该方法相对于使用标准RL后训练的强大基线，实现了持续的收益。具体而言，在AIME24上，DeepSeek-R1-Distill-Qwen-7B从54.0提高到61.3（+7.3），DeepSeek-R1-Distill-Llama-8B从43.7提高到53.7（+10.0）。模块化判别器还能够灵活地进行奖励塑造，以实现诸如教师知识蒸馏、偏好对齐和基于数学证明的推理等目标。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在数学推理过程中出现的逻辑错误、计算错误等问题。现有方法通常依赖于稀疏的奖励信号（例如，答案是否完全正确），难以对推理过程中的每一步进行有效指导，导致信用分配困难，训练效率低下。

**核心思路**：论文的核心思路是引入一个判别器，与LLM推理器进行对抗训练。判别器负责评估推理过程中的每一步是否合理，并给出结构化的理由。通过这种方式，可以为推理器提供更密集、更细粒度的奖励信号，从而提高训练效率和推理质量。

**技术框架**：整体框架包含两个主要模块：LLM推理器和LLM判别器。推理器负责生成推理步骤，判别器负责评估每个推理步骤的合理性。训练过程采用在线强化学习，推理器根据判别器的反馈调整策略，判别器根据推理器的表现调整评估标准。一个关键组件是“审查机制”，它将推理链分割成逻辑完整的片段，以便判别器进行评估。

**关键创新**：最重要的技术创新点在于使用对抗强化学习来训练LLM推理器。与传统的强化学习方法相比，该方法能够提供更密集、更细粒度的奖励信号，从而更好地指导推理过程。此外，模块化的判别器设计使得可以灵活地进行奖励塑造，以适应不同的目标，例如知识蒸馏和偏好对齐。

**关键设计**：审查机制将推理链分割成长度相当的片段，确保每个片段在逻辑上是完整的。判别器输出结构化的理由，解释其评估结果。推理器和判别器的奖励函数被设计为相互对抗，推理器试图生成能够欺骗判别器的推理步骤，而判别器试图准确地识别推理过程中的错误。具体参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

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

实验结果表明，该方法在AIME24数学基准测试中取得了显著的性能提升。具体而言，DeepSeek-R1-Distill-Qwen-7B模型从54.0提高到61.3（+7.3），DeepSeek-R1-Distill-Llama-8B模型从43.7提高到53.7（+10.0）。这些结果表明，该方法能够有效地提高LLM的推理能力，并优于现有的强化学习后训练方法。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理能力的场景，例如数学问题求解、科学研究、智能问答系统等。通过提高LLM的推理能力，可以使其在这些领域发挥更大的作用，并为自动化推理和决策提供更可靠的基础。未来的影响包括提升AI在复杂问题解决方面的能力，并可能促进AI在教育、科研等领域的应用。

## 📄 摘要（原文）

> Large language models (LLMs) with explicit reasoning capabilities excel at mathematical reasoning yet still commit process errors, such as incorrect calculations, brittle logic, and superficially plausible but invalid steps. In this paper, we introduce Generative Adversarial Reasoner, an on-policy joint training framework designed to enhance reasoning by co-evolving an LLM reasoner and an LLM-based discriminator through adversarial reinforcement learning. A compute-efficient review schedule partitions each reasoning chain into logically complete slices of comparable length, and the discriminator evaluates each slice's soundness with concise, structured justifications. Learning couples complementary signals: the LLM reasoner is rewarded for logically consistent steps that yield correct answers, while the discriminator earns rewards for correctly detecting errors or distinguishing traces in the reasoning process. This produces dense, well-calibrated, on-policy step-level rewards that supplement sparse exact-match signals, improving credit assignment, increasing sample efficiency, and enhancing overall reasoning quality of LLMs. Across various mathematical benchmarks, the method delivers consistent gains over strong baselines with standard RL post-training. Specifically, on AIME24, we improve DeepSeek-R1-Distill-Qwen-7B from 54.0 to 61.3 (+7.3) and DeepSeek-R1-Distill-Llama-8B from 43.7 to 53.7 (+10.0). The modular discriminator also enables flexible reward shaping for objectives such as teacher distillation, preference alignment, and mathematical proof-based reasoning.

