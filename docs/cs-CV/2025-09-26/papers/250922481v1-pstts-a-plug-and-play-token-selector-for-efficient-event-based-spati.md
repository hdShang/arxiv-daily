---
layout: default
title: "PSTTS: A Plug-and-Play Token Selector for Efficient Event-based Spatio-temporal Representation Learning"
---

# PSTTS: A Plug-and-Play Token Selector for Efficient Event-based Spatio-temporal Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22481" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22481v1</a>
  <a href="https://arxiv.org/pdf/2509.22481.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22481v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22481v1', 'PSTTS: A Plug-and-Play Token Selector for Efficient Event-based Spatio-temporal Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiangmo Zhao, Nan Yang, Yang Wang, Zhanwen Liu

**分类**: cs.CV

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出PSTTS即插即用模块，有效提升事件数据时空表征学习的效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `事件相机` `时空表征学习` `Token选择` `计算效率` `事件数据处理`

## 📋 核心要点

1. 现有基于事件帧序列的时空表征学习方法忽略了事件数据的高空间稀疏性和帧间运动冗余，导致计算开销过大。
2. PSTTS模块利用事件数据的时空分布特性，通过空间Token净化和时间Token选择，有效识别并去除冗余Token。
3. 实验结果表明，PSTTS在多个数据集和骨干网络上显著降低了计算量，提高了帧率，同时保持了任务精度。

## 📝 摘要（中文）

本文提出了一种渐进式时空Token选择（PSTTS）模块，用于提升事件数据的时空表征学习效率，且无需引入额外参数。主流方法通常将事件流转换为事件帧序列，但忽略了事件帧序列中固有的高空间稀疏性和帧间运动冗余，导致计算开销大。现有的RGB视频Token稀疏化方法依赖于不可靠的中间Token表征，并忽略了事件噪声的影响，不适用于事件数据。PSTTS利用原始事件数据中蕴含的时空分布特征，有效识别并丢弃冗余的时空Token，从而在精度和效率之间取得最佳平衡。PSTTS包含空间Token净化和时间Token选择两个阶段。空间Token净化评估每个事件帧内事件的时空一致性，去除噪声和非事件区域，防止干扰后续的时间冗余评估。时间Token选择评估相邻事件帧之间的运动模式相似性，精确识别并去除冗余的时间信息。在HARDVS、DailyDVS-200和SeACT数据集上，PSTTS应用于UniformerV2、VideoSwin、EVMamba和ExACT四个代表性骨干网络，实验结果表明PSTTS显著提高了效率。在DailyDVS-200数据集上，PSTTS在保持任务准确率的同时，将FLOPs降低了29-43.6%，并将FPS提高了21.6-41.3%。

## 🔬 方法详解

**问题定义**：现有基于事件相机数据的时空表征学习方法，通常将事件流转换为事件帧序列，然后应用视频处理模型。然而，事件帧序列具有高空间稀疏性和帧间运动冗余的特点，导致计算资源浪费。现有的Token稀疏化方法无法直接应用于事件数据，因为它们依赖于RGB图像的中间特征，并且没有考虑事件噪声的影响。

**核心思路**：PSTTS的核心思路是利用事件数据本身的时空分布特性，逐步识别并去除冗余的Token。通过空间Token净化去除噪声和非事件区域，减少后续计算的干扰。然后，通过时间Token选择去除帧间运动冗余，进一步降低计算量。这种方法旨在在保持任务精度的前提下，最大限度地提高计算效率。

**技术框架**：PSTTS包含两个主要阶段：空间Token净化（Spatial Token Purification）和时间Token选择（Temporal Token Selection）。首先，空间Token净化模块评估每个事件帧内事件的时空一致性，去除噪声和非事件区域。然后，时间Token选择模块评估相邻事件帧之间的运动模式相似性，精确识别并去除冗余的时间信息。PSTTS作为一个即插即用模块，可以方便地集成到现有的事件数据处理流程中。

**关键创新**：PSTTS的关键创新在于其针对事件数据的特性，设计了专门的空间Token净化和时间Token选择机制。与现有的RGB视频Token稀疏化方法不同，PSTTS直接利用原始事件数据，避免了对不可靠的中间特征的依赖，并考虑了事件噪声的影响。此外，PSTTS无需引入额外的参数，易于集成和部署。

**关键设计**：空间Token净化阶段，通过计算事件的时空一致性评分来判断是否为噪声或非事件区域，具体实现方式未知。时间Token选择阶段，通过评估相邻帧之间的运动模式相似性来识别冗余Token，具体实现方式未知。PSTTS作为一个即插即用模块，可以灵活地与不同的骨干网络结合使用，无需修改骨干网络的结构。

## 📊 实验亮点

PSTTS在DailyDVS-200数据集上，应用于UniformerV2、VideoSwin、EVMamba和ExACT四个代表性骨干网络，实现了显著的效率提升。具体而言，PSTTS在保持任务准确率的同时，将FLOPs降低了29-43.6%，并将FPS提高了21.6-41.3%。这些结果表明PSTTS在提高事件数据处理效率方面具有显著优势。

## 🎯 应用场景

PSTTS的应用场景广泛，包括自动驾驶、机器人导航、视频监控等。通过提高事件数据的处理效率，PSTTS可以降低计算成本，提高实时性，从而使这些应用在资源受限的平台上也能高效运行。未来，PSTTS有望推动事件相机在更多领域的应用，例如低功耗设备和边缘计算。

## 📄 摘要（原文）

> Mainstream event-based spatio-temporal representation learning methods typically process event streams by converting them into sequences of event frames, achieving remarkable performance. However, they neglect the high spatial sparsity and inter-frame motion redundancy inherent in event frame sequences, leading to significant computational overhead. Existing token sparsification methods for RGB videos rely on unreliable intermediate token representations and neglect the influence of event noise, making them ineffective for direct application to event data. In this paper, we propose Progressive Spatio-Temporal Token Selection (PSTTS), a Plug-and-Play module for event data without introducing any additional parameters. PSTTS exploits the spatio-temporal distribution characteristics embedded in raw event data to effectively identify and discard spatio-temporal redundant tokens, achieving an optimal trade-off between accuracy and efficiency. Specifically, PSTTS consists of two stages, Spatial Token Purification and Temporal Token Selection. Spatial Token Purification discards noise and non-event regions by assessing the spatio-temporal consistency of events within each event frame to prevent interference with subsequent temporal redundancy evaluation. Temporal Token Selection evaluates the motion pattern similarity between adjacent event frames, precisely identifying and removing redundant temporal information. We apply PSTTS to four representative backbones UniformerV2, VideoSwin, EVMamba, and ExACT on the HARDVS, DailyDVS-200, and SeACT datasets. Experimental results demonstrate that PSTTS achieves significant efficiency improvements. Specifically, PSTTS reduces FLOPs by 29-43.6% and increases FPS by 21.6-41.3% on the DailyDVS-200 dataset, while maintaining task accuracy. Our code will be available.

