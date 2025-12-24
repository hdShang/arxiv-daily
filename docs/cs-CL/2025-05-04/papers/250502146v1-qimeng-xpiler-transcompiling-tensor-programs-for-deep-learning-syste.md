---
layout: default
title: QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learning Systems with a Neural-Symbolic Approach
---

# QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learning Systems with a Neural-Symbolic Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02146" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02146v1</a>
  <a href="https://arxiv.org/pdf/2505.02146.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02146v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02146v1', 'QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learning Systems with a Neural-Symbolic Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shouyang Dong, Yuanbo Wen, Jun Bi, Di Huang, Jiaming Guo, Jianxing Xu, Ruibai Xu, Xinkai Song, Yifan Hao, Xuehai Zhou, Tianshi Chen, Qi Guo, Yunji Chen

**分类**: cs.CL, cs.LG, cs.PL

**发布日期**: 2025-05-04

**备注**: Accepted to OSDI 2025

---

## 💡 一句话要点

**提出QiMeng-Xpiler以解决异构深度学习系统的编程负担问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度学习` `转编译` `大型语言模型` `符号程序合成` `编程效率` `异构系统` `自动化编程`

## 📋 核心要点

1. 现有的转编译技术在实现张量程序跨平台转换时，面临着巨大的人工成本和功能不正确的问题。
2. 本文提出的QiMeng-Xpiler通过结合大型语言模型和符号程序合成，自动化地进行张量程序的转编译。
3. 在四种不同的DLS上进行的实验显示，QiMeng-Xpiler的翻译准确率达到95%，性能提升可达2.0倍，编程效率提高显著。

## 📝 摘要（中文）

异构深度学习系统（DLS）如GPU和ASIC在工业数据中心的广泛应用，要求为不同平台开发多个低级张量程序。现有的转编译技术面临着巨大的人工成本或功能不正确的问题，使得张量程序的“写一次，随处运行”成为一个未解之谜。为此，本文提出了一种新型转编译器QiMeng-Xpiler，利用大型语言模型（LLMs）和符号程序合成的神经符号合成方法，自动翻译DLS中的张量程序。实验表明，QiMeng-Xpiler在四种具有不同编程接口的DLS上，平均准确率达到95%，并且翻译后的程序性能比供应商提供的手动优化库提升了2.0倍，编程生产力提高了96.0倍。

## 🔬 方法详解

**问题定义**：本文旨在解决异构深度学习系统中张量程序的转编译问题。现有方法往往需要大量人工干预，且存在功能不正确的风险，导致跨平台的编程效率低下。

**核心思路**：QiMeng-Xpiler的核心思路是结合大型语言模型的代码生成能力与符号程序合成，利用神经符号合成方法，使得复杂的符号合成过程变得计算上可行。

**技术框架**：QiMeng-Xpiler的整体架构包括多个LLM辅助的编译阶段，每个阶段通过预定义的元提示进行程序转换，并在转换过程中使用高效的符号程序合成来修复不正确的代码片段。

**关键创新**：最重要的创新在于将LLM与符号合成结合，显著降低了转编译过程中的计算复杂度，与传统方法相比，能够更高效地生成正确的代码。

**关键设计**：在设计中，采用了分层自动调优的方法，系统性地探索转换阶段的参数和顺序，以确保高性能的程序生成。

## 📊 实验亮点

实验结果显示，QiMeng-Xpiler在四种不同的深度学习系统上实现了95%的翻译准确率，且翻译后的程序性能相比于手动优化库提升了2.0倍，编程生产力提升高达96.0倍，展现了其在实际应用中的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括云计算、边缘计算和高性能计算等场景，能够显著提升异构深度学习系统的编程效率和性能。未来，QiMeng-Xpiler有望推动更多深度学习框架的跨平台兼容性，降低开发成本。

## 📄 摘要（原文）

> Heterogeneous deep learning systems (DLS) such as GPUs and ASICs have been widely deployed in industrial data centers, which requires to develop multiple low-level tensor programs for different platforms. An attractive solution to relieve the programming burden is to transcompile the legacy code of one platform to others. However, current transcompilation techniques struggle with either tremendous manual efforts or functional incorrectness, rendering "Write Once, Run Anywhere" of tensor programs an open question.
>   We propose a novel transcompiler, i.e., QiMeng-Xpiler, for automatically translating tensor programs across DLS via both large language models (LLMs) and symbolic program synthesis, i.e., neural-symbolic synthesis. The key insight is leveraging the powerful code generation ability of LLM to make costly search-based symbolic synthesis computationally tractable. Concretely, we propose multiple LLM-assisted compilation passes via pre-defined meta-prompts for program transformation. During each program transformation, efficient symbolic program synthesis is employed to repair incorrect code snippets with a limited scale. To attain high performance, we propose a hierarchical auto-tuning approach to systematically explore both the parameters and sequences of transformation passes. Experiments on 4 DLS with distinct programming interfaces, i.e., Intel DL Boost with VNNI, NVIDIA GPU with CUDA, AMD MI with HIP, and Cambricon MLU with BANG, demonstrate that QiMeng-Xpiler correctly translates different tensor programs at the accuracy of 95% on average, and the performance of translated programs achieves up to 2.0x over vendor-provided manually-optimized libraries. As a result, the programming productivity of DLS is improved by up to 96.0x via transcompiling legacy tensor programs.

