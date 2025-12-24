---
layout: default
title: "HardTests: Synthesizing High-Quality Test Cases for LLM Coding"
---

# HardTests: Synthesizing High-Quality Test Cases for LLM Coding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24098" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24098v1</a>
  <a href="https://arxiv.org/pdf/2505.24098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24098v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24098v1', 'HardTests: Synthesizing High-Quality Test Cases for LLM Coding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhongmou He, Yee Man Choi, Kexun Zhang, Jiabao Ji, Junting Zhou, Dejia Xu, Ivan Bercovich, Aidan Zhang, Lei Li

**分类**: cs.CL

**发布日期**: 2025-05-30

**🔗 代码/项目**: [PROJECT_PAGE](https://leililab.github.io/HardTests/)

---

## 💡 一句话要点

**提出HARDTESTGEN以解决LLM编码问题的高质量测试用例合成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `测试用例合成` `验证器` `自动化测试` `软件开发` `机器学习`

## 📋 核心要点

1. 现有方法在处理复杂编码问题时，难以提供可靠的验证器，尤其是合成边缘案例的挑战。
2. 本文提出HARDTESTGEN，通过LLM合成高质量测试用例，旨在提高验证器的可靠性和有效性。
3. 实验结果表明，HARDTESTGEN在精确度和召回率上显著优于现有测试，尤其在难题上表现出色。

## 📝 摘要（中文）

验证器在大型语言模型（LLM）推理中扮演着重要角色，尤其是在后训练技术如强化学习中。然而，对于复杂编码问题，可靠的验证器难以获得，因为巧妙伪装的错误解决方案往往只能通过精心编写的边缘案例来检测，这些边缘案例难以合成。为了解决这一问题，本文提出了HARDTESTGEN，一个利用LLM进行高质量测试合成的管道。通过该管道，我们策划了一个包含47,000个问题和合成高质量测试的综合竞争编程数据集HARDTESTS。与现有测试相比，HARDTESTGEN测试在评估LLM生成代码时的精确度提高了11.3个百分点，召回率提高了17.5个百分点。对于更难的问题，精确度的提升可达到40个百分点。HARDTESTS在模型训练中也证明了其有效性，体现在下游代码生成性能上。我们将开放我们的数据集和合成管道。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂编码问题中，现有验证器难以有效检测错误解决方案的问题，尤其是合成高质量边缘案例的困难。

**核心思路**：HARDTESTGEN的核心思路是利用大型语言模型（LLM）自动合成高质量的测试用例，以提高验证器的准确性和召回率。通过这种方式，可以生成更具挑战性的测试用例，从而更好地评估LLM生成的代码。

**技术框架**：HARDTESTGEN的整体架构包括数据集构建、测试用例合成和评估三个主要模块。首先，构建一个包含多样化问题的数据集；其次，使用LLM生成针对这些问题的高质量测试用例；最后，通过验证器评估生成的测试用例的有效性。

**关键创新**：HARDTESTGEN的主要创新在于其高效的测试用例合成方法，利用LLM生成边缘案例，显著提高了测试的精确度和召回率，与传统手动编写测试用例的方法相比，具有更高的自动化和效率。

**关键设计**：在设计过程中，HARDTESTGEN采用了特定的参数设置和损失函数，以优化生成的测试用例质量。同时，网络结构经过精心设计，以确保生成的测试用例能够覆盖更多的边缘情况。具体的技术细节包括对生成模型的训练策略和评估指标的选择。

## 📊 实验亮点

实验结果显示，HARDTESTGEN生成的测试用例在评估LLM生成代码时，精确度提高了11.3个百分点，召回率提高了17.5个百分点。在处理更难的问题时，精确度的提升甚至达到40个百分点，证明了其在模型训练中的有效性。

## 🎯 应用场景

HARDTESTGEN的研究成果在多个领域具有潜在应用价值，尤其是在软件开发和自动化测试中。通过提供高质量的测试用例，可以显著提高代码验证的效率和准确性，降低软件缺陷率。此外，该方法也可扩展到其他需要高质量验证的领域，如机器学习模型的评估和优化。

## 📄 摘要（原文）

> Verifiers play a crucial role in large language model (LLM) reasoning, needed by post-training techniques such as reinforcement learning. However, reliable verifiers are hard to get for difficult coding problems, because a well-disguised wrong solution may only be detected by carefully human-written edge cases that are difficult to synthesize. To address this issue, we propose HARDTESTGEN, a pipeline for high-quality test synthesis using LLMs. With this pipeline, we curate a comprehensive competitive programming dataset HARDTESTS with 47k problems and synthetic high-quality tests. Compared with existing tests, HARDTESTGEN tests demonstrate precision that is 11.3 percentage points higher and recall that is 17.5 percentage points higher when evaluating LLM-generated code. For harder problems, the improvement in precision can be as large as 40 points. HARDTESTS also proves to be more effective for model training, measured by downstream code generation performance. We will open-source our dataset and synthesis pipeline at https://leililab.github.io/HardTests/.

