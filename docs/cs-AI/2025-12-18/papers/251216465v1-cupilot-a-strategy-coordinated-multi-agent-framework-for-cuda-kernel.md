---
layout: default
title: cuPilot: A Strategy-Coordinated Multi-agent Framework for CUDA Kernel Evolution
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

**关键词**: `CUDA内核优化` `多智能体系统` `进化算法` `大型语言模型` `高性能计算`

## 📋 核心要点

1. 现有CUDA内核自动优化方法在智能体设计和演化表示上存在不足，导致性能受限。
2. cuPilot提出策略协调的多智能体框架，将策略作为内核演化的中间语义表示，解决上述问题。
3. 实验表明，cuPilot生成的内核在多个基准测试中显著优于PyTorch，并实现了硬件资源的高效利用。

## 📝 摘要（中文）

优化CUDA内核是一项具有挑战性且劳动密集型的工作，需要软硬件协同设计专业知识和高性能内核库的专有性质。虽然最近的大型语言模型（LLM）与进化算法相结合在自动内核优化方面显示出希望，但由于其次优的智能体设计和不匹配的演化表示，现有方法通常在性能方面表现不佳。这项工作识别了这些不匹配之处，并提出了cuPilot，一个策略协调的多智能体框架，它引入策略作为内核演化的中间语义表示。主要贡献包括策略协调的进化算法、屋顶线引导的提示和策略级别的种群初始化。实验结果表明，cuPilot生成的内核在100个内核的基准测试中，相对于PyTorch实现了平均3.09倍的加速。在GEMM任务上，cuPilot展示了复杂的优化，并实现了关键硬件单元的高利用率。生成的内核已在https://github.com/champloo2878/cuPilot-Kernels.git上开源。

## 🔬 方法详解

**问题定义**：CUDA内核优化需要专业的软硬件协同设计知识，且高性能内核库具有专有性，导致优化过程耗时耗力。现有基于LLM和进化算法的方法，由于智能体设计不佳和演化表示不匹配，难以达到理想的优化效果。

**核心思路**：cuPilot的核心思路是将内核优化过程分解为一系列策略，并设计多智能体协同完成这些策略。通过引入“策略”这一中间语义表示，弥合了LLM生成代码与硬件性能之间的鸿沟，从而实现更有效的内核演化。

**技术框架**：cuPilot框架包含以下主要模块：1) 策略协调的进化算法：负责整体的演化流程，协调多个智能体的行为。2) 屋顶线引导的提示：利用屋顶线模型指导LLM生成更优的内核代码。3) 策略级别的种群初始化：通过策略指导初始化种群，加速演化过程。整体流程是从初始种群开始，通过策略指导的变异和交叉，生成新的内核代码，并根据性能反馈不断优化。

**关键创新**：cuPilot的关键创新在于引入了“策略”作为内核演化的中间语义表示。与直接生成内核代码相比，策略更易于理解和控制，也更符合人类专家的优化思路。此外，策略协调的多智能体框架能够更好地探索搜索空间，找到更优的内核配置。

**关键设计**：策略协调的进化算法是cuPilot的核心。具体而言，每个智能体负责一种特定的优化策略，例如循环展开、数据重排等。智能体之间通过共享信息和协同工作，共同完成内核优化任务。屋顶线引导的提示利用硬件性能模型，指导LLM生成更符合硬件特性的代码。策略级别的种群初始化则利用专家知识，加速演化过程。

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

实验结果表明，cuPilot在100个内核的基准测试中，相对于PyTorch实现了平均3.09倍的加速。在GEMM任务上，cuPilot展示了复杂的优化，并实现了关键硬件单元的高利用率。这些结果表明，cuPilot能够有效地优化CUDA内核，并显著提高程序性能。

## 🎯 应用场景

cuPilot可应用于各种需要高性能计算的领域，如深度学习、科学计算、图像处理等。它可以帮助开发者自动优化CUDA内核，提高程序运行效率，降低开发成本。该研究的成果有助于推动高性能计算的普及和发展，并为未来的自动内核优化研究提供新的思路。

## 📄 摘要（原文）

> Optimizing CUDA kernels is a challenging and labor-intensive task, given the need for hardware-software co-design expertise and the proprietary nature of high-performance kernel libraries. While recent large language models (LLMs) combined with evolutionary algorithms show promise in automatic kernel optimization, existing approaches often fall short in performance due to their suboptimal agent designs and mismatched evolution representations. This work identifies these mismatches and proposes cuPilot, a strategy-coordinated multi-agent framework that introduces strategy as an intermediate semantic representation for kernel evolution. Key contributions include a strategy-coordinated evolution algorithm, roofline-guided prompting, and strategy-level population initialization. Experimental results show that the generated kernels by cuPilot achieve an average speed up of 3.09$\times$ over PyTorch on a benchmark of 100 kernels. On the GEMM tasks, cuPilot showcases sophisticated optimizations and achieves high utilization of critical hardware units. The generated kernels are open-sourced at https://github.com/champloo2878/cuPilot-Kernels.git.

