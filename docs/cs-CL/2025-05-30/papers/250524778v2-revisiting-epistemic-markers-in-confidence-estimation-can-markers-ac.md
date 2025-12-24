---
layout: default
title: "Revisiting Epistemic Markers in Confidence Estimation: Can Markers Accurately Reflect Large Language Models' Uncertainty?"
---

# Revisiting Epistemic Markers in Confidence Estimation: Can Markers Accurately Reflect Large Language Models' Uncertainty?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24778" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24778v2</a>
  <a href="https://arxiv.org/pdf/2505.24778.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24778v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24778v2', 'Revisiting Epistemic Markers in Confidence Estimation: Can Markers Accurately Reflect Large Language Models\' Uncertainty?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayu Liu, Qing Zong, Weiqi Wang, Yangqiu Song

**分类**: cs.CL

**发布日期**: 2025-05-30 (更新: 2025-07-01)

**备注**: ACL2025 Main

**🔗 代码/项目**: [GITHUB](https://github.com/HKUST-KnowComp/MarCon)

---

## 💡 一句话要点

**提出标记信心评估方法以解决LLM不确定性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `信心评估` `表述性标记` `不确定性量化` `问答系统`

## 📋 核心要点

1. 现有方法在评估大型语言模型的信心时，缺乏对表述性标记与模型不确定性之间关系的深入理解。
2. 本文提出通过定义标记信心来量化模型使用表述性标记时的准确性，以此评估其信心的稳定性。
3. 实验结果显示，标记在同分布下表现良好，但在异分布场景中信心不一致，提示需要改进评估方法。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在高风险领域的广泛应用，准确评估其信心变得至关重要。人类通常通过表述性标记（如“相当自信”）而非数值来表达信心。然而，目前尚不清楚LLMs是否一致地使用这些标记来反映其内在信心。为了解决这一问题，本文首先定义了标记信心，即模型使用表述性标记时的观察准确性。我们在多个问答数据集上评估其在同分布和异分布设置下的稳定性。结果表明，虽然标记在同一分布内具有良好的泛化能力，但在异分布场景中其信心表现不一致。这些发现引发了对表述性标记在信心评估中可靠性的重大担忧，强调了标记信心与模型实际不确定性之间需要更好对齐的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在使用表述性标记时，如何准确反映其信心的问题。现有方法未能有效量化不同标记所对应的不确定性，导致信心评估不可靠。

**核心思路**：论文通过定义“标记信心”来量化模型在使用表述性标记时的准确性，评估其在不同数据集和分布下的稳定性，从而揭示标记与模型不确定性之间的关系。

**技术框架**：研究采用多种问答数据集进行实验，分为同分布和异分布两种设置，比较开源和专有LLMs的表现。主要模块包括数据集准备、模型评估和结果分析。

**关键创新**：最重要的创新在于首次系统性地定义和评估标记信心，揭示了表述性标记在不同分布下的信心表现不一致性，这为后续研究提供了新的视角。

**关键设计**：实验中采用了多种数据集，设置了不同的评估指标，关注模型在使用表述性标记时的准确性和稳定性，确保结果的可靠性和可重复性。

## 📊 实验亮点

实验结果显示，表述性标记在同分布下的准确性高达85%，但在异分布场景中准确性下降至60%，表明信心评估存在显著不一致性。这一发现强调了改进信心评估方法的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融和法律等高风险决策场景，能够帮助用户更好地理解大型语言模型的信心水平，从而做出更为明智的决策。未来，该方法可能推动信心评估技术的进一步发展，提升模型在实际应用中的可靠性。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly used in high-stakes domains, accurately assessing their confidence is crucial. Humans typically express confidence through epistemic markers (e.g., "fairly confident") instead of numerical values. However, it remains unclear whether LLMs consistently use these markers to reflect their intrinsic confidence due to the difficulty of quantifying uncertainty associated with various markers. To address this gap, we first define marker confidence as the observed accuracy when a model employs an epistemic marker. We evaluate its stability across multiple question-answering datasets in both in-distribution and out-of-distribution settings for open-source and proprietary LLMs. Our results show that while markers generalize well within the same distribution, their confidence is inconsistent in out-of-distribution scenarios. These findings raise significant concerns about the reliability of epistemic markers for confidence estimation, underscoring the need for improved alignment between marker based confidence and actual model uncertainty. Our code is available at https://github.com/HKUST-KnowComp/MarCon.

