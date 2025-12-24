---
layout: default
title: "VM-BeautyNet: A Synergistic Ensemble of Vision Transformer and Mamba for Facial Beauty Prediction"
---

# VM-BeautyNet: A Synergistic Ensemble of Vision Transformer and Mamba for Facial Beauty Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16220" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16220v1</a>
  <a href="https://arxiv.org/pdf/2510.16220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16220v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.16220v1', 'VM-BeautyNet: A Synergistic Ensemble of Vision Transformer and Mamba for Facial Beauty Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Djamel Eddine Boukhari

**分类**: cs.CV

**发布日期**: 2025-10-17

---

## 💡 一句话要点

**VM-BeautyNet：融合Vision Transformer与Mamba的面部美学预测模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `面部美学预测` `Vision Transformer` `Mamba` `状态空间模型` `异构集成` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有面部美学预测方法难以有效捕捉全局面部特征，限制了预测精度。
2. VM-BeautyNet融合ViT和Mamba，利用ViT提取全局结构，Mamba建模长程依赖，互补优势。
3. 在SCUT-FBP5500数据集上，VM-BeautyNet达到SOTA，PC达0.9212，MAE为0.2085，RMSE为0.2698。

## 📝 摘要（中文）

面部美学预测(FBP)是一项复杂且具有挑战性的计算机视觉任务，旨在模拟人类审美感知的复杂性和主观性。深度学习模型，特别是卷积神经网络(CNN)，已经取得了显著进展，但它们通常难以捕捉对人类判断至关重要的全局、整体面部特征。Vision Transformer (ViT)通过有效地建模长程空间关系来解决这个问题，但其二次复杂度可能成为瓶颈。本文提出了一种新颖的异构集成架构VM-BeautyNet，它协同融合了Vision Transformer和基于Mamba的视觉模型的互补优势，Mamba是状态空间模型(SSM)的最新进展。ViT骨干网络擅长捕捉全局面部结构和对称性，而Mamba骨干网络以线性复杂度有效地建模长程依赖关系，专注于序列特征和纹理。我们在基准SCUT-FBP5500数据集上评估了我们的方法。我们提出的VM-BeautyNet实现了最先进的性能，Pearson相关系数(PC)为0.9212，平均绝对误差(MAE)为0.2085，均方根误差(RMSE)为0.2698。此外，通过Grad-CAM可视化，我们提供了可解释性分析，证实了两个骨干网络的互补特征提取，为模型的决策过程提供了新的见解，并为计算美学提出了一个强大的新架构范例。

## 🔬 方法详解

**问题定义**：面部美学预测旨在通过计算机模型预测人脸的美丽程度。现有方法，特别是基于CNN的模型，在捕捉全局面部结构和长程依赖关系方面存在局限性，而ViT虽然能捕捉全局信息，但计算复杂度较高。因此，如何有效且高效地提取全局和局部面部特征，是该领域的一个关键挑战。

**核心思路**：VM-BeautyNet的核心思路是利用ViT和Mamba的互补优势。ViT擅长捕捉全局面部结构和对称性，而Mamba能够以线性复杂度建模长程依赖关系，关注序列特征和纹理。通过集成这两种模型，可以更全面地提取面部特征，从而提高美学预测的准确性。

**技术框架**：VM-BeautyNet是一个异构集成架构，包含两个主要分支：ViT分支和Mamba分支。首先，输入图像分别经过ViT和Mamba骨干网络进行特征提取。然后，将两个分支提取的特征进行融合。最后，通过一个回归头预测面部美学得分。整个框架采用端到端的方式进行训练。

**关键创新**：该论文的关键创新在于提出了VM-BeautyNet，一种新颖的异构集成架构，它有效地融合了ViT和Mamba的优势，实现了更准确的面部美学预测。与传统的CNN或单独使用ViT相比，VM-BeautyNet能够更好地捕捉全局和局部面部特征，从而提高了预测性能。

**关键设计**：ViT分支采用预训练的ViT模型作为骨干网络，Mamba分支采用基于Mamba的视觉模型。在特征融合阶段，采用加权融合的方式，根据两个分支的贡献动态调整权重。损失函数采用均方误差损失函数，优化器采用AdamW优化器。实验中，对ViT和Mamba的参数进行了精细调整，以达到最佳性能。

## 📊 实验亮点

VM-BeautyNet在SCUT-FBP5500数据集上取得了显著的性能提升，Pearson相关系数(PC)达到0.9212，平均绝对误差(MAE)为0.2085，均方根误差(RMSE)为0.2698。这些结果表明，VM-BeautyNet在面部美学预测方面达到了最先进的水平，优于现有的基于CNN或ViT的方法。

## 🎯 应用场景

VM-BeautyNet在多个领域具有潜在应用价值，包括：个性化推荐（例如，推荐更符合用户审美偏好的产品）、美容整形咨询（提供客观的美学评估）、虚拟形象设计（创建更具吸引力的虚拟角色）以及图像编辑（自动美化人脸）。该研究有助于推动计算美学的发展，并为相关应用提供更准确、可靠的技术支持。

## 📄 摘要（原文）

> Facial Beauty Prediction (FBP) is a complex and challenging computer vision task, aiming to model the subjective and intricate nature of human aesthetic perception. While deep learning models, particularly Convolutional Neural Networks (CNNs), have made significant strides, they often struggle to capture the global, holistic facial features that are critical to human judgment. Vision Transformers (ViT) address this by effectively modeling long-range spatial relationships, but their quadratic complexity can be a bottleneck. This paper introduces a novel, heterogeneous ensemble architecture, \textbf{VM-BeautyNet}, that synergistically fuses the complementary strengths of a Vision Transformer and a Mamba-based Vision model, a recent advancement in State-Space Models (SSMs). The ViT backbone excels at capturing global facial structure and symmetry, while the Mamba backbone efficiently models long-range dependencies with linear complexity, focusing on sequential features and textures. We evaluate our approach on the benchmark SCUT-FBP5500 dataset. Our proposed VM-BeautyNet achieves state-of-the-art performance, with a \textbf{Pearson Correlation (PC) of 0.9212}, a \textbf{Mean Absolute Error (MAE) of 0.2085}, and a \textbf{Root Mean Square Error (RMSE) of 0.2698}. Furthermore, through Grad-CAM visualizations, we provide interpretability analysis that confirms the complementary feature extraction of the two backbones, offering new insights into the model's decision-making process and presenting a powerful new architectural paradigm for computational aesthetics.

