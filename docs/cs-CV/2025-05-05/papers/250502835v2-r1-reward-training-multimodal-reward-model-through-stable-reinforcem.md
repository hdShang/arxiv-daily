---
layout: default
title: R1-Reward: Training Multimodal Reward Model Through Stable Reinforcement Learning
---

# R1-Reward: Training Multimodal Reward Model Through Stable Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02835" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02835v2</a>
  <a href="https://arxiv.org/pdf/2505.02835.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02835v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02835v2', 'R1-Reward: Training Multimodal Reward Model Through Stable Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi-Fan Zhang, Xingyu Lu, Xiao Hu, Chaoyou Fu, Bin Wen, Tianke Zhang, Changyi Liu, Kaiyu Jiang, Kaibing Chen, Kaiyu Tang, Haojie Ding, Jiankang Chen, Fan Yang, Zhang Zhang, Tingting Gao, Liang Wang

**分类**: cs.CV, cs.CL

**发布日期**: 2025-05-05 (更新: 2025-05-09)

**备注**: Home page: https://github.com/yfzhang114/r1_reward

---

## 💡 一句话要点

**提出R1-Reward以解决多模态奖励建模不稳定问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态奖励模型` `强化学习` `长期推理` `StableReinforce算法` `模型训练` `性能提升` `数据收集`

## 📋 核心要点

1. 现有的奖励建模方法在应用强化学习时，常常面临训练不稳定或崩溃的问题，限制了其长期推理能力的发挥。
2. 本文提出将奖励建模问题重新表述为基于规则的强化学习任务，并引入StableReinforce算法以优化训练过程。
3. R1-Reward模型在多模态奖励建模基准上取得了显著提升，展示了强化学习算法在优化多模态奖励模型中的潜力。

## 📝 摘要（中文）

多模态奖励模型（MRMs）在提升多模态大语言模型（MLLMs）的性能中起着关键作用。尽管近期的研究主要集中在模型结构和训练数据的改进上，但对长期推理能力在奖励建模中的有效性及其激活方式的探索仍然有限。本文探讨了如何利用强化学习（RL）来改善奖励建模，提出了StableReinforce算法，通过优化训练损失、优势估计策略和奖励设计，显著提高了训练的稳定性和性能。我们收集了20万条来自多样数据集的偏好数据，使用StableReinforce算法训练的R1-Reward在多模态奖励建模基准上表现优异，相较于之前的最先进模型，在VL Reward-Bench上提升了8.4%，在Multimodal Reward Bench上提升了14.3%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有奖励建模方法在应用强化学习时的不稳定性和崩溃问题，尤其是在长期推理能力的激活方面存在的不足。

**核心思路**：通过将奖励建模问题重新定义为基于规则的强化学习任务，提出StableReinforce算法，以优化训练过程中的损失函数、优势估计和奖励设计，从而提高训练的稳定性。

**技术框架**：整体架构包括数据收集、奖励建模和强化学习训练三个主要阶段。首先，收集来自多样数据集的偏好数据，然后利用StableReinforce算法进行模型训练。

**关键创新**：StableReinforce算法的提出是本研究的核心创新，它通过对现有强化学习方法的改进，克服了训练不稳定的问题，使得奖励建模更加高效。

**关键设计**：在StableReinforce算法中，优化了训练损失的计算方式，改进了优势估计策略，并重新设计了奖励机制，这些设计细节共同促进了模型的稳定性和性能提升。

## 📊 实验亮点

在实验中，R1-Reward模型在VL Reward-Bench上实现了8.4%的性能提升，在Multimodal Reward Bench上实现了14.3%的提升，显示出其在多模态奖励建模中的显著优势。这些结果表明，StableReinforce算法有效地提高了模型的训练稳定性和性能。

## 🎯 应用场景

该研究的潜在应用领域包括多模态大语言模型的训练和优化，尤其是在需要长期推理和复杂决策的任务中，如智能助手、自动内容生成和多模态交互系统。未来，R1-Reward模型可能会在实际应用中提升多模态系统的智能水平和用户体验。

## 📄 摘要（原文）

> Multimodal Reward Models (MRMs) play a crucial role in enhancing the performance of Multimodal Large Language Models (MLLMs). While recent advancements have primarily focused on improving the model structure and training data of MRMs, there has been limited exploration into the effectiveness of long-term reasoning capabilities for reward modeling and how to activate these capabilities in MRMs. In this paper, we explore how Reinforcement Learning (RL) can be used to improve reward modeling. Specifically, we reformulate the reward modeling problem as a rule-based RL task. However, we observe that directly applying existing RL algorithms, such as Reinforce++, to reward modeling often leads to training instability or even collapse due to the inherent limitations of these algorithms. To address this issue, we propose the StableReinforce algorithm, which refines the training loss, advantage estimation strategy, and reward design of existing RL methods. These refinements result in more stable training dynamics and superior performance. To facilitate MRM training, we collect 200K preference data from diverse datasets. Our reward model, R1-Reward, trained using the StableReinforce algorithm on this dataset, significantly improves performance on multimodal reward modeling benchmarks. Compared to previous SOTA models, R1-Reward achieves a $8.4\%$ improvement on the VL Reward-Bench and a $14.3\%$ improvement on the Multimodal Reward Bench. Moreover, with more inference compute, R1-Reward's performance is further enhanced, highlighting the potential of RL algorithms in optimizing MRMs.

