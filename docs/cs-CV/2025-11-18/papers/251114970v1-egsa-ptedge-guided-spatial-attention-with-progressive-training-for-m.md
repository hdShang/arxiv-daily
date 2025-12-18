---
layout: default
title: EGSA-PT:Edge-Guided Spatial Attention with Progressive Training for Monocular Depth Estimation and Segmentation of Transparent Objects
---

# EGSA-PT:Edge-Guided Spatial Attention with Progressive Training for Monocular Depth Estimation and Segmentation of Transparent Objects

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14970" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14970v1</a>
  <a href="https://arxiv.org/pdf/2511.14970.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14970v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.14970v1', 'EGSA-PT:Edge-Guided Spatial Attention with Progressive Training for Monocular Depth Estimation and Segmentation of Transparent Objects')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gbenga Omotara, Ramy Farag, Seyed Mohamad Ali Tousi, G. N. DeSouza

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-11-18

---

## 💡 一句话要点

**提出EGSA-PT，通过边缘引导空间注意力和渐进式训练提升透明物体深度估计与分割性能**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `透明物体感知` `深度估计` `语义分割` `边缘引导` `空间注意力` `多模态学习` `渐进式训练`

## 📋 核心要点

1. 透明物体感知是计算机视觉难题，传统方法在深度估计和语义分割上表现不佳，多任务学习易受负面跨任务影响。
2. 提出边缘引导空间注意力（EGSA）机制，融合语义和几何特征，利用边缘信息缓解负面交互，提升透明物体感知。
3. 引入多模态渐进式训练，从RGB边缘到预测深度边缘，无需ground-truth深度即可引导学习，并在Syn-TODD和ClearPose上验证有效性。

## 📝 摘要（中文）

透明物体感知是计算机视觉研究中的一个主要挑战，因为透明性会混淆深度估计和语义分割。最近的研究探索了多任务学习框架以提高鲁棒性，但负面的跨任务交互通常会阻碍性能。本文提出了一种边缘引导空间注意力（EGSA）融合机制，旨在通过将边界信息整合到语义和几何特征之间的融合中来减轻破坏性交互。在Syn-TODD和ClearPose基准测试中，EGSA始终优于当前最先进的方法（MODEST），提高了深度精度，同时保持了具有竞争力的分割性能，并且在透明区域的改进最为显著。除了融合设计之外，本文的第二个贡献是一种多模态渐进式训练策略，其中学习从RGB图像导出的边缘过渡到从预测深度图像导出的边缘。这种方法允许系统从RGB图像中包含的丰富纹理中引导学习，然后切换到深度图中更相关的几何内容，同时消除了训练时对ground-truth深度的需求。总之，这些贡献突出了边缘引导融合作为一种能够提高透明物体感知的鲁棒方法。

## 🔬 方法详解

**问题定义**：透明物体的深度估计和语义分割是计算机视觉中的难点。由于透明物体缺乏纹理和颜色信息，传统方法难以准确估计其深度和进行分割。现有的多任务学习方法试图同时解决这两个问题，但常常受到负面跨任务交互的影响，导致性能下降。

**核心思路**：论文的核心思路是利用边缘信息来引导特征融合，从而减轻负面跨任务交互。具体来说，通过边缘引导空间注意力（EGSA）机制，将边缘信息整合到语义和几何特征的融合中，使得模型能够更加关注物体的边界，从而提高深度估计和分割的准确性。此外，采用多模态渐进式训练策略，逐步引导模型学习，避免了对ground-truth深度的依赖。

**技术框架**：整体框架包含深度估计和语义分割两个分支，以及EGSA融合模块和渐进式训练策略。首先，RGB图像分别输入到深度估计和语义分割网络中，提取几何特征和语义特征。然后，EGSA模块利用边缘信息对这两个特征进行融合，得到融合后的特征。最后，利用融合后的特征进行深度估计和语义分割。渐进式训练策略分为两个阶段：第一阶段，使用RGB图像的边缘信息进行训练；第二阶段，使用预测深度图像的边缘信息进行训练。

**关键创新**：论文的关键创新在于提出了边缘引导空间注意力（EGSA）机制和多模态渐进式训练策略。EGSA机制能够有效地融合语义和几何特征，并利用边缘信息来引导特征融合，从而提高深度估计和分割的准确性。多模态渐进式训练策略能够逐步引导模型学习，避免了对ground-truth深度的依赖，并且能够利用RGB图像和深度图像的互补信息。

**关键设计**：EGSA模块使用空间注意力机制，根据边缘信息对特征图的不同区域进行加权。边缘信息通过Canny边缘检测器从RGB图像或预测深度图像中提取。损失函数包括深度估计损失和语义分割损失。深度估计损失采用L1损失或Smooth L1损失。语义分割损失采用交叉熵损失。网络结构可以采用各种现有的深度估计和语义分割网络，例如ResNet、UNet等。渐进式训练策略中，两个阶段的训练轮数和学习率需要根据具体数据集进行调整。

## 📊 实验亮点

EGSA在Syn-TODD和ClearPose数据集上均优于当前最先进的方法MODEST，尤其在透明区域的深度估计精度提升显著。在保持分割性能的同时，深度估计精度得到了有效提高，证明了边缘引导融合策略的有效性。此外，提出的渐进式训练策略无需ground-truth深度即可实现有效训练。

## 🎯 应用场景

该研究成果可应用于机器人、自动驾驶、增强现实等领域。例如，在机器人抓取透明物体时，准确的深度估计和分割是至关重要的。在自动驾驶中，识别透明物体（如玻璃、水面）有助于提高安全性。在增强现实中，可以实现更逼真的透明物体渲染。

## 📄 摘要（原文）

> Transparent object perception remains a major challenge in computer vision research, as transparency confounds both depth estimation and semantic segmentation. Recent work has explored multi-task learning frameworks to improve robustness, yet negative cross-task interactions often hinder performance. In this work, we introduce Edge-Guided Spatial Attention (EGSA), a fusion mechanism designed to mitigate destructive interactions by incorporating boundary information into the fusion between semantic and geometric features. On both Syn-TODD and ClearPose benchmarks, EGSA consistently improved depth accuracy over the current state of the art method (MODEST), while preserving competitive segmentation performance, with the largest improvements appearing in transparent regions. Besides our fusion design, our second contribution is a multi-modal progressive training strategy, where learning transitions from edges derived from RGB images to edges derived from predicted depth images. This approach allows the system to bootstrap learning from the rich textures contained in RGB images, and then switch to more relevant geometric content in depth maps, while it eliminates the need for ground-truth depth at training time. Together, these contributions highlight edge-guided fusion as a robust approach capable of improving transparent object perception.

