---
layout: default
title: Gather-Scatter Mamba: Accelerating Propagation with Efficient State Space Model
---

# Gather-Scatter Mamba: Accelerating Propagation with Efficient State Space Model

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.00862" target="_blank" class="toolbar-btn">arXiv: 2510.00862v1</a>
    <a href="https://arxiv.org/pdf/2510.00862.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00862v1" 
            onclick="toggleFavorite(this, '2510.00862v1', 'Gather-Scatter Mamba: Accelerating Propagation with Efficient State Space Model')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Hyun-kyu Ko, Youbin Kim, Jihyeon Park, Dongheok Park, Gyeongjin Kang, Wonjun Cho, Hyung Yi, Eunbyung Park

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-01

**备注**: Code: \url{https://github.com/Ko-Lani/GSMamba}

**🔗 代码/项目**: [GITHUB](https://github.com/Ko-Lani/GSMamba)

---

## 💡 一句话要点

**提出Gather-Scatter Mamba，结合注意力机制与选择性SSM加速视频超分中的时序传播。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频超分辨率` `状态空间模型` `Mamba` `注意力机制` `时序建模` `特征对齐` `视频处理`

## 📋 核心要点

1. 传统视频超分方法依赖循环架构，但存在梯度消失、并行性差和推理速度慢等问题。
2. 提出Gather-Scatter Mamba (GSM)，结合注意力机制和Mamba，实现高效的时序传播和空间信息聚合。
3. GSM通过对齐感知机制减少遮挡伪影，确保信息在所有帧上的有效重新分配，提升超分效果。

## 📝 摘要（中文）

状态空间模型(SSMs)，尤其是RNNs，在序列建模中扮演着核心角色。尽管Transformer等注意力机制因其建模全局上下文的能力而占据主导地位，但其二次复杂度以及有限的可扩展性使其不太适合长序列。视频超分辨率(VSR)方法传统上依赖于循环架构来跨帧传播特征。然而，这些方法存在梯度消失、缺乏并行性和推理速度慢等问题。最近选择性SSM（如Mamba）的进展提供了一种引人注目的替代方案：通过支持输入相关的状态转移和线性时间复杂度，Mamba缓解了这些问题，同时保持了强大的长程建模能力。尽管如此，由于其因果性质和缺乏显式上下文聚合，Mamba单独使用难以捕捉细粒度的空间依赖性。为了解决这个问题，我们提出了一种混合架构，该架构结合了移位窗口自注意力用于空间上下文聚合，以及基于Mamba的选择性扫描用于高效的时间传播。此外，我们引入了Gather-Scatter Mamba (GSM)，这是一种对齐感知机制，它在Mamba传播之前将特征扭曲到时间窗口内的中心锚帧，然后在之后将其分散回去，从而有效地减少了遮挡伪影，并确保在所有帧上有效重新分配聚合信息。官方实现可在https://github.com/Ko-Lani/GSMamba获取。

## 🔬 方法详解

**问题定义**：视频超分辨率（VSR）旨在从低分辨率视频序列重建高分辨率视频。传统方法依赖于循环神经网络（RNN），但RNN存在梯度消失、缺乏并行性和推理速度慢等问题，限制了其在长视频序列上的应用。此外，现有方法难以有效处理视频中的遮挡问题，导致重建质量下降。

**核心思路**：论文的核心思路是结合Mamba选择性状态空间模型（SSM）和移位窗口自注意力机制，构建一个混合架构。Mamba擅长长程时序建模，而注意力机制擅长捕捉空间依赖性。通过将两者结合，可以克服传统RNN的缺点，并有效处理视频中的遮挡问题。GSM的关键在于对齐感知机制，它将特征扭曲到中心锚帧，减少遮挡的影响，然后再将信息分散回所有帧。

**技术框架**：该方法包含两个主要模块：空间上下文聚合模块和时间传播模块。空间上下文聚合模块使用移位窗口自注意力机制，捕捉帧内的空间依赖性。时间传播模块使用Mamba选择性扫描，对序列进行高效的时序建模。Gather-Scatter Mamba (GSM)机制位于时间传播模块之前和之后，用于对齐和重新分配特征。整体流程是：输入低分辨率视频序列 -> 空间上下文聚合 -> Gather (特征扭曲到中心锚帧) -> Mamba时序传播 -> Scatter (特征分散回所有帧) -> 输出高分辨率视频序列。

**关键创新**：最重要的技术创新点是Gather-Scatter Mamba (GSM)机制。与传统的时序传播方法不同，GSM在传播之前将特征对齐到中心锚帧，减少了遮挡的影响。这种对齐感知机制使得Mamba能够更有效地利用上下文信息，从而提高重建质量。此外，结合Mamba和注意力机制的混合架构也是一个创新点，它充分利用了两种模型的优势。

**关键设计**：GSM的关键设计在于如何选择中心锚帧以及如何进行特征扭曲和分散。论文中选择时间窗口的中心帧作为锚帧。特征扭曲和分散的具体实现细节未知，但可以推测使用了某种可微的变换操作，例如光流估计或可变形卷积。损失函数未知，但通常VSR任务会使用L1或L2损失，以及感知损失和对抗损失。

## 📊 实验亮点

论文提出了Gather-Scatter Mamba (GSM)，一种用于视频超分辨率的新型时序传播方法。实验结果表明，GSM能够有效地减少遮挡伪影，并提高重建质量。具体的性能数据和对比基线未知，但论文强调了GSM在对齐感知方面的优势，这表明该方法在处理具有复杂运动和遮挡的视频序列时具有显著的优势。

## 🎯 应用场景

该研究成果可应用于各种视频处理领域，如视频监控、视频编辑、电影修复和在线视频流媒体。通过提高视频超分辨率的质量和效率，可以改善用户观看体验，并为后续的视频分析任务提供更好的数据基础。该方法在计算资源受限的边缘设备上也有潜在的应用价值。

## 📄 摘要（原文）

> State Space Models (SSMs)-most notably RNNs-have historically played a central role in sequential modeling. Although attention mechanisms such as Transformers have since dominated due to their ability to model global context, their quadratic complexity and limited scalability make them less suited for long sequences. Video super-resolution (VSR) methods have traditionally relied on recurrent architectures to propagate features across frames. However, such approaches suffer from well-known issues including vanishing gradients, lack of parallelism, and slow inference speed. Recent advances in selective SSMs like Mamba offer a compelling alternative: by enabling input-dependent state transitions with linear-time complexity, Mamba mitigates these issues while maintaining strong long-range modeling capabilities. Despite this potential, Mamba alone struggles to capture fine-grained spatial dependencies due to its causal nature and lack of explicit context aggregation. To address this, we propose a hybrid architecture that combines shifted window self-attention for spatial context aggregation with Mamba-based selective scanning for efficient temporal propagation. Furthermore, we introduce Gather-Scatter Mamba (GSM), an alignment-aware mechanism that warps features toward a center anchor frame within the temporal window before Mamba propagation and scatters them back afterward, effectively reducing occlusion artifacts and ensuring effective redistribution of aggregated information across all frames. The official implementation is provided at: https://github.com/Ko-Lani/GSMamba.

