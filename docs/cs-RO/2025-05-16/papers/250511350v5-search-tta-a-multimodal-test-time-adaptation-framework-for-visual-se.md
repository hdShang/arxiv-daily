---
layout: default
title: Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild
---

# Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11350" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11350v5</a>
  <a href="https://arxiv.org/pdf/2505.11350.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11350v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11350v5', 'Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Derek Ming Siang Tan, Shailesh, Boyang Liu, Alok Raj, Qi Xuan Ang, Weiheng Dai, Tanishq Duhan, Jimmy Chiun, Yuhong Cao, Florian Shkurti, Guillaume Sartoretti

**分类**: cs.RO

**发布日期**: 2025-05-16 (更新: 2025-11-07)

**备注**: Accepted for presentation at CORL 2025. Code, models, and data are available at https://search-tta.github.io/

---

## 💡 一句话要点

**提出Search-TTA框架以解决户外视觉搜索中的信息不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态适应` `视觉搜索` `卫星图像` `深度学习` `无人机导航` `模型优化` `不确定性处理`

## 📋 核心要点

1. 现有的视觉搜索方法往往假设没有先验信息，或未考虑先验信息的获取方式，导致搜索效率低下。
2. 本文提出的Search-TTA框架通过动态优化CLIP的预测，结合多模态输入，提升了视觉搜索的准确性和效率。
3. 实验结果显示，Search-TTA在规划性能上提高了30.0%，并在零样本泛化方面表现出色，尤其在数据不足的情况下。

## 📝 摘要（中文）

为了进行户外视觉导航和搜索，机器人可以利用卫星图像生成视觉先验信息。然而，现有的方法往往假设没有先验信息，或使用的先验信息未考虑其获取方式。为了解决这些问题，本文提出了Search-TTA，一个多模态测试时适应框架，支持多种输入模态和规划方法。通过预训练卫星图像编码器并动态优化CLIP的预测，Search-TTA在视觉搜索中显著提升了性能，尤其是在初始预测不佳的情况下。实验表明，该框架在真实无人机上测试时表现出色，具有广泛的应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决户外视觉搜索中由于缺乏高质量先验信息而导致的搜索效率低下问题。现有方法在处理卫星图像时，往往未能有效利用这些信息，导致规划策略不够精准。

**核心思路**：Search-TTA框架的核心思想是通过多模态输入和动态优化策略，提升视觉搜索的准确性。具体而言，框架利用卫星图像编码器与CLIP视觉编码器的对齐，输出目标存在的概率分布，并在搜索过程中动态调整预测。

**技术框架**：Search-TTA的整体架构包括两个主要模块：首先是卫星图像编码器的预训练，确保其与CLIP编码器的输出一致；其次是基于不确定性加权的梯度更新机制，动态优化CLIP的预测。该框架支持多种输入模态，如图像、文本和声音。

**关键创新**：最重要的技术创新在于引入了不确定性加权的梯度更新方法，灵感来源于空间泊松点过程，使得模型能够在搜索过程中有效地调整预测，克服了传统方法的局限性。

**关键设计**：在模型设计上，采用了与CLIP相对齐的卫星图像编码器，损失函数设计考虑了不确定性因素，以提高模型在不同模态下的适应能力。

## 📊 实验亮点

实验结果表明，Search-TTA在规划性能上提高了30.0%，尤其在初始CLIP预测不佳的情况下表现显著。此外，该框架在零样本泛化方面与更大规模的视觉语言模型相当，展示了其强大的适应能力。

## 🎯 应用场景

Search-TTA框架具有广泛的应用潜力，特别是在无人机视觉导航、环境监测和搜索救援等领域。通过提升视觉搜索的准确性和效率，该框架能够帮助机器人在复杂环境中更有效地执行任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> To perform outdoor visual navigation and search, a robot may leverage satellite imagery to generate visual priors. This can help inform high-level search strategies, even when such images lack sufficient resolution for target recognition. However, many existing informative path planning or search-based approaches either assume no prior information, or use priors without accounting for how they were obtained. Recent work instead utilizes large Vision Language Models (VLMs) for generalizable priors, but their outputs can be inaccurate due to hallucination, leading to inefficient search. To address these challenges, we introduce Search-TTA, a multimodal test-time adaptation framework with a flexible plug-and-play interface compatible with various input modalities (e.g., image, text, sound) and planning methods (e.g., RL-based). First, we pretrain a satellite image encoder to align with CLIP's visual encoder to output probability distributions of target presence used for visual search. Second, our TTA framework dynamically refines CLIP's predictions during search using uncertainty-weighted gradient updates inspired by Spatial Poisson Point Processes. To train and evaluate Search-TTA, we curate AVS-Bench, a visual search dataset based on internet-scale ecological data containing 380k images and taxonomy data. We find that Search-TTA improves planner performance by up to 30.0%, particularly in cases with poor initial CLIP predictions due to domain mismatch and limited training data. It also performs comparably with significantly larger VLMs, and achieves zero-shot generalization via emergent alignment to unseen modalities. Finally, we deploy Search-TTA on a real UAV via hardware-in-the-loop testing, by simulating its operation within a large-scale simulation that provides onboard sensing.

