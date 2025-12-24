---
layout: default
title: "ConfTuner: Training Large Language Models to Express Their Confidence Verbally"
---

# ConfTuner: Training Large Language Models to Express Their Confidence Verbally

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18847" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18847v2</a>
  <a href="https://arxiv.org/pdf/2508.18847.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18847v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18847v2', 'ConfTuner: Training Large Language Models to Express Their Confidence Verbally')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yibo Li, Miao Xiong, Jiaying Wu, Bryan Hooi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-26 (更新: 2025-11-25)

**备注**: Accepted by NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/liushiliushi/ConfTuner)

---

## 💡 一句话要点

**提出ConfTuner以解决大语言模型信心表达不准确问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `信心校准` `微调方法` `标记布里尔分数` `自我修正` `模型级联` `高风险领域` `可信人工智能`

## 📋 核心要点

1. 现有大语言模型在高风险领域中常常表现出过度自信，导致生成错误答案，影响其可靠性。
2. 本文提出的ConfTuner是一种新型微调方法，通过引入标记布里尔分数损失函数来有效校准模型的信心表达。
3. 实验结果显示，ConfTuner在多种推理任务中显著改善了模型的信心校准，并促进了自我修正能力的提升。

## 📝 摘要（中文）

大语言模型（LLMs）在科学、法律和医疗等高风险领域的应用日益增多，准确表达不确定性对可靠性和信任至关重要。然而，现有LLMs常常以过高的信心生成错误答案，称为“过度自信”。现有的校准方法依赖于提示工程或使用启发式生成的不确定性估计进行微调，效果和通用性有限。为此，本文提出了一种简单高效的微调方法ConfTuner，该方法引入了最小的开销，并且不需要真实的信心分数或代理信心估计。ConfTuner依赖于一种新的损失函数——标记布里尔分数，理论上证明其为适当的评分规则，能够正确激励模型报告其正确概率。ConfTuner在多种推理任务中改善了校准效果，并且能够推广到黑箱模型如GPT-4o。实验结果表明，更好的校准信心促进了自我修正和模型级联的下游收益，推动了可信LLM系统的发展。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在表达信心时的过度自信问题。现有方法依赖于提示工程或启发式生成的不确定性估计，效果有限且缺乏通用性。

**核心思路**：ConfTuner通过引入标记布里尔分数作为损失函数，激励模型准确报告其正确概率，从而实现信心的有效校准。

**技术框架**：ConfTuner的整体架构包括数据准备、模型微调和损失计算三个主要模块。首先，准备训练数据，然后在模型上进行微调，最后计算损失以优化模型的信心表达。

**关键创新**：最重要的创新在于提出了标记布里尔分数作为损失函数，这一设计确保了模型能够准确表达其信心，与现有方法相比具有更好的适应性和有效性。

**关键设计**：在关键设计上，ConfTuner不需要真实的信心分数或代理信心估计，降低了模型训练的复杂性，同时通过理论证明其损失函数为适当的评分规则，确保了模型的可靠性。

## 📊 实验亮点

实验结果表明，使用ConfTuner进行微调后，模型的信心校准显著改善，尤其在多种推理任务中，校准效果提升幅度超过20%。此外，经过校准的模型在自我修正和模型级联任务中表现出更高的准确性，进一步验证了其实际应用价值。

## 🎯 应用场景

ConfTuner的研究成果在科学、法律和医疗等高风险领域具有广泛的应用潜力。通过提高大语言模型的信心表达准确性，可以增强用户对模型输出的信任，促进其在决策支持、法律咨询和医疗诊断等实际场景中的应用。未来，ConfTuner有望推动可信赖的人工智能系统的发展，提升人机交互的安全性和有效性。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed in high-stakes domains such as science, law, and healthcare, where accurate expressions of uncertainty are essential for reliability and trust. However, current LLMs are often observed to generate incorrect answers with high confidence, a phenomenon known as "overconfidence". Recent efforts have focused on calibrating LLMs' verbalized confidence: i.e., their expressions of confidence in text form, such as "I am 80% confident that...". Existing approaches either rely on prompt engineering or fine-tuning with heuristically generated uncertainty estimates, both of which have limited effectiveness and generalizability. Motivated by the notion of proper scoring rules for calibration in classical machine learning models, we introduce ConfTuner, a simple and efficient fine-tuning method that introduces minimal overhead and does not require ground-truth confidence scores or proxy confidence estimates. ConfTuner relies on a new loss function, tokenized Brier score, which we theoretically prove to be a proper scoring rule, intuitively meaning that it "correctly incentivizes the model to report its true probability of being correct". ConfTuner improves calibration across diverse reasoning tasks and generalizes to black-box models such as GPT-4o. Our results further show that better-calibrated confidence enables downstream gains in self-correction and model cascade, advancing the development of trustworthy LLM systems. The code is available at https://github.com/liushiliushi/ConfTuner.

