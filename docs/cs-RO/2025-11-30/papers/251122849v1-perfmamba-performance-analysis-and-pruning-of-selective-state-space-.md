---
layout: default
title: PerfMamba: Performance Analysis and Pruning of Selective State Space Models
---

# PerfMamba: Performance Analysis and Pruning of Selective State Space Models

**arXiv**: [2511.22849v1](https://arxiv.org/abs/2511.22849) | [PDF](https://arxiv.org/pdf/2511.22849.pdf)

**作者**: Abdullah Al Asif, Mobina Kashaniyan, Sixing Yu, Juan Pablo Muñoz, Ali Jannesari

---

## 💡 一句话要点

**提出选择性状态空间模型性能分析与剪枝方法以优化部署效率**

**关键词**: `选择性状态空间模型` `性能分析` `模型剪枝` `序列建模` `计算效率` `内存优化`

## 📋 核心要点

1. 核心问题：选择性状态空间模型在运行时行为、资源利用和扩展特性方面缺乏全面理解，阻碍其最优部署。
2. 方法要点：对Mamba-1和Mamba-2进行系统性能分析，基于SSM组件资源消耗提出选择性剪枝低活动状态的技术。
3. 实验或效果：剪枝在保持精度下实现1.14倍加速和11.50%内存减少，适用于不同序列长度。

## 📄 摘要（原文）

> Recent advances in sequence modeling have introduced selective SSMs as promising alternatives to Transformer architectures, offering theoretical computational efficiency and sequence processing advantages. A comprehensive understanding of selective SSMs in runtime behavior, resource utilization patterns, and scaling characteristics still remains unexplored, thus obstructing their optimal deployment and further architectural improvements. This paper presents a thorough empirical study of Mamba-1 and Mamba-2, systematically profiled for performance to assess the design principles that contribute to their efficiency in state-space modeling. A detailed analysis of computation patterns, memory access, I/O characteristics, and scaling properties was performed for sequence lengths ranging from 64 to 16384 tokens. Our findings show that the SSM component, a central part of the selective SSM architecture, demands a significant portion of computational resources compared to other components in the Mamba block. Based on these insights, we propose a pruning technique that selectively removes low-activity states within the SSM component, achieving measurable throughput and memory gains while maintaining accuracy within a moderate pruning regime. This approach results in performance improvements across varying sequence lengths, achieving a 1.14x speedup and reducing memory usage by 11.50\%. These results offer valuable guidance for designing more efficient SSM architectures that can be applied to a wide range of real-world applications.

