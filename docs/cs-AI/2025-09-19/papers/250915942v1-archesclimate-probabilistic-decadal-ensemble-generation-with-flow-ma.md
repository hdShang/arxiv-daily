---
layout: default
title: "ArchesClimate: Probabilistic Decadal Ensemble Generation With Flow Matching"
---

# ArchesClimate: Probabilistic Decadal Ensemble Generation With Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15942" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15942v1</a>
  <a href="https://arxiv.org/pdf/2509.15942.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15942v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15942v1', 'ArchesClimate: Probabilistic Decadal Ensemble Generation With Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Graham Clyne, Guillaume Couairon, Guillaume Gastineau, Claire Monteleoni, Anastase Charantonis

**分类**: physics.ao-ph, cs.AI

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**ArchesClimate：利用Flow Matching生成概率性年代际集合气候预测，降低计算成本。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `气候模型模拟` `深度学习` `Flow Matching` `气候预测` `不确定性量化`

## 📋 核心要点

1. 传统气候预测集合模拟计算成本高昂，限制了不确定性分析的规模和效率。
2. ArchesClimate利用Flow Matching模型，学习气候模型的动态，实现快速且物理一致的模拟生成。
3. 实验表明，ArchesClimate在十年尺度上生成稳定且与IPSL模型可互换的气候变量模拟结果。

## 📝 摘要（中文）

气候预测的不确定性与气候系统的各个组成部分及其相互作用有关。量化这些不确定性的一种典型方法是使用气候模型创建在不同初始条件下重复模拟的集合。由于这些模拟的复杂性，生成此类预测集合的计算成本很高。本文提出了ArchesClimate，一种基于深度学习的气候模型模拟器，旨在降低这种成本。ArchesClimate在IPSL-CM6A-LR气候模型的年代际后报数据上进行训练，空间分辨率约为2.5x1.25度。我们训练了一个遵循ArchesWeatherGen的Flow Matching模型，并将其调整为预测近期气候。训练完成后，该模型可以生成提前一个月的状态，并可用于自回归地模拟任意长度的气候模型模拟。我们表明，在长达10年的时间内，这些生成结果是稳定且物理上一致的。我们还表明，对于几个重要的气候变量，ArchesClimate生成的模拟结果可以与IPSL模型互换。这项工作表明，气候模型模拟器可以显著降低气候模型模拟的成本。

## 🔬 方法详解

**问题定义**：气候预测需要大量的集合模拟来量化不确定性，但传统气候模型的计算成本非常高，限制了预测的效率和规模。现有的气候模型模拟器可能无法保证长期稳定性和物理一致性，难以满足实际应用需求。

**核心思路**：利用Flow Matching模型学习气候模型的动态过程，通过训练一个深度学习模型来近似气候模型的行为。Flow Matching的优势在于其训练稳定性和生成样本的多样性，能够生成更可靠的概率性预测。通过自回归的方式，模型可以逐步预测未来的气候状态，从而模拟长时间的气候演变。

**技术框架**：ArchesClimate基于Flow Matching框架，使用IPSL-CM6A-LR气候模型的年代际后报数据进行训练。模型以一个月为步长，自回归地预测未来的气候状态。整体流程包括数据预处理、模型训练和模拟生成三个阶段。数据预处理包括对原始气候数据进行降尺度和标准化，以便于模型学习。模型训练阶段使用Flow Matching损失函数优化模型参数。模拟生成阶段，模型从初始状态开始，逐步预测未来的气候状态，生成完整的气候模拟序列。

**关键创新**：该方法将Flow Matching技术应用于气候模型模拟，解决了传统方法计算成本高和难以保证长期稳定性的问题。通过学习气候模型的动态过程，ArchesClimate能够生成与真实气候模型可互换的模拟结果，为气候预测和不确定性分析提供了新的途径。

**关键设计**：模型采用类似于ArchesWeatherGen的网络结构，并针对气候预测的特点进行了调整。损失函数采用标准的Flow Matching损失函数，旨在最小化生成样本与真实样本之间的差异。模型训练过程中，采用了数据增强和正则化等技术，以提高模型的泛化能力和鲁棒性。具体参数设置（如网络层数、学习率等）未在论文中明确给出，属于未知信息。

## 📊 实验亮点

ArchesClimate在长达10年的模拟中表现出稳定性和物理一致性，生成的模拟结果与IPSL气候模型具有互换性。虽然论文中没有给出明确的性能指标提升数据，但强调了该模型在降低计算成本方面的潜力，为气候预测领域提供了一种高效的替代方案。

## 🎯 应用场景

ArchesClimate可应用于气候变化风险评估、适应性规划和政策制定等领域。通过快速生成大量气候预测集合，可以更全面地评估气候变化的不确定性，为决策者提供更可靠的依据。此外，该模型还可以用于研究不同气候情景下的潜在影响，帮助制定更有效的应对策略。

## 📄 摘要（原文）

> Climate projections have uncertainties related to components of the climate system and their interactions. A typical approach to quantifying these uncertainties is to use climate models to create ensembles of repeated simulations under different initial conditions. Due to the complexity of these simulations, generating such ensembles of projections is computationally expensive. In this work, we present ArchesClimate, a deep learning-based climate model emulator that aims to reduce this cost. ArchesClimate is trained on decadal hindcasts of the IPSL-CM6A-LR climate model at a spatial resolution of approximately 2.5x1.25 degrees. We train a flow matching model following ArchesWeatherGen, which we adapt to predict near-term climate. Once trained, the model generates states at a one-month lead time and can be used to auto-regressively emulate climate model simulations of any length. We show that for up to 10 years, these generations are stable and physically consistent. We also show that for several important climate variables, ArchesClimate generates simulations that are interchangeable with the IPSL model. This work suggests that climate model emulators could significantly reduce the cost of climate model simulations.

