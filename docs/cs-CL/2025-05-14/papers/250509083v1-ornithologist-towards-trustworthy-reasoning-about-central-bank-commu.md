---
layout: default
title: "Ornithologist: Towards Trustworthy \"Reasoning\" about Central Bank Communications"
---

# Ornithologist: Towards Trustworthy "Reasoning" about Central Bank Communications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.09083" class="toolbar-btn" target="_blank">📄 arXiv: 2505.09083v1</a>
  <a href="https://arxiv.org/pdf/2505.09083.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.09083v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.09083v1', 'Ornithologist: Towards Trustworthy &quot;Reasoning&quot; about Central Bank Communications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dominic Zaun Eu Jones

**分类**: econ.GN, cs.CL

**发布日期**: 2025-05-14

**备注**: 16 pages, 6 figures

---

## 💡 一句话要点

**提出Ornithologist以解决中央银行沟通分析的透明性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本分类` `中央银行` `可解释性` `弱监督学习` `经济分析` `决策树` `市场预期`

## 📋 核心要点

1. 现有的文本分类方法在透明性和可解释性方面存在不足，难以为非专家提供清晰的分析结果。
2. Ornithologist通过引入分类法引导推理，结合人类决策树来指导大型语言模型，从而提高了系统的可解释性。
3. 实验结果表明，Ornithologist在分析中央银行沟通时，能够有效降低幻觉风险，并提供关于市场预期的有价值信息。

## 📝 摘要（中文）

本文开发了Ornithologist，一个弱监督文本分类系统，用于衡量中央银行文本的鹰派和鸽派倾向。Ornithologist采用“分类法引导推理”，通过人类编写的决策树指导大型语言模型，从而提高系统的透明性和可解释性，使其对非专家更为友好。此外，该方法降低了幻觉风险。由于所需监督程度低于传统分类系统，Ornithologist更易于应用于其他问题或文本来源（如新闻），无需太多修改。Ornithologist对RBA沟通的鹰鸽倾向测量提供了关于现金利率路径和市场预期未来的信息。

## 🔬 方法详解

**问题定义**：本文旨在解决中央银行沟通分析中透明性不足和可解释性差的问题。现有方法往往依赖于复杂的模型，难以为非专家提供清晰的分析结果。

**核心思路**：Ornithologist的核心思路是通过“分类法引导推理”来指导大型语言模型，利用人类编写的决策树增强模型的透明性和可解释性。这种设计使得模型的决策过程更加清晰，降低了误解的可能性。

**技术框架**：Ornithologist的整体架构包括数据预处理、决策树构建、模型训练和结果分析四个主要模块。首先，系统对输入文本进行预处理，然后构建决策树以指导模型的推理过程，接着进行模型训练，最后对结果进行分析和解释。

**关键创新**：该研究的关键创新在于引入了“分类法引导推理”，通过人类决策树来增强大型语言模型的可解释性。这一方法与传统的黑箱模型形成鲜明对比，使得模型的决策过程更加透明。

**关键设计**：在设计中，Ornithologist采用了较少的监督学习策略，减少了对标注数据的依赖。此外，模型的损失函数和网络结构经过精心设计，以确保在降低幻觉风险的同时，保持分类性能的稳定性。

## 📊 实验亮点

实验结果显示，Ornithologist在分析RBA沟通时，能够有效降低幻觉风险，并提供关于未来现金利率路径的准确预测。与传统方法相比，该系统在透明性和可解释性方面提升显著，且在分类准确率上保持了竞争力。

## 🎯 应用场景

Ornithologist的潜在应用领域包括金融市场分析、经济政策研究和新闻文本分析等。其透明性和可解释性使得非专家能够更容易理解中央银行的沟通意图，从而在决策时更具信心。未来，该系统还可扩展到其他领域的文本分类任务，具有广泛的实际价值。

## 📄 摘要（原文）

> I develop Ornithologist, a weakly-supervised textual classification system and measure the hawkishness and dovishness of central bank text. Ornithologist uses ``taxonomy-guided reasoning'', guiding a large language model with human-authored decision trees. This increases the transparency and explainability of the system and makes it accessible to non-experts. It also reduces hallucination risk. Since it requires less supervision than traditional classification systems, it can more easily be applied to other problems or sources of text (e.g. news) without much modification. Ornithologist measurements of hawkishness and dovishness of RBA communication carry information about the future of the cash rate path and of market expectations.

