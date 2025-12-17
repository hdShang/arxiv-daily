---
layout: default
title: Universal Reasoning Model
---

# Universal Reasoning Model

**arXiv**: [2512.14693v1](https://arxiv.org/abs/2512.14693) | [PDF](https://arxiv.org/pdf/2512.14693.pdf)

**作者**: Zitian Gao, Lynx Chen, Yihao Xiao, He Xing, Ran Tao, Haoming Luo, Joey Zhou, Bryan Dai

**分类**: cs.AI

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/zitian-gao/URM)

---

## 💡 一句话要点

**提出通用推理模型以提升复杂推理任务性能，在ARC-AGI基准上实现新突破。**

**关键词**: `通用推理模型` `Transformer架构` `循环归纳偏置` `非线性组件` `短卷积` `截断反向传播` `ARC-AGI基准` `复杂推理任务`

## 📋 核心要点

1. 现有通用Transformer在复杂推理任务中性能提升来源不明确，缺乏系统性分析，限制了模型优化。
2. 论文提出通用推理模型，通过短卷积和截断反向传播增强通用Transformer，强化循环归纳偏置和非线性能力。
3. 实验显示，URM在ARC-AGI基准上取得显著提升，pass@1分数达到新高度，验证了方法的有效性。

## 📝 摘要（中文）

通用Transformer（UTs）已广泛应用于ARC-AGI和数独等复杂推理任务，但其性能提升的具体来源尚未充分探索。本研究系统分析了UTs的变体，发现ARC-AGI上的改进主要源于Transformer的循环归纳偏置和强非线性组件，而非复杂的架构设计。基于这一发现，我们提出了通用推理模型（URM），通过引入短卷积和截断反向传播来增强UT。该方法显著提升了推理性能，在ARC-AGI 1上达到53.8%的pass@1，在ARC-AGI 2上达到16.0%的pass@1，实现了最先进水平。代码已开源。

## 🔬 方法详解

通用推理模型（URM）基于通用Transformer框架，通过引入短卷积模块来增强局部特征提取能力，并结合截断反向传播技术优化训练过程，减少计算开销。关键创新在于利用短卷积强化非线性组件，同时保持循环归纳偏置，从而提升模型在复杂推理任务中的表现。与现有方法相比，URM更注重基础组件的优化，而非复杂架构设计，实现了更高效的性能提升。

## 📊 实验亮点

URM在ARC-AGI 1上达到53.8% pass@1，在ARC-AGI 2上达到16.0% pass@1，均创下最先进记录，显著超越先前方法，证明了短卷积和截断反向传播的有效性。

## 🎯 应用场景

该研究可应用于需要高级推理能力的领域，如人工智能通用智能（AGI）测试、逻辑谜题求解（如数独）和复杂决策系统，为开发更鲁棒的推理模型提供技术基础。

## 📄 摘要（原文）

> Universal transformers (UTs) have been widely used for complex reasoning tasks such as ARC-AGI and Sudoku, yet the specific sources of their performance gains remain underexplored. In this work, we systematically analyze UTs variants and show that improvements on ARC-AGI primarily arise from the recurrent inductive bias and strong nonlinear components of Transformer, rather than from elaborate architectural designs. Motivated by this finding, we propose the Universal Reasoning Model (URM), which enhances the UT with short convolution and truncated backpropagation. Our approach substantially improves reasoning performance, achieving state-of-the-art 53.8% pass@1 on ARC-AGI 1 and 16.0% pass@1 on ARC-AGI 2. Our code is avaliable at https://github.com/zitian-gao/URM.

