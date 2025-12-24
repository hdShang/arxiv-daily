---
layout: default
title: "ReplaceMe: Network Simplification via Depth Pruning and Transformer Block Linearization"
---

# ReplaceMe: Network Simplification via Depth Pruning and Transformer Block Linearization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02819" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02819v3</a>
  <a href="https://arxiv.org/pdf/2505.02819.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02819v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02819v3', 'ReplaceMe: Network Simplification via Depth Pruning and Transformer Block Linearization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dmitriy Shopkhoev, Ammar Ali, Magauiya Zhussip, Valentin Malykh, Stamatios Lefkimmiatis, Nikos Komodakis, Sergey Zagoruyko

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-05 (更新: 2025-06-20)

**🔗 代码/项目**: [GITHUB](https://github.com/mts-ai/ReplaceMe)

---

## 💡 一句话要点

**提出ReplaceMe以解决变换器块简化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度剪枝` `变换器简化` `线性化` `无训练方法` `大型语言模型` `模型压缩` `计算效率`

## 📋 核心要点

1. 现有的剪枝方法通常需要额外的训练或微调，导致计算成本高且效率低下。
2. ReplaceMe通过深度剪枝和线性化变换器块，提出了一种无需训练的简化方法，显著降低了模型复杂度。
3. 实验结果显示，ReplaceMe在多个大型语言模型上实现了高达25%的剪枝，同时保持约90%的性能，优于其他无训练方法。

## 📝 摘要（中文）

我们提出了ReplaceMe，这是一种通用的无训练深度剪枝方法，能够有效地将变换器块替换为线性操作，同时在低压缩比下保持高性能。与传统的剪枝方法不同，ReplaceMe仅需一个小的校准数据集来估计线性变换，从而近似剪枝后的块。估计的线性映射可以与剩余的变换器块无缝合并，消除额外网络参数的需求。实验表明，ReplaceMe在多个大型语言模型上实现了高达25%的剪枝，同时在开放基准上保留了约90%的原始模型性能，且无需任何训练或修复步骤，计算开销极小。我们提供了一个开源库，实施ReplaceMe及多种先进的深度剪枝技术，地址为https://github.com/mts-ai/ReplaceMe。

## 🔬 方法详解

**问题定义**：当前的变换器模型在剪枝过程中通常需要大量的训练和微调，这不仅增加了计算成本，还限制了其在资源受限环境中的应用。

**核心思路**：ReplaceMe的核心思路是通过深度剪枝将变换器块替换为线性操作，利用小规模的校准数据集来估计线性变换，从而避免了传统方法中的训练需求。

**技术框架**：ReplaceMe的整体架构包括三个主要模块：首先，使用校准数据集估计线性变换；其次，将该线性映射与剩余的变换器块合并；最后，形成一个简化的网络结构，减少了参数数量。

**关键创新**：ReplaceMe的创新之处在于其训练-free的特性，能够在不需要额外训练的情况下实现有效的剪枝，与传统方法相比，显著降低了计算开销。

**关键设计**：在设计中，ReplaceMe使用了小规模的校准数据集来进行线性映射的估计，确保了剪枝后模型性能的保留，同时避免了复杂的参数调整和网络结构修改。

## 📊 实验亮点

ReplaceMe在多个大型语言模型上实现了高达25%的剪枝，同时在开放基准上保留了约90%的原始模型性能，表现出色。与其他无训练方法相比，ReplaceMe的性能更具竞争力，且计算开销极小，展示了其在深度学习模型简化中的重要价值。

## 🎯 应用场景

ReplaceMe的研究成果在多个领域具有广泛应用潜力，尤其是在需要高效模型部署的场景，如移动设备、边缘计算和实时推理等。其简化的网络结构能够在保持性能的同时，显著降低计算资源的消耗，推动深度学习模型在实际应用中的普及与应用。

## 📄 摘要（原文）

> We introduce ReplaceMe, a generalized training-free depth pruning method that effectively replaces transformer blocks with a linear operation, while maintaining high performance for low compression ratios. In contrast to conventional pruning approaches that require additional training or fine-tuning, our approach requires only a small calibration dataset that is used to estimate a linear transformation, which approximates the pruned blocks. The estimated linear mapping can be seamlessly merged with the remaining transformer blocks, eliminating the need for any additional network parameters. Our experiments show that ReplaceMe consistently outperforms other training-free approaches and remains highly competitive with state-of-the-art pruning methods that involve extensive retraining/fine-tuning and architectural modifications. Applied to several large language models (LLMs), ReplaceMe achieves up to 25% pruning while retaining approximately 90% of the original model's performance on open benchmarks - without any training or healing steps, resulting in minimal computational overhead (see Fig.1). We provide an open-source library implementing ReplaceMe alongside several state-of-the-art depth pruning techniques, available at https://github.com/mts-ai/ReplaceMe.

