---
layout: default
title: SonicMoE: Accelerating MoE with IO and Tile-aware Optimizations
---

# SonicMoE: Accelerating MoE with IO and Tile-aware Optimizations

**arXiv**: [2512.14080v1](https://arxiv.org/abs/2512.14080) | [PDF](https://arxiv.org/pdf/2512.14080.pdf)

**作者**: Wentao Guo, Mayank Mishra, Xinle Cheng, Ion Stoica, Tri Dao

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**SonicMoE通过IO和分块优化加速MoE模型训练**

🎯 **匹配领域**: **人形/双足机器人 (Humanoid & Biped)**

**关键词**: `混合专家模型` `MoE` `模型加速` `GPU优化` `内存优化` `IO优化` `Token Rounding`

## 📋 核心要点

1. 现有细粒度和高稀疏性MoE模型面临激活内存占用大、硬件效率低以及计算浪费等问题。
2. SonicMoE通过内存高效算法、IO与计算重叠的GPU内核以及token rounding方法来解决上述问题。
3. SonicMoE在Hopper GPU上实现了1.86倍的计算吞吐量提升，并减少了45%的激活内存占用。

## 📝 摘要（中文）

混合专家模型(MoE)已成为扩展语言模型的实际架构，且不会显著增加计算成本。最近的MoE模型呈现出高专家粒度（较小的专家中间维度）和更高稀疏性（激活专家数量恒定，但专家总数更多）的趋势，从而提高了每个FLOP的模型质量。然而，细粒度MoE由于更高的IO成本而导致激活内存占用增加和硬件效率降低，而更稀疏的MoE由于分组GEMM内核中的填充而导致计算浪费。为此，我们提出了一种内存高效的算法来计算MoE的前向和后向传递，并最大限度地减少后向传递的激活缓存。我们还设计了GPU内核，将内存IO与计算重叠，从而使所有MoE架构受益。最后，我们提出了一种新颖的“token rounding”方法，该方法最大限度地减少了由于分组GEMM内核中的填充而造成的计算浪费。因此，与ScatterMoE的BF16 MoE内核相比，我们的方法SonicMoE将激活内存减少了45%，并在Hopper GPU上实现了1.86倍的计算吞吐量提升（针对细粒度7B MoE）。具体而言，在64个H100上，SonicMoE实现了每天2130亿token的训练吞吐量，与ScatterMoE在96个H100上使用lm-engine代码库和FSDP-2训练7B MoE模型时实现的每天2250亿token相当。在高MoE稀疏性设置下，与vanilla top-$K$路由相比，我们的tile-aware token rounding算法在内核执行时间上产生了额外的1.16倍加速，同时保持了相似的下游性能。我们开源了所有内核，以实现更快的MoE模型训练。

## 🔬 方法详解

**问题定义**：论文旨在解决MoE模型训练过程中由于高专家粒度和高稀疏性带来的内存占用大、硬件效率低以及计算浪费问题。现有方法，如ScatterMoE，在细粒度MoE中面临IO瓶颈，在高稀疏性MoE中存在由于padding导致的计算浪费。

**核心思路**：论文的核心思路是通过优化内存访问模式、重叠IO与计算以及减少padding带来的计算浪费来提高MoE模型的训练效率。具体来说，通过内存高效的算法减少激活缓存，通过定制的GPU内核重叠IO与计算，并通过token rounding减少padding。

**技术框架**：SonicMoE的整体框架包括三个主要部分：1) 内存高效的MoE计算算法，用于减少激活内存占用；2) IO与计算重叠的GPU内核，用于提高硬件利用率；3) tile-aware token rounding方法，用于减少padding带来的计算浪费。这些组件共同作用，优化MoE模型的训练过程。

**关键创新**：论文的关键创新点在于：1) 提出了一种内存高效的MoE计算算法，显著减少了激活内存占用；2) 设计了能够重叠IO与计算的GPU内核，提高了硬件利用率；3) 提出了一种tile-aware token rounding方法，有效减少了padding带来的计算浪费，同时保持了下游性能。

**关键设计**：在内存高效的MoE计算算法中，论文最小化了后向传递的激活缓存。在GPU内核设计中，论文考虑了内存IO与计算的重叠。在tile-aware token rounding方法中，论文设计了一种新的token分配策略，以减少padding，同时保持下游任务的性能。具体的参数设置和损失函数等细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

SonicMoE在Hopper GPU上实现了1.86倍的计算吞吐量提升，并减少了45%的激活内存占用。在64个H100上，SonicMoE实现了每天2130亿token的训练吞吐量，与ScatterMoE在96个H100上实现的每天2250亿token相当。Tile-aware token rounding算法在内核执行时间上产生了额外的1.16倍加速。

## 🎯 应用场景

SonicMoE可应用于大规模语言模型的训练，尤其是在资源受限的环境下。通过降低内存占用和提高计算效率，该方法能够加速MoE模型的训练过程，并降低训练成本。这对于推动自然语言处理领域的发展具有重要意义，并可能促进更强大、更高效的AI模型的开发。

## 📄 摘要（原文）

> Mixture of Experts (MoE) models have emerged as the de facto architecture for scaling up language models without significantly increasing the computational cost. Recent MoE models demonstrate a clear trend towards high expert granularity (smaller expert intermediate dimension) and higher sparsity (constant number of activated experts with higher number of total experts), which improve model quality per FLOP. However, fine-grained MoEs suffer from increased activation memory footprint and reduced hardware efficiency due to higher IO costs, while sparser MoEs suffer from wasted computations due to padding in Grouped GEMM kernels. In response, we propose a memory-efficient algorithm to compute the forward and backward passes of MoEs with minimal activation caching for the backward pass. We also design GPU kernels that overlap memory IO with computation benefiting all MoE architectures. Finally, we propose a novel "token rounding" method that minimizes the wasted compute due to padding in Grouped GEMM kernels. As a result, our method SonicMoE reduces activation memory by 45% and achieves a 1.86x compute throughput improvement on Hopper GPUs compared to ScatterMoE's BF16 MoE kernel for a fine-grained 7B MoE. Concretely, SonicMoE on 64 H100s achieves a training throughput of 213 billion tokens per day comparable to ScatterMoE's 225 billion tokens per day on 96 H100s for a 7B MoE model training with FSDP-2 using the lm-engine codebase. Under high MoE sparsity settings, our tile-aware token rounding algorithm yields an additional 1.16x speedup on kernel execution time compared to vanilla top-$K$ routing while maintaining similar downstream performance. We open-source all our kernels to enable faster MoE model training.

