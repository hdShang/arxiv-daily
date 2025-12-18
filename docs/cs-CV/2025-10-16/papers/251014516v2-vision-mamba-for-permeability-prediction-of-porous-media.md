---
layout: default
title: Vision Mamba for Permeability Prediction of Porous Media
---

# Vision Mamba for Permeability Prediction of Porous Media

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14516" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14516v2</a>
  <a href="https://arxiv.org/pdf/2510.14516.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14516v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.14516v2', 'Vision Mamba for Permeability Prediction of Porous Media')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Kashefi, Tapan Mukerji

**分类**: cs.CV

**发布日期**: 2025-10-16 (更新: 2025-10-20)

---

## 💡 一句话要点

**提出基于Vision Mamba的多孔介质渗透率预测模型，提升计算效率和内存利用率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Vision Mamba` `多孔介质` `渗透率预测` `深度学习` `计算机视觉`

## 📋 核心要点

1. 传统ViT模型在处理高分辨率图像时，计算复杂度和内存需求呈平方级增长，限制了其应用。
2. 论文提出使用Vision Mamba作为骨干网络，其计算复杂度随图像分辨率线性增长，显著提升计算和内存效率。
3. 实验结果表明，Vision Mamba在多孔介质渗透率预测任务中，性能优于ViT和CNN模型，验证了其有效性。

## 📝 摘要（中文）

Vision Mamba作为Vision Transformer (ViT)在图像分类中的替代方案，最近受到了广泛关注。Vision Mamba的网络大小随输入图像分辨率线性增长，而ViT则呈二次方增长，这一特性提高了计算和内存效率。此外，Vision Mamba所需的可训练参数数量明显少于传统的卷积神经网络(CNN)，因此更具内存效率。基于这些优点，本文首次提出了一种使用Vision Mamba作为骨干网络来预测三维多孔介质渗透率的神经网络。我们将Vision Mamba与ViT和CNN模型在渗透率预测的多个方面进行了性能比较，并进行了消融研究，以评估其组件对准确性的影响。实践证明，Vision Mamba在三维多孔介质渗透率预测方面优于ViT和CNN。我们公开了源代码，以方便重现，并使其他研究人员能够在此基础上进行构建和扩展。我们相信，所提出的框架有潜力被集成到大型视觉模型中，在这些模型中，Vision Mamba可以用来代替ViT。

## 🔬 方法详解

**问题定义**：论文旨在解决三维多孔介质渗透率预测问题。现有方法，如ViT和CNN，在高分辨率图像处理时存在计算量大、内存消耗高等问题，限制了其在复杂多孔介质建模中的应用。

**核心思路**：论文的核心思路是利用Vision Mamba的线性复杂度特性，替代ViT作为骨干网络，从而降低计算成本和内存需求。Vision Mamba基于选择性状态空间模型（Selective State Space Models, S6），能够更有效地捕捉长距离依赖关系，适用于多孔介质的复杂结构分析。

**技术框架**：该模型以Vision Mamba作为特征提取器，输入三维多孔介质图像，经过一系列Mamba块进行特征提取和变换。最后，通过全连接层或卷积层将提取的特征映射到渗透率预测值。整体框架简洁高效，易于实现和扩展。

**关键创新**：最重要的技术创新点在于首次将Vision Mamba应用于多孔介质渗透率预测。与传统的ViT和CNN相比，Vision Mamba在保持甚至提升预测精度的同时，显著降低了计算复杂度和内存占用。

**关键设计**：论文可能采用了特定的Mamba块配置，例如层数、通道数等。损失函数可能选择了均方误差（MSE）或平均绝对误差（MAE）等回归损失函数。此外，可能还采用了数据增强技术来提高模型的泛化能力。具体的参数设置和网络结构细节需要在论文原文中查找。

## 📊 实验亮点

实验结果表明，Vision Mamba在多孔介质渗透率预测任务中，相较于ViT和CNN模型，在计算效率和内存利用率方面具有显著优势。具体的性能提升数据（例如，预测精度、计算时间、内存占用）需要在论文原文中查找。论文公开了源代码，方便其他研究者复现和进一步研究。

## 🎯 应用场景

该研究成果可应用于石油工程、水文地质、材料科学等领域，用于快速准确地预测多孔介质的渗透率。这有助于优化油藏开发方案、评估地下水资源、设计新型多孔材料等。未来，该框架有望集成到更大规模的视觉模型中，应用于更广泛的科学和工程问题。

## 📄 摘要（原文）

> Vision Mamba has recently received attention as an alternative to Vision Transformers (ViTs) for image classification. The network size of Vision Mamba scales linearly with input image resolution, whereas ViTs scale quadratically, a feature that improves computational and memory efficiency. Moreover, Vision Mamba requires a significantly smaller number of trainable parameters than traditional convolutional neural networks (CNNs), and thus, they can be more memory efficient. Because of these features, we introduce, for the first time, a neural network that uses Vision Mamba as its backbone for predicting the permeability of three-dimensional porous media. We compare the performance of Vision Mamba with ViT and CNN models across multiple aspects of permeability prediction and perform an ablation study to assess the effects of its components on accuracy. We demonstrate in practice the aforementioned advantages of Vision Mamba over ViTs and CNNs in the permeability prediction of three-dimensional porous media. We make the source code publicly available to facilitate reproducibility and to enable other researchers to build on and extend this work. We believe the proposed framework has the potential to be integrated into large vision models in which Vision Mamba is used instead of ViTs.

