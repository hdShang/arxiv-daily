---
layout: default
title: "Trace Anything: Representing Any Video in 4D via Trajectory Fields"
---

# Trace Anything: Representing Any Video in 4D via Trajectory Fields

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13802" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13802v1</a>
  <a href="https://arxiv.org/pdf/2510.13802.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13802v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.13802v1', 'Trace Anything: Representing Any Video in 4D via Trajectory Fields')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinhang Liu, Yuxi Xiao, Donny Y. Chen, Jiashi Feng, Yu-Wing Tai, Chi-Keung Tang, Bingyi Kang

**分类**: cs.CV

**发布日期**: 2025-10-15

**🔗 代码/项目**: [PROJECT_PAGE](https://trace-anything.github.io/)

---

## 💡 一句话要点

**Trace Anything：提出基于轨迹场的视频4D表示方法，实现高效时空建模。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视频表示` `轨迹场` `时空建模` `B样条曲线` `神经网络`

## 📋 核心要点

1. 现有视频理解方法难以有效建模像素级别的时空动态，限制了其在复杂场景中的应用。
2. Trace Anything通过预测每个像素的3D轨迹函数，将视频表示为轨迹场，从而捕捉细粒度的时空信息。
3. 实验表明，Trace Anything在轨迹场估计和点跟踪任务上表现出色，并展现出目标条件操作等涌现能力。

## 📝 摘要（中文）

有效的时空表示是建模、理解和预测视频动态的基础。视频的基本单元——像素，随着时间推移会形成连续的3D轨迹，这是动态的基本元素。基于此，我们提出将任何视频表示为一个轨迹场：一个密集的映射，它为每一帧中的每个像素分配一个随时间变化的连续3D轨迹函数。基于这种表示，我们引入了Trace Anything，一个神经网络，可以通过一次前向传播预测整个轨迹场。具体来说，对于每一帧中的每个像素，我们的模型预测一组控制点，这些控制点参数化一条轨迹（即B样条），从而在任意查询时间瞬间产生其3D位置。我们在大规模4D数据上训练了Trace Anything模型，包括来自我们新平台的数据。实验表明：（i）Trace Anything在我们新的轨迹场估计基准上实现了最先进的性能，并在已建立的点跟踪基准上表现出竞争力；（ii）由于其一次性范式，无需迭代优化或辅助估计器，因此它提供了显著的效率提升；（iii）它表现出涌现能力，包括目标条件操作、运动预测和时空融合。

## 🔬 方法详解

**问题定义**：现有视频理解方法通常依赖于离散的帧序列处理，难以捕捉像素级别的连续时空动态。例如，基于光流的方法虽然可以估计像素的运动，但通常是局部和瞬时的，无法提供完整的轨迹信息。此外，迭代优化和辅助估计器增加了计算复杂度，限制了效率。因此，如何高效地表示和建模视频中的像素轨迹是亟待解决的问题。

**核心思路**：论文的核心思路是将视频中的每个像素视为一个在时空中运动的点，并用连续的3D轨迹函数来描述其运动轨迹。通过预测每个像素的轨迹函数，可以将视频表示为一个密集的轨迹场，从而捕捉细粒度的时空信息。这种表示方法可以克服传统方法的局限性，实现高效的时空建模。

**技术框架**：Trace Anything的整体框架是一个单阶段的前向神经网络。输入是视频帧序列，输出是每个像素的3D轨迹函数。具体来说，对于每一帧中的每个像素，网络预测一组控制点，这些控制点参数化一条B样条曲线，从而表示该像素的3D轨迹。整个过程无需迭代优化或辅助估计器，可以一次性完成。

**关键创新**：最重要的技术创新点在于将视频表示为轨迹场的概念，以及通过神经网络直接预测轨迹函数的方法。与现有方法相比，Trace Anything可以更完整、更高效地捕捉视频中的时空动态。此外，通过B样条曲线参数化轨迹，可以灵活地表示各种复杂的运动模式。

**关键设计**：Trace Anything的关键设计包括：(1) 使用B样条曲线参数化轨迹，通过控制点来调节轨迹的形状；(2) 设计合适的网络结构，用于预测每个像素的控制点；(3) 使用大规模4D数据进行训练，提高模型的泛化能力；(4) 设计合适的损失函数，例如轨迹平滑损失和轨迹一致性损失，以保证轨迹的质量。

## 📊 实验亮点

Trace Anything在新的轨迹场估计基准上实现了最先进的性能，并在已建立的点跟踪基准上表现出竞争力。与现有方法相比，Trace Anything具有显著的效率优势，因为它可以通过一次前向传播预测整个轨迹场，而无需迭代优化或辅助估计器。此外，Trace Anything还展现出目标条件操作、运动预测和时空融合等涌现能力。

## 🎯 应用场景

Trace Anything具有广泛的应用前景，包括视频编辑、运动捕捉、自动驾驶、机器人导航等领域。例如，在视频编辑中，可以利用Trace Anything实现精确的物体跟踪和分割；在自动驾驶中，可以利用Trace Anything预测行人和车辆的运动轨迹，提高安全性。此外，Trace Anything还可以用于生成逼真的虚拟现实场景，以及进行视频修复和增强。

## 📄 摘要（原文）

> Effective spatio-temporal representation is fundamental to modeling, understanding, and predicting dynamics in videos. The atomic unit of a video, the pixel, traces a continuous 3D trajectory over time, serving as the primitive element of dynamics. Based on this principle, we propose representing any video as a Trajectory Field: a dense mapping that assigns a continuous 3D trajectory function of time to each pixel in every frame. With this representation, we introduce Trace Anything, a neural network that predicts the entire trajectory field in a single feed-forward pass. Specifically, for each pixel in each frame, our model predicts a set of control points that parameterizes a trajectory (i.e., a B-spline), yielding its 3D position at arbitrary query time instants. We trained the Trace Anything model on large-scale 4D data, including data from our new platform, and our experiments demonstrate that: (i) Trace Anything achieves state-of-the-art performance on our new benchmark for trajectory field estimation and performs competitively on established point-tracking benchmarks; (ii) it offers significant efficiency gains thanks to its one-pass paradigm, without requiring iterative optimization or auxiliary estimators; and (iii) it exhibits emergent abilities, including goal-conditioned manipulation, motion forecasting, and spatio-temporal fusion. Project page: https://trace-anything.github.io/.

