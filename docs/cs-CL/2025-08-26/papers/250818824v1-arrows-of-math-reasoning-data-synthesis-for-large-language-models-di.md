---
layout: default
title: "Arrows of Math Reasoning Data Synthesis for Large Language Models: Diversity, Complexity and Correctness"
---

# Arrows of Math Reasoning Data Synthesis for Large Language Models: Diversity, Complexity and Correctness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18824" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18824v1</a>
  <a href="https://arxiv.org/pdf/2508.18824.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18824v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18824v1', 'Arrows of Math Reasoning Data Synthesis for Large Language Models: Diversity, Complexity and Correctness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sirui Chen, Changxin Tian, Binbin Hu, Kunlong Chen, Ziqi Liu, Zhiqiang Zhang, Jun Zhou

**分类**: cs.CL

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出程序辅助合成框架以提升大语言模型的数学推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学推理` `大语言模型` `数据合成` `程序辅助` `验证机制` `机器学习` `教育技术`

## 📋 核心要点

1. 现有方法在生成高质量数学推理数据时面临可扩展性和数据可靠性等重大挑战。
2. 提出的程序辅助合成框架通过整合数学知识和工具，系统生成高质量的数学问题解决对。
3. 实验结果显示，使用该框架生成的数据微调模型后，推理能力显著提升，达到多项基准数据集的最先进水平。

## 📝 摘要（中文）

提升大语言模型（LLMs）的数学推理能力需要高质量的训练数据，但传统方法在可扩展性、成本和数据可靠性方面面临重大挑战。为了解决这些问题，本文提出了一种新颖的程序辅助合成框架，系统地生成具有多样性、复杂性和正确性的高质量数学语料库。该框架整合了数学知识体系和领域特定工具，创建可执行程序，并将其转化为自然语言问题-解决对，并通过双向验证机制确保解决方案的正确性和程序与问题的一致性。实验表明，基于我们生成的数据微调的模型在多个基准数据集上显著提高了推理能力，展示了合成方法的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在数学推理方面的训练数据不足问题。现有方法在数据生成的可扩展性、成本和可靠性上存在明显不足。

**核心思路**：提出的框架通过程序辅助的方式，系统生成数学问题及其解决方案，确保数据的多样性、复杂性和正确性。该设计旨在提高数据生成的效率和质量。

**技术框架**：整体架构包括数学知识系统、领域特定工具和双向验证机制。首先，利用数学知识生成可执行程序，然后将程序转化为自然语言问题-解决对，最后通过验证机制确保数据的准确性和一致性。

**关键创新**：最重要的创新在于双向验证机制，它不仅验证了解决方案的正确性，还确保了程序与问题之间的一致性。这一机制显著提升了数据的可靠性。

**关键设计**：在参数设置上，框架采用了多样化的数学知识库和领域工具，损失函数设计上注重解决方案的准确性与多样性，网络结构则支持高效的程序生成与验证。

## 📊 实验亮点

实验结果表明，基于本文生成的12.3百万个问题解决对微调的模型在多个基准数据集上实现了显著提升，推理能力达到最先进水平，验证了合成方法的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能辅导系统和自动化数学问题生成等。通过提供高质量的数学问题解决对，可以帮助学生和研究人员更好地理解和应用数学知识，提升学习效果。未来，该框架还可能扩展到其他领域的知识生成与验证。

## 📄 摘要（原文）

> Enhancing the mathematical reasoning of large language models (LLMs) demands high-quality training data, yet conventional methods face critical challenges in scalability, cost, and data reliability. To address these limitations, we propose a novel program-assisted synthesis framework that systematically generates a high-quality mathematical corpus with guaranteed diversity, complexity, and correctness. This framework integrates mathematical knowledge systems and domain-specific tools to create executable programs. These programs are then translated into natural language problem-solution pairs and vetted by a bilateral validation mechanism that verifies solution correctness against program outputs and ensures program-problem consistency. We have generated 12.3 million such problem-solving triples. Experiments demonstrate that models fine-tuned on our data significantly improve their inference capabilities, achieving state-of-the-art performance on several benchmark datasets and showcasing the effectiveness of our synthesis approach.

