---
layout: default
title: "Let's Verify Math Questions Step by Step"
---

# Let's Verify Math Questions Step by Step

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13903" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13903v1</a>
  <a href="https://arxiv.org/pdf/2505.13903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13903v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13903v1', 'Let\'s Verify Math Questions Step by Step')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengyu Shen, Zhen Hao Wong, Runming He, Hao Liang, Meiyi Qiang, Zimo Meng, Zhengyang Zhao, Bohan Zeng, Zhengzhou Zhu, Bin Cui, Wentao Zhang

**分类**: cs.CL

**发布日期**: 2025-05-20

**🔗 代码/项目**: [GITHUB](https://github.com/scuuy/MathQ-Verify)

---

## 💡 一句话要点

**提出MathQ-Verify以解决数学问题验证的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学问题验证` `大型语言模型` `数据集质量` `逻辑推理` `自动化评测` `模型投票机制` `教育技术`

## 📋 核心要点

1. 现有方法主要关注生成正确答案，忽视了数学问题的有效性和准确性，导致数据集中的噪声和无效问题。
2. 本文提出MathQ-Verify，通过五个阶段的验证流程，系统性地检查和过滤不合适的数学问题，确保问题的逻辑性和完整性。
3. 实验结果显示，MathQ-Verify在多个基准测试中实现了最先进的性能，F1分数提升高达25个百分点，精度和召回率均表现优异。

## 📝 摘要（中文）

大型语言模型（LLMs）在数学推理方面取得了显著进展。然而，现有研究主要集中于生成正确的推理路径和答案，忽视了问题本身的有效性。本文提出了Math Question Verification（MathQ-Verify），一个五阶段的管道，旨在严格筛选不适当或不明确的数学问题。该方法通过格式验证、问题形式化、条件分解及逻辑矛盾检测等步骤，确保问题的完整性和有效性。实验结果表明，MathQ-Verify在多个基准测试中表现出色，F1分数提升了25个百分点，精度达到约90%。

## 🔬 方法详解

**问题定义**：本文旨在解决数学问题验证中的有效性和准确性问题。现有方法往往忽略了问题本身的合理性，导致生成的数据集存在噪声和无效问题。

**核心思路**：论文提出的MathQ-Verify通过五个阶段的严格验证流程，确保每个数学问题的格式、逻辑和信息完整性，从而提高数据集的质量。

**技术框架**：MathQ-Verify的整体架构包括五个主要阶段：格式验证、问题形式化、条件分解、逻辑矛盾检测和完整性检查。每个阶段都针对特定的验证任务，确保问题的有效性。

**关键创新**：最重要的技术创新在于系统化的五阶段验证流程，能够全面检查数学问题的各个方面，显著提高了验证的准确性和效率，与现有方法相比具有本质的区别。

**关键设计**：在设计中，采用了轻量级模型投票机制来提高精度，并通过手动双重验证构建了包含2147个多样化错误类型的数学问题数据集，确保了数据的可靠性。

## 📊 实验亮点

实验结果表明，MathQ-Verify在多个基准测试中表现优异，F1分数提升高达25个百分点，精度约为90%，召回率达到63%。通过轻量级模型投票机制，进一步提升了验证的准确性，展现了其在数学问题验证中的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、自动化评测系统和数学问题生成等。通过提供高质量的数学问题验证工具，能够有效减少数据集中的噪声，提高模型训练的效率和准确性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Large Language Models (LLMs) have recently achieved remarkable progress in mathematical reasoning. To enable such capabilities, many existing works distill strong reasoning models into long chains of thought or design algorithms to construct high-quality math QA data for training. However, these efforts primarily focus on generating correct reasoning paths and answers, while largely overlooking the validity of the questions themselves. In this work, we propose Math Question Verification (MathQ-Verify), a novel five-stage pipeline designed to rigorously filter ill-posed or under-specified math problems. MathQ-Verify first performs format-level validation to remove redundant instructions and ensure that each question is syntactically well-formed. It then formalizes each question, decomposes it into atomic conditions, and verifies them against mathematical definitions. Next, it detects logical contradictions among these conditions, followed by a goal-oriented completeness check to ensure the question provides sufficient information for solving. To evaluate this task, we use existing benchmarks along with an additional dataset we construct, containing 2,147 math questions with diverse error types, each manually double-validated. Experiments show that MathQ-Verify achieves state-of-the-art performance across multiple benchmarks, improving the F1 score by up to 25 percentage points over the direct verification baseline. It further attains approximately 90% precision and 63% recall through a lightweight model voting scheme. MathQ-Verify offers a scalable and accurate solution for curating reliable mathematical datasets, reducing label noise and avoiding unnecessary computation on invalid questions. Our code and data are available at https://github.com/scuuy/MathQ-Verify.

