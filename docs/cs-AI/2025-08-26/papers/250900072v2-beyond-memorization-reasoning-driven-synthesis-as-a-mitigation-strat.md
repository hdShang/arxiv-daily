---
layout: default
title: "Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination"
---

# Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00072" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00072v2</a>
  <a href="https://arxiv.org/pdf/2509.00072.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00072v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00072v2', 'Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Terry Jingchen Zhang, Gopal Dev, Ning Wang, Nicole Ni, Wenyuan Jiang, Yinya Huang, Bernhard Schölkopf, Mrinmaya Sachan, Zhijing Jin

**分类**: cs.AI

**发布日期**: 2025-08-26 (更新: 2025-10-06)

**备注**: The authors choose to withdraw this manuscript as it constitutes incomplete work

---

## 💡 一句话要点

**提出基于推理驱动合成的策略以应对基准污染问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数据污染` `推理能力` `合成问题` `基准评估`

## 📋 核心要点

1. 现有方法在评估大型语言模型时面临数据污染的挑战，导致对推理能力的测量不准确。
2. 本文提出了一种基于推理驱动合成的框架，直接从arXiv论文中生成多步推理问题，以提高基准的有效性。
3. 实验结果表明，不同模型在知识截止日期附近的性能没有显著衰退，验证了合成方法的有效性。

## 📝 摘要（中文）

随着对大型语言模型（LLMs）能力评估的关注增加，数据污染问题引发了对静态基准是否真正测量推理能力的质疑。本文通过一个无限可扩展的框架，直接从arXiv论文合成研究级问答，利用研究出版物的自然时间结构，评估了知识截止日期前后性能衰退的潜在污染。我们对4个前沿模型进行了评估，结果显示不同规模和开发者的模型在知识截止日期附近没有显著的性能衰退。我们假设多步推理的合成管道提供了比浅层记忆更深层次的复杂性，有效地作为基准污染的缓解策略。我们全面开源了代码和数据集，以促进可重复性，并倡导优先考虑推理驱动的合成来构建基准。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型能力评估中的数据污染问题，现有方法往往依赖于静态基准，可能导致对模型推理能力的误判。

**核心思路**：通过合成多步推理问题，利用研究文献的时间结构，提供更复杂的评估任务，从而减少模型的记忆依赖。

**技术框架**：整体架构包括数据收集、问题合成和性能评估三个主要模块。首先，从arXiv论文中提取信息，然后生成多步推理问题，最后评估模型在这些问题上的表现。

**关键创新**：最重要的创新在于提出了一种推理驱动的合成方法，能够有效区分模型的推理能力与记忆能力，与传统的基准评估方法本质上不同。

**关键设计**：在合成过程中，设置了多步推理的复杂性，并设计了相应的评估标准，以确保生成问题的有效性和挑战性。

## 📊 实验亮点

实验结果显示，评估的四个前沿模型在知识截止日期附近的性能没有显著衰退，表明合成的多步推理问题有效地减少了模型的记忆依赖。这一发现与以往研究的结果形成鲜明对比，强调了推理驱动合成的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、教育评估和人工智能模型的能力评估。通过提供更有效的基准构建方法，可以帮助研究人员更准确地评估和改进语言模型的推理能力，推动相关技术的发展。

## 📄 摘要（原文）

> Capability evaluation of large language models (LLMs) is increasingly shadowed by rising concerns of data contamination that cast doubts on whether static benchmarks measure genuine reasoning or mere memorization. We present an empirical study using an infinitely scalable framework to synthesize research-level QA directly from arXiv papers, harnessing the natural temporal structure of research publications where performance decay after knowledge cutoffs may indicate potential contamination. We evaluated 4 frontier model represented by 2 models of different knowledge cutoff dates per family on 1,643 multi-step reasoning questions synthesized from 20,277 arXiv papers stratified over 26 months, covering at least 6 months before and after all cutoff dates. Our results consistently showed a lack of significant performance decay near knowledge cutoff dates for models of various sizes, developers, and release dates. We further performed a comparative analysis with previous longitudinal studies that reported significant post-cutoff performance decay using directly retrieved questions based on public data. we hypothesize that the multi-step reasoning required by our synthesis pipeline offered additional complexity that goes deeper than shallow memorization, which effectively serves a mitigation strategy against benchmark contamination. We fully open source our code and dataset to aid reproducibility and advocate for a paradigm shift that prioritize reasoning-driven synthesis to construct benchmarks over simply collecting newly released questions periodically.

