---
layout: default
title: "EGFormer: Towards Efficient and Generalizable Multimodal Semantic Segmentation"
---

# EGFormer: Towards Efficient and Generalizable Multimodal Semantic Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14014" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14014v1</a>
  <a href="https://arxiv.org/pdf/2505.14014.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14014v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14014v1', 'EGFormer: Towards Efficient and Generalizable Multimodal Semantic Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zelin Zhang, Tao Zhang, KediLI, Xu Zheng

**分类**: cs.CV

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出EGFormer以解决多模态语义分割的效率问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态语义分割` `计算效率` `动态模态选择` `深度学习` `迁移学习`

## 📋 核心要点

1. 现有多模态语义分割方法大多专注于提高准确性，计算效率却未得到充分研究。
2. EGFormer通过引入ASM和MDM模块，动态评估模态重要性并过滤冗余信息，从而提高了效率。
3. 实验表明，EGFormer在参数和计算量上显著减少，同时在迁移学习任务中表现优异。

## 📝 摘要（中文）

近年来，研究者们探索了多模态语义分割，采用了多种主干架构。然而，大多数方法虽然提高了准确性，但在计算效率方面的研究仍显不足。为此，本文提出了EGFormer，一个高效的多模态语义分割框架，灵活整合任意数量的模态，同时显著减少模型参数和推理时间，而不牺牲性能。该框架引入了两个新模块：任何模态评分模块（ASM）和模态丢弃模块（MDM），前者为每个模态独立分配重要性评分，后者在每个阶段过滤掉信息量较少的模态。通过这些设计，EGFormer能够利用所有可用模态的信息，同时去除冗余，确保高质量的分割。此外，EGFormer在合成到真实的迁移任务中表现出良好的泛化能力。实验结果表明，EGFormer在参数上减少了多达88%，GFLOPs减少了50%，在无监督领域适应设置下，进一步实现了领先的迁移性能。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态语义分割中的计算效率问题。现有方法在提高准确性的同时，往往忽视了模型的计算开销，导致实际应用中的效率低下。

**核心思路**：EGFormer通过引入两个新模块，ASM和MDM，来动态评估和选择模态，从而减少冗余信息并提高模型效率。ASM为每个模态分配重要性评分，MDM则在每个阶段过滤掉信息量较少的模态。

**技术框架**：EGFormer的整体架构包括输入多模态数据、通过ASM进行模态评分、使用MDM进行模态选择和信息聚合，最终输出高质量的语义分割结果。该框架灵活支持任意数量的模态输入。

**关键创新**：EGFormer的核心创新在于其动态模态选择机制，通过ASM和MDM模块的结合，有效减少了模型参数和计算量，与现有方法相比，显著提高了效率和性能。

**关键设计**：在设计上，ASM模块采用独立评分机制，MDM模块则通过设定阈值来过滤模态。模型的损失函数和网络结构经过优化，以确保在减少计算量的同时保持分割精度。

## 📊 实验亮点

EGFormer在实验中表现出色，参数减少高达88%，GFLOPs减少50%。在无监督领域适应任务中，其迁移性能达到当前最优水平，显著优于现有方法，展示了其在多模态语义分割领域的强大能力。

## 🎯 应用场景

EGFormer在自动驾驶、医学影像分析和机器人视觉等领域具有广泛的应用潜力。其高效的多模态处理能力能够帮助系统在复杂环境中快速做出决策，提升智能系统的实用性和响应速度。未来，EGFormer有望在实时处理和大规模数据分析中发挥重要作用。

## 📄 摘要（原文）

> Recent efforts have explored multimodal semantic segmentation using various backbone architectures. However, while most methods aim to improve accuracy, their computational efficiency remains underexplored. To address this, we propose EGFormer, an efficient multimodal semantic segmentation framework that flexibly integrates an arbitrary number of modalities while significantly reducing model parameters and inference time without sacrificing performance. Our framework introduces two novel modules. First, the Any-modal Scoring Module (ASM) assigns importance scores to each modality independently, enabling dynamic ranking based on their feature maps. Second, the Modal Dropping Module (MDM) filters out less informative modalities at each stage, selectively preserving and aggregating only the most valuable features. This design allows the model to leverage useful information from all available modalities while discarding redundancy, thus ensuring high segmentation quality. In addition to efficiency, we evaluate EGFormer on a synthetic-to-real transfer task to demonstrate its generalizability. Extensive experiments show that EGFormer achieves competitive performance with up to 88 percent reduction in parameters and 50 percent fewer GFLOPs. Under unsupervised domain adaptation settings, it further achieves state-of-the-art transfer performance compared to existing methods.

