---
layout: default
title: "Trusted Uncertainty in Large Language Models: A Unified Framework for Confidence Calibration and Risk-Controlled Refusal"
---

# Trusted Uncertainty in Large Language Models: A Unified Framework for Confidence Calibration and Risk-Controlled Refusal

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01455" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01455v1</a>
  <a href="https://arxiv.org/pdf/2509.01455.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01455v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01455v1', 'Trusted Uncertainty in Large Language Models: A Unified Framework for Confidence Calibration and Risk-Controlled Refusal')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Markus Oehri, Giulia Conti, Kaviraj Pather, Alexandre Rossi, Laia Serra, Adrian Parody, Rogvi Johannesen, Aviaja Petersen, Arben Krasniqi

**分类**: cs.CL

**发布日期**: 2025-09-01

**备注**: 10 pages, 5 figures

---

## 💡 一句话要点

**UniCR：提出统一框架，通过校准不确定性证据实现大语言模型风险可控的拒绝回答**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `不确定性校准` `风险控制` `拒绝回答` `共形预测`

## 📋 核心要点

1. 现有大语言模型在部署时，不仅需要决定如何回答，还需要决定何时不回答，即拒绝回答。
2. UniCR框架将多种不确定性证据融合，校准为概率，并根据用户设定的误差预算进行风险控制的拒绝回答。
3. 实验表明，UniCR在校准指标、风险覆盖率和固定风险下的覆盖率方面均优于现有方法，且无需微调基础模型。

## 📝 摘要（中文）

本文提出UniCR，一个统一的框架，它将异构的不确定性证据（包括序列似然、自洽性分散、检索兼容性以及工具或验证器反馈）转化为校准后的正确概率，并通过原则性的拒绝回答来强制执行用户指定的误差预算。UniCR学习一个轻量级的校准头，采用温度缩放和适当评分，通过黑盒特征支持仅API模型，并使用共形风险控制提供无分布保证。对于长文本生成，通过监督从检索证据中获得的原子事实性分数，使置信度与语义保真度对齐，从而减少自信的幻觉并保持覆盖率。在短文本问答、代码生成（带执行测试）和检索增强的长文本问答上的实验表明，与熵或logit阈值、事后校准器和端到端选择性基线相比，校准指标得到一致改进，风险-覆盖曲线下面积更小，并且在固定风险下覆盖率更高。分析表明，证据矛盾、语义分散和工具不一致是拒绝回答的主要驱动因素，从而产生信息丰富的面向用户的拒绝消息。最终得到一个可移植的配方，即证据融合到校准概率到风险控制的决策，从而提高可信度，而无需微调基础模型，并且在分布偏移下仍然有效。

## 🔬 方法详解

**问题定义**：大语言模型在实际应用中，需要具备判断自身回答正确性的能力，并在不确定时选择拒绝回答。现有方法通常依赖于熵或logit阈值，或者事后校准器，这些方法在校准效果和风险控制方面存在不足，并且难以有效融合多种不确定性证据。

**核心思路**：UniCR的核心思路是将各种异构的不确定性证据（例如序列似然、自洽性、检索兼容性等）融合起来，通过一个轻量级的校准头将其转化为校准后的正确概率。然后，利用共形风险控制，根据用户设定的误差预算，决定何时拒绝回答。这样可以在保证回答质量的同时，控制风险。

**技术框架**：UniCR框架主要包含以下几个模块：1) **证据收集模块**：收集来自不同来源的不确定性证据，例如序列似然、自洽性分散、检索兼容性、工具或验证器反馈等。2) **校准头**：学习一个轻量级的校准头，使用温度缩放和适当评分方法，将异构的证据转化为校准后的正确概率。3) **风险控制模块**：使用共形风险控制方法，根据用户指定的误差预算，决定何时拒绝回答。

**关键创新**：UniCR的关键创新在于：1) 提出了一个统一的框架，可以融合多种异构的不确定性证据。2) 使用轻量级的校准头，可以在不微调基础模型的情况下，实现有效的校准。3) 利用共形风险控制，可以提供无分布保证，即在分布偏移的情况下仍然有效。

**关键设计**：UniCR的关键设计包括：1) 校准头的结构：可以使用简单的线性层或更复杂的神经网络。2) 损失函数：使用适当的评分函数，例如Brier score或负对数似然。3) 温度缩放：使用温度缩放来调整校准后的概率。4) 共形风险控制：使用共形预测的思想，根据历史数据估计风险，并根据用户指定的误差预算进行调整。

## 📊 实验亮点

实验结果表明，UniCR在短文本问答、代码生成和检索增强的长文本问答等任务上，均优于现有的校准方法。具体来说，UniCR在校准指标上取得了显著提升，降低了风险-覆盖曲线下面积，并在固定风险下实现了更高的覆盖率。此外，分析表明，证据矛盾、语义分散和工具不一致是拒绝回答的主要驱动因素。

## 🎯 应用场景

UniCR框架可应用于各种需要大语言模型提供可靠回答的场景，例如智能客服、医疗诊断、金融风控等。通过控制回答的风险，可以提高用户对大语言模型的信任度，并减少错误回答带来的负面影响。该研究对于提升大语言模型在实际应用中的安全性和可靠性具有重要意义。

## 📄 摘要（原文）

> Deployed language models must decide not only what to answer but also when not to answer. We present UniCR, a unified framework that turns heterogeneous uncertainty evidence including sequence likelihoods, self-consistency dispersion, retrieval compatibility, and tool or verifier feedback into a calibrated probability of correctness and then enforces a user-specified error budget via principled refusal. UniCR learns a lightweight calibration head with temperature scaling and proper scoring, supports API-only models through black-box features, and offers distribution-free guarantees using conformal risk control. For long-form generation, we align confidence with semantic fidelity by supervising on atomic factuality scores derived from retrieved evidence, reducing confident hallucinations while preserving coverage. Experiments on short-form QA, code generation with execution tests, and retrieval-augmented long-form QA show consistent improvements in calibration metrics, lower area under the risk-coverage curve, and higher coverage at fixed risk compared to entropy or logit thresholds, post-hoc calibrators, and end-to-end selective baselines. Analyses reveal that evidence contradiction, semantic dispersion, and tool inconsistency are the dominant drivers of abstention, yielding informative user-facing refusal messages. The result is a portable recipe of evidence fusion to calibrated probability to risk-controlled decision that improves trustworthiness without fine-tuning the base model and remains valid under distribution shift.

