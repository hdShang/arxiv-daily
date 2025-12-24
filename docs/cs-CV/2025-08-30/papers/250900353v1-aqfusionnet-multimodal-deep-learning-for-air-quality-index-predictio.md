---
layout: default
title: "AQFusionNet: Multimodal Deep Learning for Air Quality Index Prediction with Imagery and Sensor Data"
---

# AQFusionNet: Multimodal Deep Learning for Air Quality Index Prediction with Imagery and Sensor Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00353" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00353v1</a>
  <a href="https://arxiv.org/pdf/2509.00353.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00353v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00353v1', 'AQFusionNet: Multimodal Deep Learning for Air Quality Index Prediction with Imagery and Sensor Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Koushik Ahmed Kushal, Abdullah Al Mamun

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-30

**备注**: 8 pages, 5 figures, 2 tables

---

## 💡 一句话要点

**提出AQFusionNet以解决资源受限地区空气质量监测问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空气质量监测` `多模态深度学习` `轻量级CNN` `特征融合` `边缘计算`

## 📋 核心要点

1. 现有方法在资源受限地区的空气质量监测面临传感器稀疏和基础设施不足的挑战，导致数据获取困难。
2. AQFusionNet通过结合地面图像和污染物浓度数据，利用轻量级CNN骨干网络实现多模态融合，提高AQI预测的准确性和效率。
3. 实验结果显示，AQFusionNet在分类准确率上达到92.02%，RMSE为7.70，相比单模态方法提升18.5%，且计算开销低，适合边缘设备部署。

## 📝 摘要（中文）

空气污染监测在资源受限地区面临稀疏传感器部署和基础设施有限的挑战。本文提出AQFusionNet，一个多模态深度学习框架，用于稳健的空气质量指数（AQI）预测。该框架结合了地面大气图像与污染物浓度数据，采用轻量级CNN骨干网络（MobileNetV2、ResNet18、EfficientNet-B0）。通过语义对齐的嵌入空间结合视觉和传感器特征，实现准确高效的预测。在来自印度和尼泊尔的8000多个样本上进行的实验表明，AQFusionNet在分类准确率上达到92.02%，均方根误差（RMSE）为7.70，显著优于单模态基线，提升幅度达18.5%。该模型在保持低计算开销的同时，适合在边缘设备上部署，为基础设施有限的环境提供了可扩展和实用的AQI监测解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决资源受限地区空气质量监测中的数据稀疏问题，现有方法往往依赖单一数据源，导致预测准确性不足。

**核心思路**：AQFusionNet通过融合地面大气图像与污染物浓度数据，利用多模态深度学习框架，旨在提高AQI预测的准确性和鲁棒性。

**技术框架**：AQFusionNet的整体架构包括数据预处理、特征提取、特征融合和预测模块。采用轻量级CNN骨干网络（如MobileNetV2、ResNet18、EfficientNet-B0）进行特征提取，并通过语义对齐的嵌入空间进行特征融合。

**关键创新**：AQFusionNet的主要创新在于其多模态特征融合方法，通过语义对齐的嵌入空间有效结合视觉和传感器数据，显著提升了预测性能，与传统单模态方法相比具有本质区别。

**关键设计**：在模型设计中，采用了轻量级的CNN架构以降低计算开销，损失函数选择了适合多模态学习的交叉熵损失，确保模型在不同数据源上的有效学习。

## 📊 实验亮点

实验结果表明，AQFusionNet在分类准确率上达到92.02%，均方根误差（RMSE）为7.70，较单模态方法提升18.5%。该模型在保持低计算开销的同时，展现出优越的预测性能，适合在边缘设备上部署。

## 🎯 应用场景

AQFusionNet在空气质量监测领域具有广泛的应用潜力，尤其适用于基础设施有限的地区。其高效的预测能力能够为政策制定、环境监测和公共健康提供重要支持，未来可扩展至其他环境监测领域，如水质监测和气候变化评估。

## 📄 摘要（原文）

> Air pollution monitoring in resource-constrained regions remains challenging due to sparse sensor deployment and limited infrastructure. This work introduces AQFusionNet, a multimodal deep learning framework for robust Air Quality Index (AQI) prediction. The framework integrates ground-level atmospheric imagery with pollutant concentration data using lightweight CNN backbones (MobileNetV2, ResNet18, EfficientNet-B0). Visual and sensor features are combined through semantically aligned embedding spaces, enabling accurate and efficient prediction. Experiments on more than 8,000 samples from India and Nepal demonstrate that AQFusionNet consistently outperforms unimodal baselines, achieving up to 92.02% classification accuracy and an RMSE of 7.70 with the EfficientNet-B0 backbone. The model delivers an 18.5% improvement over single-modality approaches while maintaining low computational overhead, making it suitable for deployment on edge devices. AQFusionNet provides a scalable and practical solution for AQI monitoring in infrastructure-limited environments, offering robust predictive capability even under partial sensor availability.

