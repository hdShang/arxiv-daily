---
layout: default
title: "Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation and Supervision Study"
---

# Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation and Supervision Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04810" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04810v2</a>
  <a href="https://arxiv.org/pdf/2506.04810.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04810v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04810v2', 'Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation and Supervision Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yujun Zhou, Jiayi Ye, Zipeng Ling, Yufei Han, Yue Huang, Haomin Zhuang, Zhenwen Liang, Kehan Guo, Taicheng Guo, Xiangqi Wang, Xiangliang Zhang

**分类**: cs.CL, cs.AI, cs.LO

**发布日期**: 2025-06-05 (更新: 2025-10-09)

**备注**: Accepted by the Findings of EMNLP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/YujunZhou/FineLogic)

---

## 💡 一句话要点

**提出FineLogic框架以解决LLMs逻辑推理评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `逻辑推理` `大型语言模型` `细粒度评估` `微调策略` `自然语言处理`

## 📋 核心要点

1. 现有的逻辑推理评估方法主要依赖最终答案的准确性，无法有效反映推理过程的质量。
2. 本文提出FineLogic框架，通过整体准确性、逐步合理性和表示层次探测三个维度评估逻辑推理能力。
3. 实验结果表明，自然语言监督在处理复杂问题时表现优越，而符号监督则在推理步骤的结构合理性上更具优势。

## 📝 摘要（中文）

逻辑推理是大型语言模型（LLMs）的核心能力，但现有基准仅依赖最终答案的准确性，无法全面捕捉推理过程的质量。为此，本文提出FineLogic，一个细粒度评估框架，从整体准确性、逐步合理性和表示层次探测三个维度评估逻辑推理。通过该框架，我们全面研究了不同微调监督格式对推理能力的影响，发现自然语言监督在处理分布外和长链问题时表现优越，而符号监督则在构建结构合理的原子推理步骤上更具优势。此外，探测分析表明，微调主要优化模型的逐步生成过程，而非早期收敛能力。我们的框架和分析为评估和提升LLMs的逻辑推理提供了更严格的视角。

## 🔬 方法详解

**问题定义**：本文旨在解决现有逻辑推理评估方法无法全面捕捉推理过程质量的问题，现有方法仅关注最终答案的准确性，忽视了推理过程中的细节和合理性。

**核心思路**：提出FineLogic框架，通过细粒度的评估方式，从多个维度分析LLMs的逻辑推理能力，旨在提升评估的全面性和准确性。

**技术框架**：FineLogic框架包括三个主要模块：整体准确性评估、逐步合理性评估和表示层次探测。整体准确性评估关注最终答案的正确性，逐步合理性评估分析推理过程中的每一步，表示层次探测则评估模型对推理表示的理解能力。

**关键创新**：最重要的创新在于引入了细粒度的评估维度，使得逻辑推理的评估不仅限于最终结果，还关注推理过程的每一步，提供了更全面的评估视角。

**关键设计**：在微调过程中，采用了四种不同的监督格式，包括自然语言和三种符号变体，实验中发现自然语言监督在处理复杂问题时表现更佳，而符号监督则在推理步骤的结构合理性上更为突出。

## 📊 实验亮点

实验结果显示，自然语言监督在处理分布外和长链问题时的准确率显著高于符号监督，后者在推理步骤的结构合理性上表现更佳。FineLogic框架提供了更全面的评估方法，为LLMs的逻辑推理能力提升提供了新的思路。

## 🎯 应用场景

该研究的潜在应用领域包括教育、法律推理、自动化决策等，能够帮助提升LLMs在复杂推理任务中的表现。通过更精细的评估和微调策略，未来可以在更广泛的实际场景中应用LLMs，提升其逻辑推理能力和可靠性。

## 📄 摘要（原文）

> Logical reasoning is a core capability for large language models (LLMs), yet existing benchmarks that rely solely on final-answer accuracy fail to capture the quality of the reasoning process. To address this, we introduce FineLogic, a fine-grained evaluation framework that assesses logical reasoning across three dimensions: overall accuracy, stepwise soundness, and representation-level probing. Leveraging this framework, we conduct a comprehensive study on how different supervision formats in fine-tuning shape reasoning abilities. We fine-tune LLMs on four supervision styles: one in natural language and three symbolic variants. We find a key trade-off: natural language supervision excels at generalization to out-of-distribution and long-chain problems, whereas symbolic supervision is superior at instilling structurally sound, atomic reasoning steps. Furthermore, our probing analysis indicates that fine-tuning primarily refines the model's step-by-step generation process, rather than improving its ability to converge on an answer early. Together, our framework and analysis provide a more rigorous lens for evaluating and improving logical reasoning in LLMs. The code is available at https://github.com/YujunZhou/FineLogic.

