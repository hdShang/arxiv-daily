---
layout: default
title: "BAQ: Efficient Bit Allocation Quantization for Large Language Models"
---

# BAQ: Efficient Bit Allocation Quantization for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05664" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05664v1</a>
  <a href="https://arxiv.org/pdf/2506.05664.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05664v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05664v1', 'BAQ: Efficient Bit Allocation Quantization for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chao Zhang, Li Wang, Samson Lasaulce, Merouane Debbah

**分类**: cs.LG, cs.CL

**发布日期**: 2025-06-06

**🔗 代码/项目**: [GITHUB](https://github.com/CSU-ModelCompression/BAQ)

---

## 💡 一句话要点

**提出BAQ以优化大语言模型的量化位分配问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化技术` `大语言模型` `Hessian代理` `凸优化` `模型压缩` `敏感性度量`

## 📋 核心要点

1. 现有的量化方法多依赖于均匀位宽分配，未考虑权重对量化噪声的敏感性，导致性能损失。
2. 本文提出了一种基于Hessian代理的敏感性度量的量化位宽分配框架，通过凸优化方法实现精度自适应。
3. 实验结果显示，BAQ在多个大语言模型上均优于GPTQ，困惑度降低幅度可达56倍，展现出良好的性能与复杂度平衡。

## 📝 摘要（中文）

后训练模型量化是一种广泛采用的技术，用于减少大语言模型的内存和计算成本。然而，大多数现有方法依赖于均匀或启发式的位宽分配，未能考虑权重对量化噪声的非均匀敏感性。本文提出了一种基于Hessian代理的敏感性度量的量化位宽分配新框架。通过关键假设，层/组件级损失函数可以明确表示为位宽的函数，从而将位分配问题形式化为一个凸优化任务。实验结果表明，BAQ在相同位宽下在125M到30B参数的大语言模型上，表现出比GPTQ低56倍的困惑度。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型量化过程中位宽分配不均的问题。现有方法通常采用均匀或启发式的位宽分配，未能充分考虑权重对量化噪声的不同敏感性，导致量化损失较大。

**核心思路**：论文提出了一种基于Hessian代理的敏感性度量方法，通过分析层级损失函数与位宽之间的关系，将位分配问题转化为凸优化任务，从而实现精度的自适应分配。

**技术框架**：整体框架包括敏感性度量计算、损失函数构建和凸优化求解三个主要模块。首先计算每层的敏感性，然后构建损失函数，最后通过优化算法求解最优位宽分配。

**关键创新**：最重要的创新在于将量化位宽分配问题形式化为一个凸优化问题，利用Hessian代理来精确度量权重的敏感性。这一方法与传统的均匀分配方法本质上不同，能够更有效地降低量化损失。

**关键设计**：在损失函数设计中，考虑了层级损失与位宽的明确关系，采用了闭式解来实现位宽的自适应分配。此外，算法的复杂度控制得当，使得BAQ能够轻松集成到标准量化流程中。

## 📊 实验亮点

实验结果表明，BAQ在相同位宽下显著优于现有的GPTQ方法，困惑度降低幅度可达56倍，尤其在参数量从125M到30B的大语言模型上表现突出。这一结果验证了BAQ在量化性能上的有效性和优势。

## 🎯 应用场景

该研究的潜在应用场景包括大语言模型的部署与优化，尤其是在资源受限的环境中。通过有效的量化位宽分配，BAQ能够显著降低模型的内存和计算需求，提升模型在实际应用中的可用性和效率。未来，随着大语言模型的广泛应用，该方法可能在多种自然语言处理任务中发挥重要作用。

## 📄 摘要（原文）

> Post-training model quantization is a widely adopted technique for reducing the memory and computational costs of large language models (LLMs). However, most existing methods rely on uniform or heuristic bitwidth assignments, failing to account for the nonuniform sensitivity of weights to quantization noise. In this paper, we propose a novel framework for allocating quantization bitwidths based on sensitivity metrics derived from a Hessian proxy. We make key assumptions, which allow the layer/component-wise loss function to be expressed as an explicit function of the bitwidths. This enables a neat formulation of the bit allocation problem as a convex optimization task, whose closed-form solution adapts precision across weights to minimize the layer-wise quantization loss. Inspecting the solution provides several insights (such as the equal-loss structure), which are then exploited to design the proposed \textbf{BAQ} (Bit Allocation Quantization) algorithm. The proposed algorithm achieves a good trade-off between loss minimization and complexity and allows BAQ to be integrated into standard quantization pipelines with minimal overhead. Experimental results show that BAQ consistently outperforms GPTQ, achieving up to 56$\times$ lower perplexity at the same bitwidth on large language models ranging from 125M to 30B parameters. Leveraging our analytical results derived from solving the optimal bit allocation problem, we also provide a theoretical explanation for the observed gains. All codes of this paper are available at https://github.com/CSU-ModelCompression/BAQ.

