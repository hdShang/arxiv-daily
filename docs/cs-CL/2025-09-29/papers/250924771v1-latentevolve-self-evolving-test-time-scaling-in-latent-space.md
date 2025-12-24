---
layout: default
title: "LatentEvolve: Self-Evolving Test-Time Scaling in Latent Space"
---

# LatentEvolve: Self-Evolving Test-Time Scaling in Latent Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24771" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24771v1</a>
  <a href="https://arxiv.org/pdf/2509.24771.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24771v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24771v1', 'LatentEvolve: Self-Evolving Test-Time Scaling in Latent Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guibin Zhang, Fanci Meng, Guancheng Wan, Zherui Li, Kun Wang, Zhenfei Yin, Lei Bai, Shuicheng Yan

**分类**: cs.CL

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出LatentEvolve，通过潜空间自进化测试时缩放提升大语言模型推理能力。**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `测试时缩放` `大语言模型` `自进化学习` `互补学习系统` `潜空间表示`

## 📋 核心要点

1. 现有测试时缩放（TTS）方法相互独立，忽略了LLM在推理过程中持续学习和优化缩放策略的能力。
2. LatentEvolve模拟人脑的互补学习系统，通过“白天缩放”和“夜间缩放”交替进化LLM的TTS能力。
3. 实验结果表明，LatentEvolve在多个基准测试和模型上显著优于现有TTS方法，并具有良好的泛化性。

## 📝 摘要（中文）

本文提出了一种名为LatentEvolve的自进化潜在测试时缩放（TTS）框架，旨在使大语言模型（LLM）能够逐步学习如何更有效地进行缩放，从而提升推理能力。该框架受到互补学习系统（CLS）理论的启发，包含两个进化组件：“白天缩放”，快速检索历史潜在表示以更好地指导当前的LLM推理；以及“夜间缩放”，以类似于人脑在睡眠期间巩固经验的方式整合过去的潜在优化。白天和夜间过程的交替促进了LLM TTS的快速和缓慢进化，以完全无监督的方式模拟人类认知动态。在八个基准测试和五个模型骨干上的大量实验表明，LatentEvolve超越了最先进的TTS方法，例如LatentSeek和TTRL，高达13.33％，并表现出卓越的跨领域和跨骨干泛化能力。

## 🔬 方法详解

**问题定义**：现有测试时缩放（TTS）方法通常是独立的，没有充分利用LLM在推理过程中学习和适应的能力。这些方法没有考虑到LLM应该能够随着时间的推移，逐步进化并学会如何更有效地进行缩放，从而提高推理性能。因此，如何让LLM在测试时自适应地学习和优化缩放策略是一个关键问题。

**核心思路**：LatentEvolve的核心思路是模拟人脑的互补学习系统（CLS），将LLM的TTS过程分解为两个阶段：“白天缩放”和“夜间缩放”。“白天缩放”类似于人脑的快速回忆，利用历史潜在表示来指导当前的推理过程；“夜间缩放”则类似于人脑在睡眠期间巩固经验，将过去的潜在优化整合到模型中。通过这两个阶段的交替进行，LLM可以快速且稳定地进化其TTS能力。

**技术框架**：LatentEvolve框架包含两个主要模块：白天缩放模块和夜间缩放模块。白天缩放模块负责在推理过程中快速检索相关的历史潜在表示，并将其融入到当前的推理过程中，以提高推理的准确性。夜间缩放模块则负责在推理过程结束后，对历史潜在表示进行整合和优化，并将优化后的表示用于指导未来的推理过程。这两个模块交替运行，形成一个自进化的TTS系统。

**关键创新**：LatentEvolve的关键创新在于其自进化的学习机制，该机制允许LLM在测试时不断学习和优化其缩放策略。与传统的TTS方法相比，LatentEvolve能够更好地利用历史信息，并能够随着时间的推移不断提高推理性能。此外，LatentEvolve的框架设计灵感来源于人脑的互补学习系统，这使得该方法具有更强的生物学合理性。

**关键设计**：LatentEvolve的具体实现细节包括：如何选择和存储历史潜在表示，如何将历史潜在表示融入到当前的推理过程中，以及如何对历史潜在表示进行整合和优化。这些设计细节直接影响了LatentEvolve的性能。例如，可以使用一个队列来存储最近的潜在表示，并使用注意力机制来选择相关的历史潜在表示。此外，可以使用对比学习或自监督学习等方法来对历史潜在表示进行整合和优化。

## 📊 实验亮点

实验结果表明，LatentEvolve在八个基准测试和五个模型骨干上均取得了显著的性能提升。例如，LatentEvolve在某些任务上超越了最先进的TTS方法LatentSeek和TTRL高达13.33％。此外，LatentEvolve还表现出卓越的跨领域和跨骨干泛化能力，这意味着该方法可以有效地应用于不同的任务和模型。

## 🎯 应用场景

LatentEvolve具有广泛的应用前景，可用于提升各种大语言模型在不同领域的推理能力，例如自然语言处理、机器翻译、问答系统等。该方法尤其适用于需要持续学习和适应的应用场景，例如在线客服、智能助手等。通过不断学习和优化缩放策略，LatentEvolve可以使LLM在这些应用中表现得更加智能和高效。

## 📄 摘要（原文）

> Test-time Scaling (TTS) has been demonstrated to significantly enhance the reasoning capabilities of Large Language Models (LLMs) during the inference phase without altering model parameters. However, existing TTS methods are largely independent, implying that LLMs have not yet evolved to progressively learn how to scale more effectively. With the objective of evolving LLMs to learn ``how to scale test-time computation,'' we propose LatentEvolve, a self-evolving latent TTS framework inspired by the complementary learning system (CLS) theory. Analogous to the human brain's dual system of a fast-recall hippocampus and a slow-consolidating neocortex, LatentEvolve comprises two evolutionary components: \textit{daytime scaling}, which rapidly retrieves historical latent representations to better guide current LLM reasoning; and \textit{nighttime scaling}, which integrates past latent optimizations in a manner akin to the human brain's consolidation of experiences during sleep. The alternation of daytime and nighttime processes facilitates a fast and slow evolution of LLM TTS, mirroring human cognitive dynamics in a fully unsupervised manner. Extensive experiments across eight benchmarks and five model backbones demonstrate that our LatentEvolve surpasses state-of-the-art TTS methods such as LatentSeek and TTRL by up to $13.33\%$ and exhibits exceptional cross-domain and cross-backbone generalization.

