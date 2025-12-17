---
layout: default
title: 3D Point Cloud Object Detection on Edge Devices for Split Computing
---

# 3D Point Cloud Object Detection on Edge Devices for Split Computing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.02293" class="toolbar-btn" target="_blank">📄 arXiv: 2511.02293v1</a>
  <a href="https://arxiv.org/pdf/2511.02293.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02293v1" onclick="toggleFavorite(this, '2511.02293v1', '3D Point Cloud Object Detection on Edge Devices for Split Computing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taisuke Noguchi, Takuya Azumi

**分类**: cs.DC, cs.CV

**发布日期**: 2025-11-04

**备注**: 6 pages. This version includes minor lstlisting configuration adjustments for successful compilation. No changes to content or layout. Originally published at ACM/IEEE RAGE 2024

**期刊**: Proceedings of the 3rd Real-time And intelliGent Edge computing workshop (RAGE), 2024, pp. 1-6

**DOI**: [10.1109/RAGE62451.2024.00009](https://doi.org/10.1109/RAGE62451.2024.00009)

---

## 💡 一句话要点

**针对边缘设备，提出基于Split Computing的3D点云目标检测方法，降低计算负担。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D目标检测` `点云` `边缘计算` `Split Computing` `自动驾驶`

## 📋 核心要点

1. 现有3D目标检测模型复杂，导致边缘设备处理时间长、功耗高，难以满足自动驾驶等实时性要求。
2. 采用Split Computing，将深度学习模型分割，部分计算放在云端，减轻边缘设备计算负担。
3. 实验表明，该方法显著降低了边缘设备的推理时间和执行时间，同时降低了数据泄露风险。

## 📝 摘要（中文）

本文旨在解决自动驾驶技术中，边缘设备上3D点云目标检测模型计算复杂度高、处理时间长、功耗大的问题。通过利用分布式机器学习推理方法Split Computing，来减轻边缘设备的计算负担，从而减少处理时间和功耗。Split Computing还能通过仅传输深度神经网络模型的中间数据，最大限度地降低数据泄露的风险。实验结果表明，在体素化后进行分割，可将推理时间减少70.8%，边缘设备执行时间减少90.0%。在网络内部进行分割，推理时间最多可减少57.1%，边缘设备执行时间最多可减少69.5%。

## 🔬 方法详解

**问题定义**：论文旨在解决在边缘设备上部署3D点云目标检测模型时，由于模型复杂度高，导致的处理时间过长和功耗过大的问题。现有方法难以在资源受限的边缘设备上实现实时、高效的3D目标检测。

**核心思路**：论文的核心思路是利用Split Computing，将深度神经网络模型分割成两部分，一部分在边缘设备上运行，另一部分在云端服务器上运行。通过将计算密集型的部分放在云端，可以显著减轻边缘设备的计算负担，从而降低处理时间和功耗。

**技术框架**：整体框架包括以下几个阶段：1) 数据采集：通过LiDAR传感器获取3D点云数据。2) 边缘设备处理：边缘设备运行模型的前半部分，提取中间特征。3) 数据传输：将中间特征传输到云端服务器。4) 云端服务器处理：云端服务器运行模型的后半部分，完成目标检测任务。5) 结果返回：将检测结果返回给边缘设备。

**关键创新**：论文的关键创新在于探索了Split Computing在3D点云目标检测中的应用，并针对不同的分割点进行了实验分析。通过选择合适的分割点，可以在保证检测精度的前提下，最大程度地降低边缘设备的计算负担。

**关键设计**：论文中，作者尝试了在体素化之后以及在网络内部进行分割。具体的网络结构和参数设置取决于所使用的3D目标检测模型（论文中未明确指出具体模型）。关键在于选择合适的分割点，使得边缘设备上的计算量尽可能小，同时保证传输的中间特征包含足够的信息。

## 📊 实验亮点

实验结果表明，在体素化后进行分割，可将推理时间减少70.8%，边缘设备执行时间减少90.0%。在网络内部进行分割，推理时间最多可减少57.1%，边缘设备执行时间最多可减少69.5%。这些数据表明，Split Computing可以显著降低边缘设备的计算负担，提高3D目标检测的效率。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、智能交通等领域。通过降低边缘设备的计算负担，可以实现更高效、更实时的3D目标检测，从而提高系统的安全性和可靠性。此外，该方法还可以降低边缘设备的功耗，延长其使用寿命。

## 📄 摘要（原文）

> The field of autonomous driving technology is rapidly advancing, with deep learning being a key component. Particularly in the field of sensing, 3D point cloud data collected by LiDAR is utilized to run deep neural network models for 3D object detection. However, these state-of-the-art models are complex, leading to longer processing times and increased power consumption on edge devices. The objective of this study is to address these issues by leveraging Split Computing, a distributed machine learning inference method. Split Computing aims to lessen the computational burden on edge devices, thereby reducing processing time and power consumption. Furthermore, it minimizes the risk of data breaches by only transmitting intermediate data from the deep neural network model. Experimental results show that splitting after voxelization reduces the inference time by 70.8% and the edge device execution time by 90.0%. When splitting within the network, the inference time is reduced by up to 57.1%, and the edge device execution time is reduced by up to 69.5%.

