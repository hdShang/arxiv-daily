---
layout: default
title: "MNN-LLM: A Generic Inference Engine for Fast Large Language Model Deployment on Mobile Devices"
---

# MNN-LLM: A Generic Inference Engine for Fast Large Language Model Deployment on Mobile Devices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10443" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10443v1</a>
  <a href="https://arxiv.org/pdf/2506.10443.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10443v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10443v1', 'MNN-LLM: A Generic Inference Engine for Fast Large Language Model Deployment on Mobile Devices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaode Wang, Jingbang Yang, Xinyu Qian, Shiwen Xing, Xiaotang Jiang, Chengfei Lv, Shengyu Zhang

**分类**: cs.LG

**发布日期**: 2025-06-12

**备注**: 7 pages, 5 figures. Published in the Proceedings of the 6th ACM International Conference on Multimedia in Asia Workshops (MMAsia '24 Workshops). The final authenticated version is available at https://dl.acm.org/doi/10.1145/3700410.3702126

**DOI**: [10.1145/3700410.3702126](https://doi.org/10.1145/3700410.3702126)

---

## 💡 一句话要点

**提出MNN-LLM以解决移动设备上大语言模型推理速度慢的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `移动设备` `推理优化` `模型量化` `边缘计算` `混合精度运算` `多核负载均衡`

## 📋 核心要点

1. 现有大语言模型在移动设备上的推理速度慢且内存消耗大，限制了其实际应用。
2. MNN-LLM框架通过模型量化和混合存储等技术，优化了大语言模型在移动设备上的部署。
3. 实验结果表明，MNN-LLM在推理速度上相比主流框架提升了8.6倍，显著提高了性能。

## 📝 摘要（中文）

大语言模型（LLMs）在多种任务中表现出色，但其庞大的规模导致推理时消耗大量计算资源，成本高昂。因此，边缘设备推理成为一种有前景的解决方案。本文提出了MNN-LLM框架，旨在加速大语言模型在移动设备上的部署。MNN-LLM通过模型量化和DRAM-Flash混合存储来降低内存使用，并根据移动CPU指令集和GPU特性重新排列权重和输入，同时采用多核负载均衡、混合精度浮点运算和几何计算等策略来提升性能。值得注意的是，MNN-LLM相比当前主流的LLM专用框架实现了高达8.6倍的速度提升。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在移动设备上推理时的速度慢和内存消耗大的问题。现有方法在资源受限的边缘设备上表现不佳，导致应用受限。

**核心思路**：MNN-LLM通过模型量化和DRAM-Flash混合存储来降低内存使用，同时优化计算过程以提高推理速度。该设计旨在充分利用移动设备的硬件特性。

**技术框架**：MNN-LLM的整体架构包括模型量化模块、存储管理模块和推理优化模块。模型量化模块负责减少模型大小，存储管理模块优化数据存取，推理优化模块则通过多核负载均衡和混合精度运算提升计算效率。

**关键创新**：MNN-LLM的主要创新在于其针对移动设备特性进行的权重和输入重排，以及采用混合精度运算和几何计算策略，这些设计显著提升了推理性能。

**关键设计**：在参数设置上，MNN-LLM采用了适应移动CPU和GPU的指令集，优化了内存访问模式，并在多核处理上实现了负载均衡，以确保高效的推理过程。

## 📊 实验亮点

MNN-LLM在实验中实现了高达8.6倍的速度提升，相比于当前主流的LLM专用框架，显著提高了推理效率。这一结果表明，MNN-LLM在移动设备上的应用潜力巨大，能够有效解决大语言模型的性能瓶颈。

## 🎯 应用场景

MNN-LLM框架的潜在应用领域包括移动智能设备、边缘计算和实时自然语言处理等场景。其高效的推理能力使得大语言模型能够在资源受限的环境中运行，推动了智能助手、聊天机器人等应用的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated exceptional performance across a variety of tasks. However, their substantial scale leads to significant computational resource consumption during inference, resulting in high costs. Consequently, edge device inference presents a promising solution. The primary challenges of edge inference include memory usage and inference speed. This paper introduces MNN-LLM, a framework specifically designed to accelerate the deployment of large language models on mobile devices. MNN-LLM addresses the runtime characteristics of LLMs through model quantization and DRAM-Flash hybrid storage, effectively reducing memory usage. It rearranges weights and inputs based on mobile CPU instruction sets and GPU characteristics while employing strategies such as multicore load balancing, mixed-precision floating-point operations, and geometric computations to enhance performance. Notably, MNN-LLM achieves up to a 8.6x speed increase compared to current mainstream LLM-specific frameworks.

