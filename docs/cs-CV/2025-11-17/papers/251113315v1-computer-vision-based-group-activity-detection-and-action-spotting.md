---
layout: default
title: Computer Vision based group activity detection and action spotting
---

# Computer Vision based group activity detection and action spotting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13315" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13315v1</a>
  <a href="https://arxiv.org/pdf/2511.13315.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13315v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.13315v1', 'Computer Vision based group activity detection and action spotting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Narthana Sivalingam, Santhirarajah Sivasthigan, Thamayanthi Mahendranathan, G. M. R. I. Godaliyadda, M. P. B. Ekanayake, H. M. V. R. Herath

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-17

---

## 💡 一句话要点

**提出基于计算机视觉的群体活动检测与行为定位框架，融合深度学习与图推理。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `群体活动检测` `行为定位` `图神经网络` `关系推理` `计算机视觉` `深度学习` `实例分割`

## 📋 核心要点

1. 群体活动检测面临复杂交互、遮挡和外观变化等挑战，现有方法难以有效建模个体关系。
2. 本文提出结合Mask R-CNN进行个体分割，构建Actor Relation Graph建模个体关系，并用GCN进行推理。
3. 实验表明，该方法在Collective Activity数据集上表现出优越的识别性能，尤其是在拥挤场景下。

## 📝 摘要（中文）

本文提出了一种基于计算机视觉的框架，用于群体活动识别和行为定位，该框架结合了深度学习模型和基于图的关系推理。系统首先使用Mask R-CNN通过边界框和实例分割掩码来实现精确的个体定位。然后，使用包括Inception V3、MobileNet和VGG16在内的多个骨干网络来提取特征图，并应用RoIAlign来保持生成个体特定特征时的空间对齐。掩码信息与特征图融合，以获得每个个体的精细化掩码特征表示。为了建模个体之间的交互，我们构建了Actor Relation Graphs，使用归一化互相关、绝对差之和以及点积等方法来编码外观相似性和位置关系。图卷积网络作用于这些图，以推理关系并预测个体行为和群体层面的活动。在Collective Activity数据集上的实验表明，基于掩码的特征精细化、鲁棒的相似性搜索和图神经网络推理的结合，提高了拥挤和非拥挤场景下的识别性能。该方法突出了集成分割、特征提取和关系图推理在复杂视频理解任务中的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决多人场景下的群体活动检测和行为定位问题。现有方法在处理复杂的人际交互、遮挡以及个体外观随时间变化时存在不足，难以准确识别群体活动和个体行为。

**核心思路**：论文的核心思路是结合深度学习的检测分割能力和图神经网络的关系推理能力。首先利用Mask R-CNN进行精确的个体检测和分割，然后构建Actor Relation Graph来显式地建模个体之间的关系，最后利用图卷积网络进行关系推理，从而实现更准确的群体活动识别。

**技术框架**：该框架主要包含三个阶段：1) 个体检测与分割：使用Mask R-CNN检测和分割视频中的个体，获得边界框和实例掩码。2) 特征提取与融合：使用多个骨干网络（如Inception V3、MobileNet、VGG16）提取特征图，并利用RoIAlign保持空间对齐。将掩码信息与特征图融合，得到精细化的个体特征表示。3) 关系建模与推理：构建Actor Relation Graph，节点表示个体，边表示个体之间的关系（如外观相似性和位置关系）。使用图卷积网络在图上进行推理，预测个体行为和群体活动。

**关键创新**：该方法最重要的创新点在于将实例分割信息与图神经网络相结合，显式地建模个体之间的关系。通过融合掩码信息，可以获得更精确的个体特征表示，从而提高关系推理的准确性。此外，使用Actor Relation Graph能够有效地捕捉个体之间的交互模式，从而更好地理解群体活动。

**关键设计**：在构建Actor Relation Graph时，使用归一化互相关、绝对差之和以及点积等方法来计算个体之间的外观相似性。位置关系则通过计算个体之间的相对位置来表示。图卷积网络的具体结构和参数设置未知，损失函数也未知。

## 📊 实验亮点

实验结果表明，该方法在Collective Activity数据集上取得了显著的性能提升。通过结合掩码信息和图神经网络，该方法能够更准确地识别群体活动和个体行为，尤其是在拥挤场景下。具体的性能数据和对比基线未知，但摘要强调了该方法在拥挤和非拥挤场景下的识别性能提升。

## 🎯 应用场景

该研究成果可应用于视频监控、智能安防、体育赛事分析、社交行为分析等领域。例如，在视频监控中，可以自动检测异常群体行为，提高安全预警能力。在体育赛事分析中，可以识别运动员的战术配合，为教练提供决策支持。该研究有助于提升计算机对复杂场景的理解能力，具有重要的实际应用价值。

## 📄 摘要（原文）

> Group activity detection in multi-person scenes is challenging due to complex human interactions, occlusions, and variations in appearance over time. This work presents a computer vision based framework for group activity recognition and action spotting using a combination of deep learning models and graph based relational reasoning. The system first applies Mask R-CNN to obtain accurate actor localization through bounding boxes and instance masks. Multiple backbone networks, including Inception V3, MobileNet, and VGG16, are used to extract feature maps, and RoIAlign is applied to preserve spatial alignment when generating actor specific features. The mask information is then fused with the feature maps to obtain refined masked feature representations for each actor. To model interactions between individuals, we construct Actor Relation Graphs that encode appearance similarity and positional relations using methods such as normalized cross correlation, sum of absolute differences, and dot product. Graph Convolutional Networks operate on these graphs to reason about relationships and predict both individual actions and group level activities. Experiments on the Collective Activity dataset demonstrate that the combination of mask based feature refinement, robust similarity search, and graph neural network reasoning leads to improved recognition performance across both crowded and non crowded scenarios. This approach highlights the potential of integrating segmentation, feature extraction, and relational graph reasoning for complex video understanding tasks.

