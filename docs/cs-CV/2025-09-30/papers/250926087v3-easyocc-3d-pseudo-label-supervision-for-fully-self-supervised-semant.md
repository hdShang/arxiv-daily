---
layout: default
title: "EasyOcc: 3D Pseudo-Label Supervision for Fully Self-Supervised Semantic Occupancy Prediction Models"
---

# EasyOcc: 3D Pseudo-Label Supervision for Fully Self-Supervised Semantic Occupancy Prediction Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26087" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26087v3</a>
  <a href="https://arxiv.org/pdf/2509.26087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26087v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26087v3', 'EasyOcc: 3D Pseudo-Label Supervision for Fully Self-Supervised Semantic Occupancy Prediction Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seamie Hayes, Ganesh Sistu, Ciarán Eising

**分类**: cs.CV

**发布日期**: 2025-09-30 (更新: 2025-11-27)

---

## 💡 一句话要点

**EasyOcc：利用3D伪标签监督实现全自监督语义占据预测模型**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语义占据预测` `自监督学习` `3D伪标签` `视觉基础模型` `时间信息融合`

## 📋 核心要点

1. 现有自监督语义占据预测模型依赖复杂的新视角合成等技术，导致计算成本高昂和内存占用大。
2. 论文提出利用Grounded-SAM和Metric3Dv2等基础模型生成3D伪标签，并结合时间信息进行标签稠密化，降低计算复杂度。
3. 实验表明，该方法能显著提升现有模型的性能，例如在OccNeRF上mIoU提升45%，并提出了一个更高效的模型EasyOcc。

## 📝 摘要（中文）

自监督模型在语义占据预测领域取得了显著进展。这些模型利用复杂的损失计算策略来弥补真实标签的缺失。例如，新视角合成、跨视角渲染和深度估计等技术已被用于解决语义和深度模糊问题。然而，这些技术通常在训练阶段产生高昂的计算成本和内存使用，尤其是在新视角合成的情况下。为了缓解这些问题，我们提出了由基础模型Grounded-SAM和Metric3Dv2生成的3D伪真值标签，并利用时间信息进行标签稠密化。我们的3D伪标签可以轻松集成到现有模型中，从而显著提高性能，当应用于OccNeRF模型时，mIoU从9.73提高到14.09，提升了45%。此外，我们提出了一个简化的模型EasyOcc，实现了13.86的mIoU。该模型仅从我们的标签中学习，避免了前面提到的复杂渲染策略。此外，我们的方法使模型能够在完整场景上评估时达到最先进的性能，而无需应用相机掩码，EasyOcc实现了7.71的mIoU，优于之前的最佳模型31%。这些发现突出了基础模型、时间上下文和损失计算空间的选择在自监督学习中对于全面场景理解的关键重要性。

## 🔬 方法详解

**问题定义**：现有的自监督语义占据预测方法，例如基于新视角合成的方法，在训练过程中需要大量的计算资源和内存，限制了其应用范围和效率。这些方法通常需要复杂的渲染策略来解决语义和深度模糊问题，导致训练过程缓慢且难以扩展。

**核心思路**：论文的核心思路是利用预训练的视觉基础模型（如Grounded-SAM和Metric3Dv2）生成高质量的3D伪标签，并结合时间信息来提高标签的稠密度。通过使用这些伪标签作为监督信号，模型可以学习到场景的语义占据信息，而无需依赖复杂的渲染过程。这样可以显著降低计算成本和内存需求，并提高训练效率。

**技术框架**：整体框架包括以下几个主要步骤：1) 使用Grounded-SAM和Metric3Dv2等基础模型生成初始的3D伪标签。2) 利用时间信息，例如连续帧之间的信息，对伪标签进行稠密化和优化，以减少噪声和提高准确性。3) 使用生成的3D伪标签作为监督信号，训练语义占据预测模型。4) 提出一个简化的模型EasyOcc，直接从伪标签中学习，避免了复杂的渲染策略。

**关键创新**：最重要的技术创新点在于利用预训练的视觉基础模型生成高质量的3D伪标签，并将其应用于自监督语义占据预测任务。与传统的自监督方法相比，该方法避免了复杂的渲染过程，降低了计算成本和内存需求。此外，利用时间信息进行标签稠密化也提高了伪标签的质量和模型的性能。

**关键设计**：论文的关键设计包括：1) 选择合适的视觉基础模型（Grounded-SAM和Metric3Dv2）来生成3D伪标签。2) 设计有效的时间信息融合策略，以提高标签的稠密度和准确性。3) 设计一个简化的模型EasyOcc，使其能够有效地从伪标签中学习。4) 损失函数的设计需要考虑伪标签的噪声和不确定性，例如可以使用鲁棒的损失函数或引入置信度加权。

## 📊 实验亮点

实验结果表明，该方法能够显著提升现有自监督语义占据预测模型的性能。例如，在OccNeRF模型上应用该方法后，mIoU从9.73提高到14.09，提升了45%。此外，提出的简化模型EasyOcc也取得了13.86的mIoU，并且在完整场景评估中，EasyOcc实现了7.71的mIoU，优于之前的最佳模型31%。这些结果表明，该方法在自监督语义占据预测领域具有显著的优势。

## 🎯 应用场景

该研究成果可广泛应用于自动驾驶、机器人导航、增强现实等领域。通过高效的自监督学习，模型能够更好地理解周围环境，从而提高自动驾驶车辆的安全性，增强机器人的自主导航能力，并为用户提供更沉浸式的增强现实体验。此外，该方法还可以应用于三维重建、场景理解等任务。

## 📄 摘要（原文）

> Self-supervised models have recently achieved notable advancements, particularly in the domain of semantic occupancy prediction. These models utilize sophisticated loss computation strategies to compensate for the absence of ground-truth labels. For instance, techniques such as novel view synthesis, cross-view rendering, and depth estimation have been explored to address the issue of semantic and depth ambiguity. However, such techniques typically incur high computational costs and memory usage during the training stage, especially in the case of novel view synthesis. To mitigate these issues, we propose 3D pseudo-ground-truth labels generated by the foundation models Grounded-SAM and Metric3Dv2, and harness temporal information for label densification. Our 3D pseudo-labels can be easily integrated into existing models, which yields substantial performance improvements, with mIoU increasing by 45\%, from 9.73 to 14.09, when implemented into the OccNeRF model. This stands in contrast to earlier advancements in the field, which are often not readily transferable to other architectures. Additionally, we propose a streamlined model, EasyOcc, achieving 13.86 mIoU. This model conducts learning solely from our labels, avoiding complex rendering strategies mentioned previously. Furthermore, our method enables models to attain state-of-the-art performance when evaluated on the full scene without applying the camera mask, with EasyOcc achieving 7.71 mIoU, outperforming the previous best model by 31\%. These findings highlight the critical importance of foundation models, temporal context, and the choice of loss computation space in self-supervised learning for comprehensive scene understanding.

