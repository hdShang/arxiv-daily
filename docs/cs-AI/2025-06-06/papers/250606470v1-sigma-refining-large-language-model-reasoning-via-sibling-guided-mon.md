---
layout: default
title: "SIGMA: Refining Large Language Model Reasoning via Sibling-Guided Monte Carlo Augmentation"
---

# SIGMA: Refining Large Language Model Reasoning via Sibling-Guided Monte Carlo Augmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06470" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06470v1</a>
  <a href="https://arxiv.org/pdf/2506.06470.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06470v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06470v1', 'SIGMA: Refining Large Language Model Reasoning via Sibling-Guided Monte Carlo Augmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanwei Ren, Haotian Zhang, Fuxiang Wu, Jiayan Qiu, Jiaxing Huang, Baosheng Yu, Liu Liu

**分类**: cs.AI, cs.LG

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出SIGMA框架以提升大型语言模型推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理能力` `蒙特卡罗树搜索` `数据质量` `兄弟节点` `优化算法` `自然语言处理`

## 📋 核心要点

1. 现有方法在提升大型语言模型推理能力时，简单扩展数据集已开始出现收益递减，数据质量成为关键挑战。
2. SIGMA框架通过重新整合被丢弃的兄弟节点，利用这些节点中的信息来优化推理过程，提升模型性能。
3. 在MATH基准测试中，SIGMA调优的7B模型仅使用30K样本便达到了54.92%的准确率，显著优于590K样本训练的模型。

## 📝 摘要（中文）

随着大型语言模型的训练数据规模不断扩大，数据质量的重要性愈发凸显。传统的蒙特卡罗树搜索（MCTS）方法通常只保留搜索树中的最佳轨迹，忽略了包含有价值部分见解的兄弟节点。本文提出SIGMA（Sibling Guided Monte Carlo Augmentation）框架，通过重新整合这些被丢弃的兄弟节点，提升大型语言模型的推理能力。SIGMA通过在每条搜索路径上建立兄弟节点之间的语义联系，采用两阶段的精炼过程，首先由批评模型识别兄弟节点集中的优缺点，然后通过文本反向传播模型对最佳轨迹进行修正。实验表明，SIGMA显著提高了推理轨迹的质量，在MATH基准测试中，使用仅30K样本的7B模型达到了54.92%的准确率，超越了在590K样本上训练的最先进模型。

## 🔬 方法详解

**问题定义**：本文旨在解决传统蒙特卡罗树搜索方法中，仅保留最佳轨迹而忽略兄弟节点的问题。这种做法导致有价值的信息被浪费，影响了大型语言模型的推理能力。

**核心思路**：SIGMA框架的核心思想是重新整合被丢弃的兄弟节点，通过建立兄弟节点之间的语义联系，利用这些节点中的信息来优化推理过程。

**技术框架**：SIGMA框架包括两个主要模块：批评模型和修正模型。批评模型负责识别兄弟节点集中的优缺点，而修正模型则通过文本反向传播对最佳轨迹进行修正。

**关键创新**：SIGMA的创新在于其兄弟节点的再利用策略，区别于传统方法仅关注最佳轨迹，充分挖掘了非最优推理分支中的信息。

**关键设计**：在模型设计中，采用了两阶段的精炼过程，批评模型和修正模型的具体结构和损失函数设置尚未详细披露，可能需要进一步的研究来优化这些参数。

## 📊 实验亮点

在MATH基准测试中，SIGMA调优的7B模型仅使用30K样本便达到了54.92%的准确率，显著超越了在590K样本上训练的最先进模型，展示了兄弟引导优化的有效性。

## 🎯 应用场景

SIGMA框架的潜在应用领域包括自然语言处理、智能问答系统和教育辅助工具等。通过提升大型语言模型的推理能力，SIGMA能够在更复杂的任务中提供更准确的结果，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Enhancing large language models by simply scaling up datasets has begun to yield diminishing returns, shifting the spotlight to data quality. Monte Carlo Tree Search (MCTS) has emerged as a powerful technique for generating high-quality chain-of-thought data, yet conventional approaches typically retain only the top-scoring trajectory from the search tree, discarding sibling nodes that often contain valuable partial insights, recurrent error patterns, and alternative reasoning strategies. This unconditional rejection of non-optimal reasoning branches may waste vast amounts of informative data in the whole search tree. We propose SIGMA (Sibling Guided Monte Carlo Augmentation), a novel framework that reintegrates these discarded sibling nodes to refine LLM reasoning. SIGMA forges semantic links among sibling nodes along each search path and applies a two-stage refinement: a critique model identifies overlooked strengths and weaknesses across the sibling set, and a revision model conducts text-based backpropagation to refine the top-scoring trajectory in light of this comparative feedback. By recovering and amplifying the underutilized but valuable signals from non-optimal reasoning branches, SIGMA substantially improves reasoning trajectories. On the challenging MATH benchmark, our SIGMA-tuned 7B model achieves 54.92% accuracy using only 30K samples, outperforming state-of-the-art models trained on 590K samples. This result highlights that our sibling-guided optimization not only significantly reduces data usage but also significantly boosts LLM reasoning.

