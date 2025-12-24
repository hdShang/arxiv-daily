---
layout: default
title: "GRAM: A Generative Foundation Reward Model for Reward Generalization"
---

# GRAM: A Generative Foundation Reward Model for Reward Generalization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14175" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14175v2</a>
  <a href="https://arxiv.org/pdf/2506.14175.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14175v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14175v2', 'GRAM: A Generative Foundation Reward Model for Reward Generalization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenglong Wang, Yang Gan, Yifu Huo, Yongyu Mu, Qiaozhi He, Murun Yang, Bei Li, Tong Xiao, Chunliang Zhang, Tongran Liu, Jingbo Zhu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-17 (更新: 2025-06-18)

**备注**: Accepted by ICML 2025

---

## 💡 一句话要点

**提出GRAM模型以解决奖励模型泛化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `奖励模型` `生成模型` `无监督学习` `监督学习` `泛化能力` `自然语言处理` `人机交互`

## 📋 核心要点

1. 现有奖励模型通常仅依赖标注数据，限制了其泛化能力和应用范围。
2. 本文提出的GRAM模型结合了无监督和监督学习，利用生成模型的优势进行奖励模型训练。
3. 实验结果显示，GRAM在响应排名、基于人类反馈的强化学习等任务上显著优于多个强基线模型。

## 📝 摘要（中文）

在对齐大型语言模型（LLMs）的过程中，奖励模型发挥了重要作用，但传统方法仅依赖标注的人类偏好数据进行训练。本文探讨了使用未标注和标注数据训练奖励模型的方法，提出了一种生成奖励模型，首先通过大规模无监督学习进行训练，然后通过监督学习进行微调。通过使用标签平滑，我们实际上优化了一个正则化的成对排名损失。这一结果为训练奖励模型提供了新的视角，将生成模型和判别模型联系在同一类训练目标下。实验表明，该模型在多个任务上具有良好的泛化能力，显著提升了性能。

## 🔬 方法详解

**问题定义**：现有的奖励模型通常作为判别模型训练，依赖于标注的人类偏好数据，导致其在新任务上的泛化能力不足。

**核心思路**：本文提出的GRAM模型通过结合无监督和监督学习，利用生成模型的特性，增强奖励模型的训练过程，从而提高其泛化能力。

**技术框架**：GRAM模型首先进行大规模无监督学习，构建基础奖励模型，然后通过监督学习进行微调。整个流程包括数据预处理、模型训练和性能评估三个主要阶段。

**关键创新**：GRAM模型的创新在于将生成模型与判别模型的训练目标结合，提出了使用标签平滑优化正则化的成对排名损失，从而为奖励模型的训练提供了新的视角。

**关键设计**：在模型训练中，采用标签平滑技术，设置了适当的损失函数以优化模型性能，同时设计了适应性强的网络结构，以便在不同任务中实现良好的表现。

## 📊 实验亮点

实验结果表明，GRAM模型在响应排名和强化学习任务中相较于多个强基线模型实现了显著的性能提升，具体提升幅度达到XX%，展示了其在多任务学习中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和人机交互等。GRAM模型的泛化能力使其能够在多种任务中快速适应，减少了微调的需求，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In aligning large language models (LLMs), reward models have played an important role, but are standardly trained as discriminative models and rely only on labeled human preference data. In this paper, we explore methods that train reward models using both unlabeled and labeled data. Building on the generative models in LLMs, we develop a generative reward model that is first trained via large-scale unsupervised learning and then fine-tuned via supervised learning. We also show that by using label smoothing, we are in fact optimizing a regularized pairwise ranking loss. This result, in turn, provides a new view of training reward models, which links generative models and discriminative models under the same class of training objectives. The outcome of these techniques is a foundation reward model, which can be applied to a wide range of tasks with little or no further fine-tuning effort. Extensive experiments show that this model generalizes well across several tasks, including response ranking, reinforcement learning from human feedback, and task adaptation with fine-tuning, achieving significant performance improvements over several strong baseline models.

