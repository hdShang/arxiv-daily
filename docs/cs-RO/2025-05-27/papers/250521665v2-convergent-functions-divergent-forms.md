---
layout: default
title: Convergent Functions, Divergent Forms
---

# Convergent Functions, Divergent Forms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21665" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21665v2</a>
  <a href="https://arxiv.org/pdf/2505.21665.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21665v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21665v2', 'Convergent Functions, Divergent Forms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyeonseong Jeon, Ainaz Eftekhar, Aaron Walsman, Kuo-Hao Zeng, Ali Farhadi, Ranjay Krishna

**分类**: cs.RO

**发布日期**: 2025-05-27 (更新: 2025-11-14)

---

## 💡 一句话要点

**提出LOKI框架以高效设计适应性形态与控制策略**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `形态设计` `控制策略` `生物启发` `进化算法` `样本效率` `动态搜索` `多样性` `适应性`

## 📋 核心要点

1. 现有的进化算法和质量多样性算法在设计适应性形态时效率低下，难以快速适应新任务。
2. LOKI框架通过学习共享控制策略和动态局部搜索，提升了形态设计的效率和多样性。
3. 实验结果显示，LOKI能够探索780倍的设计，使用78%更少的模拟步骤，且在未见任务中表现出更高的适应性。

## 📝 摘要（中文）

我们提出了LOKI，一个计算高效的框架，用于共同设计在未见任务中具有泛化能力的形态和控制策略。受生物适应启发，我们的方法克服了传统进化和质量多样性算法的低效。通过在学习的潜在空间中训练共享控制策略，LOKI显著降低了每种设计的训练成本。同时，通过用动态局部搜索替代突变，促进了形态的多样性，防止了过早收敛。LOKI在UNIMAL设计空间和平坦地形运动任务中发现了丰富多样的设计，且这些形态在未见的下游任务中表现更佳，展现出更高的适应性和样本效率。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有进化算法在设计适应性形态时的低效问题，尤其是在面对新任务时的适应能力不足。传统方法往往需要大量的计算资源和时间，难以实现快速的形态调整。

**核心思路**：LOKI框架的核心思路是通过学习共享控制策略来降低每种设计的训练成本，同时利用动态局部搜索来替代传统的突变操作，从而促进形态的多样性和探索能力。

**技术框架**：LOKI的整体架构包括两个主要模块：一是共享控制策略的学习，通过聚类相似形态的设计来提高训练效率；二是动态局部搜索，允许在设计空间中进行更广泛的探索，避免过早收敛。

**关键创新**：LOKI的关键创新在于引入了共享控制策略和动态局部搜索的结合，这一设计使得形态设计的样本效率显著提高，能够在更少的计算资源下探索更多的设计。与传统方法相比，LOKI在多样性和适应性上表现出明显优势。

**关键设计**：在关键设计方面，LOKI采用了聚类算法来识别形态相似性，并通过动态局部搜索算法来引导探索过程。此外，损失函数的设计也经过优化，以确保控制策略的有效性和适应性。整体网络结构则基于深度学习框架，确保了高效的训练和推理能力。

## 📊 实验亮点

实验结果表明，LOKI能够在设计空间中探索780倍的设计，使用78%更少的模拟步骤，且每种设计的计算成本降低了40%。在未见的下游任务中，LOKI的设计在灵活性、稳定性和操作能力上表现出2倍的奖励提升，显示出其优越的适应性和样本效率。

## 🎯 应用场景

LOKI框架的潜在应用领域包括机器人设计、自动化制造和生物启发的工程设计等。其高效的形态与控制策略共同设计能力，可以在多种复杂环境中实现更高的适应性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce LOKI, a compute-efficient framework for co-designing morphologies and control policies that generalize across unseen tasks. Inspired by biological adaptation -- where animals quickly adjust to morphological changes -- our method overcomes the inefficiencies of traditional evolutionary and quality-diversity algorithms. We propose learning convergent functions: shared control policies trained across clusters of morphologically similar designs in a learned latent space, drastically reducing the training cost per design. Simultaneously, we promote divergent forms by replacing mutation with dynamic local search, enabling broader exploration and preventing premature convergence. The policy reuse allows us to explore 780$\times$ more designs using 78% fewer simulation steps and 40% less compute per design. Local competition paired with a broader search results in a diverse set of high-performing final morphologies. Using the UNIMAL design space and a flat-terrain locomotion task, LOKI discovers a rich variety of designs -- ranging from quadrupeds to crabs, bipedals, and spinners -- far more diverse than those produced by prior work. These morphologies also transfer better to unseen downstream tasks in agility, stability, and manipulation domains (e.g., 2$\times$ higher reward on bump and push box incline tasks). Overall, our approach produces designs that are both diverse and adaptable, with substantially greater sample efficiency than existing co-design methods. (Project website: https://loki-codesign.github.io/)

