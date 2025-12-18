---
layout: default
title: Learning Efficient Meshflow and Optical Flow from Event Cameras
---

# Learning Efficient Meshflow and Optical Flow from Event Cameras

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04111" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04111v1</a>
  <a href="https://arxiv.org/pdf/2510.04111.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04111v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.04111v1', 'Learning Efficient Meshflow and Optical Flow from Event Cameras')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinglong Luo, Ao Luo, Kunming Luo, Zhengning Wang, Ping Tan, Bing Zeng, Shuaicheng Liu

**分类**: cs.CV

**发布日期**: 2025-10-05

**备注**: Accepted by TPAMI 2025

**DOI**: [10.1109/TPAMI.2025.3615144](https://doi.org/10.1109/TPAMI.2025.3615144)

**🔗 代码/项目**: [GITHUB](https://github.com/boomluo02/EEMFlowPlus)

---

## 💡 一句话要点

**提出EEMFlow网络，解决事件相机Meshflow和光流高效估计问题，并构建高分辨率数据集HREM。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `事件相机` `Meshflow估计` `光流估计` `神经网络` `高分辨率数据集`

## 📋 核心要点

1. 现有事件相机flow估计缺乏针对meshflow的数据集和方法，且对事件数据密度挑战研究不足。
2. 提出EEMFlow网络，采用轻量级编码器-解码器架构，并设计Confidence-induced Detail Completion (CDC)模块。
3. 实验表明，EEMFlow模型比现有方法快30倍，且自适应密度模块(ADM)能显著提升模型性能。

## 📝 摘要（中文）

本文探讨了基于事件相机的meshflow估计问题，这是一个新颖的任务，旨在预测空间平滑的稀疏运动场。首先，回顾了基于事件的flow估计的最新技术，强调了两个需要进一步研究的关键领域：i) 缺乏针对meshflow的事件数据集和方法，以及 ii) 事件数据密度未被充分探索的挑战。为此，我们生成了一个大规模的高分辨率事件Meshflow (HREM)数据集，该数据集具有1280x720的高分辨率、处理动态对象和复杂运动模式以及提供光流和meshflow标签的优点。此外，我们提出了高效的基于事件的MeshFlow (EEMFlow)网络，这是一个轻量级模型，具有专门设计的编码器-解码器架构，以促进快速准确的meshflow估计。我们还将EEMFlow网络升级为支持密集事件光流，并提出了置信度引导的细节补全(CDC)模块，以保持清晰的运动边界。我们进行了全面的实验，表明与最新的flow方法相比，我们的EEMFlow模型具有卓越的性能和运行效率（快30倍）。作为扩展，我们将HREM扩展到HREM+，这是一个多密度事件数据集，有助于全面研究现有方法在不同密度数据上的鲁棒性，并提出了自适应密度模块(ADM)，以将输入事件数据的密度调整到更优的范围，从而提高模型的泛化能力。经验表明，ADM有助于显著提高EEMFlow和EEMFlow+的性能，分别提高了8%和10%。代码和数据集已在https://github.com/boomluo02/EEMFlowPlus上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决基于事件相机的meshflow和光流估计问题。现有方法缺乏针对meshflow的专用数据集，并且没有充分考虑事件数据密度变化对性能的影响。此外，现有方法在计算效率方面存在瓶颈，难以满足实时应用的需求。

**核心思路**：论文的核心思路是设计一个轻量级且高效的神经网络EEMFlow，能够从事件数据中准确估计meshflow和光流。通过构建大规模高分辨率数据集HREM/HREM+，并引入自适应密度模块ADM，提高模型在不同数据密度下的泛化能力。

**技术框架**：EEMFlow网络采用编码器-解码器架构。编码器负责提取事件数据的特征，解码器则根据提取的特征预测meshflow和光流。为了处理密集光流估计，论文提出了Confidence-induced Detail Completion (CDC)模块，用于保持运动边界的清晰度。此外，自适应密度模块ADM用于调整输入事件数据的密度，以优化模型的性能。

**关键创新**：论文的关键创新点包括：1) 提出了EEMFlow网络，实现了高效的meshflow和光流估计；2) 构建了大规模高分辨率事件相机数据集HREM/HREM+，为相关研究提供了数据基础；3) 提出了自适应密度模块ADM，提高了模型在不同数据密度下的鲁棒性。与现有方法相比，EEMFlow在计算效率和精度上都取得了显著提升。

**关键设计**：EEMFlow网络的编码器和解码器都采用了轻量级卷积神经网络。CDC模块利用置信度信息来引导细节补全，从而保持运动边界的清晰度。ADM模块通过学习一个映射函数，将输入事件数据的密度调整到最优范围。损失函数包括meshflow损失、光流损失和置信度损失，用于优化网络的参数。

## 📊 实验亮点

EEMFlow模型在HREM数据集上取得了显著的性能提升，与最先进的方法相比，运行速度提高了30倍。此外，自适应密度模块ADM能够显著提高EEMFlow和EEMFlow+的性能，分别提高了8%和10%，表明该方法对事件数据密度具有良好的适应性。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、虚拟现实等领域。通过高效准确地估计场景中的运动信息，可以帮助机器人更好地理解周围环境，从而实现更智能的决策和控制。此外，该技术还可以用于视频监控、运动分析等领域，具有广泛的应用前景。

## 📄 摘要（原文）

> In this paper, we explore the problem of event-based meshflow estimation, a novel task that involves predicting a spatially smooth sparse motion field from event cameras. To start, we review the state-of-the-art in event-based flow estimation, highlighting two key areas for further research: i) the lack of meshflow-specific event datasets and methods, and ii) the underexplored challenge of event data density. First, we generate a large-scale High-Resolution Event Meshflow (HREM) dataset, which showcases its superiority by encompassing the merits of high resolution at 1280x720, handling dynamic objects and complex motion patterns, and offering both optical flow and meshflow labels. These aspects have not been fully explored in previous works. Besides, we propose Efficient Event-based MeshFlow (EEMFlow) network, a lightweight model featuring a specially crafted encoder-decoder architecture to facilitate swift and accurate meshflow estimation. Furthermore, we upgrade EEMFlow network to support dense event optical flow, in which a Confidence-induced Detail Completion (CDC) module is proposed to preserve sharp motion boundaries. We conduct comprehensive experiments to show the exceptional performance and runtime efficiency (30x faster) of our EEMFlow model compared to the recent state-of-the-art flow method. As an extension, we expand HREM into HREM+, a multi-density event dataset contributing to a thorough study of the robustness of existing methods across data with varying densities, and propose an Adaptive Density Module (ADM) to adjust the density of input event data to a more optimal range, enhancing the model's generalization ability. We empirically demonstrate that ADM helps to significantly improve the performance of EEMFlow and EEMFlow+ by 8% and 10%, respectively. Code and dataset are released at https://github.com/boomluo02/EEMFlowPlus.

