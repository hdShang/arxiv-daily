---
layout: default
title: Thinking with Camera: A Unified Multimodal Model for Camera-Centric Understanding and Generation
---

# Thinking with Camera: A Unified Multimodal Model for Camera-Centric Understanding and Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08673" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08673v1</a>
  <a href="https://arxiv.org/pdf/2510.08673.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08673v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.08673v1', 'Thinking with Camera: A Unified Multimodal Model for Camera-Centric Understanding and Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kang Liao, Size Wu, Zhonghua Wu, Linyi Jin, Chao Wang, Yikai Wang, Fei Wang, Wei Li, Chen Change Loy

**分类**: cs.CV

**发布日期**: 2025-10-09

**备注**: Project Page: https://kangliao929.github.io/projects/puffin/

---

## 💡 一句话要点

**Puffin：提出统一的多模态模型，实现相机视角的理解与生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `相机视角` `多模态学习` `视觉语言模型` `扩散模型` `空间智能` `相机参数估计` `跨视角生成`

## 📋 核心要点

1. 现有方法通常孤立地研究以相机为中心的理解和生成，忽略了它们之间的联系。
2. Puffin将相机视为一种语言，通过语言回归和扩散生成，统一理解和生成任务。
3. Puffin在Puffin-4M数据集上训练，实验表明其在相机中心任务上优于专用模型。

## 📝 摘要（中文）

本文提出Puffin，一个统一的、以相机为中心的多模态模型，旨在扩展相机维度的空间感知能力。Puffin集成了语言回归和基于扩散的生成方法，能够从任意视角解释和创建场景。为了弥合相机和视觉-语言之间的模态差距，本文引入了一种新颖的范例，将相机视为一种语言，从而实现“用相机思考”。这引导模型将空间相关的视觉线索与摄影术语对齐，同时进行跨几何上下文的推理。Puffin在包含400万个视觉-语言-相机三元组的大规模数据集Puffin-4M上进行训练。模型同时结合了全局相机参数和像素级相机地图，从而产生灵活可靠的空间生成结果。实验表明，Puffin在相机中心生成和理解方面优于专门的模型。通过指令微调，Puffin可以泛化到各种跨视角任务，例如空间想象、世界探索和摄影指导。代码、模型、数据集管道和基准测试将开源，以推进多模态空间智能研究。

## 🔬 方法详解

**问题定义**：现有方法通常将以相机为中心的理解和生成任务孤立地研究，缺乏统一的框架来整合这两种能力。这限制了模型在复杂空间推理和跨视角任务中的表现。此外，如何有效地弥合相机参数和视觉信息之间的模态差距也是一个挑战。

**核心思路**：Puffin的核心思路是将相机参数视为一种语言，通过学习相机“语言”与视觉信息之间的对应关系，实现以相机为中心的理解和生成。这种方法允许模型利用摄影术语和几何上下文进行推理，从而提高空间感知的准确性和可靠性。

**技术框架**：Puffin的整体架构包含两个主要模块：语言回归模块和基于扩散的生成模块。语言回归模块用于理解场景并预测相机参数，而扩散生成模块则根据给定的相机参数和文本描述生成图像。这两个模块通过共享的视觉编码器和相机“语言”嵌入空间进行连接，实现信息的有效传递和融合。

**关键创新**：Puffin最重要的技术创新在于将相机参数视为一种语言，并设计了一种新的范例来实现“用相机思考”。这种方法不仅弥合了相机和视觉-语言之间的模态差距，还允许模型利用摄影知识和几何约束进行推理，从而提高了生成图像的质量和一致性。

**关键设计**：Puffin的关键设计包括：1) 使用全局相机参数和像素级相机地图来表示相机姿态；2) 设计了一种新的相机“语言”嵌入方法，将相机参数映射到语义空间；3) 使用大规模数据集Puffin-4M进行训练，以提高模型的泛化能力；4) 使用指令微调来增强模型在各种跨视角任务中的表现。

## 📊 实验亮点

实验结果表明，Puffin在相机中心生成和理解任务上均取得了优异的性能，显著优于专门的模型。例如，在跨视角图像生成任务中，Puffin生成的图像在视觉质量和空间一致性方面均优于基线模型。通过指令微调，Puffin在空间想象、世界探索和摄影指导等任务中也展现出强大的泛化能力。

## 🎯 应用场景

Puffin具有广泛的应用前景，包括虚拟现实、增强现实、机器人导航、自动驾驶、摄影辅助等领域。它可以帮助用户在虚拟环境中自由探索，指导机器人进行空间推理和导航，辅助摄影师进行构图和拍摄，并为自动驾驶系统提供更准确的环境感知能力。未来，Puffin有望成为空间智能领域的重要基石。

## 📄 摘要（原文）

> Camera-centric understanding and generation are two cornerstones of spatial intelligence, yet they are typically studied in isolation. We present Puffin, a unified camera-centric multimodal model that extends spatial awareness along the camera dimension. Puffin integrates language regression and diffusion-based generation to interpret and create scenes from arbitrary viewpoints. To bridge the modality gap between cameras and vision-language, we introduce a novel paradigm that treats camera as language, enabling thinking with camera. This guides the model to align spatially grounded visual cues with photographic terminology while reasoning across geometric context. Puffin is trained on Puffin-4M, a large-scale dataset of 4 million vision-language-camera triplets. We incorporate both global camera parameters and pixel-wise camera maps, yielding flexible and reliable spatial generation. Experiments demonstrate Puffin superior performance over specialized models for camera-centric generation and understanding. With instruction tuning, Puffin generalizes to diverse cross-view tasks such as spatial imagination, world exploration, and photography guidance. We will release the code, models, dataset pipeline, and benchmark to advance multimodal spatial intelligence research.

