---
layout: default
title: Harnessing On-Device Large Language Model: Empirical Results and Implications for AI PC
---

# Harnessing On-Device Large Language Model: Empirical Results and Implications for AI PC

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.15030" class="toolbar-btn" target="_blank">📄 arXiv: 2505.15030v3</a>
  <a href="https://arxiv.org/pdf/2505.15030.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.15030v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.15030v3', 'Harnessing On-Device Large Language Model: Empirical Results and Implications for AI PC')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingyu Song, Peiyu Liao, Wenqian Zhao, Yiwen Wang, Shoubo Hu, Hui-Ling Zhen, Ning Jiang, Mingxuan Yuan

**分类**: cs.LG

**发布日期**: 2025-05-21 (更新: 2025-06-07)

**备注**: 18 pages, 14 figures

**🔗 代码/项目**: [GITHUB](https://github.com/simmonssong/LLMOnDevice)

---

## 💡 一句话要点

**提出系统化方法评估边缘设备上的大型语言模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `边缘计算` `量化方法` `性能评估` `隐私保护`

## 📋 核心要点

1. 现有的边缘设备上大型语言模型面临性能限制，主要由于模型容量和压缩技术的不足。
2. 本文提出了一种系统化的方法论，综合考虑模型能力、开发效率和系统资源，以评估和优化边缘设备上的LLMs。
3. 实验结果显示，系统级指标与有效比特每权重近似线性关系，低BPW量化在准确度损失小的情况下实现显著内存节省。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在边缘设备上的日益部署，隐私保护的优势愈加明显。然而，这些设备上的LLMs由于模型容量受限和压缩技术的必要性，面临性能限制。为此，本文提出了一种系统化的方法论，涵盖模型能力、开发效率和系统资源，以评估边缘设备上的LLMs。通过对0.5B至14B参数模型及七种后训练量化（PTQ）方法的综合评估，我们获得了若干关键见解，包括系统级指标与有效比特每权重（BPW）近似线性扩展、约3.5有效BPW的实用阈值，以及低BPW量化带来的边际准确度损失与显著内存节省。这些发现为资源受限的边缘设备上LLMs的高效部署和优化配置提供了重要指导。

## 🔬 方法详解

**问题定义**：本文旨在解决边缘设备上大型语言模型性能受限的问题，现有方法在模型容量和压缩技术上存在不足，导致无法充分发挥LLMs的潜力。

**核心思路**：提出一种系统化的评估方法，涵盖模型能力、开发效率和系统资源，旨在为边缘设备上的LLMs提供有效的配置和优化指导。

**技术框架**：整体架构包括模型评估、量化方法选择和系统资源分析三个主要模块。首先评估不同参数规模模型的性能，然后选择合适的后训练量化方法，最后分析系统资源的使用情况。

**关键创新**：最重要的创新点在于发现了有效比特每权重（BPW）与系统级指标之间的近线性关系，并提出了约3.5有效BPW的实用阈值，这与现有方法的经验法则有显著区别。

**关键设计**：在实验中，采用了七种后训练量化方法，重点关注低BPW量化对模型性能的影响，确保在内存节省的同时，尽量减少准确度损失。

## 📊 实验亮点

实验结果表明，系统级指标与有效比特每权重（BPW）之间存在近线性关系，且在约3.5有效BPW的阈值下，大模型在低比特量化下的表现优于小模型。低BPW量化方法实现了边际准确度损失的同时，显著节省了内存，提供了有效的资源利用方案。

## 🎯 应用场景

该研究的潜在应用领域包括智能手机、物联网设备和其他资源受限的边缘计算环境。通过优化大型语言模型的配置，可以在保证隐私的前提下，提升用户体验和应用性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The increasing deployment of Large Language Models (LLMs) on edge devices, driven by model advancements and hardware improvements, offers significant privacy benefits. However, these on-device LLMs inherently face performance limitations due to reduced model capacity and necessary compression techniques. To address this, we introduce a systematic methodology -- encompassing model capability, development efficiency, and system resources -- for evaluating on-device LLMs. Our comprehensive evaluation, encompassing models from 0.5B to 14B parameters and seven post-training quantization (PTQ) methods on commodity laptops, yields several critical insights: 1) System-level metrics exhibit near-linear scaling with effective bits-per-weight (BPW). 2) A practical threshold exists around $\sim$3.5 effective BPW, larger models subjected to low-bit quantization consistently outperform smaller models utilizing higher bit-precision. 3) Quantization with low BPW incurs marginal accuracy loss but significant memory savings. 4) Determined by low-level implementation specifics power consumption on CPU, where computation-intensive operations spend more power than memory-intensive ones. These findings offer crucial insights and practical guidelines for the efficient deployment and optimized configuration of LLMs on resource-constrained edge devices. Our codebase is available at https://github.com/simmonssong/LLMOnDevice.

