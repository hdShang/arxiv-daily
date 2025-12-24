---
layout: default
title: "CodeSimpleQA: Scaling Factuality in Code Large Language Models"
---

# CodeSimpleQA: Scaling Factuality in Code Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19424" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19424v1</a>
  <a href="https://arxiv.org/pdf/2512.19424.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19424v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19424v1', 'CodeSimpleQA: Scaling Factuality in Code Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Yang, Wei Zhang, Yizhi Li, Shawn Guo, Haowen Wang, Aishan Liu, Ge Zhang, Zili Wang, Zhoujun Li, Xianglong Liu, Weifeng Lv

**分类**: cs.CL

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**CodeSimpleQA：提升代码大语言模型的事实性准确度**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码大语言模型` `事实性评估` `基准测试` `指令微调` `强化学习` `编程知识` `代码生成`

## 📋 核心要点

1. 现有代码基准测试主要关注代码执行的正确性，忽略了模型对编程知识理解的事实准确性。
2. 论文提出CodeSimpleQA基准和CodeSimpleQA-Instruct指令数据集，用于评估和提升代码大语言模型的事实性。
3. 通过监督微调和强化学习的后训练框架，显著提升了模型在CodeSimpleQA上的事实性准确度。

## 📝 摘要（中文）

大型语言模型（LLM）在代码生成方面取得了显著进展，在从自然语言指令合成代码片段方面表现出令人印象深刻的能力。然而，一个关键挑战仍然存在，即确保LLM生成关于编程概念、技术实现等方面的、在事实上准确的响应。以往大多数代码相关基准侧重于代码执行的正确性，而忽略了编程知识的事实准确性。为了解决这一差距，我们提出了CodeSimpleQA，这是一个全面的双语基准，旨在评估代码LLM在回答代码相关问题时的事实准确性，其中包含精心策划的英语和中文问答对，涵盖不同的编程语言和主要的计算机科学领域。此外，我们创建了CodeSimpleQA-Instruct，一个包含6600万个样本的大规模指令语料库，并开发了一个结合了监督微调和强化学习的后训练框架。我们对各种LLM的全面评估表明，即使是最先进的LLM也在代码事实性方面存在困难。我们提出的框架证明了相对于基础模型的显著改进，突显了在开发可靠的代码LLM中，事实性感知对齐的关键重要性。

## 🔬 方法详解

**问题定义**：现有代码大语言模型在生成代码时，虽然代码可以执行，但对编程概念、技术实现等方面的理解可能存在事实性错误。以往的评测基准主要关注代码执行的正确性，缺乏对模型编程知识事实准确性的评估。

**核心思路**：论文的核心思路是构建一个专门用于评估代码大语言模型事实性准确度的基准测试集CodeSimpleQA，并利用大规模指令数据集CodeSimpleQA-Instruct，通过监督微调和强化学习来提升模型的事实性。

**技术框架**：整体框架包含三个主要部分：1) 构建双语基准测试集CodeSimpleQA，包含高质量的编程相关问答对；2) 创建大规模指令数据集CodeSimpleQA-Instruct，用于模型的指令微调；3) 提出一个后训练框架，结合监督微调（SFT）和强化学习（RL），以提升模型的事实性。

**关键创新**：关键创新在于提出了一个专门针对代码大语言模型事实性评估的基准测试集，并设计了一个结合监督微调和强化学习的后训练框架。与以往侧重于代码执行正确性的方法不同，该方法直接关注模型对编程知识的理解是否准确。

**关键设计**：CodeSimpleQA包含英语和中文两种语言的问答对，覆盖多种编程语言和计算机科学领域。CodeSimpleQA-Instruct包含6600万个样本，用于指令微调。后训练框架中，首先使用CodeSimpleQA-Instruct进行监督微调，然后使用强化学习进一步提升模型的事实性。具体的损失函数和网络结构细节在论文中未详细说明（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19424v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19424v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19424v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过在CodeSimpleQA基准测试集上对多种LLM进行评估，发现即使是最先进的LLM在代码事实性方面也存在困难。提出的后训练框架显著提升了模型在CodeSimpleQA上的事实性准确度，证明了事实性感知对齐在开发可靠代码LLM中的重要性。具体提升幅度未在摘要中明确给出（未知）。

## 🎯 应用场景

该研究成果可应用于提升代码大语言模型的可靠性和可信度，使其在代码生成、代码解释、编程问答等场景中提供更准确、更可靠的编程知识。这有助于提高开发效率，降低错误率，并促进编程教育和知识共享。

## 📄 摘要（原文）

> Large language models (LLMs) have made significant strides in code generation, achieving impressive capabilities in synthesizing code snippets from natural language instructions. However, a critical challenge remains in ensuring LLMs generate factually accurate responses about programming concepts, technical implementations, etc. Most previous code-related benchmarks focus on code execution correctness, overlooking the factual accuracy of programming knowledge. To address this gap, we present CodeSimpleQA, a comprehensive bilingual benchmark designed to evaluate the factual accuracy of code LLMs in answering code-related questions, which contains carefully curated question-answer pairs in both English and Chinese, covering diverse programming languages and major computer science domains. Further, we create CodeSimpleQA-Instruct, a large-scale instruction corpus with 66M samples, and develop a post-training framework combining supervised fine-tuning and reinforcement learning. Our comprehensive evaluation of diverse LLMs reveals that even frontier LLMs struggle with code factuality. Our proposed framework demonstrates substantial improvements over the base model, underscoring the critical importance of factuality-aware alignment in developing reliable code LLMs.

