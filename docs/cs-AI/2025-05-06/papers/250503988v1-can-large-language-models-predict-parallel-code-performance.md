---
layout: default
title: Can Large Language Models Predict Parallel Code Performance?
---

# Can Large Language Models Predict Parallel Code Performance?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03988" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03988v1</a>
  <a href="https://arxiv.org/pdf/2505.03988.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03988v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03988v1', 'Can Large Language Models Predict Parallel Code Performance?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gregory Bolet, Giorgis Georgakoudis, Harshitha Menon, Konstantinos Parasyris, Niranjan Hasabnis, Hayden Estes, Kirk W. Cameron, Gal Oren

**分类**: cs.DC, cs.AI, cs.PF

**发布日期**: 2025-05-06

**备注**: 5 pages, 4 figures, accepted to AI4Sys Workshop at HPDC 2025

---

## 💡 一句话要点

**利用大型语言模型预测并行代码性能以解决GPU性能评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `GPU性能预测` `屋顶线模型` `并行计算` `高性能计算` `性能分析` `代码优化`

## 📋 核心要点

1. 现有的GPU性能评估方法依赖于硬件执行时间分析，限制了高端GPU的访问。
2. 本文提出利用大型语言模型进行GPU内核的性能预测，将问题视为屋顶线分类任务。
3. 实验结果显示，LLMs在提供分析数据时达到100%准确率，推理能力强的模型在无分析信息下也能取得64%的准确率。

## 📝 摘要（中文）

准确评估并行GPU代码的性能通常需要在目标硬件上进行执行时间分析，这在高端GPU访问受限的情况下变得越来越困难。本文探讨了大型语言模型（LLMs）是否可以提供一种不依赖硬件的GPU性能预测替代方法。我们将问题框定为屋顶线分类任务：给定GPU内核的源代码和目标GPU的硬件规格，LLM能否预测该内核是计算受限还是带宽受限。我们构建了一个包含340个GPU内核的平衡数据集，并在四种场景下评估LLMs的表现。结果表明，最先进的LLMs在提供明确的分析数据时能够达到100%的分类准确率，并且具有推理能力的LLMs在零样本和少样本设置中显著优于标准LLMs，最高可达64%的准确率。最后，我们发现LLM的微调需要比目前可用的数据更多。此研究为源级屋顶线性能预测提供了新的视角，展示了LLMs在运行时分析不可行时的优化潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决并行GPU代码性能评估的难题，现有方法依赖于硬件执行时间分析，限制了其适用性和可访问性。

**核心思路**：通过将GPU内核的源代码和目标GPU的硬件规格输入大型语言模型，预测内核的计算特性（计算受限或带宽受限），从而避免硬件依赖。

**技术框架**：研究构建了一个包含340个GPU内核的平衡数据集，评估了LLMs在四种不同场景下的表现，包括使用分析数据、零样本、少样本和微调。

**关键创新**：本研究是首次将LLMs应用于源级屋顶线性能预测，通过分类任务展示了其在缺乏硬件分析时的潜力，与传统方法相比具有更高的灵活性和可扩展性。

**关键设计**：在实验中，使用了明确的分析数据进行训练，推理能力强的LLMs在零样本和少样本设置中表现出色，且微调过程需要更多的数据支持。实验设计中关注了数据集的平衡性和多样性，以确保模型的泛化能力。

## 📊 实验亮点

实验结果显示，最先进的LLMs在提供明确的分析数据时达到了100%的分类准确率。在零样本和少样本设置中，推理能力强的LLMs在GPU源代码的预测准确率最高可达64%，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括高性能计算（HPC）性能分析和优化，尤其在高端GPU资源有限的情况下。通过利用LLMs进行性能预测，开发者可以更有效地指导代码优化，提升并行计算的性能和可移植性。未来，随着数据集和提示策略的改进，LLMs可能成为HPC领域的重要工具。

## 📄 摘要（原文）

> Accurate determination of the performance of parallel GPU code typically requires execution-time profiling on target hardware -- an increasingly prohibitive step due to limited access to high-end GPUs. This paper explores whether Large Language Models (LLMs) can offer an alternative approach for GPU performance prediction without relying on hardware. We frame the problem as a roofline classification task: given the source code of a GPU kernel and the hardware specifications of a target GPU, can an LLM predict whether the GPU kernel is compute-bound or bandwidth-bound?
>   For this study, we build a balanced dataset of 340 GPU kernels, obtained from HeCBench benchmark and written in CUDA and OpenMP, along with their ground-truth labels obtained via empirical GPU profiling. We evaluate LLMs across four scenarios: (1) with access to profiling data of the kernel source, (2) zero-shot with source code only, (3) few-shot with code and label pairs, and (4) fine-tuned on a small custom dataset.
>   Our results show that state-of-the-art LLMs have a strong understanding of the Roofline model, achieving 100% classification accuracy when provided with explicit profiling data. We also find that reasoning-capable LLMs significantly outperform standard LLMs in zero- and few-shot settings, achieving up to 64% accuracy on GPU source codes, without profiling information. Lastly, we find that LLM fine-tuning will require much more data than what we currently have available.
>   This work is among the first to use LLMs for source-level roofline performance prediction via classification, and illustrates their potential to guide optimization efforts when runtime profiling is infeasible. Our findings suggest that with better datasets and prompt strategies, LLMs could become practical tools for HPC performance analysis and performance portability.

