---
layout: default
title: "MAC: A Live Benchmark for Multimodal Large Language Models in Scientific Understanding"
---

# MAC: A Live Benchmark for Multimodal Large Language Models in Scientific Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15802" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15802v1</a>
  <a href="https://arxiv.org/pdf/2508.15802.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15802v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15802v1', 'MAC: A Live Benchmark for Multimodal Large Language Models in Scientific Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohan Jiang, Jin Gao, Jiahao Zhan, Dequan Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-14

**🔗 代码/项目**: [GITHUB](https://github.com/mhjiang0408/MAC_Bench)

---

## 💡 一句话要点

**提出MAC基准以提升多模态大语言模型的科学理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `科学理解` `动态基准` `跨模态推理` `图像-文本对` `DAD方法` `性能提升`

## 📋 核心要点

1. 现有的固定基准无法有效评估多模态大语言模型在科学理解方面的能力，导致评估结果的局限性。
2. 提出了MAC基准，利用大量图像-文本对，旨在挑战MLLMs在科学内容的跨模态推理能力。
3. 实验表明，MLLMs在感知能力上表现良好，但跨模态推理能力有限，DAD方法能够提升其性能达11%。

## 📝 摘要（中文）

随着多模态大语言模型（MLLMs）能力的提升，固定基准逐渐失去在高水平科学理解评估中的有效性。本文提出了多模态学术封面基准（MAC），这是一个能够随着科学进展和模型进步不断演变的动态基准。MAC利用来自顶级科学期刊（如《自然》、《科学》和《细胞》）的超过25,000个图像-文本对，挑战MLLMs在抽象视觉和文本科学内容上的推理能力。实验结果显示，尽管MLLMs在感知能力上表现强劲，但其跨模态科学推理仍然有限。为此，本文提出了DAD，一种轻量级推理时间方法，通过扩展MLLM的视觉特征与语言空间推理相结合，提升性能达11%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有固定基准在评估多模态大语言模型（MLLMs）科学理解能力时的不足，尤其是在跨模态推理方面的局限性。

**核心思路**：提出MAC基准，利用来自顶级科学期刊的图像-文本对，动态更新以适应科学进展，挑战MLLMs的推理能力。同时引入DAD方法，通过结合视觉特征与语言推理，提升模型性能。

**技术框架**：MAC基准包括数据收集、模型评估和动态更新三个主要模块。数据收集阶段从顶级期刊获取图像-文本对，模型评估阶段通过标准化测试评估MLLMs的推理能力，动态更新阶段根据最新科学进展调整基准内容。

**关键创新**：MAC基准的动态特性使其能够与科学前沿保持一致，DAD方法则通过轻量级推理增强了MLLMs的跨模态推理能力，这是与现有静态基准的本质区别。

**关键设计**：在DAD方法中，设计了特定的参数设置和损失函数，以优化视觉特征与语言推理的结合，确保模型在推理时能够有效利用两种模态的信息。具体的网络结构细节尚未公开。

## 📊 实验亮点

实验结果显示，MLLMs在MAC基准上的表现揭示了其在感知能力上的优势，但在跨模态科学推理方面仍显不足。通过DAD方法，模型性能提升达11%，显示出该方法在增强推理能力方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括科学研究、教育和信息检索等。通过提升多模态大语言模型在科学理解方面的能力，MAC基准能够帮助研究人员更好地处理和分析科学文献，促进科学知识的传播与应用，未来可能对科学研究的效率和质量产生深远影响。

## 📄 摘要（原文）

> As multimodal large language models (MLLMs) grow increasingly capable, fixed benchmarks are gradually losing their effectiveness in evaluating high-level scientific understanding. In this paper, we introduce the Multimodal Academic Cover benchmark (MAC), a live benchmark that could continuously evolve with scientific advancement and model progress. MAC leverages over 25,000 image-text pairs sourced from issues of top-tier scientific journals such as Nature, Science, and Cell, challenging MLLMs to reason across abstract visual and textual scientific content. Experiments on our most recent yearly snapshot, MAC-2025, reveal that while MLLMs demonstrate strong perceptual abilities, their cross-modal scientific reasoning remains limited. To bridge this gap, we propose DAD, a lightweight inference-time approach that enhances MLLMs by extending MLLM visual features with language space reasoning, achieving performance improvements of up to 11%. Finally, we highlight the live nature of MAC through experiments on updating journal covers and models for curation, illustrating its potential to remain aligned with the frontier of human knowledge. We release our benchmark at https://github.com/mhjiang0408/MAC_Bench.

