---
layout: default
title: 4D-ROLLS: 4D Radar Occupancy Learning via LiDAR Supervision
---

# 4D-ROLLS: 4D Radar Occupancy Learning via LiDAR Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13905" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13905v1</a>
  <a href="https://arxiv.org/pdf/2505.13905.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13905v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13905v1', '4D-ROLLS: 4D Radar Occupancy Learning via LiDAR Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruihan Liu, Xiaoyi Wu, Xijun Chen, Liang Hu, Yunjiang Lou

**分类**: cs.CV, cs.RO

**发布日期**: 2025-05-20

**🔗 代码/项目**: [GITHUB](https://github.com/CLASS-Lab/4D-ROLLS)

---

## 💡 一句话要点

**提出4D-ROLLS以解决4D雷达占用估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `4D雷达` `占用估计` `弱监督学习` `LiDAR` `自动驾驶` `深度学习` `多模态融合`

## 📋 核心要点

1. 现有的占用估计方法多依赖于LiDAR或摄像头，且在恶劣环境下表现不佳，限制了其应用。
2. 本文提出4D-ROLLS，通过LiDAR点云生成伪标签，进行弱监督训练，提升4D雷达的占用估计能力。
3. 实验结果显示，4D-ROLLS在恶劣环境下表现优异，且在下游任务中具有良好的迁移性，推向更广泛的应用。

## 📝 摘要（中文）

全面理解3D场景对于自动驾驶汽车至关重要，而占用估计在提供可驾驶和被占空间的通用表示中扮演核心角色。然而，现有方法多依赖于LiDAR或摄像头，在烟雾、雨雪和雾霾等恶劣环境中表现不佳。本文提出了4D-ROLLS，这是首个使用LiDAR点云作为监督信号的弱监督4D雷达占用估计方法。我们引入了一种生成伪LiDAR标签的方法，包括占用查询和LiDAR高度图，作为多阶段监督来训练4D雷达占用估计模型。通过与LiDAR生成的占用图对齐，模型的占用估计精度得到了提升。大量实验验证了4D-ROLLS的卓越性能，展示了其在恶劣环境中的鲁棒性和跨数据集训练的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有占用估计方法在恶劣环境下的性能不足，尤其是依赖于LiDAR和摄像头的局限性。

**核心思路**：提出4D-ROLLS，通过生成伪LiDAR标签来进行弱监督训练，使4D雷达能够更准确地进行占用估计。这样的设计使得模型在缺乏高质量标注的情况下仍能学习到有效的特征。

**技术框架**：整体架构包括伪标签生成模块和占用估计模型。伪标签生成模块负责生成占用查询和LiDAR高度图，作为多阶段监督信号；占用估计模型则通过与LiDAR生成的占用图对齐进行训练。

**关键创新**：4D-ROLLS的创新在于首次将LiDAR点云作为弱监督信号用于4D雷达的占用估计，显著提升了在恶劣环境下的鲁棒性。

**关键设计**：模型采用轻量级网络结构，确保在4060 GPU上以约30 Hz的速度进行快速推理。损失函数设计为多阶段损失，结合占用查询和高度图信息，优化模型的学习过程。

## 📊 实验亮点

实验结果表明，4D-ROLLS在恶劣环境中的占用估计性能显著优于传统方法，尤其是在跨数据集训练中表现出色，验证了其在实际应用中的有效性和鲁棒性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其是在自动驾驶、智能交通系统和机器人导航等领域。通过提高4D雷达在复杂环境中的占用估计能力，能够显著提升自动驾驶系统的安全性和可靠性，推动智能交通技术的发展。

## 📄 摘要（原文）

> A comprehensive understanding of 3D scenes is essential for autonomous vehicles (AVs), and among various perception tasks, occupancy estimation plays a central role by providing a general representation of drivable and occupied space. However, most existing occupancy estimation methods rely on LiDAR or cameras, which perform poorly in degraded environments such as smoke, rain, snow, and fog. In this paper, we propose 4D-ROLLS, the first weakly supervised occupancy estimation method for 4D radar using the LiDAR point cloud as the supervisory signal. Specifically, we introduce a method for generating pseudo-LiDAR labels, including occupancy queries and LiDAR height maps, as multi-stage supervision to train the 4D radar occupancy estimation model. Then the model is aligned with the occupancy map produced by LiDAR, fine-tuning its accuracy in occupancy estimation. Extensive comparative experiments validate the exceptional performance of 4D-ROLLS. Its robustness in degraded environments and effectiveness in cross-dataset training are qualitatively demonstrated. The model is also seamlessly transferred to downstream tasks BEV segmentation and point cloud occupancy prediction, highlighting its potential for broader applications. The lightweight network enables 4D-ROLLS model to achieve fast inference speeds at about 30 Hz on a 4060 GPU. The code of 4D-ROLLS will be made available at https://github.com/CLASS-Lab/4D-ROLLS.

