---
layout: default
title: "The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason"
---

# The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12286" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12286v4</a>
  <a href="https://arxiv.org/pdf/2506.12286.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12286v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12286v4', 'The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shanchao Liang, Spandan Garg, Roshanak Zilouchian Moghaddam

**分类**: cs.AI, cs.SE

**发布日期**: 2025-06-14 (更新: 2025-12-01)

---

## 💡 一句话要点

**提出新诊断任务以揭示LLMs在编码能力评估中的记忆偏差**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `编码能力` `基准测试` `记忆偏差` `软件工程` `诊断任务`

## 📋 核心要点

1. 现有的评估方法可能夸大了大型语言模型在编码任务中的真实能力，尤其是其记忆与推理的区分不明确。
2. 本研究提出了两个新的诊断任务，旨在通过仅依赖问题描述和当前文件上下文来探测模型的基础知识。
3. 实验结果显示，当前最先进的模型在SWE-Bench-Verified上表现出高达76%的准确率，但在未包含的任务上仅为53%，表明可能存在数据污染或记忆现象。

## 📝 摘要（中文）

随着大型语言模型（LLMs）能力的提升和广泛应用，基准测试在评估其实际效用方面发挥了重要作用。SWE-Bench Verified作为评估LLMs软件工程能力的重要基准，显示出这些模型在复杂编码任务上的良好表现。然而，现有评估协议可能夸大了这些模型的真实能力。本研究引入了两个诊断任务，以探测模型的基础知识，并提供实证证据表明，SWE-Bench-Verified上的性能提升可能部分源于记忆而非真正的问题解决能力。这些发现引发了对现有结果有效性的担忧，并强调了需要更稳健、抗污染的基准来可靠评估LLMs的编码能力。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在编码能力评估中存在的记忆偏差问题。现有方法未能有效区分模型的真正问题解决能力与其记忆能力，导致评估结果的可靠性受到质疑。

**核心思路**：论文通过引入两个新的诊断任务，分别是从问题描述中识别文件路径和在仅有当前文件上下文的情况下重现真实函数，来探测模型的基础知识。这种设计旨在揭示模型在编码任务中的真实能力，而非仅仅依赖于记忆。

**技术框架**：整体架构包括两个主要模块：文件路径识别和函数重现。每个模块通过分析问题描述和上下文信息，评估模型的推理能力和知识掌握情况。

**关键创新**：最重要的技术创新点在于通过新的诊断任务揭示了模型在编码能力评估中的记忆偏差。这与现有方法的本质区别在于，现有方法往往未能考虑模型的记忆效应。

**关键设计**：在实验中，模型的评估依赖于准确的上下文信息和问题描述，采用了特定的准确率指标来衡量模型在不同基准上的表现，确保了评估的严谨性。具体的参数设置和损失函数设计未在摘要中详细说明，需参考完整论文。

## 📊 实验亮点

实验结果显示，当前最先进的模型在SWE-Bench-Verified上识别错误文件路径的准确率高达76%，而在未包含的任务上仅为53%。此外，函数重现任务的连续5-gram准确率在SWE-Bench Verified上达到35%，而在其他基准上仅为18%，显示出显著的性能差异。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程、自动化编码和智能助手等。通过更准确地评估大型语言模型的编码能力，能够提升这些模型在实际应用中的可靠性和有效性，进而推动智能编程工具的发展。

## 📄 摘要（原文）

> As large language models (LLMs) become increasingly capable and widely adopted, benchmarks play a central role in assessing their practical utility. For example, SWE-Bench Verified has emerged as a critical benchmark for evaluating LLMs' software engineering abilities, particularly their aptitude for resolving real-world GitHub issues. Recent LLMs show impressive performance on SWE-Bench, leading to optimism about their capacity for complex coding tasks. However, current evaluation protocols may overstate these models' true capabilities. It is crucial to distinguish LLMs' generalizable problem-solving ability and other learned artifacts. In this work, we introduce two diagnostic tasks: file path identification from issue descriptions alone and ground truth function reproduction with only the current file context and issue description to probe models' underlying knowledge. We present empirical evidence that performance gains on SWE-Bench-Verified may be partially driven by memorization rather than genuine problem-solving. We show that state-of-the-art models achieve up to 76% accuracy in identifying buggy file paths using only issue descriptions, without access to repository structure. This performance is merely up to 53% on tasks from repositories not included in SWE-Bench, pointing to possible data contamination or memorization. Similar patterns are also observed for the function reproduction task, where the verbatim similarity is much higher on SWE-Bench Verified than on other similar coding benchmarks (up to 35% consecutive 5-gram accuracy on SWE-Bench Verified and Full, but only up to 18% for tasks in other benchmarks). These findings raise concerns about the validity of existing results and underscore the need for more robust, contamination-resistant benchmarks to reliably evaluate LLMs' coding abilities.

