---
layout: default
title: "cuPilot: A Strategy-Coordinated Multi-agent Framework for CUDA Kernel Evolution"
---

# cuPilot: A Strategy-Coordinated Multi-agent Framework for CUDA Kernel Evolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16465" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16465v1</a>
  <a href="https://arxiv.org/pdf/2512.16465.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16465v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16465v1', 'cuPilot: A Strategy-Coordinated Multi-agent Framework for CUDA Kernel Evolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinwu Chen, Qidie Wu, Bin Li, Lin Ma, Xin Si, Yang Hu, Shouyi Yin, Jun Yang

**分类**: cs.AI

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/champloo2878/cuPilot-Kernels.git)

---

## 💡 一句话要点

**cuPilot：一种策略协调的多智能体框架，用于CUDA内核演化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `CUDA内核优化` `多智能体系统` `进化算法` `大型语言模型` `Roofline模型`

## 📋 核心要点

1. 现有CUDA内核优化方法依赖专家知识，且基于LLM的方法存在智能体设计和演化表示不匹配的问题。
2. cuPilot提出策略协调的多智能体框架，将策略作为内核演化的中间语义表示，解决上述不匹配问题。
3. 实验表明，cuPilot生成的内核在多个基准测试中显著优于PyTorch，并在GEMM任务中实现了硬件的高效利用。

## 📝 摘要（中文）

优化CUDA内核是一项具有挑战性且劳动密集型的工作，需要软硬件协同设计专业知识和高性能内核库的专有性质。虽然最近的大型语言模型（LLM）与进化算法相结合在自动内核优化方面显示出希望，但由于其次优的智能体设计和不匹配的演化表示，现有方法通常在性能方面表现不佳。这项工作识别了这些不匹配之处，并提出了cuPilot，一个策略协调的多智能体框架，它引入策略作为内核演化的中间语义表示。主要贡献包括策略协调的进化算法、roofline引导的提示和策略级别的种群初始化。实验结果表明，cuPilot生成的内核在100个内核的基准测试中，平均比PyTorch加速3.09倍。在GEMM任务中，cuPilot展示了复杂的优化，并实现了关键硬件单元的高利用率。生成的内核已在https://github.com/champloo2878/cuPilot-Kernels.git上开源。

## 🔬 方法详解

**问题定义**：CUDA内核优化需要深厚的软硬件协同设计知识，且高性能内核库通常是专有的，导致优化过程耗时且困难。现有基于LLM和进化算法的方法，由于智能体设计不佳和演化表示不匹配，难以达到理想的优化效果。这些方法通常缺乏对CUDA内核优化策略的有效建模和利用。

**核心思路**：cuPilot的核心思路是将CUDA内核优化过程分解为一系列策略，并使用策略作为中间语义表示，从而弥合LLM和内核演化之间的差距。通过策略协调，多个智能体可以协同工作，探索不同的优化方向，并最终生成高性能的CUDA内核。这种方法能够更好地利用LLM的生成能力，并指导内核演化过程。

**技术框架**：cuPilot框架包含以下主要模块：1) 策略协调的进化算法：该算法使用策略作为演化的基本单元，并设计了相应的交叉和变异操作。2) Roofline引导的提示：利用Roofline模型指导LLM生成更有效的优化策略。3) 策略级别的种群初始化：通过预先定义的策略集合初始化种群，加速演化过程。整体流程为：首先，使用Roofline模型分析目标内核的性能瓶颈；然后，根据瓶颈选择合适的优化策略；接着，使用LLM生成相应的CUDA代码；最后，通过进化算法不断优化策略组合，最终生成高性能的CUDA内核。

**关键创新**：cuPilot的关键创新在于引入了策略作为CUDA内核演化的中间语义表示。与直接使用LLM生成CUDA代码相比，cuPilot能够更好地控制优化过程，并利用LLM的知识进行策略选择和代码生成。此外，策略协调的进化算法能够有效地探索不同的优化方向，并找到最优的策略组合。

**关键设计**：Roofline引导的提示机制利用Roofline模型提供的硬件性能上限信息，指导LLM生成更符合硬件特性的优化策略。策略协调的进化算法采用了一种新的交叉和变异操作，能够有效地探索策略空间。策略级别的种群初始化使用预定义的策略集合，加速了演化过程的收敛。具体的参数设置和损失函数等技术细节在论文中进行了详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16465v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16465v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16465v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，cuPilot在100个内核的基准测试中，平均比PyTorch加速3.09倍。在GEMM任务中，cuPilot展示了复杂的优化，并实现了关键硬件单元的高利用率。这些结果表明，cuPilot能够有效地优化CUDA内核，并显著提高应用程序的性能。

## 🎯 应用场景

cuPilot可应用于各种需要高性能CUDA内核的领域，例如深度学习、科学计算和图像处理。它可以帮助开发者自动优化CUDA内核，提高应用程序的性能，并降低开发成本。该研究的成果可以促进高性能计算的发展，并推动人工智能技术的应用。

## 📄 摘要（原文）

> Optimizing CUDA kernels is a challenging and labor-intensive task, given the need for hardware-software co-design expertise and the proprietary nature of high-performance kernel libraries. While recent large language models (LLMs) combined with evolutionary algorithms show promise in automatic kernel optimization, existing approaches often fall short in performance due to their suboptimal agent designs and mismatched evolution representations. This work identifies these mismatches and proposes cuPilot, a strategy-coordinated multi-agent framework that introduces strategy as an intermediate semantic representation for kernel evolution. Key contributions include a strategy-coordinated evolution algorithm, roofline-guided prompting, and strategy-level population initialization. Experimental results show that the generated kernels by cuPilot achieve an average speed up of 3.09$\times$ over PyTorch on a benchmark of 100 kernels. On the GEMM tasks, cuPilot showcases sophisticated optimizations and achieves high utilization of critical hardware units. The generated kernels are open-sourced at https://github.com/champloo2878/cuPilot-Kernels.git.

