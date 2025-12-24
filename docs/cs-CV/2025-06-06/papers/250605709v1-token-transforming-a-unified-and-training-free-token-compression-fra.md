---
layout: default
title: "Token Transforming: A Unified and Training-Free Token Compression Framework for Vision Transformer Acceleration"
---

# Token Transforming: A Unified and Training-Free Token Compression Framework for Vision Transformer Acceleration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05709" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05709v1</a>
  <a href="https://arxiv.org/pdf/2506.05709.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05709v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05709v1', 'Token Transforming: A Unified and Training-Free Token Compression Framework for Vision Transformer Acceleration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fanhu Zeng, Deli Yu, Zhenglun Kong, Hao Tang

**分类**: cs.CV

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出Token Transforming框架以加速视觉Transformer并减少信息损失**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉Transformer` `令牌压缩` `模型加速` `深度学习` `计算机视觉` `信息保留` `无训练加速` `密集预测任务`

## 📋 核心要点

1. 现有的视觉Transformer压缩方法主要依赖于令牌剪枝或合并，导致信息损失和性能恢复的需求。
2. 本文提出了一种多对多的Token Transforming框架，将令牌压缩视为令牌矩阵变换，旨在保留更多信息并实现无训练加速。
3. 实验结果显示，该框架能有效减少计算量，提升推理速度，并在多个任务中保持良好的性能表现。

## 📝 摘要（中文）

视觉Transformer在各种视觉任务中得到了广泛应用，但由于其高计算成本，动态压缩视觉Transformer的研究受到关注。现有方法主要集中在令牌剪枝或合并上，导致信息损失并需后续训练恢复性能。本文重新思考令牌减少，将其统一为令牌矩阵变换的显式形式，提出了一种多对多的Token Transforming框架，能够保留更多信息，实现无训练加速。实验表明，该框架可减少40%的FLOPs，并将DeiT-S加速1.5倍，准确率仅下降0.1%。此外，该方法还扩展到密集预测任务，结果显示其在计算性能权衡、预算减少和推理加速方面均有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉Transformer压缩方法中信息损失严重的问题，尤其是在令牌剪枝和合并过程中，导致后续训练恢复性能的需求。

**核心思路**：提出Token Transforming框架，将令牌压缩过程视为令牌矩阵的变换，统一现有方法，确保信息保留最大化，并实现训练无关的加速。

**技术框架**：该框架包括多个模块，首先对输入的令牌矩阵进行变换，然后通过多对多的映射关系进行压缩，最后输出压缩后的令牌矩阵供后续处理使用。

**关键创新**：最重要的创新在于将所有现有的令牌压缩方法整合为一个统一的框架，避免了信息损失，并实现了训练无关的加速，这与传统方法有本质区别。

**关键设计**：在设计中，采用了特定的矩阵变换技术，确保在压缩过程中尽可能保留信息，同时设置了适当的参数以优化计算效率和性能。实验中使用的损失函数和网络结构经过精心设计，以适应不同的视觉任务。

## 📊 实验亮点

实验结果表明，Token Transforming框架能够减少40%的FLOPs，并将DeiT-S的推理速度提升1.5倍，准确率仅下降0.1%。此外，该方法在密集预测任务中也表现出显著的性能提升，展示了良好的计算性能权衡。

## 🎯 应用场景

该研究的潜在应用领域包括图像分类、目标检测、语义分割等视觉任务，能够有效提升视觉Transformer的推理速度和计算效率，具有重要的实际价值。未来，该框架还可能扩展到其他深度学习模型的压缩和加速中，推动更广泛的应用。

## 📄 摘要（原文）

> Vision transformers have been widely explored in various vision tasks. Due to heavy computational cost, much interest has aroused for compressing vision transformer dynamically in the aspect of tokens. Current methods mainly pay attention to token pruning or merging to reduce token numbers, in which tokens are compressed exclusively, causing great information loss and therefore post-training is inevitably required to recover the performance. In this paper, we rethink token reduction and unify the process as an explicit form of token matrix transformation, in which all existing methods are constructing special forms of matrices within the framework. Furthermore, we propose a many-to-many Token Transforming framework that serves as a generalization of all existing methods and reserves the most information, even enabling training-free acceleration. We conduct extensive experiments to validate our framework. Specifically, we reduce 40% FLOPs and accelerate DeiT-S by $\times$1.5 with marginal 0.1% accuracy drop. Furthermore, we extend the method to dense prediction tasks including segmentation, object detection, depth estimation, and language model generation. Results demonstrate that the proposed method consistently achieves substantial improvements, offering a better computation-performance trade-off, impressive budget reduction and inference acceleration.

