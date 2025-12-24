---
layout: default
title: Calibrating LLM Confidence by Probing Perturbed Representation Stability
---

# Calibrating LLM Confidence by Probing Perturbed Representation Stability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21772" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21772v2</a>
  <a href="https://arxiv.org/pdf/2505.21772.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21772v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21772v2', 'Calibrating LLM Confidence by Probing Perturbed Representation Stability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese H. Smiley, Kundan Thind, Mohammad M. Ghassemi

**分类**: cs.CL

**发布日期**: 2025-05-27 (更新: 2025-09-18)

---

## 💡 一句话要点

**提出CCPS以解决大型语言模型置信度校准问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `置信度校准` `对抗扰动` `特征提取` `机器学习`

## 📋 核心要点

1. 现有大型语言模型在置信度估计上存在误校准问题，影响其可靠性和实用性。
2. CCPS方法通过分析模型内部表示的稳定性，利用对抗扰动来改进置信度估计。
3. 实验结果显示，CCPS在多个基准测试中显著提升了模型的准确性和校准性能。

## 📝 摘要（中文）

大型语言模型（LLMs）的置信度误校准削弱了其可靠性，迫切需要准确的置信度估计。本文提出了一种新方法CCPS（通过探测扰动表示稳定性来校准LLM置信度），分析LLMs内部表示的稳定性。CCPS对最终隐藏状态施加有针对性的对抗扰动，提取反映模型对这些扰动响应的特征，并使用轻量级分类器预测答案的正确性。通过在多个LLM（参数从8B到32B，涵盖Llama、Qwen和Mistral架构）上进行评估，结果表明CCPS显著优于现有方法，降低了预期校准误差约55%，Brier分数降低21%，同时提高了5个百分点的准确率和4个百分点的精确率-召回曲线下面积，6个百分点的受试者工作特征曲线下面积，提升了LLM的可信度。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在置信度估计上的误校准问题。现有方法往往无法准确反映模型的真实信心，导致决策不可靠。

**核心思路**：CCPS通过施加对抗扰动来探测模型内部表示的稳定性，从而更准确地估计模型对答案的置信度。该方法利用扰动引发的特征变化来训练分类器，提升置信度的准确性。

**技术框架**：CCPS的整体架构包括扰动生成模块、特征提取模块和分类器模块。首先，对模型的最终隐藏状态施加对抗扰动，然后提取模型对这些扰动的响应特征，最后通过轻量级分类器进行答案正确性的预测。

**关键创新**：CCPS的主要创新在于通过扰动表示的稳定性来校准置信度，这一方法与传统的基于输出概率的校准方法本质上不同，提供了更深层次的模型内部分析。

**关键设计**：在设计中，CCPS使用了特定的对抗扰动策略，并选择了适合的损失函数来优化分类器的性能，同时确保了模型的计算效率。

## 📊 实验亮点

CCPS在多个大型语言模型上进行了评估，结果显示其在降低预期校准误差方面表现优异，约降低55%；Brier分数降低21%；同时提高了5个百分点的准确率，4个百分点的精确率-召回曲线下面积，以及6个百分点的受试者工作特征曲线下面积，均优于现有最强方法。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能问答等。通过提高大型语言模型的置信度估计准确性，CCPS能够增强这些系统在实际应用中的可靠性，进而提升用户的信任度和满意度。未来，该方法可能在更多领域中得到推广，促进智能系统的安全性和有效性。

## 📄 摘要（原文）

> Miscalibration in Large Language Models (LLMs) undermines their reliability, highlighting the need for accurate confidence estimation. We introduce CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability), a novel method analyzing internal representational stability in LLMs. CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness. CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats. Our results show that CCPS significantly outperforms current approaches. Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points, all relative to the strongest prior method. CCPS delivers an efficient, broadly applicable, and more accurate solution for estimating LLM confidence, thereby improving their trustworthiness.

