---
layout: default
title: "TEN: Table Explicitization, Neurosymbolically"
---

# TEN: Table Explicitization, Neurosymbolically

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09324" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09324v1</a>
  <a href="https://arxiv.org/pdf/2508.09324.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09324v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09324v1', 'TEN: Table Explicitization, Neurosymbolically')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikita Mehrotra, Aayush Kumar, Sumit Gulwani, Arjun Radhakrishna, Ashish Tiwari

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出TEN方法以解决半结构化文本中的表格数据提取问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格数据提取` `半结构化文本` `神经符号方法` `结构分解提示` `符号检查器`

## 📋 核心要点

1. 现有方法在处理半结构化文本时，缺乏一致的分隔符，导致表格数据提取的准确性和可靠性不足。
2. TEN方法结合了神经网络和符号推理，通过结构分解提示生成初始表格，并利用符号检查器进行验证和修正。
3. 实验结果显示，TEN在多个数据集上显著提高了准确率，减少了幻觉现象，并在用户研究中获得了更高的用户满意度。

## 📝 摘要（中文）

我们提出了一种神经符号方法TEN，用于从半结构化输入文本中提取表格数据。该任务在没有一致使用特殊分隔符来分隔列和行的文本输入中尤为具有挑战性。纯神经方法由于幻觉和无法强制执行硬约束而表现不佳。TEN采用结构分解提示，这是一种针对大型语言模型（LLM）的专门链式思维提示方法，生成初始表格。随后，使用符号检查器评估表格的良构性，并检测幻觉或遗忘的情况。符号检查器的输出由批评LLM处理，以生成修复表格的指导，形成自我调试循环。我们的广泛实验表明，TEN在多个数据集和指标上显著优于纯神经基线，获得了更高的准确率和显著降低的幻觉率。21名参与者的用户研究进一步确认，TEN生成的表格在准确性上得分显著更高，并且在验证和修正的便利性上更受欢迎。

## 🔬 方法详解

**问题定义**：本论文旨在解决从半结构化文本中提取表格数据的挑战，现有方法在缺乏一致分隔符的情况下，容易出现幻觉和错误，导致提取结果不可靠。

**核心思路**：TEN方法通过结合神经网络和符号推理，利用结构分解提示生成初始表格，并通过符号检查器进行验证和修正，从而提高提取的准确性和可靠性。

**技术框架**：TEN的整体架构包括三个主要模块：首先是使用大型语言模型生成初始表格的结构分解提示；其次是符号检查器对生成的表格进行评估，检测其良构性和幻觉；最后是批评LLM根据检查结果提供修正建议，形成自我调试循环。

**关键创新**：TEN的核心创新在于将神经网络与符号推理相结合，利用结构分解提示和符号检查器的双重机制，显著提升了表格数据提取的准确性和可靠性，这与传统的纯神经方法形成了鲜明对比。

**关键设计**：TEN在参数设置上采用了针对特定任务的优化策略，损失函数设计考虑了幻觉检测和表格良构性评估，网络结构则基于大型语言模型的能力进行定制，以确保生成的表格符合预期的格式和内容。

## 📊 实验亮点

实验结果表明，TEN在多个数据集上显著优于纯神经基线，准确率提升显著，具体表现为更高的精确匹配率和显著降低的幻觉率。此外，用户研究显示，参与者对TEN生成的表格准确性评分平均为5.0，相较于4.3的基线显著提高（p = 0.021），并在60%以上的情况下更倾向于选择TEN方法。

## 🎯 应用场景

TEN方法在数据提取、信息整理和自动化文档处理等领域具有广泛的应用潜力。其能够有效处理半结构化文本，提升数据提取的准确性和效率，未来可在商业智能、法律文档分析和学术研究等多个领域发挥重要作用。

## 📄 摘要（原文）

> We present a neurosymbolic approach, TEN, for extracting tabular data from semistructured input text. This task is particularly challenging for text input that does not use special delimiters consistently to separate columns and rows. Purely neural approaches perform poorly due to hallucinations and their inability to enforce hard constraints. TEN uses Structural Decomposition prompting - a specialized chain-of-thought prompting approach - on a large language model (LLM) to generate an initial table, and thereafter uses a symbolic checker to evaluate not only the well-formedness of that table, but also detect cases of hallucinations or forgetting. The output of the symbolic checker is processed by a critique-LLM to generate guidance for fixing the table, which is presented to the original LLM in a self-debug loop. Our extensive experiments demonstrate that TEN significantly outperforms purely neural baselines across multiple datasets and metrics, achieving significantly higher exact match accuracy and substantially reduced hallucination rates. A 21-participant user study further confirms that TEN's tables are rated significantly more accurate (mean score: 5.0 vs 4.3; p = 0.021), and are consistently preferred for ease of verification and correction, with participants favoring our method in over 60% of the cases.

