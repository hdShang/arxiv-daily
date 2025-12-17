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

**提出通用推理模型以提升复杂推理任务性能，在ARC-AGI基准上实现新突破**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `通用推理模型` `Transformer架构` `复杂推理任务` `ARC-AGI基准` `短卷积` `截断反向传播` `归纳偏置` `非线性组件`

## 📋 核心要点

1. 现有通用Transformer在复杂推理任务中性能提升来源不明确，限制了进一步优化。
2. 提出URM模型，通过短卷积和截断反向传播增强通用Transformer的推理能力。
3. 在ARC-AGI基准上取得显著提升，达到最先进水平，验证了方法的有效性。

## 📝 摘要（中文）

通用Transformer（UT）已被广泛应用于ARC-AGI和数独等复杂推理任务，但其性能提升的具体来源尚未得到充分探索。本研究系统分析了UT的变体，发现ARC-AGI上的改进主要源于Transformer的循环归纳偏置和强非线性组件，而非复杂的架构设计。基于这一发现，我们提出了通用推理模型（URM），通过引入短卷积和截断反向传播来增强UT。该方法显著提升了推理性能，在ARC-AGI 1上达到了53.8%的pass@1，在ARC-AGI 2上达到了16.0%的pass@1，实现了最先进水平。代码已开源：https://github.com/zitian-gao/URM。

## 🔬 方法详解

通用推理模型（URM）基于通用Transformer（UT）框架进行改进。整体框架保留了UT的循环归纳偏置和强非线性组件，这是性能提升的关键基础。关键技术创新点包括引入短卷积模块来增强局部特征提取能力，以及采用截断反向传播技术来优化训练效率和稳定性。与现有方法的主要区别在于，URM不依赖复杂的架构设计，而是通过简单有效的增强手段，直接针对推理任务的核心需求进行优化，从而在保持模型简洁性的同时大幅提升性能。

## 📊 实验亮点

URM在ARC-AGI基准上实现了最先进性能：ARC-AGI 1达到53.8% pass@1，ARC-AGI 2达到16.0% pass@1。相比现有方法，性能提升显著，验证了短卷积和截断反向传播的有效性，为复杂推理任务提供了新的解决方案。

## 🎯 应用场景

该研究主要应用于复杂推理任务，如抽象推理（ARC-AGI）、逻辑谜题（如数独）和需要高级认知能力的AI系统。潜在价值包括推动通用人工智能的发展，提升模型在少样本或零样本场景下的推理能力，为教育、游戏和自动化决策等领域提供技术支持。

## 📄 摘要（原文）

> Universal transformers (UTs) have been widely used for complex reasoning tasks such as ARC-AGI and Sudoku, yet the specific sources of their performance gains remain underexplored. In this work, we systematically analyze UTs variants and show that improvements on ARC-AGI primarily arise from the recurrent inductive bias and strong nonlinear components of Transformer, rather than from elaborate architectural designs. Motivated by this finding, we propose the Universal Reasoning Model (URM), which enhances the UT with short convolution and truncated backpropagation. Our approach substantially improves reasoning performance, achieving state-of-the-art 53.8% pass@1 on ARC-AGI 1 and 16.0% pass@1 on ARC-AGI 2. Our code is avaliable at https://github.com/zitian-gao/URM.

