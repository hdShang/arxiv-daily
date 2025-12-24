---
layout: default
title: "FSA: An Alternative Efficient Implementation of Native Sparse Attention Kernel"
---

# FSA: An Alternative Efficient Implementation of Native Sparse Attention Kernel

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18224" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18224v2</a>
  <a href="https://arxiv.org/pdf/2508.18224.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18224v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18224v2', 'FSA: An Alternative Efficient Implementation of Native Sparse Attention Kernel')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ran Yan, Youhe Jiang, Zhuoming Chen, Haohui Mai, Beidi Chen, Binhang Yuan

**分类**: cs.DC, cs.LG

**发布日期**: 2025-08-25 (更新: 2025-10-13)

**🔗 代码/项目**: [GITHUB](https://github.com/Relaxed-System-Lab/Flash-Sparse-Attention)

---

## 💡 一句话要点

**提出Flash Sparse Attention以解决稀疏注意力核效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏注意力` `大型语言模型` `计算效率` `深度学习` `GPU优化` `自然语言处理` `模型训练` `推理速度`

## 📋 核心要点

1. 现有的原生稀疏注意力方法在查询头数量较少的情况下效率低下，限制了其在大型语言模型中的应用。
2. 本文提出Flash Sparse Attention（FSA），通过改进内核实现，使得稀疏注意力计算在多种流行LLMs中更加高效。
3. 实验结果表明，FSA在内核级延迟上最高可减少3.5倍，端到端训练速度提升最高达1.25倍，生成推理速度提升最高达1.36倍。

## 📝 摘要（中文）

近年来，稀疏注意力机制在大型语言模型（LLMs）的长上下文训练和推理中展现出强大的潜力。原生稀疏注意力（NSA）作为一种先进方法，提供了硬件对齐的稀疏注意力，显著提升了系统性能。然而，NSA的内核实现对查询头数量的限制使得其在现有LLMs中的应用受到限制。本文提出了Flash Sparse Attention（FSA），一种新的内核实现，能够在现代GPU上高效计算，适用于查询头数量较少的多种流行LLMs。与传统NSA内核相比，FSA在内核级延迟、端到端训练速度和生成推理速度上均实现了显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决原生稀疏注意力（NSA）内核实现对查询头数量的限制，导致其在现有大型语言模型（LLMs）中的应用受限。现有方法在查询头数量较少时效率低下，无法充分发挥稀疏注意力的优势。

**核心思路**：本文提出Flash Sparse Attention（FSA），通过优化内核实现，支持在较少查询头的情况下高效计算稀疏注意力，从而提高在现代GPU上的计算效率。

**技术框架**：FSA的整体架构包括多个模块，首先是输入数据的预处理，然后是稀疏注意力计算模块，最后是输出结果的后处理。该框架设计旨在兼容多种流行的LLMs，并优化计算路径以提高效率。

**关键创新**：FSA的主要创新在于其内核实现的灵活性，能够适应不同数量的查询头，从而克服了NSA在查询头数量较少时的性能瓶颈。这一设计使得FSA在多种应用场景中具有更广泛的适用性。

**关键设计**：FSA在参数设置上进行了优化，确保在不同的查询头数量下仍能保持高效的计算性能。此外，损失函数和网络结构经过精心设计，以确保在保持准确性的同时提升计算速度。具体的技术细节包括对内存访问模式的优化和计算并行性的增强。

## 📊 实验亮点

FSA在实验中表现出色，相较于传统的NSA内核实现，内核级延迟最高减少3.5倍，平均减少1.6倍；端到端训练速度提升最高1.25倍，平均提升1.09倍；生成推理的预填充阶段速度提升最高1.36倍，平均提升1.11倍。这些结果表明FSA在性能上具有显著优势。

## 🎯 应用场景

Flash Sparse Attention（FSA）在大型语言模型的训练和推理中具有广泛的应用潜力，尤其是在需要处理长上下文的自然语言处理任务中。其高效的计算能力可以显著降低资源消耗，提高模型的响应速度，适用于实时应用场景，如对话系统和智能助手等。未来，FSA有望推动更多基于稀疏注意力的研究和应用。

## 📄 摘要（原文）

> Recent advance in sparse attention mechanisms has demonstrated strong potential for reducing the computational cost of long-context training and inference in large language models (LLMs). Native Sparse Attention (NSA), one state-of-the-art approach, introduces natively trainable, hardware-aligned sparse attention that delivers substantial system-level performance boost while maintaining accuracy comparable to full attention. However, the kernel implementation of NSA forces a loop order that is only efficient with a relatively large number of query heads in each Grouped Query Attention (GQA) group, whereas existing LLMs widely adopt much smaller number of query heads in each GQA group -- such an inconsistency significantly limits the applicability of this sparse algorithmic advance. In this work, we propose Flash Sparse Attention (FSA), an alternative kernel implementation that enables efficient NSA computation across a wide range of popular LLMs with varied smaller number of heads in each GQA group on modern GPUs. Compared to vanilla NSA kernel implementation, our empirical evaluation demonstrates that FSA achieves (i) up to 3.5x and on average 1.6x kernel-level latency reduction, (ii) up to 1.25x and 1.09x on average end-to-end training speedup on state-of-the-art LLMs, and (iii) up to 1.36x and 1.11x on average for prefill-phase speedup in LLM generative inference. Github Repo at https://github.com/Relaxed-System-Lab/Flash-Sparse-Attention.

