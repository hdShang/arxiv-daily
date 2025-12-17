---
layout: default
title: RSPose: Ranking Based Losses for Human Pose Estimation
---

# RSPose: Ranking Based Losses for Human Pose Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13857" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13857v1</a>
  <a href="https://arxiv.org/pdf/2511.13857.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13857v1" onclick="toggleFavorite(this, '2511.13857v1', 'RSPose: Ranking Based Losses for Human Pose Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammed Can Keles, Bedrettin Cetinkaya, Sinan Kalkan, Emre Akbas

**分类**: cs.CV

**发布日期**: 2025-11-17

---

## 💡 一句话要点

**RSPose：提出基于排序损失的人体姿态估计方法，显著提升mAP**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `人体姿态估计` `排序损失` `热图回归` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有基于热图的姿态估计方法使用MSE损失，无法有效聚焦关节峰值定位，且热图存在不平衡问题。
2. RSPose提出基于排序的损失函数，旨在提高置信度与定位质量的相关性，从而优化NMS过程。
3. 实验表明，RSPose在COCO等数据集上超越现有方法，ViTPose-H模型达到79.9 mAP，SimCC Resnet-50提升1.5 AP。

## 📝 摘要（中文）

本文针对基于热图的人体姿态估计方法中存在的三个主要问题：(P1)常用的均方误差(MSE)损失对所有像素偏差同等惩罚，未能有效锐化和定位关节对应的峰值；(P2)热图存在空间和类别不平衡；(P3)评估指标(mAP)与损失函数之间存在差异。为此，我们提出了基于排序的损失函数来解决这些问题。理论和实验均表明，我们提出的损失优于常用的热图损失(MSE、KL散度)。我们的损失显著提高了置信度分数与定位质量之间的相关性，这有利于在非极大值抑制(NMS)期间进行更准确的实例选择，并提高平均精度(mAP)性能。我们将使用我们的损失训练的模型称为RSPose。我们在COCO、CrowdPose和MPII三个不同的数据集上，展示了RSPose在一维和二维热图两种模式下的有效性。据我们所知，我们是第一个提出与人体姿态估计的评估指标(mAP)对齐的损失函数。RSPose在COCO-val集上优于之前的最先进水平，使用ViTPose-H模型达到了79.9的mAP分数。我们还使用SimCC Resnet-50，一种基于坐标分类的姿态估计方法，在COCO-val集上提高了1.5 AP，达到了73.6 AP。

## 🔬 方法详解

**问题定义**：现有基于热图的人体姿态估计方法主要面临三个问题。一是常用的均方误差（MSE）损失函数对所有像素偏差一视同仁，无法有效聚焦于关节位置的精确峰值定位。二是热图本身存在空间和类别上的不平衡性，导致模型训练的偏差。三是训练过程中使用的损失函数（如MSE、KL散度）与最终评估指标（mAP）之间存在不一致性，优化目标不明确。

**核心思路**：RSPose的核心思路是设计一种基于排序的损失函数，使得模型在训练过程中能够更加关注关键点定位的准确性，并提高预测置信度与定位质量之间的相关性。通过优化置信度与定位质量的相关性，可以改善非极大值抑制（NMS）过程中的实例选择，从而提升整体的平均精度（mAP）。

**技术框架**：RSPose的整体框架仍然基于现有的热图回归方法，但关键在于损失函数的替换。模型首先预测人体关键点的热图，然后使用提出的排序损失函数进行训练。该方法可以应用于一维和二维热图，并且可以与不同的骨干网络（如ResNet、ViT）结合使用。训练完成后，使用标准的NMS算法进行后处理，得到最终的姿态估计结果。

**关键创新**：RSPose最关键的创新在于提出了与评估指标（mAP）对齐的排序损失函数。该损失函数不再简单地惩罚像素级别的偏差，而是通过比较不同预测结果的排序关系，鼓励模型生成更准确的关键点定位和更可靠的置信度分数。这种排序损失的设计使得模型能够更好地学习到关键点定位的内在规律，从而提高整体的性能。

**关键设计**：RSPose的关键设计在于排序损失函数的具体形式。具体实现细节在论文中应该有详细描述，可能包括如何定义正样本和负样本，如何计算排序损失，以及如何平衡不同关键点之间的损失权重。此外，可能还涉及到一些超参数的设置，例如排序损失的margin值等。这些细节对最终的性能至关重要。

## 📊 实验亮点

RSPose在COCO-val数据集上取得了显著的性能提升。使用ViTPose-H模型，RSPose达到了79.9的mAP，超越了之前的state-of-the-art。此外，RSPose还使SimCC Resnet-50在COCO-val数据集上提高了1.5 AP，达到了73.6 AP。这些结果表明，RSPose提出的排序损失函数能够有效提高人体姿态估计的准确性。

## 🎯 应用场景

RSPose在人体姿态估计领域具有广泛的应用前景，可应用于视频监控、人机交互、运动分析、虚拟现实等领域。通过提高姿态估计的准确性和鲁棒性，可以为这些应用提供更可靠的基础数据，从而提升用户体验和应用效果。未来，该方法有望进一步扩展到其他目标检测和识别任务中。

## 📄 摘要（原文）

> While heatmap-based human pose estimation methods have shown strong performance, they suffer from three main problems: (P1) "Commonly used Mean Squared Error (MSE)" Loss may not always improve joint localization because it penalizes all pixel deviations equally, without focusing explicitly on sharpening and correctly localizing the peak corresponding to the joint; (P2) heatmaps are spatially and class-wise imbalanced; and, (P3) there is a discrepancy between the evaluation metric (i.e., mAP) and the loss functions.
>   We propose ranking-based losses to address these issues.
>   Both theoretically and empirically, we show that our proposed losses are superior to commonly used heatmap losses (MSE, KL-Divergence). Our losses considerably increase the correlation between confidence scores and localization qualities, which is desirable because higher correlation leads to more accurate instance selection during Non-Maximum Suppression (NMS) and better Average Precision (mAP) performance. We refer to the models trained with our losses as RSPose.
>   We show the effectiveness of RSPose across two different modes: one-dimensional and two-dimensional heatmaps, on three different datasets (COCO, CrowdPose, MPII).
>   To the best of our knowledge, we are the first to propose losses that align with the evaluation metric (mAP) for human pose estimation.
>   RSPose outperforms the previous state of the art on the COCO-val set and achieves an mAP score of 79.9 with ViTPose-H, a vision transformer model for human pose estimation.
>   We also improve SimCC Resnet-50, a coordinate classification-based pose estimation method, by 1.5 AP on the COCO-val set, achieving 73.6 AP.

