---
layout: default
title: "LearnAlign: Reasoning Data Selection for Reinforcement Learning in Large Language Models Based on Improved Gradient Alignment"
---

# LearnAlign: Reasoning Data Selection for Reinforcement Learning in Large Language Models Based on Improved Gradient Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11480" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11480v3</a>
  <a href="https://arxiv.org/pdf/2506.11480.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11480v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11480v3', 'LearnAlign: Reasoning Data Selection for Reinforcement Learning in Large Language Models Based on Improved Gradient Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shipeng Li, Shikun Li, Zhiqin Yang, Xinghua Zhang, Gaode Chen, Xiaobo Xia, Hengyu Liu, Zhe Peng

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-13 (更新: 2025-07-04)

---

## 💡 一句话要点

**提出LearnAlign以解决大语言模型强化学习中的数据选择问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大语言模型` `数据选择` `梯度对齐` `推理能力` `数据效率` `机器学习`

## 📋 核心要点

1. 现有的强化学习方法在大语言模型的推理能力提升中面临数据效率低下的挑战。
2. 本文提出的LearnAlign方法通过智能选择可学习的推理数据，优化了后训练过程中的数据使用效率。
3. 实验结果显示，LearnAlign在GSM8K基准上将数据需求减少至1000个数据点，同时性能达到77.53%，优于全数据集的77.04%。

## 📝 摘要（中文）

强化学习（RL）已成为提升大语言模型（LLM）推理能力的关键技术，但其数据效率低下仍是主要瓶颈。为了解决这一关键且具有挑战性的问题，本文提出了一种基于梯度对齐的智能数据选择方法LearnAlign，该方法能够为RL后训练智能选择可学习和具有代表性的推理训练数据。通过引入基于成功率的数据可学习性，克服了梯度范数中的响应长度偏差问题。实验结果表明，该方法在三个数学推理基准上显著减少了训练数据需求，同时在性能上仅有轻微下降，甚至在某些情况下表现更佳。该研究为数据高效的RL后训练提供了宝贵的见解，并为未来优化推理数据选择的研究奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在强化学习过程中面临的数据效率低下问题。现有方法在训练时通常依赖于大量数据，导致资源浪费和训练时间延长。

**核心思路**：LearnAlign通过引入基于成功率的数据可学习性，智能选择最具代表性的训练数据，从而提高数据使用效率，减少对数据量的依赖。

**技术框架**：该方法的整体架构包括数据选择模块和强化学习训练模块。数据选择模块根据梯度对齐和成功率评估数据的可学习性，随后将选出的数据用于强化学习训练。

**关键创新**：LearnAlign的核心创新在于引入了基于成功率的学习潜力评估机制，这一机制有效克服了传统方法中响应长度偏差的问题，使得数据选择更加精准。

**关键设计**：在技术细节上，LearnAlign采用了特定的损失函数来优化梯度对齐，同时在数据选择过程中设置了阈值，以确保选出的数据在推理任务中具有较高的代表性和学习价值。

## 📊 实验亮点

实验结果表明，LearnAlign在GSM8K基准上将数据需求减少至1000个数据点，同时性能达到77.53%，优于全数据集的77.04%。这一结果显示了LearnAlign在数据选择效率和模型性能之间的良好平衡，验证了其在强化学习后训练中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融和科学研究等需要推理能力的场景。通过优化数据选择，LearnAlign可以显著提高大语言模型在特定任务上的表现，降低训练成本，推动智能系统的广泛应用。未来，随着更多优化策略的提出，LearnAlign有望在更广泛的领域中发挥重要作用。

## 📄 摘要（原文）

> Reinforcement learning (RL) has become a key technique for enhancing LLMs' reasoning abilities, yet its data inefficiency remains a major bottleneck. To address this critical yet challenging issue, we present a novel gradient-alignment-based method, named LearnAlign, which intelligently selects the learnable and representative training reasoning data for RL post-training. To overcome the issue of response-length bias in gradient norms, we introduce the data learnability based on the success rate, which can indicate the learning potential of each data point. Experiments across three mathematical reasoning benchmarks demonstrate that our method significantly reduces training data requirements while achieving minor performance degradation or even improving performance compared to full-data training. For example, it reduces data requirements by up to 1,000 data points with better performance (77.53%) than that on the full dataset on GSM8K benchmark (77.04%). Furthermore, we show its effectiveness in the staged RL setting. This work provides valuable insights into data-efficient RL post-training and establishes a foundation for future research in optimizing reasoning data selection. To facilitate future work, we will release code.

