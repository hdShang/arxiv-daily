---
layout: default
title: "DACoN: DINO for Anime Paint Bucket Colorization with Any Number of Reference Images"
---

# DACoN: DINO for Anime Paint Bucket Colorization with Any Number of Reference Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14685" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14685v2</a>
  <a href="https://arxiv.org/pdf/2509.14685.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14685v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14685v2', 'DACoN: DINO for Anime Paint Bucket Colorization with Any Number of Reference Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kazuma Nagata, Naoshi Kaneko

**分类**: cs.CV

**发布日期**: 2025-09-18 (更新: 2025-10-01)

**备注**: Accepted to ICCV 2025. v2: Added results on the subset used by the baseline for consistency; full test set results are also reported (Tables 1 and 2)

**🔗 代码/项目**: [GITHUB](https://github.com/kzmngt/DACoN)

---

## 💡 一句话要点

**DACoN：利用DINO和任意数量参考图像的动漫线稿自动着色**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动漫着色` `线稿着色` `深度学习` `视觉基础模型` `特征融合`

## 📋 核心要点

1. 现有动漫线稿着色方法难以处理遮挡、姿势变化和视角变化等复杂情况。
2. DACoN融合基础模型的语义特征和CNN的空间特征，实现更鲁棒的特征提取，提升着色效果。
3. DACoN突破了参考图像数量的限制，支持任意数量的参考图像，显著提升着色性能。

## 📝 摘要（中文）

为了降低手绘动漫制作的人工成本，线稿自动着色技术得到了广泛研究。深度学习方法，包括图像/视频生成和基于特征的对应，提高了着色精度，但仍难以处理遮挡、姿势变化和视角变化等问题。为了解决这些挑战，我们提出了DACoN，一个利用基础模型捕获部件级语义信息的框架，即使是在线稿中也能有效工作。我们的方法融合了来自基础模型的低分辨率语义特征和来自CNN的高分辨率空间特征，以实现细粒度且鲁棒的特征提取。与之前依赖Multiplex Transformer且仅支持一到两张参考图像的方法不同，DACoN消除了这一限制，允许使用任意数量的参考图像。定量和定性评估表明，使用多个参考图像的优势明显，实现了卓越的着色性能。我们的代码和模型已在https://github.com/kzmngt/DACoN上提供。

## 🔬 方法详解

**问题定义**：论文旨在解决动漫线稿自动着色问题，现有方法在处理遮挡、姿势变化和视角变化时表现不佳，且大多限制了参考图像的数量，影响着色效果。这些痛点限制了自动着色技术在实际动漫制作中的应用。

**核心思路**：DACoN的核心思路是利用预训练的视觉基础模型（如DINO）提取线稿的语义信息，并将其与CNN提取的空间信息融合，从而获得更全面、鲁棒的特征表示。同时，解除参考图像数量的限制，允许模型利用多张参考图像的信息进行着色。

**技术框架**：DACoN的整体框架包含以下几个主要模块：1) 使用DINO等基础模型提取线稿的低分辨率语义特征；2) 使用CNN提取线稿的高分辨率空间特征；3) 设计特征融合模块，将语义特征和空间特征进行有效融合；4) 使用着色网络，根据融合后的特征和参考图像进行着色。整个流程旨在充分利用不同来源的信息，提升着色质量。

**关键创新**：DACoN的关键创新在于：1) 利用视觉基础模型提取线稿的语义信息，增强了模型对线稿的理解能力；2) 解除了参考图像数量的限制，允许模型利用多张参考图像的信息，提升了着色效果；3) 设计了有效的特征融合模块，将语义特征和空间特征进行有效融合，避免了信息损失。

**关键设计**：DACoN的关键设计包括：1) 选择合适的视觉基础模型，并对其进行微调，以适应线稿着色任务；2) 设计合适的特征融合策略，例如使用注意力机制或卷积操作，将语义特征和空间特征进行有效融合；3) 设计合适的损失函数，例如使用像素级别的L1或L2损失，以及感知损失，以提升着色质量。

## 📊 实验亮点

DACoN通过定量和定性实验验证了其有效性。实验结果表明，使用多个参考图像可以显著提升着色性能。与现有方法相比，DACoN在着色质量和视觉效果上均有明显提升。具体性能数据（如PSNR、SSIM等）在论文中进行了详细展示。

## 🎯 应用场景

DACoN可应用于动漫制作、游戏美术、插画设计等领域，降低人工着色成本，提高生产效率。该研究的突破在于利用基础模型理解线稿语义，为其他图像生成任务提供了借鉴。未来，DACoN有望扩展到视频着色、风格迁移等更广泛的应用场景。

## 📄 摘要（原文）

> Automatic colorization of line drawings has been widely studied to reduce the labor cost of hand-drawn anime production. Deep learning approaches, including image/video generation and feature-based correspondence, have improved accuracy but struggle with occlusions, pose variations, and viewpoint changes. To address these challenges, we propose DACoN, a framework that leverages foundation models to capture part-level semantics, even in line drawings. Our method fuses low-resolution semantic features from foundation models with high-resolution spatial features from CNNs for fine-grained yet robust feature extraction. In contrast to previous methods that rely on the Multiplex Transformer and support only one or two reference images, DACoN removes this constraint, allowing any number of references. Quantitative and qualitative evaluations demonstrate the benefits of using multiple reference images, achieving superior colorization performance. Our code and model are available at https://github.com/kzmngt/DACoN.

