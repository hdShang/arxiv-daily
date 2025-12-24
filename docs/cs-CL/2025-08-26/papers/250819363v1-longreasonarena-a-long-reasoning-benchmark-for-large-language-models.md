---
layout: default
title: "LongReasonArena: A Long Reasoning Benchmark for Large Language Models"
---

# LongReasonArena: A Long Reasoning Benchmark for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19363" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19363v1</a>
  <a href="https://arxiv.org/pdf/2508.19363.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19363v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19363v1', 'LongReasonArena: A Long Reasoning Benchmark for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayu Ding, Shuming Ma, Lei Cui, Nanning Zheng, Furu Wei

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-26

**🔗 代码/项目**: [GITHUB](https://github.com/LongReasonArena/LongReasonArena)

---

## 💡 一句话要点

**提出LongReasonArena以评估大型语言模型的长推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长推理能力` `大型语言模型` `基准评估` `多步骤算法` `自然语言处理`

## 📋 核心要点

1. 现有的长文本基准未能有效评估大型语言模型的长推理能力，存在明显的评估空白。
2. LongReasonArena通过设计多步骤算法任务，专注于长推理的关键方面，如检索和回溯，填补了这一空白。
3. 实验结果显示，现有模型在LongReasonArena上的表现不佳，Deepseek-R1仅有7.5%的准确率，表明该基准的挑战性。

## 📝 摘要（中文）

现有的大型语言模型（LLMs）长文本基准主要关注对长输入的理解评估，而忽视了长推理能力的评估。为了解决这一问题，我们提出了LongReasonArena，这是一个专门设计用于评估LLMs长推理能力的基准。我们的任务要求模型通过执行多步骤算法来解决问题，反映长推理的关键方面，如检索和回溯。通过控制输入，所需的推理长度可以任意扩展，最具挑战性的任务可达到100万标记的推理。广泛的评估结果表明，LongReasonArena对开源和专有LLMs都提出了显著挑战。例如，Deepseek-R1在我们的任务中仅达到7.5%的准确率。进一步分析还显示，准确率与预期推理步骤的对数呈线性下降关系。我们的代码和数据可在https://github.com/LongReasonArena/LongReasonArena获取。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有长文本基准未能评估大型语言模型长推理能力的问题。现有方法主要集中于理解长输入，而忽视了推理过程的复杂性和多样性。

**核心思路**：我们提出LongReasonArena基准，设计多步骤算法任务，要求模型在长推理过程中进行检索和回溯。这种设计旨在全面评估模型的长推理能力，尤其是在面对复杂问题时的表现。

**技术框架**：LongReasonArena的整体架构包括任务设计、输入控制和评估机制。任务设计涵盖多种推理任务，输入控制允许推理长度的灵活调整，评估机制则基于模型的推理准确性进行评分。

**关键创新**：本研究的关键创新在于引入了长推理能力的评估标准，特别是通过控制输入长度和推理步骤，提供了一个可扩展的评估框架。这与现有方法的单一理解评估形成了鲜明对比。

**关键设计**：在设计中，我们设置了多种参数以适应不同的推理任务，损失函数采用了适合长推理的设计，确保模型在多步骤推理中的表现得到有效评估。

## 📊 实验亮点

实验结果显示，Deepseek-R1在LongReasonArena任务中仅达到7.5%的准确率，表明该基准对现有模型提出了显著挑战。此外，准确率与预期推理步骤的对数呈线性下降关系，进一步揭示了长推理任务的复杂性。

## 🎯 应用场景

LongReasonArena的研究成果可广泛应用于自然语言处理、智能问答系统和复杂决策支持等领域。通过提升大型语言模型的长推理能力，能够在实际应用中更好地处理复杂问题，提供更准确的答案和建议，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Existing long-context benchmarks for Large Language Models (LLMs) focus on evaluating comprehension of long inputs, while overlooking the evaluation of long reasoning abilities. To address this gap, we introduce LongReasonArena, a benchmark specifically designed to assess the long reasoning capabilities of LLMs. Our tasks require models to solve problems by executing multi-step algorithms that reflect key aspects of long reasoning, such as retrieval and backtracking. By controlling the inputs, the required reasoning length can be arbitrarily scaled, reaching up to 1 million tokens of reasoning for the most challenging tasks. Extensive evaluation results demonstrate that LongReasonArena presents a significant challenge for both open-source and proprietary LLMs. For instance, Deepseek-R1 achieves only 7.5% accuracy on our task. Further analysis also reveals that the accuracy exhibits a linear decline with respect to the logarithm of the expected number of reasoning steps. Our code and data is available at https://github.com/LongReasonArena/LongReasonArena.

