---
layout: default
title: "Scale-interaction transformer: a hybrid cnn-transformer model for facial beauty prediction"
---

# Scale-interaction transformer: a hybrid cnn-transformer model for facial beauty prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05078" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05078v1</a>
  <a href="https://arxiv.org/pdf/2509.05078.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05078v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05078v1', 'Scale-interaction transformer: a hybrid cnn-transformer model for facial beauty prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Djamel Eddine Boukhari

**分类**: cs.CV

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**提出Scale-Interaction Transformer (SIT)模型，用于提升面部美学预测的准确性。**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `面部美学预测` `卷积神经网络` `Transformer` `多尺度特征` `自注意力机制`

## 📋 核心要点

1. 现有面部美学预测方法难以有效捕捉不同尺度面部特征之间的复杂关联。
2. 提出Scale-Interaction Transformer (SIT)模型，结合CNN的多尺度特征提取和Transformer的关系建模能力。
3. 在SCUT-FBP5500数据集上，SIT模型取得了0.9187的Pearson相关性，达到新的state-of-the-art。

## 📝 摘要（中文）

面部美学预测(FBP)是一项具有挑战性的计算机视觉任务，因为它受到影响人类感知的局部和全局面部特征复杂相互作用的影响。卷积神经网络(CNN)擅长特征提取，但通常以固定尺度处理信息，可能忽略了不同粒度级别特征之间的关键相互依赖关系。为了解决这个限制，我们引入了Scale-Interaction Transformer (SIT)，这是一种新型混合深度学习架构，它将CNN的特征提取能力与Transformer的关系建模能力相结合。SIT首先采用具有并行卷积的多尺度模块，以捕获不同感受野的面部特征。然后，这些多尺度表示被构建为序列，并由Transformer编码器处理，该编码器通过自注意力机制显式地建模它们的交互和上下文关系。我们在广泛使用的SCUT-FBP5500基准数据集上进行了大量实验，所提出的SIT模型建立了新的state-of-the-art，实现了0.9187的Pearson相关性，优于以前的方法。我们的研究结果表明，显式地建模多尺度视觉线索之间的相互作用对于高性能FBP至关重要。SIT架构的成功突出了混合CNN-Transformer模型在需要整体的、上下文感知的理解的复杂图像回归任务中的潜力。

## 🔬 方法详解

**问题定义**：面部美学预测(FBP)旨在自动评估面部的美观程度。现有方法，特别是基于CNN的方法，虽然擅长特征提取，但通常以固定尺度处理信息，难以捕捉不同尺度面部特征之间的复杂相互依赖关系，这限制了预测的准确性。

**核心思路**：论文的核心思路是利用混合CNN-Transformer架构，结合CNN的多尺度特征提取能力和Transformer的关系建模能力。通过多尺度卷积提取不同感受野的特征，然后利用Transformer显式地建模这些特征之间的交互和上下文关系，从而更全面地理解面部美学。

**技术框架**：SIT模型主要包含两个阶段：多尺度特征提取和Transformer编码。首先，使用一个多尺度模块，包含多个并行的卷积层，以不同的感受野提取面部特征。然后，将这些多尺度特征表示成一个序列，输入到Transformer编码器中。Transformer编码器利用自注意力机制，显式地建模不同尺度特征之间的交互和上下文关系。最后，Transformer的输出被用于预测面部美学得分。

**关键创新**：SIT模型的关键创新在于显式地建模多尺度面部特征之间的交互。传统方法通常独立地处理不同尺度的特征，忽略了它们之间的关联。SIT通过Transformer的自注意力机制，能够学习到不同尺度特征之间的依赖关系，从而更准确地预测面部美学。

**关键设计**：多尺度模块使用了多个并行的卷积层，每个卷积层具有不同的卷积核大小，以提取不同尺度的特征。Transformer编码器使用了标准的Transformer结构，包括多头自注意力机制和前馈神经网络。损失函数使用了均方误差(MSE)损失，用于衡量预测得分和真实得分之间的差异。

## 📊 实验亮点

SIT模型在SCUT-FBP5500数据集上取得了显著的性能提升，Pearson相关性达到0.9187，超越了之前所有方法。相比于之前的state-of-the-art方法，SIT模型在预测精度上取得了明显的进步，证明了显式建模多尺度特征交互的有效性。

## 🎯 应用场景

该研究成果可应用于个性化美容推荐、虚拟形象设计、以及人脸识别等领域。通过对面部美学进行自动评估，可以为用户提供更精准的美容建议，提升虚拟形象的吸引力，并改善人脸识别系统的性能。未来，该技术有望在医疗美容、社交媒体等领域发挥更大的作用。

## 📄 摘要（原文）

> Automated Facial Beauty Prediction (FBP) is a challenging computer vision task due to the complex interplay of local and global facial features that influence human perception. While Convolutional Neural Networks (CNNs) excel at feature extraction, they often process information at a fixed scale, potentially overlooking the critical inter-dependencies between features at different levels of granularity. To address this limitation, we introduce the Scale-Interaction Transformer (SIT), a novel hybrid deep learning architecture that synergizes the feature extraction power of CNNs with the relational modeling capabilities of Transformers. The SIT first employs a multi-scale module with parallel convolutions to capture facial characteristics at varying receptive fields. These multi-scale representations are then framed as a sequence and processed by a Transformer encoder, which explicitly models their interactions and contextual relationships via a self-attention mechanism. We conduct extensive experiments on the widely-used SCUT-FBP5500 benchmark dataset, where the proposed SIT model establishes a new state-of-the-art. It achieves a Pearson Correlation of 0.9187, outperforming previous methods. Our findings demonstrate that explicitly modeling the interplay between multi-scale visual cues is crucial for high-performance FBP. The success of the SIT architecture highlights the potential of hybrid CNN-Transformer models for complex image regression tasks that demand a holistic, context-aware understanding.

