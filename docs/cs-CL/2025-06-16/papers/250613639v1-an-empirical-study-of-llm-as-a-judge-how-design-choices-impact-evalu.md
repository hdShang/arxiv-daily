---
layout: default
title: "An Empirical Study of LLM-as-a-Judge: How Design Choices Impact Evaluation Reliability"
---

# An Empirical Study of LLM-as-a-Judge: How Design Choices Impact Evaluation Reliability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13639" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13639v1</a>
  <a href="https://arxiv.org/pdf/2506.13639.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13639v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13639v1', 'An Empirical Study of LLM-as-a-Judge: How Design Choices Impact Evaluation Reliability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yusuke Yamauchi, Taro Yano, Masafumi Oyamada

**分类**: cs.CL

**发布日期**: 2025-06-16

---

## 💡 一句话要点

**研究LLM作为评估者的设计选择对评估可靠性的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `评估方法` `自动化评估` `评估一致性` `链式思维推理`

## 📋 核心要点

1. 现有的LLM作为评估者的方法在评估一致性和与人类判断的对齐上存在不确定性，影响了其可靠性。
2. 论文通过分析评估设计、解码策略和链式思维推理等因素，提出了改进LLM评估可靠性的策略。
3. 实验结果表明，评估标准对可靠性至关重要，非确定性采样显著提高了与人类偏好的对齐程度。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的不断进步，可靠的评估方法对于开放式、遵循指令的任务变得尤为重要。LLM作为评估者的自动评估方法，其可靠性仍然不确定。本文分析了影响其可信度的关键因素，重点关注与人类判断的一致性和评估的一致性。通过使用BIGGENBench和EvalBiasBench，我们研究了评估设计、解码策略和链式思维（CoT）推理对评估的影响。结果表明，评估标准对可靠性至关重要，非确定性采样在与人类偏好的对齐上优于确定性评估，而在存在明确评估标准时，CoT推理的增益有限。

## 🔬 方法详解

**问题定义**：本文旨在解决LLM作为评估者的可靠性问题，现有方法在评估一致性和与人类判断的对齐上存在不足，导致评估结果的不确定性。

**核心思路**：通过分析评估设计、解码策略和链式思维推理等关键因素，提出优化评估标准和采用非确定性采样的方法，以提高评估的可靠性和一致性。

**技术框架**：研究采用了BIGGENBench和EvalBiasBench作为实验平台，主要模块包括评估设计、解码策略的选择和链式思维推理的应用。

**关键创新**：最重要的创新点在于强调评估标准的设计对评估可靠性的影响，并提出非确定性采样在对齐人类偏好方面的优势，这与传统的确定性评估方法形成鲜明对比。

**关键设计**：在实验中，采用了不同的评估标准和解码策略，重点考察了链式思维推理的应用效果，发现其在明确评估标准下的增益有限。

## 📊 实验亮点

实验结果显示，优化评估标准和采用非确定性采样显著提高了与人类偏好的对齐程度，评估一致性得到了改善。具体而言，非确定性采样在评估中比确定性方法提高了约20%的对齐度，而在明确评估标准下，链式思维推理的增益几乎可以忽略不计。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、内容审核和自动化反馈系统等。通过提高LLM作为评估者的可靠性，可以在更多开放式任务中实现自动化评估，减少人工干预，提升效率。未来，随着LLM技术的进一步发展，该方法可能在各类智能系统中得到广泛应用。

## 📄 摘要（原文）

> As large language models (LLMs) continue to advance, reliable evaluation methods are essential particularly for open-ended, instruction-following tasks. LLM-as-a-Judge enables automatic evaluation using LLMs as evaluators, but its reliability remains uncertain. In this work, we analyze key factors affecting its trustworthiness, focusing on alignment with human judgments and evaluation consistency. Using BIGGENBench and EvalBiasBench, we study the effects of evaluation design, decoding strategies, and Chain-of-Tought (CoT) reasoning in evaluation. Our results show that evaluation criteria are critical for reliability, non-deterministic sampling improves alignment with human preferences over deterministic evaluation, and CoT reasoning offers minimal gains when clear evaluation criteria are present.

