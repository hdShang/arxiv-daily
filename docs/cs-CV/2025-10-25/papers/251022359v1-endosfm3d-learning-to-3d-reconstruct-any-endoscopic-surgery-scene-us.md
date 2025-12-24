---
layout: default
title: "EndoSfM3D: Learning to 3D Reconstruct Any Endoscopic Surgery Scene using Self-supervised Foundation Model"
---

# EndoSfM3D: Learning to 3D Reconstruct Any Endoscopic Surgery Scene using Self-supervised Foundation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22359" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22359v1</a>
  <a href="https://arxiv.org/pdf/2510.22359.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22359v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.22359v1', 'EndoSfM3D: Learning to 3D Reconstruct Any Endoscopic Surgery Scene using Self-supervised Foundation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changhao Zhang, Matthew J. Clarkson, Mobarak I. Hoque

**分类**: cs.CV

**发布日期**: 2025-10-25

**备注**: 11 pages

**🔗 代码/项目**: [GITHUB](https://github.com/MOYF-beta/EndoSfM3D)

---

## 💡 一句话要点

**EndoSfM3D：利用自监督基础模型学习内窥镜手术场景的3D重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内窥镜手术` `3D重建` `自监督学习` `单目深度估计` `固有参数估计` `深度学习` `姿态估计`

## 📋 核心要点

1. 现有内窥镜3D重建方法难以准确估计内窥镜的固有参数，限制了重建的准确性和可靠性。
2. 论文提出EndoSfM3D，通过自监督学习联合预测深度、姿态和内窥镜固有参数，实现更精确的3D重建。
3. 实验表明，该方法在公共数据集上优于现有自监督单目深度估计和3D重建方法，性能显著提升。

## 📝 摘要（中文）

内窥镜手术场景的3D重建在增强场景感知、实现AR可视化以及支持图像引导手术中上下文感知的决策制定方面起着至关重要的作用。该过程中的一个关键但具有挑战性的步骤是准确估计内窥镜的固有参数。在实际手术环境中，固有参数的标定受到无菌约束以及使用具有连续变焦和望远镜旋转的专用内窥镜的限制。大多数现有的内窥镜3D重建方法不估计固有参数，限制了它们在准确和可靠重建方面的有效性。在本文中，我们通过调整Depth Anything V2 (DA2)模型以进行联合深度、姿态和固有参数预测，将固有参数估计集成到自监督单目深度估计框架中。我们引入了一个基于注意力的姿态网络和一个权重分解低秩适应(DoRA)策略，用于DA2的有效微调。我们的方法在SCARED和C3VD公共数据集上进行了验证，证明了与最近最先进的自监督单目深度估计和3D重建方法相比，具有优越的性能。

## 🔬 方法详解

**问题定义**：内窥镜手术场景的3D重建需要准确的内窥镜固有参数，但实际手术中，内窥镜的无菌要求和特殊设计（连续变焦、望远镜旋转）使得传统标定方法难以应用。现有方法通常忽略或简化固有参数估计，导致重建精度受限。

**核心思路**：论文的核心在于将内窥镜固有参数估计融入到自监督单目深度估计框架中，通过深度、姿态和固有参数的联合预测，实现更准确的3D重建。利用自监督学习避免了对真实深度信息的依赖，适用于内窥镜手术场景。

**技术框架**：EndoSfM3D基于Depth Anything V2 (DA2)模型，并对其进行改进。整体流程包括：1) 使用DA2模型作为backbone提取图像特征；2) 利用改进的姿态网络预测相机姿态；3) 联合预测深度图和内窥镜固有参数；4) 使用自监督损失函数进行训练，优化深度、姿态和固有参数的预测。

**关键创新**：主要创新点在于：1) 将内窥镜固有参数估计集成到自监督单目深度估计框架中；2) 引入基于注意力的姿态网络，提升姿态估计的准确性；3) 采用权重分解低秩适应(DoRA)策略，高效地微调DA2模型，降低计算成本。

**关键设计**：1) 姿态网络：采用注意力机制，增强对关键特征的关注，提高姿态估计精度。2) DoRA：通过分解权重矩阵，只训练少量参数，降低了微调DA2模型的计算量。3) 自监督损失函数：结合光度一致性损失、深度一致性损失等，约束深度、姿态和固有参数的预测。

## 📊 实验亮点

EndoSfM3D在SCARED和C3VD公共数据集上进行了验证，实验结果表明，该方法在自监督单目深度估计和3D重建任务中均优于现有方法。具体性能提升数据在论文中给出，证明了该方法在内窥镜手术场景3D重建方面的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于增强内窥镜手术的场景感知，实现AR可视化，辅助医生进行更精确的手术操作。通过提供上下文感知的3D信息，帮助医生做出更明智的决策，提高手术成功率，并可用于术前规划和术后评估。未来，该技术有望集成到智能手术机器人系统中，实现更高级的自动化手术。

## 📄 摘要（原文）

> 3D reconstruction of endoscopic surgery scenes plays a vital role in enhancing scene perception, enabling AR visualization, and supporting context-aware decision-making in image-guided surgery. A critical yet challenging step in this process is the accurate estimation of the endoscope's intrinsic parameters. In real surgical settings, intrinsic calibration is hindered by sterility constraints and the use of specialized endoscopes with continuous zoom and telescope rotation. Most existing methods for endoscopic 3D reconstruction do not estimate intrinsic parameters, limiting their effectiveness for accurate and reliable reconstruction. In this paper, we integrate intrinsic parameter estimation into a self-supervised monocular depth estimation framework by adapting the Depth Anything V2 (DA2) model for joint depth, pose, and intrinsics prediction. We introduce an attention-based pose network and a Weight-Decomposed Low-Rank Adaptation (DoRA) strategy for efficient fine-tuning of DA2. Our method is validated on the SCARED and C3VD public datasets, demonstrating superior performance compared to recent state-of-the-art approaches in self-supervised monocular depth estimation and 3D reconstruction. Code and model weights can be found in project repository: https://github.com/MOYF-beta/EndoSfM3D.

