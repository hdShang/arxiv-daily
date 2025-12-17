---
layout: default
title: A Comparative Study of Vision Transformers and CNNs for Few-Shot Rigid Transformation and Fundamental Matrix Estimation
---

# A Comparative Study of Vision Transformers and CNNs for Few-Shot Rigid Transformation and Fundamental Matrix Estimation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.04794" target="_blank" class="toolbar-btn">arXiv: 2510.04794v1</a>
    <a href="https://arxiv.org/pdf/2510.04794.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04794v1" 
            onclick="toggleFavorite(this, '2510.04794v1', 'A Comparative Study of Vision Transformers and CNNs for Few-Shot Rigid Transformation and Fundamental Matrix Estimation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Alon Kaya, Igal Bilik, Inna Stainvas

**分类**: cs.CV

**发布日期**: 2025-10-06

---

## 💡 一句话要点

**对比ViT与CNN在少样本刚性变换和本质矩阵估计中的性能，揭示不同数据规模下的架构选择策略。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉Transformer` `卷积神经网络` `少样本学习` `刚性变换估计` `本质矩阵估计` `几何估计` `迁移学习`

## 📋 核心要点

1. 现有方法在高精度几何估计任务中，尤其是在数据量较少的情况下，对局部和全局特征的平衡存在挑战。
2. 通过对比ViT和CNN在不同数据规模下的性能，探索适用于少样本几何估计任务的骨干网络架构。
3. 实验表明，ViT在大数据微调和跨域泛化方面表现出色，而CNN在小数据场景下具有竞争力。

## 📝 摘要（中文）

视觉Transformer (ViT) 和大规模卷积神经网络 (CNN) 通过预训练的特征表示重塑了计算机视觉，为各种任务实现了强大的迁移学习。然而，它们作为骨干架构在低数据情况下，处理涉及图像形变的几何估计任务的效率仍然是一个悬而未决的问题。本文考虑了两个这样的任务：1) 估计图像对之间的2D刚性变换；2) 预测立体图像对的本质矩阵，这是自主移动、机器人和3D场景重建等各种应用中的重要问题。本文系统地比较了大规模CNN（ResNet、EfficientNet、CLIP-ResNet）与基于ViT的基础模型（CLIP-ViT变体和DINO）在各种数据规模设置（包括少样本场景）下的性能。这些预训练模型针对分类或对比学习进行了优化，鼓励它们主要关注高层语义。所考虑的任务需要不同地平衡局部和全局特征，这给直接采用这些模型作为骨干带来了挑战。实证比较分析表明，与从头开始训练类似，ViT在大型下游数据场景中的微调优于CNN。然而，在小数据场景中，CNN的归纳偏置和较小的容量改善了它们的性能，使其能够与ViT相匹配。此外，ViT在数据分布发生变化的跨域评估中表现出更强的泛化能力。这些结果强调了仔细选择模型架构进行微调的重要性，并推动未来研究混合架构，以平衡局部和全局表示。

## 🔬 方法详解

**问题定义**：论文旨在解决在少样本情况下，如何选择合适的骨干网络（ViT或CNN）来进行图像对之间的2D刚性变换估计以及立体图像对的本质矩阵预测问题。现有方法直接应用预训练的ViT或CNN，忽略了在低数据场景下，模型架构的归纳偏置和容量对性能的影响。

**核心思路**：论文的核心思路是通过对比实验，分析ViT和CNN在不同数据规模下的性能差异，从而为几何估计任务选择合适的骨干网络提供指导。论文认为，ViT和CNN在局部和全局特征的提取能力上存在差异，而几何估计任务需要平衡这两种特征。

**技术框架**：论文的技术框架主要包括以下几个步骤：1) 选择预训练的ViT（CLIP-ViT和DINO）和CNN（ResNet、EfficientNet、CLIP-ResNet）作为骨干网络；2) 在2D刚性变换估计和本质矩阵预测两个任务上进行实验；3) 评估不同数据规模下，ViT和CNN的性能；4) 分析实验结果，总结ViT和CNN的优缺点。

**关键创新**：论文的关键创新在于系统地对比了ViT和CNN在少样本几何估计任务中的性能，并揭示了不同数据规模下，模型架构选择的重要性。与现有方法不同，论文没有直接应用预训练模型，而是关注模型架构本身对性能的影响。

**关键设计**：论文的关键设计包括：1) 选择具有代表性的ViT和CNN模型；2) 在两个不同的几何估计任务上进行实验；3) 采用不同的数据规模设置，包括少样本场景；4) 使用标准的评估指标，如平均端点误差（Average Endpoint Error）和Sampson距离。

## 📊 实验亮点

实验结果表明，在大型下游数据场景中，ViT在微调后优于CNN。然而，在小数据场景中，CNN的归纳偏置和较小的容量使其性能与ViT相匹配。此外，ViT在跨域评估中表现出更强的泛化能力。这些结果强调了在微调时仔细选择模型架构的重要性。

## 🎯 应用场景

该研究成果可应用于自主移动、机器人和3D场景重建等领域，为这些应用中的几何估计任务提供更有效的骨干网络选择策略。通过选择合适的模型架构，可以提高几何估计的精度和鲁棒性，从而提升相关应用的性能和可靠性。未来的研究可以进一步探索混合架构，以更好地平衡局部和全局特征，从而在各种数据规模下实现更好的性能。

## 📄 摘要（原文）

> Vision-transformers (ViTs) and large-scale convolution-neural-networks (CNNs) have reshaped computer vision through pretrained feature representations that enable strong transfer learning for diverse tasks. However, their efficiency as backbone architectures for geometric estimation tasks involving image deformations in low-data regimes remains an open question. This work considers two such tasks: 1) estimating 2D rigid transformations between pairs of images and 2) predicting the fundamental matrix for stereo image pairs, an important problem in various applications, such as autonomous mobility, robotics, and 3D scene reconstruction. Addressing this intriguing question, this work systematically compares large-scale CNNs (ResNet, EfficientNet, CLIP-ResNet) with ViT-based foundation models (CLIP-ViT variants and DINO) in various data size settings, including few-shot scenarios. These pretrained models are optimized for classification or contrastive learning, encouraging them to focus mostly on high-level semantics. The considered tasks require balancing local and global features differently, challenging the straightforward adoption of these models as the backbone. Empirical comparative analysis shows that, similar to training from scratch, ViTs outperform CNNs during refinement in large downstream-data scenarios. However, in small data scenarios, the inductive bias and smaller capacity of CNNs improve their performance, allowing them to match that of a ViT. Moreover, ViTs exhibit stronger generalization in cross-domain evaluation where the data distribution changes. These results emphasize the importance of carefully selecting model architectures for refinement, motivating future research towards hybrid architectures that balance local and global representations.

