---
layout: default
title: OASIS: Online Sample Selection for Continual Visual Instruction Tuning
---

# OASIS: Online Sample Selection for Continual Visual Instruction Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02011" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02011v2</a>
  <a href="https://arxiv.org/pdf/2506.02011.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02011v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02011v2', 'OASIS: Online Sample Selection for Continual Visual Instruction Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minjae Lee, Minhyuk Seo, Tingyu Qu, Tinne Tuytelaars, Jonghyun Choi

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-10-09)

---

## 💡 一句话要点

**提出OASIS以解决持续视觉指令调优中的样本选择问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `持续指令调优` `在线样本选择` `自适应学习` `信息量评估` `深度学习`

## 📋 核心要点

1. 现有的持续指令调优方法在面对大规模数据时，训练延迟显著影响实时适应能力。
2. OASIS通过相对有效性评估和迭代选择分数更新，选择信息量丰富的样本，克服了固定样本选择的局限。
3. 实验表明，OASIS在仅使用25%数据的情况下，性能与全数据训练相当，且优于现有采样方法。

## 📝 摘要（中文）

在持续指令调优（CIT）场景中，新的指令调优数据以在线流的方式不断到来，来自大规模数据的训练延迟显著阻碍了实时适应。数据选择可以缓解这一开销，但现有策略通常依赖于预训练的参考模型，这在CIT设置中并不实用。最近的无参考模型在线样本选择方法虽然解决了这一问题，但通常每批次选择固定数量的样本（如top-k），使其在分布变化时容易受到影响。为了解决这些局限性，我们提出了OASIS，一种自适应在线样本选择方法，通过估计每个样本相对于所有已见数据的有效性，选择信息量丰富的样本，并通过迭代选择分数更新来最小化所选样本的信息冗余。实验结果表明，OASIS仅使用25%的数据便能达到与全数据训练相当的性能，并超越了现有的采样方法。

## 🔬 方法详解

**问题定义**：论文旨在解决持续指令调优（CIT）中样本选择的效率问题。现有方法依赖于预训练模型或固定样本数量选择，无法适应数据分布的变化，导致信息利用不充分。

**核心思路**：OASIS的核心思想是通过估计每个样本的有效性，动态选择信息量丰富的样本，并通过迭代更新选择分数来减少冗余，从而提高样本选择的灵活性和有效性。

**技术框架**：OASIS的整体架构包括样本有效性评估模块和迭代选择模块。首先，评估每个样本的有效性，然后根据评估结果动态选择样本，最后通过迭代更新选择分数来优化样本集。

**关键创新**：OASIS的主要创新在于其自适应样本选择机制，能够根据历史数据动态调整选择策略，区别于传统的固定样本选择方法，提升了在数据分布变化时的适应能力。

**关键设计**：在参数设置上，OASIS采用了动态更新的选择分数机制，损失函数设计上注重信息量的最大化，网络结构上则结合了有效性评估与选择模块，确保了选择过程的高效性与准确性。

## 📊 实验亮点

OASIS在实验中仅使用25%的数据便实现了与全数据训练相当的性能，且在多个大型基础模型上超越了现有的最先进采样方法，显示出其在样本选择效率上的显著提升。

## 🎯 应用场景

OASIS的研究成果在多个领域具有潜在应用价值，尤其是在需要实时适应的视觉指令调优场景中，如智能机器人、自动驾驶和人机交互等。通过提高样本选择的效率，OASIS能够加速模型的在线学习过程，提升系统的响应能力和智能水平。

## 📄 摘要（原文）

> In continual instruction tuning (CIT) scenarios, where new instruction tuning data continuously arrive in an online streaming manner, training delays from large-scale data significantly hinder real-time adaptation. Data selection can mitigate this overhead, but existing strategies often rely on pretrained reference models, which are impractical in CIT setups since future data are unknown. Recent reference model-free online sample selection methods address this, but typically select a fixed number of samples per batch (e.g., top-k), making them vulnerable to distribution shifts where informativeness varies across batches. To address these limitations, we propose OASIS, an adaptive online sample selection approach for CIT that (1) selects informative samples by estimating each sample's informativeness relative to all previously seen data, beyond batch-level constraints, and (2) minimizes informative redundancy of selected samples through iterative selection score updates. Experiments on various large foundation models show that OASIS, using only 25 percent of the data, achieves comparable performance to full-data training and outperforms the state-of-the-art sampling methods.

