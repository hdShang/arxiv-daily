---
layout: default
title: "ProfilingAgent: Profiling-Guided Agentic Reasoning for Adaptive Model Optimization"
---

# ProfilingAgent: Profiling-Guided Agentic Reasoning for Adaptive Model Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05584" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05584v1</a>
  <a href="https://arxiv.org/pdf/2509.05584.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05584v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05584v1', 'ProfilingAgent: Profiling-Guided Agentic Reasoning for Adaptive Model Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sadegh Jafari, Aishwarya Sarkar, Mohiuddin Bilwal, Ali Jannesari

**分类**: cs.LG, cs.CV, cs.PF

**发布日期**: 2025-09-06

**备注**: 13 pages, 3 figures, 5 tables, 1 algorithm

---

## 💡 一句话要点

**ProfilingAgent：利用Profiling引导的Agentic推理实现自适应模型优化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型压缩` `大型语言模型` `Profiling` `剪枝` `量化` `自适应优化` `Agentic推理`

## 📋 核心要点

1. 现有模型压缩方法依赖于统一启发式策略，忽略了架构和运行时异构性，导致优化效果受限。
2. ProfilingAgent利用大型语言模型作为Agent，根据Profiling数据进行推理，自适应地进行模型剪枝和量化。
3. 实验表明，ProfilingAgent在保持或提升模型精度的同时，显著降低了内存占用和推理延迟。

## 📝 摘要（中文）

基础模型面临着日益增长的计算和内存瓶颈，阻碍了其在资源受限平台上的部署。虽然剪枝和量化等压缩技术被广泛使用，但大多数都依赖于忽略架构和运行时异构性的统一启发式方法。Profiling工具可以暴露每层的延迟、内存和计算成本，但很少被集成到自动化流程中。我们提出了ProfilingAgent，一种Profiling引导的、基于Agentic的方法，它使用大型语言模型（LLM）通过结构化剪枝和训练后动态量化来自动化压缩。我们的模块化多Agent系统对静态指标（MACs、参数计数）和动态信号（延迟、内存）进行推理，以设计特定于架构的策略。与启发式基线不同，ProfilingAgent根据瓶颈定制逐层决策。在ImageNet-1K、CIFAR-10和CIFAR-100上，使用ResNet-101、ViT-B/16、Swin-B和DeiT-B/16进行的实验表明，剪枝保持了有竞争力的或改进的准确性（ImageNet-1K上约1%的下降，较小数据集上ViT-B/16的+2%的增益），而量化实现了高达74%的内存节省，且准确率损失小于0.5%。我们的量化还实现了高达1.74倍的一致推理加速。与GPT-4o和GPT-4-Turbo的对比研究突出了LLM推理质量对于迭代剪枝的重要性。这些结果表明，Agentic系统是用于Profiling引导的模型优化的可扩展解决方案。

## 🔬 方法详解

**问题定义**：现有模型压缩方法，如剪枝和量化，通常采用统一的启发式策略，无法充分利用不同模型架构和运行时环境的异构性。这导致压缩后的模型在精度、内存占用和推理速度方面无法达到最优。

**核心思路**：ProfilingAgent的核心思路是利用大型语言模型（LLM）作为智能Agent，根据Profiling工具提供的模型各层延迟、内存和计算成本等信息，进行推理和决策，从而自适应地进行模型压缩。通过这种方式，可以针对不同的模型架构和运行时环境，定制最优的压缩策略。

**技术框架**：ProfilingAgent是一个模块化的多Agent系统，主要包含以下几个阶段：1) Profiling：使用Profiling工具收集模型各层的延迟、内存和计算成本等信息。2) Reasoning：LLM Agent根据Profiling数据和模型架构信息，进行推理，制定剪枝和量化策略。3) Compression：根据Agent制定的策略，对模型进行剪枝和量化。4) Evaluation：评估压缩后模型的精度、内存占用和推理速度。5) Iteration：根据评估结果，迭代优化剪枝和量化策略。

**关键创新**：ProfilingAgent的关键创新在于将大型语言模型引入到模型压缩流程中，利用其强大的推理能力，根据Profiling数据自适应地进行模型优化。与传统的启发式方法相比，ProfilingAgent能够更好地利用模型架构和运行时环境的异构性，从而获得更好的压缩效果。

**关键设计**：ProfilingAgent的关键设计包括：1) 使用结构化剪枝，避免破坏模型的结构。2) 使用训练后动态量化，降低量化带来的精度损失。3) 设计合适的Prompt，引导LLM Agent进行有效的推理和决策。4) 设计合适的奖励函数，指导Agent进行迭代优化。

## 📊 实验亮点

实验结果表明，ProfilingAgent在ImageNet-1K数据集上，使用ResNet-101进行剪枝，精度下降约1%。在较小数据集上，使用ViT-B/16进行剪枝，精度提升2%。量化方面，ProfilingAgent实现了高达74%的内存节省，且精度损失小于0.5%。同时，量化还带来了高达1.74倍的推理速度提升。与GPT-4o和GPT-4-Turbo的对比研究表明，LLM的推理质量对迭代剪枝至关重要。

## 🎯 应用场景

ProfilingAgent可应用于各种需要模型压缩的场景，例如移动设备、嵌入式系统和边缘计算等。通过自适应地优化模型，ProfilingAgent可以降低模型的内存占用和计算复杂度，从而使其能够在资源受限的平台上高效运行。该研究对于推动深度学习模型在实际应用中的部署具有重要意义。

## 📄 摘要（原文）

> Foundation models face growing compute and memory bottlenecks, hindering deployment on resource-limited platforms. While compression techniques such as pruning and quantization are widely used, most rely on uniform heuristics that ignore architectural and runtime heterogeneity. Profiling tools expose per-layer latency, memory, and compute cost, yet are rarely integrated into automated pipelines. We propose ProfilingAgent, a profiling-guided, agentic approach that uses large language models (LLMs) to automate compression via structured pruning and post-training dynamic quantization. Our modular multi-agent system reasons over static metrics (MACs, parameter counts) and dynamic signals (latency, memory) to design architecture-specific strategies. Unlike heuristic baselines, ProfilingAgent tailors layer-wise decisions to bottlenecks. Experiments on ImageNet-1K, CIFAR-10, and CIFAR-100 with ResNet-101, ViT-B/16, Swin-B, and DeiT-B/16 show pruning maintains competitive or improved accuracy (about 1% drop on ImageNet-1K, +2% gains for ViT-B/16 on smaller datasets), while quantization achieves up to 74% memory savings with <0.5% accuracy loss. Our quantization also yields consistent inference speedups of up to 1.74 times faster. Comparative studies with GPT-4o and GPT-4-Turbo highlight the importance of LLM reasoning quality for iterative pruning. These results establish agentic systems as scalable solutions for profiling-guided model optimization.

