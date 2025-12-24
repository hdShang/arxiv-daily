---
layout: default
title: "CAMERA: Multi-Matrix Joint Compression for MoE Models via Micro-Expert Redundancy Analysis"
---

# CAMERA: Multi-Matrix Joint Compression for MoE Models via Micro-Expert Redundancy Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02322" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02322v4</a>
  <a href="https://arxiv.org/pdf/2508.02322.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02322v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02322v4', 'CAMERA: Multi-Matrix Joint Compression for MoE Models via Micro-Expert Redundancy Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuzhuang Xu, Xu Han, Yuanchi Zhang, Yixuan Wang, Yijun Liu, Shiyu Ji, Qingfu Zhu, Wanxiang Che

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-04 (更新: 2025-11-26)

**备注**: Accepted in AAAI 2026

---

## 💡 一句话要点

**提出CAMERA框架以解决MoE模型的冗余压缩问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家` `模型压缩` `微专家` `剪枝` `量化` `大型语言模型` `计算效率`

## 📋 核心要点

1. 现有MoE模型在参数增长时性能提升不成比例，且面临计算和存储开销大等挑战。
2. 本文提出微专家作为更细粒度的压缩单元，建立CAMERA框架以识别微专家冗余，提升模型效率。
3. 在九个下游任务中，CAMERA-P在剪枝比20%至60%下均优于基线，CAMERA-Q在2位量化下表现优异。

## 📝 摘要（中文）

大型语言模型（LLMs）采用混合专家（MoE）架构，虽然在多任务上表现出色，但面临显著的计算和存储开销。现有方法在专家级别的剪枝、合并或分解上存在性能和计算效率的挑战。本文提出CAMERA框架，通过微专家冗余分析，识别微专家的贡献差异，进而提出CAMERA-P和CAMERA-Q，分别用于结构化剪枝和混合精度量化。实验表明，CAMERA-P在20%到60%的剪枝比下优于强基线，而CAMERA-Q在2位量化下也表现出色，显著提升了模型效率。

## 🔬 方法详解

**问题定义**：本文旨在解决MoE模型在参数增长时性能提升不成比例的问题，现有方法在剪枝和合并方面存在性能和效率的不足。

**核心思路**：通过引入微专家作为压缩单元，CAMERA框架能够更细致地分析和识别冗余，从而优化模型的计算和存储效率。

**技术框架**：CAMERA框架包括微专家冗余分析、CAMERA-P结构化剪枝和CAMERA-Q混合精度量化三个主要模块，整体流程为：首先进行微专家识别，然后实施剪枝和量化。

**关键创新**：CAMERA框架的核心创新在于微专家的引入，使得冗余分析更加细致，能够在更高的压缩比下保持模型性能，区别于传统的专家级别剪枝方法。

**关键设计**：在CAMERA-P中，剪枝比率设置在20%至60%之间，CAMERA-Q则采用2位量化策略，确保在压缩的同时保持模型的有效性和准确性。实验表明，这些设计显著提升了模型的计算效率。

## 📊 实验亮点

实验结果显示，CAMERA-P在剪枝比20%至60%下均优于强基线，且CAMERA-Q在2位量化下的性能超越现有的矩阵和通道级方法，展现出显著的效率提升。具体而言，CAMERA方法在单个NVIDIA A100-40GB GPU上对Qwen2-57B-A14B的微专家分析耗时不足5分钟。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等，能够有效降低大型语言模型的计算和存储需求，提高其在实际应用中的可用性和效率。未来，CAMERA框架有望推动更多基于MoE架构的模型优化研究。

## 📄 摘要（原文）

> Large Language Models (LLMs) with Mixture-of-Experts (MoE) architectures are distinguished by their strong performance scaling with increasing parameters across a wide range of tasks, yet they also suffer from substantial computational and storage overheads. Notably, the performance gains of MoE models do not scale proportionally with the growth in expert parameters. While prior works attempt to reduce parameters via expert-level pruning, merging, or decomposition, they still suffer from challenges in both performance and computational efficiency. In this paper, we address these challenges by introducing micro-expert as a finer-grained compression unit that spans across matrices. We first establish a more fundamental perspective, viewing MoE layers as mixtures of micro-experts, and present CAMERA, a lightweight and training-free framework for identifying micro-expert redundancy. Our analysis uncovers significant variance in micro-expert contributions during decoding. Based on this insight, we further propose CAMERA-P, a structured micro-expert pruning framework, and CAMERA-Q, a mixed-precision quantization idea designed for micro-experts. Extensive experiments on nine downstream tasks show that CAMERA-P consistently outperforms strong baselines under pruning ratios ranging from 20% to 60%. Furthermore, CAMERA-Q achieves superior results under aggressive 2-bit quantization, surpassing existing matrix- and channel-level ideas. Notably, our method enables complete micro-expert analysis of Qwen2-57B-A14B in less than 5 minutes on a single NVIDIA A100-40GB GPU.

