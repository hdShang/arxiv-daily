---
layout: default
title: Joint Learning of Pose Regression and Denoising Diffusion with Score Scaling Sampling for Category-level 6D Pose Estimation
---

# Joint Learning of Pose Regression and Denoising Diffusion with Score Scaling Sampling for Category-level 6D Pose Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04125" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04125v1</a>
  <a href="https://arxiv.org/pdf/2510.04125.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04125v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.04125v1', 'Joint Learning of Pose Regression and Denoising Diffusion with Score Scaling Sampling for Category-level 6D Pose Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seunghyun Lee, Tae-Kyun Kim

**分类**: cs.CV

**发布日期**: 2025-10-05

---

## 💡 一句话要点

**提出基于姿态回归和去噪扩散联合学习的类别级6D姿态估计方法**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `6D姿态估计` `类别级姿态估计` `扩散模型` `姿态回归` `联合学习` `深度学习` `机器人视觉`

## 📋 核心要点

1. 现有基于扩散模型的6D姿态估计方法存在训练收敛慢，需要额外网络评估姿态假设等问题。
2. 提出一种联合学习姿态回归和去噪扩散模型的方法，并引入时间依赖性得分缩放的采样指导。
3. 在多个数据集上实验表明，该方法在训练和推理效率上优于现有方法，并实现了更高的精度。

## 📝 摘要（中文）

本文提出了一种新的类别级6D物体姿态估计流程，该流程利用深度图像输入，通过联合学习姿态回归和去噪扩散模型来建模条件姿态分布，克服了现有方法训练收敛慢、编码器与扩散去噪网络端到端学习以及需要额外网络评估姿态假设等局限性。该方法首先使用直接姿态回归头预训练编码器，然后通过回归头和去噪扩散头联合学习网络，显著加速训练收敛并提高准确性。其次，提出了基于时间依赖性得分缩放的采样指导，有效平衡探索-利用，无需额外的评估网络。该采样指导在早期去噪步骤中保持对称对象的多模态特性，同时确保在最后步骤中生成高质量的姿态。在REAL275、HouseCat6D和ROPE等多个基准测试上的大量实验表明，该方法简单有效，即使在单姿态推理下也能实现最先进的精度，同时在训练和推理方面都更有效。

## 🔬 方法详解

**问题定义**：现有基于扩散模型的类别级6D姿态估计方法，在训练过程中收敛速度较慢，并且通常需要一个额外的网络来评估采样得到的姿态假设，以过滤掉低质量的候选姿态。此外，现有方法通常以端到端的方式训练编码器和扩散去噪网络，这可能导致训练不稳定和次优性能。

**核心思路**：本文的核心思路是通过联合学习姿态回归和去噪扩散模型来加速训练收敛，并利用时间依赖性得分缩放的采样指导来提高采样质量，从而避免使用额外的姿态评估网络。通过姿态回归预训练编码器，可以提供更好的初始化，加速扩散模型的学习。

**技术框架**：该方法包含以下主要模块：1) 编码器：用于提取深度图像的特征；2) 姿态回归头：用于直接预测物体姿态，用于预训练和联合训练；3) 去噪扩散头：用于建模条件姿态分布，通过迭代去噪过程生成姿态；4) 时间依赖性得分缩放模块：用于指导采样过程，平衡探索和利用。整体流程是先用姿态回归头预训练编码器，然后联合训练姿态回归头和去噪扩散头，最后使用时间依赖性得分缩放的采样指导进行姿态生成。

**关键创新**：该方法的主要创新点在于：1) 联合学习姿态回归和去噪扩散模型，加速训练收敛并提高准确性；2) 提出时间依赖性得分缩放的采样指导，有效平衡探索-利用，无需额外的评估网络。这种采样指导能够在早期去噪步骤中保持对称对象的多模态特性，同时确保在最后步骤中生成高质量的姿态。

**关键设计**：时间依赖性得分缩放函数的设计是关键。该函数根据去噪的时间步长动态调整得分的缩放比例，在早期步长中保持较高的探索性，允许模型探索更多的姿态空间，而在后期步长中增加利用性，引导模型生成高质量的姿态。损失函数包括姿态回归损失和扩散模型的去噪损失，通过调整两者的权重来平衡回归和扩散学习。

## 📊 实验亮点

实验结果表明，该方法在REAL275、HouseCat6D和ROPE等多个基准测试上取得了state-of-the-art的精度，并且在训练和推理效率上优于现有方法。尤其是在单姿态推理的情况下，仍然能够保持较高的精度，证明了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于机器人抓取、自动驾驶、增强现实等领域。在机器人抓取中，可以帮助机器人准确识别和定位物体，从而实现精确抓取。在自动驾驶中，可以用于识别和跟踪车辆、行人等目标，提高驾驶安全性。在增强现实中，可以将虚拟物体与真实场景进行精确对齐，提升用户体验。

## 📄 摘要（原文）

> Latest diffusion models have shown promising results in category-level 6D object pose estimation by modeling the conditional pose distribution with depth image input. The existing methods, however, suffer from slow convergence during training, learning its encoder with the diffusion denoising network in end-to-end fashion, and require an additional network that evaluates sampled pose hypotheses to filter out low-quality pose candidates. In this paper, we propose a novel pipeline that tackles these limitations by two key components. First, the proposed method pretrains the encoder with the direct pose regression head, and jointly learns the networks via the regression head and the denoising diffusion head, significantly accelerating training convergence while achieving higher accuracy. Second, sampling guidance via time-dependent score scaling is proposed s.t. the exploration-exploitation trade-off is effectively taken, eliminating the need for the additional evaluation network. The sampling guidance maintains multi-modal characteristics of symmetric objects at early denoising steps while ensuring high-quality pose generation at final steps. Extensive experiments on multiple benchmarks including REAL275, HouseCat6D, and ROPE, demonstrate that the proposed method, simple yet effective, achieves state-of-the-art accuracies even with single-pose inference, while being more efficient in both training and inference.

