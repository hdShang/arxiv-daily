---
layout: default
title: "OVSeg3R: Learn Open-vocabulary Instance Segmentation from 2D via 3D Reconstruction"
---

# OVSeg3R: Learn Open-vocabulary Instance Segmentation from 2D via 3D Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23541" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23541v1</a>
  <a href="https://arxiv.org/pdf/2509.23541.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23541v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23541v1', 'OVSeg3R: Learn Open-vocabulary Instance Segmentation from 2D via 3D Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyang Li, Jinyuan Qu, Lei Zhang

**分类**: cs.CV

**发布日期**: 2025-09-28

---

## 💡 一句话要点

**OVSeg3R：通过3D重建从2D学习开放词汇实例分割**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇分割` `3D实例分割` `3D重建` `知识迁移` `伪标签学习`

## 📋 核心要点

1. 现有方法难以直接利用2D开放词汇分割的优势进行3D场景的开放词汇实例分割。
2. OVSeg3R通过3D重建建立2D和3D的对应关系，将2D的开放词汇知识迁移到3D场景中。
3. 实验表明，OVSeg3R在ScanNet200数据集上显著提升了开放词汇3D实例分割的性能。

## 📝 摘要（中文）

本文提出了一种名为OVSeg3R的训练方案，旨在借助3D重建，从充分研究的2D感知模型中学习开放词汇3D实例分割。OVSeg3R直接采用从2D视频重建的场景作为输入，避免了昂贵的手动调整，同时使输入与实际应用对齐。通过利用3D重建模型提供的2D到3D的对应关系，OVSeg3R将每个视图的2D实例掩码预测（从开放词汇2D模型获得）投影到3D，从而为该视图对应的子场景生成注释。为了避免由于2D到3D的部分注释而错误地引入假阳性作为监督，我们提出了一种视图级实例划分算法，该算法将预测划分到各自的视图以进行监督，从而稳定训练过程。此外，由于3D重建模型倾向于过度平滑几何细节，因此像主流3D分割方法中那样，仅基于几何形状将重建点聚类为代表性的超点可能会忽略几何形状上不显著的对象。因此，我们引入了2D实例边界感知超点，该超点利用2D掩码来约束超点聚类，防止超点违反实例边界。通过这些设计，OVSeg3R不仅将最先进的封闭词汇3D实例分割模型扩展到开放词汇，而且大大缩小了尾部类和头部类之间的性能差距，最终在ScanNet200基准测试上实现了+2.3 mAP的总体改进。此外，在标准开放词汇设置下，OVSeg3R超过了以前的方法约+7.1 mAP的新类别，进一步验证了其有效性。

## 🔬 方法详解

**问题定义**：现有的3D实例分割方法通常依赖于封闭词汇表，无法识别训练集中未出现的新类别。直接训练开放词汇3D实例分割模型需要大量的3D标注数据，成本高昂。此外，如何有效地利用已有的2D开放词汇分割模型是一个挑战。

**核心思路**：利用3D重建技术，将2D图像的开放词汇分割结果投影到3D空间，生成3D场景的伪标签，从而训练开放词汇3D实例分割模型。通过这种方式，可以有效地利用2D模型的知识，避免直接标注3D数据的成本。

**技术框架**：OVSeg3R的整体框架包括以下几个主要阶段：1) 使用2D开放词汇分割模型对视频帧进行实例分割；2) 使用3D重建算法（如COLMAP）重建3D场景；3) 将2D分割结果投影到3D空间，生成3D实例分割的伪标签；4) 使用生成的伪标签训练3D实例分割模型。

**关键创新**：该方法的核心创新在于利用3D重建技术，将2D开放词汇分割的知识迁移到3D场景中，从而实现了开放词汇3D实例分割。此外，论文还提出了视图级实例划分算法和2D实例边界感知超点聚类方法，以提高伪标签的质量和分割精度。

**关键设计**：视图级实例划分算法旨在解决由于2D到3D投影的不完整性导致的假阳性问题。2D实例边界感知超点聚类方法通过引入2D分割结果的边界信息，约束超点的聚类过程，防止超点跨越实例边界，从而提高分割精度。损失函数方面，可以使用标准的交叉熵损失或Dice损失等。

## 📊 实验亮点

OVSeg3R在ScanNet200数据集上取得了显著的性能提升。在标准开放词汇设置下，OVSeg3R超过了之前的方法约+7.1 mAP的新类别。此外，OVSeg3R还缩小了尾部类和头部类之间的性能差距，最终在ScanNet200基准测试上实现了+2.3 mAP的总体改进。这些结果表明，OVSeg3R是一种有效的开放词汇3D实例分割方法。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、增强现实等领域。例如，机器人可以利用开放词汇3D实例分割技术识别和理解周围环境中的各种物体，从而更好地进行导航和交互。在自动驾驶领域，该技术可以帮助车辆识别道路上的各种交通参与者和障碍物，提高驾驶安全性。在增强现实领域，该技术可以用于将虚拟物体与真实场景进行精确的融合。

## 📄 摘要（原文）

> In this paper, we propose a training scheme called OVSeg3R to learn open-vocabulary 3D instance segmentation from well-studied 2D perception models with the aid of 3D reconstruction. OVSeg3R directly adopts reconstructed scenes from 2D videos as input, avoiding costly manual adjustment while aligning input with real-world applications. By exploiting the 2D to 3D correspondences provided by 3D reconstruction models, OVSeg3R projects each view's 2D instance mask predictions, obtained from an open-vocabulary 2D model, onto 3D to generate annotations for the view's corresponding sub-scene. To avoid incorrectly introduced false positives as supervision due to partial annotations from 2D to 3D, we propose a View-wise Instance Partition algorithm, which partitions predictions to their respective views for supervision, stabilizing the training process. Furthermore, since 3D reconstruction models tend to over-smooth geometric details, clustering reconstructed points into representative super-points based solely on geometry, as commonly done in mainstream 3D segmentation methods, may overlook geometrically non-salient objects. We therefore introduce 2D Instance Boundary-aware Superpoint, which leverages 2D masks to constrain the superpoint clustering, preventing superpoints from violating instance boundaries. With these designs, OVSeg3R not only extends a state-of-the-art closed-vocabulary 3D instance segmentation model to open-vocabulary, but also substantially narrows the performance gap between tail and head classes, ultimately leading to an overall improvement of +2.3 mAP on the ScanNet200 benchmark. Furthermore, under the standard open-vocabulary setting, OVSeg3R surpasses previous methods by about +7.1 mAP on the novel classes, further validating its effectiveness.

