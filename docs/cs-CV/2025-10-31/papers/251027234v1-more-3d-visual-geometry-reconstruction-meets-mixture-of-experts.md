---
layout: default
title: MoRE: 3D Visual Geometry Reconstruction Meets Mixture-of-Experts
---

# MoRE: 3D Visual Geometry Reconstruction Meets Mixture-of-Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27234" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27234v1</a>
  <a href="https://arxiv.org/pdf/2510.27234.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27234v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27234v1', 'MoRE: 3D Visual Geometry Reconstruction Meets Mixture-of-Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingnan Gao, Zhe Wang, Xianze Fang, Xingyu Ren, Zhuo Chen, Shengqi Liu, Yuhao Cheng, Jiangjing Lyu, Xiaokang Yang, Yichao Yan

**分类**: cs.CV

**发布日期**: 2025-10-31

**备注**: Project Page: https://g-1nonly.github.io/MoRE_Website/, Code: https://github.com/alibaba/Taobao3D

---

## 💡 一句话要点

**提出MoRE：基于混合专家模型的3D视觉几何重建框架，提升可扩展性和适应性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D视觉几何重建` `混合专家模型` `深度学习` `模型扩展` `鲁棒性` `表面法线预测` `置信度深度细化`

## 📋 核心要点

1. 现有3D视觉几何重建模型难以进一步扩展，受限于几何监督的复杂性和3D数据的多样性。
2. MoRE采用混合专家模型，动态路由特征到特定任务专家，提升模型对不同数据特征的适应性和可扩展性。
3. MoRE通过置信度深度细化模块和定制损失函数，在多个基准测试中达到SOTA，并支持下游应用。

## 📝 摘要（中文）

本文提出了一种名为MoRE的密集3D视觉基础模型，该模型基于混合专家(MoE)架构，能够动态地将特征路由到特定任务的专家，从而使专家能够专注于互补的数据方面，并增强模型的可扩展性和适应性。为了提高在真实世界条件下的鲁棒性，MoRE包含一个基于置信度的深度细化模块，该模块可以稳定和细化几何估计。此外，它还集成了密集语义特征与全局对齐的3D骨干表示，以实现高保真度的表面法线预测。MoRE通过定制的损失函数进行进一步优化，以确保跨不同输入和多个几何任务的鲁棒学习。大量实验表明，MoRE在多个基准测试中实现了最先进的性能，并支持有效的下游应用，而无需额外的计算。

## 🔬 方法详解

**问题定义**：论文旨在解决3D视觉几何重建中模型扩展的难题。现有方法在处理复杂几何监督和多样化3D数据时面临挑战，难以进一步提升性能。模型规模的扩大受到限制，阻碍了3D视觉领域的发展。

**核心思路**：论文的核心思路是利用混合专家模型（MoE），将模型的能力分散到多个专家网络中，每个专家负责处理特定的数据特征或任务。通过动态路由机制，将输入特征分配给最合适的专家，从而提高模型的适应性和可扩展性。这种方法允许模型在不显著增加计算成本的情况下，学习更丰富的表示。

**技术框架**：MoRE的整体架构包含以下几个主要模块：1) 3D骨干网络：用于提取全局对齐的3D特征表示。2) 混合专家层：包含多个专家网络，每个专家专门处理特定的数据方面。3) 动态路由机制：根据输入特征的特性，将特征路由到最合适的专家。4) 置信度深度细化模块：用于稳定和细化几何估计，提高鲁棒性。5) 表面法线预测模块：集成了密集语义特征，用于高保真度的表面法线预测。

**关键创新**：MoRE的关键创新在于将混合专家模型引入到3D视觉几何重建领域。与传统的单一模型相比，MoRE能够动态地调整模型的结构，以适应不同的输入数据和任务。此外，置信度深度细化模块和表面法线预测模块也进一步提高了模型的性能和鲁棒性。

**关键设计**：MoRE的关键设计包括：1) 专家网络的数量和结构：根据任务的复杂度和数据的多样性进行调整。2) 动态路由机制的设计：采用可学习的路由函数，根据输入特征的特性进行路由。3) 损失函数的设计：采用定制的损失函数，以确保跨不同输入和多个几何任务的鲁棒学习。例如，可能包括深度预测损失、表面法线预测损失和语义分割损失等。

## 📊 实验亮点

MoRE在多个3D视觉几何重建基准测试中取得了最先进的性能。具体而言，MoRE在深度预测、表面法线预测等任务上显著优于现有方法。实验结果表明，MoRE能够有效地利用混合专家模型，提高模型的适应性和可扩展性，从而实现更高的精度和鲁棒性。此外，MoRE还支持有效的下游应用，而无需额外的计算。

## 🎯 应用场景

MoRE在机器人导航、自动驾驶、虚拟现实、增强现实、3D建模等领域具有广泛的应用前景。它可以用于构建更精确、更鲁棒的3D环境模型，从而提高机器人的自主导航能力，改善自动驾驶系统的安全性，并为用户提供更沉浸式的虚拟现实和增强现实体验。此外，MoRE还可以用于生成高质量的3D模型，应用于游戏开发、电影制作等领域。

## 📄 摘要（原文）

> Recent advances in language and vision have demonstrated that scaling up model capacity consistently improves performance across diverse tasks. In 3D visual geometry reconstruction, large-scale training has likewise proven effective for learning versatile representations. However, further scaling of 3D models is challenging due to the complexity of geometric supervision and the diversity of 3D data. To overcome these limitations, we propose MoRE, a dense 3D visual foundation model based on a Mixture-of-Experts (MoE) architecture that dynamically routes features to task-specific experts, allowing them to specialize in complementary data aspects and enhance both scalability and adaptability. Aiming to improve robustness under real-world conditions, MoRE incorporates a confidence-based depth refinement module that stabilizes and refines geometric estimation. In addition, it integrates dense semantic features with globally aligned 3D backbone representations for high-fidelity surface normal prediction. MoRE is further optimized with tailored loss functions to ensure robust learning across diverse inputs and multiple geometric tasks. Extensive experiments demonstrate that MoRE achieves state-of-the-art performance across multiple benchmarks and supports effective downstream applications without extra computation.

