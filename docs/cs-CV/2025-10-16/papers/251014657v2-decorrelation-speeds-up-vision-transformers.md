---
layout: default
title: Decorrelation Speeds Up Vision Transformers
---

# Decorrelation Speeds Up Vision Transformers

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14657" target="_blank" class="toolbar-btn">arXiv: 2510.14657v2</a>
    <a href="https://arxiv.org/pdf/2510.14657.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14657v2" 
            onclick="toggleFavorite(this, '2510.14657v2', 'Decorrelation Speeds Up Vision Transformers')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kieran Carrigg, Rob van Gastel, Melda Yeghaian, Sander Dalm, Faysal Boughorbel, Marcel van Gerven

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-16 (更新: 2025-11-26)

**备注**: 16 pages, 12 figures, submitted to CVC 2026

---

## 💡 一句话要点

**提出DBP-MAE加速ViT预训练，降低计算成本和碳排放，提升下游任务性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Vision Transformer` `掩码自编码器` `解相关反向传播` `高效预训练` `低碳AI`

## 📋 核心要点

1. MAE预训练ViT虽然性能强大，但计算成本高昂，限制了其在资源受限场景下的应用。
2. 本文将解相关反向传播(DBP)融入MAE预训练，通过减少层间输入相关性来加速收敛。
3. 实验表明，DBP-MAE在降低训练时间和碳排放的同时，还能提升下游分割任务的性能。

## 📝 摘要（中文）

本文提出将解相关反向传播(DBP)集成到掩码自编码器(MAE)的ViT预训练中，DBP是一种优化方法，通过迭代减少每一层的输入相关性来加速收敛。DBP选择性地应用于编码器，可以在不损失稳定性的前提下实现更快的预训练。为了模拟约束数据场景，我们在ImageNet-1K预训练和ADE20K微调上，使用随机采样的子集评估了该方法。在此设置下，DBP-MAE将达到基线性能的实际运行时间减少了21.1%，碳排放降低了21.4%，并提高了1.1个百分点的分割mIoU。在专有的工业数据上进行预训练和微调时，也观察到了类似的增益，证实了该方法在实际场景中的适用性。这些结果表明，DBP可以减少大规模ViT预训练的训练时间和能源消耗，同时提高下游性能。

## 🔬 方法详解

**问题定义**：论文旨在解决Vision Transformer (ViT) 的 Masked Autoencoder (MAE) 预训练计算成本高昂的问题，尤其是在时间和资源受限的工业环境中。现有的MAE预训练方法虽然性能优越，但其巨大的计算量使其难以在实际应用中普及。

**核心思路**：论文的核心思路是将 Decorrelated Backpropagation (DBP) 集成到 MAE 预训练过程中。DBP 旨在减少神经网络每一层的输入相关性，从而加速训练过程的收敛。通过降低输入特征之间的冗余信息，DBP 可以使网络更快地学习到有效的特征表示。

**技术框架**：DBP-MAE 的整体框架与标准的 MAE 类似，包括一个 ViT 编码器和一个 ViT 解码器。不同之处在于，DBP 被选择性地应用于编码器部分。在预训练阶段，输入图像被随机掩码，编码器处理未被掩码的部分，然后解码器重建原始图像。DBP 在编码器的反向传播过程中起作用，通过调整梯度来减少输入相关性。

**关键创新**：该论文的关键创新在于将 DBP 成功地应用于 ViT 的 MAE 预训练中，并证明了其在加速训练和降低计算成本方面的有效性。与直接应用 DBP 到整个网络不同，论文选择性地将其应用于编码器，从而在加速收敛的同时保持了训练的稳定性。

**关键设计**：DBP 的具体实现涉及在反向传播过程中修改梯度。具体来说，对于每一层，计算输入特征的协方差矩阵，并使用该协方差矩阵来调整梯度。这种调整旨在减少输入特征之间的相关性。论文中没有详细说明具体的 DBP 参数设置，但强调了选择性应用 DBP 到编码器的重要性。

## 📊 实验亮点

在ImageNet-1K预训练和ADE20K微调实验中，DBP-MAE将达到基线性能的实际运行时间减少了21.1%，碳排放降低了21.4%，并提高了1.1个百分点的分割mIoU。在专有工业数据集上的实验也验证了DBP-MAE的有效性。

## 🎯 应用场景

该研究成果可广泛应用于需要高效预训练ViT模型的场景，例如工业视觉检测、自动驾驶、医学图像分析等。通过降低计算成本和碳排放，DBP-MAE 有助于推动大规模ViT模型在资源受限环境中的应用，并促进绿色人工智能的发展。

## 📄 摘要（原文）

> Masked Autoencoder (MAE) pre-training of vision transformers (ViTs) yields strong performance in low-label data regimes but comes with substantial computational costs, making it impractical in time- and resource-constrained industrial settings. We address this by nitegrating Decorrelated Backpropagation (DBP) into MAE pre-training, an optimization method that iteratively reduces input correlations at each layer to accelerate convergence. Applied selectively to the encoder, DBP achieves faster pre-training without loss of stability. To mimic constrained-data scenarios, we evaluate our approach on ImageNet-1K pre-training and ADE20K fine-tuning using randomly sampled subsets of each dataset. Under this setting, DBP-MAE reduces wall-clock time to baseline performance by 21.1%, lowers carbon emissions by 21.4%, and improves segmentation mIoU by 1.1 points. We observe similar gains when pre-training and fine-tuning on proprietary industrial data, confirming the method's applicability in real-world scenarios. These results demonstrate that DBP can reduce training time and energy use while improving downstream performance for large-scale ViT pre-training.
>   Keywords: Deep learning, Vision transformers, Efficient AI, Decorrelation

