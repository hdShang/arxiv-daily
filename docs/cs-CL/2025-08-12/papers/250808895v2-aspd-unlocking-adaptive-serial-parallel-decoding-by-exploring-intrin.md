---
layout: default
title: "ASPD: Unlocking Adaptive Serial-Parallel Decoding by Exploring Intrinsic Parallelism in LLMs"
---

# ASPD: Unlocking Adaptive Serial-Parallel Decoding by Exploring Intrinsic Parallelism in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08895" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08895v2</a>
  <a href="https://arxiv.org/pdf/2508.08895.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08895v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08895v2', 'ASPD: Unlocking Adaptive Serial-Parallel Decoding by Exploring Intrinsic Parallelism in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keyu Chen, Zhifeng Shen, Daohai Yu, Haoqian Wu, Wei Wen, Jianfeng He, Ruizhi Qiao, Xing Sun

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-12 (更新: 2025-08-14)

**备注**: 20 pages, 9 figures

---

## 💡 一句话要点

**提出自适应串行-并行解码以解决大语言模型推理延迟问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自适应解码` `大语言模型` `并行计算` `推理加速` `混合解码引擎`

## 📋 核心要点

1. 现有的大语言模型在推理过程中面临显著的延迟挑战，主要由于自回归解码的顺序特性。
2. 本文提出自适应串行-并行解码（ASPD），通过自动提取可并行化结构来提升解码效率。
3. 实验表明，ASPD在多个任务上实现了显著的性能提升，尤其在速度和生成质量方面表现优异。

## 📝 摘要（中文）

随着大语言模型（LLMs）规模和复杂性的增加，推理延迟问题日益严重，主要源于其自回归解码范式的顺序特性。通过重新审视自回归模型的输出，发现某些片段具有可并行化的结构，称为内在并行性。本文提出了一种自适应串行-并行解码（ASPD）方法，自动构建可并行化数据并实现高效的并行解码机制。我们实现了一个混合解码引擎，能够在串行和并行解码模式之间无缝切换，同时保持可重用的KV缓存，最大化计算效率。实验结果表明，ASPD在多个任务上实现了前所未有的效果和效率提升，尤其在Vicuna Bench上，速度提升达到3.19倍，平均提升1.85倍，同时生成质量保持在1%的差异范围内。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在推理过程中由于自回归解码的顺序特性导致的延迟问题。现有方法无法有效利用模型输出中的可并行化结构，限制了推理速度的提升。

**核心思路**：论文的核心思路是通过识别和提取自回归模型输出中的内在并行性，采用自适应串行-并行解码策略，允许同时解码多个可并行化的分支，从而显著提高推理速度。

**技术框架**：整体架构包括一个非侵入式管道，用于自动提取和验证可并行化结构，以及一个混合解码引擎，支持串行与并行解码模式的无缝切换。该框架还维护一个可重用的KV缓存，以提高计算效率。

**关键创新**：最重要的技术创新在于提出了自适应串行-并行解码机制，能够自动识别并利用模型输出中的并行结构，与传统的顺序解码方法本质上不同。

**关键设计**：在设计中，采用了高效的参数设置和损失函数，确保在并行解码时能够保持生成质量，同时优化了网络结构以支持混合解码模式。具体的参数和结构细节在实验部分进行了详细说明。

## 📊 实验亮点

实验结果显示，ASPD在Vicuna Bench上实现了最高3.19倍的速度提升，平均提升为1.85倍，同时生成质量与自回归模型相比保持在1%的差异范围内。这一结果表明，ASPD在效率和效果上均取得了显著进展。

## 🎯 应用场景

该研究的潜在应用领域包括AI驱动的客户服务机器人和答案检索引擎等延迟敏感的应用场景。通过显著提升推理速度，ASPD能够为实时交互和快速响应的应用提供支持，推动大语言模型在实际场景中的广泛应用。

## 📄 摘要（原文）

> The increasing scale and complexity of large language models (LLMs) pose significant inference latency challenges, primarily due to their autoregressive decoding paradigm characterized by the sequential nature of next-token prediction. By re-examining the outputs of autoregressive models, we observed that some segments exhibit parallelizable structures, which we term intrinsic parallelism. Decoding each parallelizable branch simultaneously (i.e. parallel decoding) can significantly improve the overall inference speed of LLMs. In this paper, we propose an Adaptive Serial-Parallel Decoding (ASPD), which addresses two core challenges: automated construction of parallelizable data and efficient parallel decoding mechanism. More specifically, we introduce a non-invasive pipeline that automatically extracts and validates parallelizable structures from the responses of autoregressive models. To empower efficient adaptive serial-parallel decoding, we implement a Hybrid Decoding Engine which enables seamless transitions between serial and parallel decoding modes while maintaining a reusable KV cache, maximizing computational efficiency. Extensive evaluations across General Tasks, Retrieval-Augmented Generation, Mathematical Reasoning, demonstrate that ASPD achieves unprecedented performance in both effectiveness and efficiency. Notably, on Vicuna Bench, our method achieves up to 3.19x speedup (1.85x on average) while maintaining response quality within 1% difference compared to autoregressive models, realizing significant acceleration without compromising generation quality. Our framework sets a groundbreaking benchmark for efficient LLM parallel inference, paving the way for its deployment in latency-sensitive applications such as AI-powered customer service bots and answer retrieval engines.

