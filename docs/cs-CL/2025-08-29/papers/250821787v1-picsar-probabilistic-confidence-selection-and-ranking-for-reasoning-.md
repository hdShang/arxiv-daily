---
layout: default
title: "PiCSAR: Probabilistic Confidence Selection And Ranking for Reasoning Chains"
---

# PiCSAR: Probabilistic Confidence Selection And Ranking for Reasoning Chains

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21787" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21787v1</a>
  <a href="https://arxiv.org/pdf/2508.21787.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21787v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21787v1', 'PiCSAR: Probabilistic Confidence Selection And Ranking for Reasoning Chains')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joshua Ong Jun Leang, Zheng Zhao, Aryo Pradipta Gema, Sohee Yang, Wai-Chung Kwan, Xuanli He, Wenda Li, Pasquale Minervini, Eleonora Giunchiglia, Shay B. Cohen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-29

---

## 💡 一句话要点

**提出PiCSAR以解决推理链评分问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理链` `评分函数` `联合对数似然` `无训练方法` `性能提升`

## 📋 核心要点

1. 现有方法在推理任务中面临设计评分函数的挑战，无法利用真实答案来识别正确的推理链。
2. 论文提出的PiCSAR方法通过联合对数似然评分候选生成，分解为推理置信度和答案置信度，简化了评分过程。
3. 实验结果显示，PiCSAR在多个基准测试中显著提升性能，尤其在MATH500和AIME2025上分别提高了10.18和9.81的分数。

## 📝 摘要（中文）

最佳采样方法通过生成多个候选解并选择奖励最高的解来提高大型语言模型和推理模型的准确性。推理任务的关键挑战在于设计评分函数，以便在没有真实答案的情况下识别正确的推理链。我们提出了概率置信选择与排序（PiCSAR）：一种简单的无训练方法，通过推理和最终答案的联合对数似然来评分每个候选生成。PiCSAR在多个基准测试中取得了显著提升，尤其在MATH500和AIME2025上分别提高了10.18和9.81的分数，且在20次比较中有16次以至少2倍更少的样本超越了基线。我们的分析表明，正确的推理链表现出显著更高的推理和答案置信度，从而证明了PiCSAR的有效性。

## 🔬 方法详解

**问题定义**：本论文旨在解决推理任务中如何有效评分候选推理链的问题。现有方法通常依赖于真实答案进行评分，但在缺乏真实答案的情况下，难以准确识别正确的推理链。

**核心思路**：PiCSAR的核心思路是通过计算推理和最终答案的联合对数似然来评分候选生成。这种方法不需要训练，能够有效地分解为推理置信度和答案置信度，从而提供更可靠的评分依据。

**技术框架**：PiCSAR的整体架构包括生成候选推理链、计算联合对数似然、以及根据置信度进行排序和选择。主要模块包括候选生成器和评分模块，后者负责计算每个候选的置信度。

**关键创新**：PiCSAR的主要创新在于其无训练的评分机制，通过联合对数似然的分解，能够在没有真实答案的情况下有效评估候选推理链的质量。这与传统方法依赖真实答案的评分方式形成了鲜明对比。

**关键设计**：在设计上，PiCSAR使用了简单的统计方法来计算联合对数似然，确保了方法的高效性和可扩展性。具体的参数设置和损失函数设计未在摘要中详细说明，可能需要参考完整论文以获取更多技术细节。

## 📊 实验亮点

实验结果表明，PiCSAR在MATH500和AIME2025基准测试中分别提高了10.18和9.81的分数，且在20次比较中有16次以至少2倍更少的样本超越了基线。这些结果突显了PiCSAR在推理任务中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动问答系统和智能助手等。通过提高推理链的准确性，PiCSAR可以帮助这些系统更好地理解和处理复杂问题，从而提升用户体验和决策支持能力。未来，随着推理任务的广泛应用，PiCSAR的影响力有望进一步扩大。

## 📄 摘要（原文）

> Best-of-n sampling improves the accuracy of large language models (LLMs) and large reasoning models (LRMs) by generating multiple candidate solutions and selecting the one with the highest reward. The key challenge for reasoning tasks is designing a scoring function that can identify correct reasoning chains without access to ground-truth answers. We propose Probabilistic Confidence Selection And Ranking (PiCSAR): a simple, training-free method that scores each candidate generation using the joint log-likelihood of the reasoning and final answer. The joint log-likelihood of the reasoning and final answer naturally decomposes into reasoning confidence and answer confidence. PiCSAR achieves substantial gains across diverse benchmarks (+10.18 on MATH500, +9.81 on AIME2025), outperforming baselines with at least 2x fewer samples in 16 out of 20 comparisons. Our analysis reveals that correct reasoning chains exhibit significantly higher reasoning and answer confidence, justifying the effectiveness of PiCSAR.

