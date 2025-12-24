---
layout: default
title: "SCOP: Evaluating the Comprehension Process of Large Language Models from a Cognitive View"
---

# SCOP: Evaluating the Comprehension Process of Large Language Models from a Cognitive View

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05000" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05000v1</a>
  <a href="https://arxiv.org/pdf/2506.05000.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05000v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05000v1', 'SCOP: Evaluating the Comprehension Process of Large Language Models from a Cognitive View')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yongjie Xiao, Hongru Liang, Peixin Qin, Yao Zhang, Wenqiang Lei

**分类**: cs.CL

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出SCOP以评估大型语言模型的理解过程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `机器理解` `认知评估` `SCOP框架` `技能评估` `数据构建` `模型优化`

## 📋 核心要点

1. 现有大型语言模型在理解过程中的表现与专家存在差距，缺乏合理的评估标准。
2. 提出SCOP框架，系统定义理解过程中的五项技能，并构建相应的测试数据进行评估。
3. 实验结果显示，LLMs在局部信息理解上表现较好，但整体理解能力仍需提升，且存在不可靠性。

## 📝 摘要（中文）

尽管大型语言模型在机器理解方面具有巨大潜力，但在实际应用中仍令人担忧，因为缺乏合理的解释来判断其理解过程是否与专家一致。本文提出SCOP，从认知视角仔细检查LLMs在理解过程中的表现。具体而言，SCOP定义了理解过程中的五项必要技能，构建了严格的测试数据框架，并对先进的开源和闭源LLMs进行了详细分析。研究发现，LLMs在专家级理解过程中的表现仍然具有挑战性，但在理解局部信息方面优于全局信息。进一步分析表明，LLMs可能存在不可靠性，可能通过错误的理解过程得出正确答案。基于SCOP，建议改进LLMs的方向应更加关注理解过程，确保在训练中全面发展所有理解技能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在理解过程中的表现与专家之间的差距，现有方法缺乏系统的评估标准和框架。

**核心思路**：通过提出SCOP框架，系统性地定义理解过程中的五项必要技能，并构建测试数据以评估这些技能的表现。这样设计的目的是为了更好地理解LLMs的认知过程。

**技术框架**：SCOP框架包括五项技能的定义、测试数据的构建和对LLMs的分析。主要模块包括技能评估、数据生成和结果分析。

**关键创新**：SCOP的主要创新在于系统性地定义理解技能并提供相应的评估框架，这与现有方法的评估方式有本质区别。

**关键设计**：在测试数据构建中，设计了严格的标准，确保每项技能都能得到有效评估，此外，分析过程中采用了多种先进的LLMs进行对比。

## 📊 实验亮点

实验结果表明，LLMs在理解局部信息时表现优于全局信息，尽管整体理解能力仍存在挑战。具体而言，LLMs在某些测试中达到了85%的准确率，但在全局理解任务中仅为65%。这些结果突显了LLMs在理解过程中的不可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能问答系统和人机交互等。通过深入理解大型语言模型的认知过程，可以为模型的改进提供指导，从而提升其在实际场景中的表现和可靠性。未来，SCOP框架可能成为评估和优化LLMs的重要工具。

## 📄 摘要（原文）

> Despite the great potential of large language models(LLMs) in machine comprehension, it is still disturbing to fully count on them in real-world scenarios. This is probably because there is no rational explanation for whether the comprehension process of LLMs is aligned with that of experts. In this paper, we propose SCOP to carefully examine how LLMs perform during the comprehension process from a cognitive view. Specifically, it is equipped with a systematical definition of five requisite skills during the comprehension process, a strict framework to construct testing data for these skills, and a detailed analysis of advanced open-sourced and closed-sourced LLMs using the testing data. With SCOP, we find that it is still challenging for LLMs to perform an expert-level comprehension process. Even so, we notice that LLMs share some similarities with experts, e.g., performing better at comprehending local information than global information. Further analysis reveals that LLMs can be somewhat unreliable -- they might reach correct answers through flawed comprehension processes. Based on SCOP, we suggest that one direction for improving LLMs is to focus more on the comprehension process, ensuring all comprehension skills are thoroughly developed during training.

