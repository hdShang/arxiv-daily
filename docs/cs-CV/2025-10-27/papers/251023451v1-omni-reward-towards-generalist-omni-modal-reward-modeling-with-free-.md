---
layout: default
title: Omni-Reward: Towards Generalist Omni-Modal Reward Modeling with Free-Form Preferences
---

# Omni-Reward: Towards Generalist Omni-Modal Reward Modeling with Free-Form Preferences

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23451" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23451v1</a>
  <a href="https://arxiv.org/pdf/2510.23451.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23451v1" onclick="toggleFavorite(this, '2510.23451v1', 'Omni-Reward: Towards Generalist Omni-Modal Reward Modeling with Free-Form Preferences')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuoran Jin, Hongbang Yuan, Kejian Zhu, Jiachun Li, Pengfei Cao, Yubo Chen, Kang Liu, Jun Zhao

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-10-27

**备注**: 48 pages, 17 figures

---

## 💡 一句话要点

**提出Omni-Reward，用于支持自由形式偏好的通用全模态奖励建模。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `奖励模型` `多模态学习` `偏好建模` `通用人工智能` `人机对齐` `自由形式偏好` `全模态数据`

## 📋 核心要点

1. 现有奖励模型主要集中于文本和图像模态，缺乏对视频、音频等模态的支持，且难以捕捉个性化偏好的复杂性。
2. Omni-Reward通过构建全模态奖励模型，并引入自由形式偏好，旨在提升奖励模型在多模态数据和个性化偏好方面的建模能力。
3. Omni-Reward在自建的Omni-RewardBench基准测试以及其他常用基准上表现出色，验证了其在全模态奖励建模方面的有效性。

## 📝 摘要（中文）

奖励模型（RM）在使AI行为与人类偏好对齐方面起着关键作用，但它们面临两个根本挑战：（1）模态不平衡，大多数RM主要集中在文本和图像模态，对视频、音频和其他模态的支持有限；（2）偏好刚性，在固定的二元偏好对上训练无法捕捉个性化偏好的复杂性和多样性。为了解决上述挑战，我们提出了Omni-Reward，旨在实现支持自由形式偏好的通用全模态奖励建模，包括：（1）评估：我们引入了Omni-RewardBench，这是第一个具有自由形式偏好的全模态RM基准，涵盖文本、图像、视频、音频和3D等五种模态的九个任务；（2）数据：我们构建了Omni-RewardData，一个包含248K个通用偏好对和69K个指令调优对的多模态偏好数据集，用于训练通用全模态RM；（3）模型：我们提出了Omni-RewardModel，包括判别式和生成式RM，并在Omni-RewardBench以及其他广泛使用的奖励建模基准上取得了强大的性能。

## 🔬 方法详解

**问题定义**：现有奖励模型主要集中于文本和图像模态，对视频、音频等模态的支持不足，导致在处理多模态任务时性能受限。此外，传统的二元偏好对训练方式无法捕捉用户个性化偏好的复杂性和多样性，限制了模型的泛化能力。

**核心思路**：Omni-Reward的核心思路是构建一个能够处理多种模态数据并支持自由形式偏好的通用奖励模型。通过引入全模态数据和自由形式偏好，模型能够更好地理解用户意图，从而更准确地评估不同模态数据的质量。

**技术框架**：Omni-Reward包含三个主要组成部分：Omni-RewardBench（评估基准）、Omni-RewardData（多模态偏好数据集）和Omni-RewardModel（奖励模型）。Omni-RewardBench用于评估模型在不同模态和任务上的性能。Omni-RewardData用于训练奖励模型。Omni-RewardModel包含判别式和生成式两种模型结构，用于学习不同模态数据之间的关系和用户偏好。

**关键创新**：Omni-Reward的关键创新在于其对全模态数据和自由形式偏好的支持。通过构建包含多种模态数据和自由形式偏好的数据集，并设计相应的模型结构，Omni-Reward能够更好地捕捉用户意图，从而更准确地评估不同模态数据的质量。此外，Omni-RewardBench的提出为全模态奖励建模提供了一个统一的评估平台。

**关键设计**：Omni-RewardModel采用了判别式和生成式两种模型结构。判别式模型用于直接预测奖励值，而生成式模型用于生成符合用户偏好的内容。具体的技术细节包括：使用Transformer架构作为基础模型，采用对比学习损失函数来学习不同模态数据之间的关系，并使用强化学习算法来优化模型的生成能力。数据集构建方面，采用了人工标注和自动生成相结合的方式，以保证数据的质量和多样性。

## 📊 实验亮点

Omni-Reward在Omni-RewardBench基准测试中取得了显著的性能提升，尤其是在视频、音频和3D等模态上，相较于现有方法有明显优势。此外，Omni-Reward在其他常用的奖励建模基准上也表现出色，验证了其通用性和有效性。

## 🎯 应用场景

Omni-Reward可应用于各种需要理解和对齐人类偏好的多模态任务中，例如：多模态内容推荐、智能对话系统、机器人行为规划等。通过更准确地捕捉用户意图，Omni-Reward可以提升用户体验，并促进人机协作。

## 📄 摘要（原文）

> Reward models (RMs) play a critical role in aligning AI behaviors with human preferences, yet they face two fundamental challenges: (1) Modality Imbalance, where most RMs are mainly focused on text and image modalities, offering limited support for video, audio, and other modalities; and (2) Preference Rigidity, where training on fixed binary preference pairs fails to capture the complexity and diversity of personalized preferences. To address the above challenges, we propose Omni-Reward, a step toward generalist omni-modal reward modeling with support for free-form preferences, consisting of: (1) Evaluation: We introduce Omni-RewardBench, the first omni-modal RM benchmark with free-form preferences, covering nine tasks across five modalities including text, image, video, audio, and 3D; (2) Data: We construct Omni-RewardData, a multimodal preference dataset comprising 248K general preference pairs and 69K instruction-tuning pairs for training generalist omni-modal RMs; (3) Model: We propose Omni-RewardModel, which includes both discriminative and generative RMs, and achieves strong performance on Omni-RewardBench as well as other widely used reward modeling benchmarks.

