---
layout: default
title: "SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning"
---

# SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16548" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16548v2</a>
  <a href="https://arxiv.org/pdf/2509.16548.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16548v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16548v2', 'SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuyang Ding, Xinyu Shi, Juntao Li, Xiaobo Liang, Zhaopeng Tu, Min Zhang

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-20 (更新: 2025-10-14)

**备注**: NeurIPS 2025. Project page: https://scan-prm.github.io/

---

## 💡 一句话要点

**提出SCAN自降噪蒙特卡洛标注方法，用于稳健的过程奖励学习。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `过程奖励模型` `蒙特卡洛估计` `自降噪` `弱监督学习` `数据合成`

## 📋 核心要点

1. 人工标注过程奖励模型数据成本高、可扩展性差，蒙特卡洛估计合成数据噪声大，易过拟合。
2. 提出SCAN框架，通过自降噪策略生成高质量合成数据，并采用容错学习方法训练PRM。
3. 实验表明，SCAN仅用少量合成数据即可超越大规模人工标注数据训练的模型，且性能随数据规模增大而提升。

## 📝 摘要（中文）

过程奖励模型(PRM)能够提供细粒度的、步骤级别的评估，从而促进大型语言模型(LLM)中更深层次的推理过程，在数学推理等复杂任务中表现出色。然而，由于人工标注数据的高成本和有限的可扩展性，开发PRM具有挑战性。来自蒙特卡洛(MC)估计的合成数据是一个有希望的替代方案，但存在高噪声比的问题，这可能导致过拟合并阻碍大规模训练。本文对来自MC估计的合成数据中的噪声分布进行了初步研究，发现标注模型由于其标注能力的限制，往往会低估和高估步骤的正确性。基于这些见解，我们提出了自降噪蒙特卡洛标注(SCAN)，这是一种高效的数据合成和容错学习框架。我们的关键发现表明：(1)即使是轻量级模型(例如，15亿参数)也可以通过自降噪策略生成高质量的标注，使PRM能够以仅为原始MC估计6%的推理成本实现卓越的性能。(2)通过我们稳健的学习策略，PRM可以有效地从这种弱监督中学习，在ProcessBench中实现了39.2 F1值的提升(从19.9到59.1)。尽管只使用了紧凑的合成数据集，我们的模型超越了强大的基线，包括那些在大型人工标注数据集(如PRM800K)上训练的模型。此外，随着我们扩大合成数据规模，性能持续提高，突出了SCAN在可扩展、经济高效和稳健的PRM训练方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决过程奖励模型（PRM）训练中人工标注数据成本高昂且难以扩展的问题。现有方法依赖人工标注或蒙特卡洛（MC）估计生成的合成数据，但MC估计的合成数据噪声过大，导致模型训练时容易过拟合，影响PRM的性能。

**核心思路**：论文的核心思路是利用自降噪策略生成高质量的合成数据，并设计一种容错学习方法，使PRM能够从这些弱监督数据中有效学习。通过分析MC估计噪声的分布，发现标注模型会系统性地低估和高估步骤的正确性，从而设计自降噪策略来纠正这些偏差。

**技术框架**：SCAN框架主要包含两个阶段：数据合成阶段和模型训练阶段。在数据合成阶段，首先使用MC估计生成初始的合成数据，然后利用自降噪策略对这些数据进行清洗和校正，生成高质量的训练数据。在模型训练阶段，使用容错学习方法，训练PRM模型，使其能够从噪声数据中学习到有效的奖励信号。

**关键创新**：SCAN的关键创新在于提出了自降噪蒙特卡洛标注方法。该方法通过分析MC估计噪声的分布，设计了一种自降噪策略，能够有效地降低合成数据中的噪声，从而提高PRM的训练效果。与传统的MC估计方法相比，SCAN能够生成更高质量的合成数据，从而降低了对大规模人工标注数据的依赖。

**关键设计**：自降噪策略的具体实现包括：(1) 使用多个不同的标注模型进行标注，然后对标注结果进行集成，以减少单个模型的偏差。(2) 设计一种噪声感知损失函数，该函数能够根据数据的噪声水平调整损失权重，从而使模型更加关注高质量的数据。(3) 使用数据增强技术，增加数据的多样性，从而提高模型的泛化能力。

## 📊 实验亮点

实验结果表明，SCAN框架在ProcessBench数据集上取得了显著的性能提升，F1值从19.9提升到59.1，提升幅度高达39.2。即使使用紧凑的合成数据集，SCAN训练的模型也超越了在大型人工标注数据集（如PRM800K）上训练的强大基线。此外，随着合成数据规模的扩大，SCAN的性能持续提升，验证了其可扩展性。

## 🎯 应用场景

SCAN框架可应用于各种需要过程奖励模型的场景，例如数学推理、代码生成、机器人控制等。通过降低对人工标注数据的依赖，SCAN能够显著降低PRM的训练成本，并提高其可扩展性。该研究成果有助于推动LLM在复杂任务中的应用。

## 📄 摘要（原文）

> Process reward models (PRMs) offer fine-grained, step-level evaluations that facilitate deeper reasoning processes in large language models (LLMs), proving effective in complex tasks like mathematical reasoning. However, developing PRMs is challenging due to the high cost and limited scalability of human-annotated data. Synthetic data from Monte Carlo (MC) estimation is a promising alternative but suffers from a high noise ratio, which can cause overfitting and hinder large-scale training. In this work, we conduct a preliminary study on the noise distribution in synthetic data from MC estimation, identifying that annotation models tend to both underestimate and overestimate step correctness due to limitations in their annotation capabilities. Building on these insights, we propose Self-Denoising Monte Carlo Annotation (SCAN), an efficient data synthesis and noise-tolerant learning framework. Our key findings indicate that: (1) Even lightweight models (e.g., 1.5B parameters) can produce high-quality annotations through a self-denoising strategy, enabling PRMs to achieve superior performance with only 6% the inference cost required by vanilla MC estimation. (2) With our robust learning strategy, PRMs can effectively learn from this weak supervision, achieving a 39.2 F1 score improvement (from 19.9 to 59.1) in ProcessBench. Despite using only a compact synthetic dataset, our models surpass strong baselines, including those trained on large-scale human-annotated datasets such as PRM800K. Furthermore, performance continues to improve as we scale up the synthetic data, highlighting the potential of SCAN for scalable, cost-efficient, and robust PRM training.

