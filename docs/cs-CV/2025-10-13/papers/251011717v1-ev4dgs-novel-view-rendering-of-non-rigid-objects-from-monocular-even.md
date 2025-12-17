---
layout: default
title: Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event Streams
---

# Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event Streams

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11717" target="_blank" class="toolbar-btn">arXiv: 2510.11717v1</a>
    <a href="https://arxiv.org/pdf/2510.11717.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11717v1" 
            onclick="toggleFavorite(this, '2510.11717v1', 'Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event Streams')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Takuya Nakabayashi, Navami Kairanda, Hideo Saito, Vladislav Golyanik

**分类**: cs.CV

**发布日期**: 2025-10-13

**期刊**: British Machine Vision Conference (BMVC) 2025

---

## 💡 一句话要点

**提出Ev4DGS以解决单目事件流下非刚性物体的新视角渲染问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `事件相机` `新视角渲染` `非刚性物体` `单目事件流` `3D变形模型` `计算机视觉` `深度学习`

## 📋 核心要点

1. 现有方法在处理非刚性物体时依赖稀疏RGB输入，限制了其实际应用。
2. Ev4DGS通过单目事件流直接渲染非刚性物体，避免了对RGB图像的依赖。
3. 实验结果显示，Ev4DGS在合成和真实数据集上均优于多个基线方法，验证了其有效性。

## 📝 摘要（中文）

事件相机在新视角渲染方面相较于同步工作的RGB相机具有多种优势。尽管已有针对刚性场景的高效事件驱动技术，但在非刚性物体的情况下，现有方法通常需要稀疏的RGB输入，这在实际应用中存在显著限制。本文提出Ev4DGS，首次实现了从单目事件流中渲染非刚性变形物体的RGB或灰度图像。该方法通过损失函数将估计模型的输出与2D事件观测空间关联，并利用从事件生成的二进制掩膜训练粗略的3D变形模型。实验结果表明，Ev4DGS在多个基准测试中表现优越，验证了其有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决从单目事件流中渲染非刚性变形物体的挑战。现有方法通常需要稀疏的RGB输入，这在实际应用中存在限制。

**核心思路**：Ev4DGS通过回归可变形的3D高斯点云表示，利用事件流直接生成RGB或灰度图像，避免了对RGB图像的依赖。

**技术框架**：该方法主要包括两个模块：1) 通过损失函数将模型输出与2D事件观测空间关联；2) 从事件生成的二进制掩膜中训练粗略的3D变形模型。

**关键创新**：Ev4DGS是首个仅基于单目事件流实现非刚性物体新视角渲染的方法，突破了对RGB输入的依赖，具有重要的理论和实践意义。

**关键设计**：损失函数设计为将模型输出与2D事件观测空间进行有效关联，确保生成的图像与实际观测相符。同时，采用从事件生成的二进制掩膜来训练3D变形模型，增强了模型的鲁棒性。

## 📊 实验亮点

实验结果表明，Ev4DGS在多个基准测试中表现优越，相较于多个基线方法，其性能提升显著，具体提升幅度未知。该方法在合成和真实数据集上均展示了良好的效果，验证了其有效性。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在机器人视觉、增强现实和虚拟现实等领域。通过实现非刚性物体的新视角渲染，Ev4DGS可以提升这些领域中的物体识别、跟踪和交互能力，推动相关技术的发展。

## 📄 摘要（原文）

> Event cameras offer various advantages for novel view rendering compared to synchronously operating RGB cameras, and efficient event-based techniques supporting rigid scenes have been recently demonstrated in the literature. In the case of non-rigid objects, however, existing approaches additionally require sparse RGB inputs, which can be a substantial practical limitation; it remains unknown if similar models could be learned from event streams only. This paper sheds light on this challenging open question and introduces Ev4DGS, i.e., the first approach for novel view rendering of non-rigidly deforming objects in the explicit observation space (i.e., as RGB or greyscale images) from monocular event streams. Our method regresses a deformable 3D Gaussian Splatting representation through 1) a loss relating the outputs of the estimated model with the 2D event observation space, and 2) a coarse 3D deformation model trained from binary masks generated from events. We perform experimental comparisons on existing synthetic and newly recorded real datasets with non-rigid objects. The results demonstrate the validity of Ev4DGS and its superior performance compared to multiple naive baselines that can be applied in our setting. We will release our models and the datasets used in the evaluation for research purposes; see the project webpage: https://4dqv.mpi-inf.mpg.de/Ev4DGS/.

