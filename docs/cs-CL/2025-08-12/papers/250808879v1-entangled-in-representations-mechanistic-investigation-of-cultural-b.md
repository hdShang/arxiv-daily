---
layout: default
title: "Entangled in Representations: Mechanistic Investigation of Cultural Biases in Large Language Models"
---

# Entangled in Representations: Mechanistic Investigation of Cultural Biases in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08879" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08879v1</a>
  <a href="https://arxiv.org/pdf/2508.08879.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08879v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08879v1', 'Entangled in Representations: Mechanistic Investigation of Cultural Biases in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haeun Yu, Seogyeong Jeong, Siddhesh Pawar, Jisu Shin, Jiho Jin, Junho Myung, Alice Oh, Isabelle Augenstein

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-12

**备注**: 16 pages, 7 figures

---

## 💡 一句话要点

**提出Culturescope以解决大语言模型中的文化偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文化偏见` `大型语言模型` `机制可解释性` `文化知识` `文化扁平化` `低资源文化` `西方主导偏见`

## 📋 核心要点

1. 现有研究主要通过外部评估来考察LLMs的文化能力，未能深入分析其内部机制如何导致文化偏见。
2. 本文提出Culturescope，通过机制可解释性的方法探讨LLMs的内部表示，揭示其文化知识空间。
3. 实验结果表明，LLMs在文化知识空间中存在西方主导偏见和文化扁平化现象，低资源文化的偏见敏感性较低。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在多元文化背景下的广泛应用，理解其内部机制对文化理解的影响变得尤为重要。以往的研究仅对LLMs的文化能力进行外部评估，未考虑其内部机制如何导致文化（误）表现。为此，本文提出了Culturescope，这是一种基于机制可解释性的方法，探讨LLMs的内部表示以揭示其文化知识空间。Culturescope采用补丁方法提取文化知识，并引入文化扁平化评分作为内在文化偏见的衡量标准。实验结果显示，LLMs在其文化知识空间中编码了西方主导偏见和文化扁平化现象。研究发现，低资源文化对文化偏见的敏感性较低，可能与其训练资源有限有关。本文为未来减轻文化偏见和增强LLMs文化理解提供了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLMs）在文化理解中存在的偏见问题，现有方法未能深入探讨其内部机制如何导致文化（误）表现。

**核心思路**：提出Culturescope，通过机制可解释性的方法分析LLMs的内部表示，提取文化知识并量化文化偏见。

**技术框架**：Culturescope的整体架构包括数据预处理、文化知识提取、文化扁平化评分计算以及偏见分析四个主要模块。

**关键创新**：引入文化扁平化评分作为衡量内在文化偏见的新指标，首次从机制层面探讨LLMs的文化知识空间。

**关键设计**：采用补丁方法提取文化知识，设计了特定的损失函数以优化文化知识的表示，确保模型能够有效捕捉文化偏见。

## 📊 实验亮点

实验结果表明，LLMs在其文化知识空间中显著编码了西方主导偏见和文化扁平化现象。研究发现，低资源文化对文化偏见的敏感性较低，可能与其训练资源的限制有关。这些发现为未来的研究提供了重要的实证基础。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、文化研究和社会科学等。通过深入理解LLMs的文化偏见，能够为模型的公平性和多样性提供理论支持，促进更具包容性的人工智能系统的开发。未来，研究成果可为减轻文化偏见提供指导，提升LLMs在多文化环境中的表现。

## 📄 摘要（原文）

> The growing deployment of large language models (LLMs) across diverse cultural contexts necessitates a better understanding of how the overgeneralization of less documented cultures within LLMs' representations impacts their cultural understanding. Prior work only performs extrinsic evaluation of LLMs' cultural competence, without accounting for how LLMs' internal mechanisms lead to cultural (mis)representation. To bridge this gap, we propose Culturescope, the first mechanistic interpretability-based method that probes the internal representations of LLMs to elicit the underlying cultural knowledge space. CultureScope utilizes a patching method to extract the cultural knowledge. We introduce a cultural flattening score as a measure of the intrinsic cultural biases. Additionally, we study how LLMs internalize Western-dominance bias and cultural flattening, which allows us to trace how cultural biases emerge within LLMs. Our experimental results reveal that LLMs encode Western-dominance bias and cultural flattening in their cultural knowledge space. We find that low-resource cultures are less susceptible to cultural biases, likely due to their limited training resources. Our work provides a foundation for future research on mitigating cultural biases and enhancing LLMs' cultural understanding. Our codes and data used for experiments are publicly available.

