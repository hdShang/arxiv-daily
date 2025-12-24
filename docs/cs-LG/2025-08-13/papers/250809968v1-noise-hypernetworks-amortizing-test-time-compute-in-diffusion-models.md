---
layout: default
title: "Noise Hypernetworks: Amortizing Test-Time Compute in Diffusion Models"
---

# Noise Hypernetworks: Amortizing Test-Time Compute in Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09968" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09968v1</a>
  <a href="https://arxiv.org/pdf/2508.09968.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09968v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09968v1', 'Noise Hypernetworks: Amortizing Test-Time Compute in Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luca Eyring, Shyamgopal Karthik, Alexey Dosovitskiy, Nataniel Ruiz, Zeynep Akata

**分类**: cs.LG, cs.CV

**发布日期**: 2025-08-13

**备注**: Project page: https://noisehypernetworks.github.io/

**🔗 代码/项目**: [GITHUB](https://github.com/ExplainableML/HyperNoise)

---

## 💡 一句话要点

**提出噪声超网络以解决扩散模型推理效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `噪声超网络` `扩散模型` `测试时间扩展` `计算效率` `生成模型`

## 📋 核心要点

1. 现有的测试时间扩展方法在推理过程中显著增加了计算时间，导致效率低下，限制了其在实际应用中的可行性。
2. 本文提出了一种噪声超网络，通过调节初始输入噪声来整合测试时间扩展知识，从而减少推理过程中的计算开销。
3. 实验结果表明，该方法在保持模型质量的同时，计算成本显著降低，恢复了大部分显式测试时间优化带来的质量提升。

## 📝 摘要（中文）

测试时间扩展的新范式在大型语言模型和生成视觉模型中取得了显著突破，允许模型在推理过程中分配额外计算以应对复杂问题。然而，这种方法的一个重要限制是计算时间的大幅增加，使得过程在许多应用中变得缓慢且不切实际。为了解决这一问题，本文提出了一种将测试时间扩展知识集成到模型中的解决方案，具体是用噪声超网络替代扩散模型中的奖励引导噪声优化。我们提出了一个理论基础的框架，通过可处理的噪声空间目标来学习奖励倾斜分布，从而在保持基础模型保真度的同时优化所需特性。我们的研究表明，该方法在显著降低计算成本的同时，恢复了显著的质量提升。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散模型在推理过程中因测试时间扩展而导致的计算效率低下问题。现有方法在提升模型性能的同时，显著增加了推理时间，使得实际应用受到限制。

**核心思路**：论文的核心思路是通过引入噪声超网络来替代传统的奖励引导噪声优化，从而在后训练阶段有效整合测试时间扩展的知识，减少推理时的计算开销。

**技术框架**：整体架构包括噪声超网络模块，该模块负责调节输入噪声，并通过一个理论基础的框架来学习奖励倾斜分布。该框架确保在优化过程中保持基础模型的保真度，同时实现所需特性。

**关键创新**：最重要的技术创新在于引入噪声超网络，替代了传统的噪声优化方法。这一设计使得模型能够在推理时动态调整噪声，显著降低了计算成本。

**关键设计**：关键设计包括噪声空间目标的构建，该目标在训练过程中通过特定的损失函数进行优化，以确保模型在推理时能够有效利用学习到的知识。

## 📊 实验亮点

实验结果显示，采用噪声超网络的方法在保持模型质量的同时，计算成本降低了显著比例。与传统的显式测试时间优化相比，该方法恢复了大部分质量提升，且推理速度更快，适用于更广泛的应用场景。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理等需要高效推理的生成模型。通过减少推理过程中的计算开销，本文的方法可以使得复杂模型在实时应用中变得更加可行，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The new paradigm of test-time scaling has yielded remarkable breakthroughs in Large Language Models (LLMs) (e.g. reasoning models) and in generative vision models, allowing models to allocate additional computation during inference to effectively tackle increasingly complex problems. Despite the improvements of this approach, an important limitation emerges: the substantial increase in computation time makes the process slow and impractical for many applications. Given the success of this paradigm and its growing usage, we seek to preserve its benefits while eschewing the inference overhead. In this work we propose one solution to the critical problem of integrating test-time scaling knowledge into a model during post-training. Specifically, we replace reward guided test-time noise optimization in diffusion models with a Noise Hypernetwork that modulates initial input noise. We propose a theoretically grounded framework for learning this reward-tilted distribution for distilled generators, through a tractable noise-space objective that maintains fidelity to the base model while optimizing for desired characteristics. We show that our approach recovers a substantial portion of the quality gains from explicit test-time optimization at a fraction of the computational cost. Code is available at https://github.com/ExplainableML/HyperNoise

