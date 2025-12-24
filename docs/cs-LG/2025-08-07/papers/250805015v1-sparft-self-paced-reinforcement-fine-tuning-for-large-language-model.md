---
layout: default
title: "SPaRFT: Self-Paced Reinforcement Fine-Tuning for Large Language Models"
---

# SPaRFT: Self-Paced Reinforcement Fine-Tuning for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.05015" class="toolbar-btn" target="_blank">📄 arXiv: 2508.05015v1</a>
  <a href="https://arxiv.org/pdf/2508.05015.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.05015v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.05015v1', 'SPaRFT: Self-Paced Reinforcement Fine-Tuning for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dai Do, Manh Nguyen, Svetha Venkatesh, Hung Le

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-07

---

## 💡 一句话要点

**提出SPaRFT以解决大语言模型训练效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自适应学习` `强化学习` `数据选择` `大语言模型` `推理能力` `聚类算法` `多臂老虎机`

## 📋 核心要点

1. 现有的强化学习微调方法需要大量数据和计算资源，限制了小型模型的应用。
2. SPaRFT通过自适应学习框架，优化数据选择和训练时机，提升训练效率。
3. 实验结果显示，SPaRFT在多个推理任务上表现优异，样本使用量显著减少，提升了资源利用率。

## 📝 摘要（中文）

大语言模型（LLMs）在强化学习（RL）微调时展现出强大的推理能力。然而，现有方法需要大量数据和计算资源，使得小型模型难以应用。当前的课程学习或数据选择方法多为启发式驱动，且计算资源消耗巨大，限制了其可扩展性和普适性。本文提出SPaRFT，一个自适应学习框架，通过优化数据使用和训练时机，基于模型能力实现高效学习。首先，采用基于聚类的数据减少方法对训练数据进行语义和难度划分，提取出紧凑且多样的子集以减少冗余。然后，利用多臂老虎机算法将数据集群视为臂，优化训练样本的分配。实验结果表明，SPaRFT在多个推理基准上实现了与最先进基线相当或更好的准确率，同时使用的样本量减少了多达100倍。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在强化学习微调中对数据和计算资源的高需求问题。现有方法往往依赖大量样本和计算，导致小型模型难以有效训练。

**核心思路**：SPaRFT的核心思路是通过自适应学习框架，优化数据选择和训练时机，以提升训练效率和模型性能。通过聚类和多臂老虎机算法，动态调整训练样本的分配，确保模型在适当的时机接触到合适的数据。

**技术框架**：SPaRFT的整体架构包括两个主要模块：首先是基于聚类的数据减少模块，将训练数据按语义和难度进行划分；其次是多臂老虎机模块，优化训练样本的分配策略。

**关键创新**：SPaRFT的主要创新在于结合了数据聚类和自适应样本选择，显著减少了训练所需的样本量，同时保持或提升了模型的推理能力。这一方法与传统的启发式数据选择方法有本质区别。

**关键设计**：在关键设计上，SPaRFT采用了聚类算法对数据进行语义和难度划分，确保训练数据的多样性和代表性。同时，多臂老虎机算法用于动态调整样本分配，依据模型当前性能进行优化。

## 📊 实验亮点

SPaRFT在多个推理基准上表现出色，准确率与最先进的基线相当或更优，同时样本使用量减少了多达100倍。这一显著提升展示了自适应学习框架在资源利用上的优势。

## 🎯 应用场景

SPaRFT的研究成果在多个领域具有潜在应用价值，包括自然语言处理、对话系统和智能助手等。通过提高小型模型的训练效率，该方法能够使得资源有限的环境下也能实现高效的推理能力，推动AI技术的普及和应用。

## 📄 摘要（原文）

> Large language models (LLMs) have shown strong reasoning capabilities when fine-tuned with reinforcement learning (RL). However, such methods require extensive data and compute, making them impractical for smaller models. Current approaches to curriculum learning or data selection are largely heuristic-driven or demand extensive computational resources, limiting their scalability and generalizability. We propose \textbf{SPaRFT}, a self-paced learning framework that enables efficient learning based on the capability of the model being trained through optimizing which data to use and when. First, we apply \emph{cluster-based data reduction} to partition training data by semantics and difficulty, extracting a compact yet diverse subset that reduces redundancy. Then, a \emph{multi-armed bandit} treats data clusters as arms, optimized to allocate training samples based on model current performance. Experiments across multiple reasoning benchmarks show that SPaRFT achieves comparable or better accuracy than state-of-the-art baselines while using up to \(100\times\) fewer samples. Ablation studies and analyses further highlight the importance of both data clustering and adaptive selection. Our results demonstrate that carefully curated, performance-driven training curricula can unlock strong reasoning abilities in LLMs with minimal resources.

