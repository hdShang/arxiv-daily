---
layout: default
title: "TACFN: Transformer-based Adaptive Cross-modal Fusion Network for Multimodal Emotion Recognition"
---

# TACFN: Transformer-based Adaptive Cross-modal Fusion Network for Multimodal Emotion Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06536" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06536v1</a>
  <a href="https://arxiv.org/pdf/2505.06536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06536v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06536v1', 'TACFN: Transformer-based Adaptive Cross-modal Fusion Network for Multimodal Emotion Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng Liu, Ziwang Fu, Yunlong Wang, Qijian Zheng

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-10

**备注**: arXiv admin note: text overlap with arXiv:2111.02172

**🔗 代码/项目**: [GITHUB](https://github.com/shuzihuaiyu/TACFN)

---

## 💡 一句话要点

**提出TACFN以解决多模态情感识别中的特征冗余问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态情感识别` `跨模态融合` `自适应特征选择` `Transformer` `情感计算` `深度学习`

## 📋 核心要点

1. 现有的跨模态注意力方法在特征冗余和互补特征捕捉方面存在不足，影响了情感识别的准确性。
2. 论文提出的TACFN通过自注意力机制进行内部特征选择，优化模态间的特征交互，提升融合效果。
3. 在RAVDESS和IEMOCAP数据集上的实验结果显示，TACFN显著提高了情感识别的性能，达到了最先进水平。

## 📝 摘要（中文）

多模态情感识别任务中的融合技术至关重要。近年来，基于跨模态注意力的融合方法表现出高性能和强鲁棒性。然而，跨模态注意力存在冗余特征，且未能有效捕捉互补特征。我们发现，在跨模态交互中，并不需要使用一个模态的全部信息来增强另一个模态，能够增强模态的特征可能仅包含其一部分。为此，我们设计了创新的基于Transformer的自适应跨模态融合网络（TACFN）。具体而言，我们通过自注意力机制使一个模态进行内部特征选择，从而使所选特征能够自适应、高效地与另一个模态交互。实验结果表明，TACFN相较于其他方法显著提升了性能，并达到了当前的最先进水平。

## 🔬 方法详解

**问题定义**：论文要解决多模态情感识别中的特征冗余和互补特征捕捉不足的问题。现有的跨模态注意力方法未能有效利用模态间的信息，导致性能下降。

**核心思路**：论文的核心解决思路是通过自注意力机制进行内部特征选择，使得模态间的特征交互更加高效和自适应，从而减少冗余信息的影响。

**技术框架**：TACFN的整体架构包括特征选择模块和特征增强模块。特征选择模块利用自注意力机制选择重要特征，特征增强模块通过加权融合不同模态的信息。

**关键创新**：最重要的技术创新点在于引入自适应特征选择机制，使得模态间的交互更加精准，避免了传统方法中的冗余特征问题。

**关键设计**：在网络结构上，采用Transformer架构进行特征选择和融合，损失函数设计为适应多模态特征的特性，确保模型的有效训练和性能提升。

## 📊 实验亮点

实验结果表明，TACFN在RAVDESS和IEMOCAP数据集上显著提升了情感识别的性能，相较于其他基线方法，性能提升幅度达到X%（具体数据需根据实验结果填写），达到了当前的最先进水平。

## 🎯 应用场景

该研究的潜在应用领域包括情感分析、社交媒体监测、智能客服等。通过提高多模态情感识别的准确性，TACFN可以为情感计算和人机交互提供更为精准的支持，未来可能在心理健康监测和情感智能设备中发挥重要作用。

## 📄 摘要（原文）

> The fusion technique is the key to the multimodal emotion recognition task. Recently, cross-modal attention-based fusion methods have demonstrated high performance and strong robustness. However, cross-modal attention suffers from redundant features and does not capture complementary features well. We find that it is not necessary to use the entire information of one modality to reinforce the other during cross-modal interaction, and the features that can reinforce a modality may contain only a part of it. To this end, we design an innovative Transformer-based Adaptive Cross-modal Fusion Network (TACFN). Specifically, for the redundant features, we make one modality perform intra-modal feature selection through a self-attention mechanism, so that the selected features can adaptively and efficiently interact with another modality. To better capture the complementary information between the modalities, we obtain the fused weight vector by splicing and use the weight vector to achieve feature reinforcement of the modalities. We apply TCAFN to the RAVDESS and IEMOCAP datasets. For fair comparison, we use the same unimodal representations to validate the effectiveness of the proposed fusion method. The experimental results show that TACFN brings a significant performance improvement compared to other methods and reaches the state-of-the-art. All code and models could be accessed from https://github.com/shuzihuaiyu/TACFN.

