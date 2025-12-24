---
layout: default
title: "Accelerating Diffusion Large Language Models with SlowFast Sampling: The Three Golden Principles"
---

# Accelerating Diffusion Large Language Models with SlowFast Sampling: The Three Golden Principles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10848" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10848v2</a>
  <a href="https://arxiv.org/pdf/2506.10848.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10848v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10848v2', 'Accelerating Diffusion Large Language Models with SlowFast Sampling: The Three Golden Principles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingyan Wei, Yaojie Zhang, Zhiyuan Liu, Dongrui Liu, Linfeng Zhang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-12 (更新: 2025-06-13)

**备注**: 11 pages; 5 figures;

---

## 💡 一句话要点

**提出SlowFast采样以解决扩散语言模型的效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散语言模型` `动态采样` `加速解码` `自然语言处理` `高效生成`

## 📋 核心要点

1. 现有的扩散语言模型在采样策略上存在静态行为，导致效率低下和灵活性不足。
2. 本文提出的SlowFast采样策略通过动态切换解码阶段，提升了采样效率和灵活性。
3. 实验结果显示，SlowFast采样在多个基准测试中实现了显著的速度提升，且准确率保持稳定。

## 📝 摘要（中文）

扩散语言模型（dLLMs）作为传统自回归语言模型的有力替代，能够实现并行生成并显著降低推理延迟。然而，现有的采样策略如基于置信度或半自回归解码，常常表现出静态行为，导致效率低下和灵活性不足。本文提出了一种新颖的动态采样策略——SlowFast采样，能够自适应地在探索性和加速解码阶段之间切换。该方法遵循三个黄金原则：确定性原则、收敛原则和位置原则，指导何时何地可以自信且高效地解码令牌。通过与dLLM-Cache的结合，进一步减少冗余计算。大量实验表明，SlowFast采样在LLaDA上实现了最高15.63倍的加速，结合缓存时可达34.22倍，且准确率下降极小。我们的方案在吞吐量上超越了强大的自回归基线LLaMA3 8B，证明了精心设计的采样能够充分释放dLLMs在快速高质量生成中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有扩散语言模型在采样策略上的静态行为问题，这导致了效率低下和灵活性不足。

**核心思路**：提出SlowFast采样策略，通过动态切换探索性和加速解码阶段，优化采样过程，提高生成效率。

**技术框架**：整体架构包括两个主要阶段：探索性解码和加速解码，结合三个黄金原则指导采样过程，并与dLLM-Cache集成以减少冗余计算。

**关键创新**：最重要的创新在于动态采样策略的设计，能够根据当前解码状态自适应调整采样策略，与传统静态方法形成鲜明对比。

**关键设计**：在参数设置上，结合了确定性原则、收敛原则和位置原则，确保在不同阶段的采样效率和准确性，同时采用了适应性缓存机制以进一步提升性能。

## 📊 实验亮点

实验结果显示，SlowFast采样在LLaDA上实现了最高15.63倍的速度提升，结合dLLM-Cache时可达34.22倍，且准确率下降极小。此外，该方法在吞吐量上超越了LLaMA3 8B等强大的自回归基线，展现出显著的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等，能够显著提升生成模型的推理速度和响应能力。未来，随着技术的进一步发展，SlowFast采样有望在更广泛的AI应用中发挥重要作用，推动智能系统的实时交互能力。

## 📄 摘要（原文）

> Diffusion-based language models (dLLMs) have emerged as a promising alternative to traditional autoregressive LLMs by enabling parallel token generation and significantly reducing inference latency. However, existing sampling strategies for dLLMs, such as confidence-based or semi-autoregressive decoding, often suffer from static behavior, leading to suboptimal efficiency and limited flexibility. In this paper, we propose SlowFast Sampling, a novel dynamic sampling strategy that adaptively alternates between exploratory and accelerated decoding stages. Our method is guided by three golden principles: certainty principle, convergence principle, and positional principle, which govern when and where tokens can be confidently and efficiently decoded. We further integrate our strategy with dLLM-Cache to reduce redundant computation. Extensive experiments across benchmarks and models show that SlowFast Sampling achieves up to 15.63$\times$ speedup on LLaDA with minimal accuracy drop, and up to 34.22$\times$ when combined with caching. Notably, our approach outperforms strong autoregressive baselines like LLaMA3 8B in throughput, demonstrating that well-designed sampling can unlock the full potential of dLLMs for fast and high-quality generation.

