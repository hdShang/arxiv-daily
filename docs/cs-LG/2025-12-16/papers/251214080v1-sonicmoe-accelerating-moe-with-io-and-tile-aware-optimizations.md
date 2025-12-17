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

**提出SonicMoE以解决细粒度MoE模型中的内存和计算效率问题，通过IO感知优化和令牌舍入方法加速训练。**

**关键词**: `混合专家模型` `GPU加速` `内存优化` `计算效率` `令牌舍入` `训练吞吐量` `稀疏计算` `IO感知优化`

## 📋 核心要点

1. 核心问题：细粒度MoE模型因高IO成本导致激活内存占用增加和硬件效率降低，稀疏MoE因分组GEMM内核填充造成计算浪费。
2. 方法要点：提出内存高效算法减少激活缓存，设计IO与计算重叠的GPU内核，并引入令牌舍入方法优化分组GEMM效率。
3. 实验或效果：在7B MoE上，SonicMoE减少45%激活内存，提升1.86倍计算吞吐量，并在高稀疏设置下实现额外1.16倍加速。

## 📝 摘要（中文）

混合专家（MoE）模型已成为扩展语言模型而不显著增加计算成本的事实架构。最近的MoE模型显示出高专家粒度（较小的专家中间维度）和更高稀疏性（激活专家数量恒定但总专家数更多）的明显趋势，这提高了每FLOP的模型质量。然而，细粒度MoE由于更高的IO成本而面临激活内存占用增加和硬件效率降低的问题，而更稀疏的MoE则因分组GEMM内核中的填充而导致计算浪费。为此，我们提出了一种内存高效的算法来计算MoE的前向和后向传递，最小化后向传递的激活缓存。我们还设计了GPU内核，将内存IO与计算重叠，使所有MoE架构受益。最后，我们提出了一种新颖的“令牌舍入”方法，最小化分组GEMM内核中填充造成的计算浪费。因此，我们的方法SonicMoE在细粒度7B MoE上，相比ScatterMoE的BF16 MoE内核，减少了45%的激活内存，并在Hopper GPU上实现了1.86倍的计算吞吐量提升。具体来说，在64个H100上，SonicMoE实现了每天2130亿令牌的训练吞吐量，与ScatterMoE在96个H100上使用lm-engine代码库进行7B MoE模型训练（使用FSDP-2）的每天2250亿令牌吞吐量相当。在高MoE稀疏性设置下，我们的瓦片感知令牌舍入算法相比普通top-K路由，在保持类似下游性能的同时，实现了额外1.16倍的内核执行时间加速。我们开源了所有内核以加速MoE模型训练。

## 🔬 方法详解

SonicMoE的整体框架基于MoE模型，通过系统级优化提升训练效率。关键技术创新包括：1) 内存高效算法，最小化后向传递的激活缓存，减少内存占用；2) GPU内核设计，实现内存IO与计算的重叠，提高硬件利用率；3) 瓦片感知令牌舍入方法，动态调整令牌分配以减少分组GEMM内核中的填充浪费。与现有方法（如ScatterMoE）的主要区别在于，SonicMoE综合解决了IO瓶颈和计算浪费问题，通过算法和内核层面的协同优化，而非仅依赖单一改进。

## 📊 实验亮点

在Hopper GPU上，SonicMoE相比ScatterMoE的BF16 MoE内核，对细粒度7B MoE实现45%激活内存减少和1.86倍计算吞吐量提升；在高稀疏设置下，令牌舍入算法带来额外1.16倍内核执行加速，同时保持下游性能。

## 🎯 应用场景

该研究主要应用于大规模语言模型的训练加速，特别是在需要高专家粒度和稀疏性的MoE架构中。潜在应用领域包括自然语言处理、AI推理和生成任务，实际价值在于降低训练成本、提高资源利用率，促进更高效的大模型部署和开发。

## 📄 摘要（原文）

> Mixture of Experts (MoE) models have emerged as the de facto architecture for scaling up language models without significantly increasing the computational cost. Recent MoE models demonstrate a clear trend towards high expert granularity (smaller expert intermediate dimension) and higher sparsity (constant number of activated experts with higher number of total experts), which improve model quality per FLOP. However, fine-grained MoEs suffer from increased activation memory footprint and reduced hardware efficiency due to higher IO costs, while sparser MoEs suffer from wasted computations due to padding in Grouped GEMM kernels. In response, we propose a memory-efficient algorithm to compute the forward and backward passes of MoEs with minimal activation caching for the backward pass. We also design GPU kernels that overlap memory IO with computation benefiting all MoE architectures. Finally, we propose a novel "token rounding" method that minimizes the wasted compute due to padding in Grouped GEMM kernels. As a result, our method SonicMoE reduces activation memory by 45% and achieves a 1.86x compute throughput improvement on Hopper GPUs compared to ScatterMoE's BF16 MoE kernel for a fine-grained 7B MoE. Concretely, SonicMoE on 64 H100s achieves a training throughput of 213 billion tokens per day comparable to ScatterMoE's 225 billion tokens per day on 96 H100s for a 7B MoE model training with FSDP-2 using the lm-engine codebase. Under high MoE sparsity settings, our tile-aware token rounding algorithm yields an additional 1.16x speedup on kernel execution time compared to vanilla top-$K$ routing while maintaining similar downstream performance. We open-source all our kernels to enable faster MoE model training.

