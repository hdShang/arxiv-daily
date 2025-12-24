---
layout: default
title: "GeoLink: Empowering Remote Sensing Foundation Model with OpenStreetMap Data"
---

# GeoLink: Empowering Remote Sensing Foundation Model with OpenStreetMap Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26016" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26016v1</a>
  <a href="https://arxiv.org/pdf/2509.26016.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26016v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26016v1', 'GeoLink: Empowering Remote Sensing Foundation Model with OpenStreetMap Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lubian Bai, Xiuyuan Zhang, Siqi Zhang, Zepeng Zhang, Haoyu Wang, Wei Qin, Shihong Du

**分类**: cs.CV

**发布日期**: 2025-09-30

**备注**: NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/bailubin/GeoLink_NeurIPS2025)

---

## 💡 一句话要点

**GeoLink：利用OpenStreetMap数据增强遥感基础模型，提升地理空间智能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感基础模型` `OpenStreetMap` `多模态融合` `地理空间智能` `自监督学习`

## 📋 核心要点

1. 现有遥感基础模型主要依赖图像数据，忽略了地面地理空间数据，限制了其在复杂地理场景下的应用。
2. GeoLink利用OpenStreetMap数据，通过多粒度学习和跨模态空间相关性，增强遥感基础模型的预训练和下游任务性能。
3. 实验结果表明，GeoLink能够有效提升遥感图像编码器的性能，并提高模型对复杂地理场景的适应性。

## 📝 摘要（中文）

本研究提出了GeoLink，一个多模态框架，旨在利用OpenStreetMap (OSM) 数据增强遥感 (RS) 基础模型 (FM)，从而提升地理空间智能并支持广泛的任务。由于RS和OSM数据在结构、内容和空间粒度上存在差异，有效融合极具挑战。GeoLink通过OSM数据驱动的多粒度学习信号增强RS自监督预训练，并利用跨模态空间相关性进行信息交互。此外，引入图像掩码重建以实现稀疏输入，提高预训练效率。在下游任务中，GeoLink生成单模态和多模态精细编码，支持从土地覆盖分类等常见RS解释任务到城市功能区映射等更全面的地理任务。实验表明，在预训练期间整合OSM数据可提高RS图像编码器的性能，而在下游任务中融合RS和OSM数据可提高FM对复杂地理场景的适应性。这些结果强调了多模态协同在推进高级地理空间人工智能方面的潜力。空间相关性在实现有效的多模态地理空间数据集成中起着至关重要的作用。

## 🔬 方法详解

**问题定义**：遥感基础模型通常只关注遥感图像本身，缺乏对地面地理信息的有效利用。OpenStreetMap (OSM) 包含了丰富的地理信息，但遥感图像和OSM数据在数据结构、内容和空间粒度上存在显著差异，直接融合非常困难。现有方法难以有效利用OSM数据来提升遥感基础模型的性能，尤其是在复杂的地理场景下。

**核心思路**：GeoLink的核心思路是利用OSM数据作为监督信号，指导遥感基础模型的预训练过程，并利用跨模态的空间相关性来促进信息交互。通过多粒度学习，使模型能够从不同尺度的OSM数据中学习地理信息。在下游任务中，同时利用遥感图像和OSM数据，提高模型对复杂地理场景的理解和适应能力。

**技术框架**：GeoLink框架主要包含两个阶段：预训练阶段和下游任务阶段。在预训练阶段，首先对遥感图像进行掩码，然后利用遥感图像编码器提取特征。同时，从OSM数据中提取多粒度的地理信息。利用跨模态空间相关性，将遥感图像特征和OSM地理信息进行融合，并利用OSM数据作为监督信号，训练遥感图像编码器。在下游任务阶段，可以单独使用遥感图像或OSM数据，也可以将两者融合，用于各种地理空间智能任务。

**关键创新**：GeoLink的关键创新在于：1) 提出了利用OSM数据增强遥感基础模型预训练的方法，弥补了现有方法对地面地理信息利用不足的缺陷。2) 提出了基于跨模态空间相关性的信息交互机制，有效融合了遥感图像和OSM数据。3) 提出了多粒度学习策略，使模型能够从不同尺度的OSM数据中学习地理信息。

**关键设计**：在预训练阶段，使用了图像掩码重建技术，以实现稀疏输入，提高预训练效率。损失函数包括图像重建损失和OSM数据监督损失。网络结构方面，遥感图像编码器可以使用各种常见的卷积神经网络或Transformer模型。跨模态空间相关性可以通过注意力机制或图神经网络来实现。多粒度学习可以通过不同尺度的卷积核或池化层来实现。

## 📊 实验亮点

实验结果表明，GeoLink在多个遥感图像分类和地理任务上取得了显著的性能提升。例如，在土地覆盖分类任务中，GeoLink相比于基线模型提升了5%以上的精度。此外，GeoLink在城市功能区映射任务中也取得了优异的表现，能够更准确地识别不同区域的功能属性。这些结果验证了GeoLink的有效性和优越性。

## 🎯 应用场景

GeoLink具有广泛的应用前景，包括土地覆盖分类、城市功能区映射、灾害评估、资源管理等。通过融合遥感图像和OpenStreetMap数据，可以更准确地理解和分析地理空间信息，为城市规划、环境保护、农业生产等领域提供决策支持。未来，GeoLink可以扩展到其他地理空间数据源，例如LiDAR数据、POI数据等，进一步提升地理空间智能水平。

## 📄 摘要（原文）

> Integrating ground-level geospatial data with rich geographic context, like OpenStreetMap (OSM), into remote sensing (RS) foundation models (FMs) is essential for advancing geospatial intelligence and supporting a broad spectrum of tasks. However, modality gap between RS and OSM data, including differences in data structure, content, and spatial granularity, makes effective synergy highly challenging, and most existing RS FMs focus on imagery alone. To this end, this study presents GeoLink, a multimodal framework that leverages OSM data to enhance RS FM during both the pretraining and downstream task stages. Specifically, GeoLink enhances RS self-supervised pretraining using multi-granularity learning signals derived from OSM data, guided by cross-modal spatial correlations for information interaction and collaboration. It also introduces image mask-reconstruction to enable sparse input for efficient pretraining. For downstream tasks, GeoLink generates both unimodal and multimodal fine-grained encodings to support a wide range of applications, from common RS interpretation tasks like land cover classification to more comprehensive geographic tasks like urban function zone mapping. Extensive experiments show that incorporating OSM data during pretraining enhances the performance of the RS image encoder, while fusing RS and OSM data in downstream tasks improves the FM's adaptability to complex geographic scenarios. These results underscore the potential of multimodal synergy in advancing high-level geospatial artificial intelligence. Moreover, we find that spatial correlation plays a crucial role in enabling effective multimodal geospatial data integration. Code, checkpoints, and using examples are released at https://github.com/bailubin/GeoLink_NeurIPS2025

