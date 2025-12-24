---
layout: default
title: "COIN: Uncertainty-Guarding Selective Question Answering for Foundation Models with Provable Risk Guarantees"
---

# COIN: Uncertainty-Guarding Selective Question Answering for Foundation Models with Provable Risk Guarantees

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20178" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20178v1</a>
  <a href="https://arxiv.org/pdf/2506.20178.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20178v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20178v1', 'COIN: Uncertainty-Guarding Selective Question Answering for Foundation Models with Provable Risk Guarantees')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyuan Wang, Jinhao Duan, Qingni Wang, Xiaofeng Zhu, Tianlong Chen, Xiaoshuang Shi, Kaidi Xu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出COIN框架以解决基础模型的不确定性量化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `不确定性量化` `假发现率` `文本生成` `风险控制` `多模态学习` `自动问答` `置信区间`

## 📋 核心要点

1. 现有的不确定性量化方法在选择预测时缺乏对假发现率的正式保证，导致生成答案的实用性受限。
2. COIN框架通过校准有效阈值，确保在用户指定的假发现率约束下，过滤出单一生成答案。
3. 实验结果表明，COIN在风险控制和样本保留方面表现出色，且在多模态文本生成任务中具有较强的预测效率。

## 📝 摘要（中文）

不确定性量化（UQ）对于基础模型至关重要，以识别和减轻自动生成文本中的潜在幻觉。然而，现有的启发式UQ方法在选择预测时缺乏对假发现率（FDR）的正式保证。为了解决这一问题，本文提出了COIN，一个不确定性保护选择框架，能够在用户指定的FDR约束下，校准统计有效的阈值，以过滤每个问题的单一生成答案。COIN通过在校准集上估计经验误差率，并应用Clopper-Pearson等置信区间方法，建立真实误差率的高概率上界。这使得在测试数据上选择最大的阈值成为可能，同时显著提高样本保留率。我们展示了COIN在风险控制方面的稳健性、在有限校准数据下的强测试时效能及预测效率。

## 🔬 方法详解

**问题定义**：本文旨在解决基础模型在自动生成文本时的不确定性量化问题，现有方法在假发现率控制上存在不足，导致生成答案中包含错误候选项。

**核心思路**：COIN框架通过校准统计有效的阈值，确保在用户指定的假发现率约束下，能够有效过滤出单一生成答案，从而提高生成文本的可靠性。

**技术框架**：COIN的整体架构包括两个主要模块：首先是经验误差率的估计，其次是基于置信区间方法（如Clopper-Pearson）构建真实误差率的高概率上界。

**关键创新**：COIN的主要创新在于其不确定性保护机制，通过有效的阈值选择，显著提高了假发现率控制的能力，与现有的分裂保形预测方法相比，提供了更高的实用性。

**关键设计**：在设计上，COIN采用了经验误差率的估计和置信区间构建的结合，确保了在有限校准数据下的高效性，同时通过调整阈值来优化样本保留率。

## 📊 实验亮点

实验结果显示，COIN在假发现率控制上表现优异，能够在测试数据上选择最大的阈值，同时显著提高样本保留率。与基线方法相比，COIN在多模态文本生成任务中提升了预测效率，展现了其强大的实用性。

## 🎯 应用场景

COIN框架在多个领域具有广泛的应用潜力，特别是在需要高可靠性文本生成的场景，如自动问答系统、内容生成和对话系统等。其不确定性控制能力将有助于提高用户信任度和系统的实际应用效果。

## 📄 摘要（原文）

> Uncertainty quantification (UQ) for foundation models is essential to identify and mitigate potential hallucinations in automatically generated text. However, heuristic UQ approaches lack formal guarantees for key metrics such as the false discovery rate (FDR) in selective prediction. Previous work adopts the split conformal prediction (SCP) framework to ensure desired coverage of admissible answers by constructing prediction sets, but these sets often contain incorrect candidates, limiting their practical utility. To address this, we propose COIN, an uncertainty-guarding selection framework that calibrates statistically valid thresholds to filter a single generated answer per question under user-specified FDR constraints. COIN estimates the empirical error rate on a calibration set and applies confidence interval methods such as Clopper-Pearson to establish a high-probability upper bound on the true error rate (i.e., FDR). This enables the selection of the largest uncertainty threshold that ensures FDR control on test data while significantly increasing sample retention. We demonstrate COIN's robustness in risk control, strong test-time power in retaining admissible answers, and predictive efficiency under limited calibration data across both general and multimodal text generation tasks. Furthermore, we show that employing alternative upper bound constructions and UQ strategies can further boost COIN's power performance, which underscores its extensibility and adaptability to diverse application scenarios.

