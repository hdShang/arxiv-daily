---
layout: default
title: "ROVR-Open-Dataset: A Large-Scale Depth Dataset for Autonomous Driving"
---

# ROVR-Open-Dataset: A Large-Scale Depth Dataset for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13977" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13977v2</a>
  <a href="https://arxiv.org/pdf/2508.13977.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13977v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13977v2', 'ROVR-Open-Dataset: A Large-Scale Depth Dataset for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianda Guo, Ruijun Zhang, Yiqun Duan, Ruilin Wang, Matteo Poggi, Keyuan Zhou, Wenzhao Zheng, Wenke Huang, Gangwei Xu, Mike Horton, Yuan Si, Qin Zou, Hao Zhao, Long Chen

**分类**: cs.CV

**发布日期**: 2025-08-19 (更新: 2025-09-16)

---

## 💡 一句话要点

**提出ROVR数据集以解决深度估计多样性不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度估计` `数据集` `自动驾驶` `多样性` `鲁棒性` `模型训练` `跨数据集泛化`

## 📋 核心要点

1. 现有深度数据集在多样性和可扩展性方面存在不足，限制了模型的泛化能力。
2. ROVR数据集通过轻量级采集管道，提供了200K高分辨率图像，涵盖多种场景和条件。
3. 实验结果显示，当前模型在ROVR上表现不佳，强调了该数据集在深度估计领域的挑战性。

## 📝 摘要（中文）

深度估计是自动驾驶、机器人和增强现实中的基本任务。现有的数据集如KITTI、nuScenes和DDAD虽然推动了该领域的发展，但在多样性和可扩展性方面存在局限。随着基准性能的接近饱和，迫切需要新一代大规模、多样化且成本效益高的数据集来支持基础模型和多模态学习的时代。本文提出ROVR，一个大规模、多样化且成本效益高的深度数据集，旨在捕捉真实驾驶的复杂性。ROVR包含20万帧高分辨率图像，涵盖高速公路、乡村和城市场景，跨越昼夜和恶劣天气条件。轻量级采集管道确保了可扩展的收集，而稀疏但统计上足够的真实值支持了稳健的训练。对最先进的单目深度模型的基准测试揭示了严重的跨数据集泛化失败，强调了ROVR在场景多样性、动态环境和稀疏真实值方面所带来的独特挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决现有深度估计数据集在多样性和可扩展性方面的不足，尤其是在动态和复杂环境下的泛化能力问题。现有方法在KITTI等数据集上表现良好，但在新的数据集上却面临严重的性能下降。

**核心思路**：ROVR数据集的核心思想是通过大规模、多样化的场景采集，提供一个更具挑战性的训练平台，以提高深度估计模型在真实世界中的鲁棒性。设计上注重捕捉不同环境和天气条件下的复杂性。

**技术框架**：ROVR的整体架构包括数据采集、数据标注和模型训练三个主要模块。数据采集使用轻量级的设备和流程，确保高效和可扩展性；数据标注则采用稀疏但统计上有效的真实值，以支持模型训练。

**关键创新**：ROVR的主要创新在于其大规模和多样化的场景设置，尤其是在昼夜和不同天气条件下的覆盖。这与现有数据集的单一场景设置形成鲜明对比，提供了更具挑战性的训练数据。

**关键设计**：在数据采集过程中，采用了高分辨率的图像采集设备，并结合多种环境条件进行数据记录。此外，稀疏的真实值设计使得模型在训练时能够更好地适应不同场景的变化。通过这些设计，ROVR能够有效支持深度估计模型的训练和评估。

## 📊 实验亮点

实验结果表明，当前最先进的单目深度模型在ROVR数据集上的表现显著低于在KITTI上的表现，显示出跨数据集泛化能力的严重不足。这一发现强调了ROVR在深度估计研究中的重要性，并为未来的研究提供了新的方向。

## 🎯 应用场景

ROVR数据集的潜在应用领域包括自动驾驶、机器人导航和增强现实等。通过提供多样化的训练数据，ROVR能够帮助研究人员和工程师开发出更具鲁棒性的深度估计模型，从而提升自动驾驶系统在复杂环境下的安全性和可靠性。未来，ROVR有望成为深度学习领域的重要基准数据集，推动相关技术的进步。

## 📄 摘要（原文）

> Depth estimation is a fundamental task for 3D scene understanding in autonomous driving, robotics, and augmented reality. Existing depth datasets, such as KITTI, nuScenes, and DDAD, have advanced the field but suffer from limitations in diversity and scalability. As benchmark performance on these datasets approaches saturation, there is an increasing need for a new generation of large-scale, diverse, and cost-efficient datasets to support the era of foundation models and multi-modal learning. We present ROVR, a large-scale, diverse, and cost-efficient depth dataset designed to capture the complexity of real-world driving. ROVR comprises 200K high-resolution frames across highway, rural, and urban scenarios, spanning day/night and adverse weather conditions. A lightweight acquisition pipeline ensures scalable collection, while sparse but statistically sufficient ground truth supports robust training. Benchmarking with state-of-the-art monocular depth models reveals severe cross-dataset generalization failures: models achieving near-ceiling accuracy on KITTI degrade drastically on ROVR, and even when trained on ROVR, current methods fall short of saturation. These results highlight the unique challenges posed by ROVR-scene diversity, dynamic environments, and sparse ground truth, establishing it as a demanding new platform for advancing depth estimation and building models with stronger real-world robustness. Extensive ablation studies provide a more intuitive understanding of our dataset across different scenarios, lighting conditions, and generalized ability.

