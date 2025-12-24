---
layout: default
title: "SelfReflect: Can LLMs Communicate Their Internal Answer Distribution?"
---

# SelfReflect: Can LLMs Communicate Their Internal Answer Distribution?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20295" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20295v3</a>
  <a href="https://arxiv.org/pdf/2505.20295.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20295v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20295v3', 'SelfReflect: Can LLMs Communicate Their Internal Answer Distribution?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Michael Kirchhof, Luca Füger, Adam Goliński, Eeshan Gunesh Dhekane, Arno Blaas, Seong Joon Oh, Sinead Williamson

**分类**: cs.CL, cs.AI, cs.LG, stat.ML

**发布日期**: 2025-05-26 (更新: 2025-09-30)

---

## 💡 一句话要点

**提出SelfReflect以揭示大型语言模型的不确定性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `不确定性表达` `信息论` `透明度` `信念分布` `摘要生成` `模型评估`

## 📋 核心要点

1. 现有方法在表达大型语言模型的不确定性时，缺乏透明度和全面性，通常只能给出单一答案及其模糊描述。
2. 本文提出SelfReflect度量，通过信息论方法评估模型内部信念分布与生成摘要之间的差异，增强模型的透明度。
3. 实验结果表明，SelfReflect能够有效捕捉模型输出的微小偏差，且通过反馈机制，模型能够生成更为忠实的输出摘要。

## 📝 摘要（中文）

现有大型语言模型（LLM）在表达不确定性时，通常仅通过添加百分比或模糊词汇来进行。然而，用户需要的是模型能够反映其内部信念分布，并输出所有可能选项及其概率。为此，本文提出了SelfReflect度量，作为一种信息论距离，用于评估摘要与答案分布之间的差异。通过干预和人类研究，发现SelfReflect能够敏感地捕捉到微小偏差，提供了摘要字符串与LLM实际内部答案分布之间的忠实度量。尽管现代LLM普遍无法直接揭示其不确定性，但通过采样多个输出并反馈到上下文中，模型能够生成忠实的摘要，从而为未来LLM不确定性沟通的发展提供了新的视角。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在表达不确定性时的透明度不足问题。现有方法通常只能提供单一答案，缺乏对内部信念分布的反映。

**核心思路**：论文提出SelfReflect度量，旨在通过信息论的距离度量，评估模型生成的摘要与其内部答案分布之间的相似性，从而提高模型的透明度。

**技术框架**：整体架构包括三个主要模块：首先，模型生成多个可能的输出；其次，计算这些输出的分布；最后，利用SelfReflect度量评估生成摘要的忠实度。

**关键创新**：最重要的创新在于引入SelfReflect度量，能够敏感地捕捉模型输出的微小偏差，与现有方法相比，提供了更为全面的信念分布表达方式。

**关键设计**：在实验中，模型通过采样多个输出并将其反馈到上下文中，以此提高生成摘要的忠实度。具体的参数设置和损失函数设计尚未详细披露，需进一步研究。

## 📊 实验亮点

实验结果显示，SelfReflect能够有效捕捉模型输出的微小偏差，提供了更为准确的忠实度量。尽管现代LLM在直接表达不确定性方面存在局限，但通过反馈机制，模型生成的摘要的忠实度得到了显著提升，展示了未来发展的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、对话系统和任何需要表达不确定性的自然语言处理任务。通过提高模型对不确定性的表达能力，可以增强用户的信任感和交互体验，推动人机交互的进一步发展。

## 📄 摘要（原文）

> The common approach to communicate a large language model's (LLM) uncertainty is to add a percentage number or a hedging word to its response. But is this all we can do? Instead of generating a single answer and then hedging it, an LLM that is fully transparent to the user needs to be able to reflect on its internal belief distribution and output a summary of all options it deems possible, and how likely they are. To test whether LLMs possess this capability, we develop the SelfReflect metric, an information-theoretic distance between a given summary and a distribution over answers. In interventional and human studies, we find that SelfReflect indicates even slight deviations, yielding a fine measure of faithfulness between a summary string and an LLM's actual internal distribution over answers. With SelfReflect, we make a resounding negative observation: modern LLMs are, across the board, incapable of revealing what they are uncertain about, neither through reasoning, nor chains-of-thoughts, nor explicit finetuning. However, we do find that LLMs are able to generate faithful summaries of their uncertainties if we help them by sampling multiple outputs and feeding them back into the context. This simple approach shines a light at the universal way of communicating LLM uncertainties whose future development the SelfReflect score enables.

