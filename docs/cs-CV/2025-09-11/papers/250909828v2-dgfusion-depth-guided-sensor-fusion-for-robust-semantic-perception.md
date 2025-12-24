---
layout: default
title: "DGFusion: Depth-Guided Sensor Fusion for Robust Semantic Perception"
---

# DGFusion: Depth-Guided Sensor Fusion for Robust Semantic Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09828" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09828v2</a>
  <a href="https://arxiv.org/pdf/2509.09828.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09828v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09828v2', 'DGFusion: Depth-Guided Sensor Fusion for Robust Semantic Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tim Broedermannn, Christos Sakaridis, Luigi Piccinelli, Wim Abbeloos, Luc Van Gool

**分类**: cs.CV, cs.LG, cs.RO

**发布日期**: 2025-09-11 (更新: 2025-12-03)

**备注**: Code and models will be available at https://github.com/timbroed/DGFusion

**🔗 代码/项目**: [GITHUB](https://github.com/timbroed/DGFusion)

---

## 💡 一句话要点

**提出DGFusion，利用深度信息引导传感器融合，提升语义感知鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `深度学习` `语义分割` `全景分割` `自动驾驶` `传感器融合` `深度估计`

## 📋 核心要点

1. 现有传感器融合方法在空间上均匀处理传感器数据，在复杂条件下性能受限。
2. DGFusion利用深度信息引导传感器融合，学习深度感知特征，动态调整传感器融合策略。
3. 在MUSES和DeLiVER数据集上，DGFusion实现了最先进的全景和语义分割性能。

## 📝 摘要（中文）

针对自动驾驶车辆的鲁棒语义感知，本文提出了一种新颖的深度引导多模态融合方法DGFusion，通过整合深度信息来改进条件感知融合。该网络将多模态分割视为多任务问题，利用激光雷达测量数据作为模型输入和深度学习的真值。辅助深度头有助于学习深度感知特征，这些特征被编码为空间变化的局部深度令牌，从而调节注意力跨模态融合。结合全局条件令牌，这些局部深度令牌动态地调整传感器融合，以适应场景中每个传感器在空间上变化的可靠性，这主要取决于深度。此外，本文还提出了一种鲁棒的深度损失函数，这对于从恶劣条件下通常稀疏且嘈杂的激光雷达输入中学习至关重要。该方法在具有挑战性的MUSES和DeLiVER数据集上实现了最先进的全景和语义分割性能。

## 🔬 方法详解

**问题定义**：自动驾驶的语义感知依赖于多传感器融合，但现有方法在处理不同传感器数据时，通常采用空间上均匀的处理方式，忽略了传感器在不同区域的可靠性差异。尤其是在恶劣天气或光照条件下，某些传感器的数据质量会显著下降，导致融合结果不佳。因此，如何根据场景条件动态调整传感器融合策略，是提升语义感知鲁棒性的关键问题。

**核心思路**：DGFusion的核心思路是利用深度信息来引导传感器融合。深度信息可以反映场景的几何结构和传感器与物体的距离，从而帮助判断不同传感器在不同区域的可靠性。通过学习深度感知特征，并将其编码为空间变化的局部深度令牌，可以动态地调整跨模态融合的权重，使模型更加关注可靠的传感器数据。

**技术框架**：DGFusion的网络架构包含以下几个主要模块：1) 多模态输入：接收来自不同传感器的输入数据，例如图像和激光雷达点云。2) 深度预测头：利用激光雷达数据作为真值，学习预测场景深度。3) 深度感知特征提取：从多模态输入中提取深度感知特征，并将其编码为空间变化的局部深度令牌。4) 注意力跨模态融合：利用局部深度令牌和全局条件令牌，动态地调整跨模态融合的权重。5) 分割头：输出语义分割和全景分割结果。

**关键创新**：DGFusion的关键创新在于：1) 提出了深度引导的传感器融合方法，利用深度信息动态调整融合策略。2) 设计了深度感知特征提取模块，学习深度感知的局部特征表示。3) 引入了鲁棒的深度损失函数，用于从稀疏和噪声的激光雷达数据中学习深度信息。

**关键设计**：DGFusion的关键设计包括：1) 使用Transformer结构进行跨模态融合，利用注意力机制学习不同传感器之间的关系。2) 设计了局部深度令牌和全局条件令牌，用于动态调整融合权重。3) 采用了Huber损失函数作为深度损失函数，以提高对噪声数据的鲁棒性。4) 将多模态分割问题建模为多任务学习问题，同时预测语义分割、全景分割和深度信息。

## 📊 实验亮点

DGFusion在MUSES和DeLiVER数据集上取得了显著的性能提升。在MUSES数据集上，DGFusion的全景分割质量（PQ）超过了现有最佳方法，在DeLiVER数据集上，DGFusion的语义分割精度（mIoU）也达到了新的高度。实验结果表明，DGFusion能够有效地利用深度信息引导传感器融合，提高语义感知的鲁棒性。

## 🎯 应用场景

DGFusion可应用于自动驾驶、机器人导航、智能监控等领域。通过提升在复杂环境下的语义感知鲁棒性，可以提高自动驾驶车辆的安全性和可靠性，增强机器人在未知环境中的适应能力，并改善智能监控系统的目标检测和识别性能。该研究有助于推动智能系统在更广泛的应用场景中的部署。

## 📄 摘要（原文）

> Robust semantic perception for autonomous vehicles relies on effectively combining multiple sensors with complementary strengths and weaknesses. State-of-the-art sensor fusion approaches to semantic perception often treat sensor data uniformly across the spatial extent of the input, which hinders performance when faced with challenging conditions. By contrast, we propose a novel depth-guided multimodal fusion method that upgrades condition-aware fusion by integrating depth information. Our network, DGFusion, poses multimodal segmentation as a multi-task problem, utilizing the lidar measurements, which are typically available in outdoor sensor suites, both as one of the model's inputs and as ground truth for learning depth. Our corresponding auxiliary depth head helps to learn depth-aware features, which are encoded into spatially varying local depth tokens that condition our attentive cross-modal fusion. Together with a global condition token, these local depth tokens dynamically adapt sensor fusion to the spatially varying reliability of each sensor across the scene, which largely depends on depth. In addition, we propose a robust loss for our depth, which is essential for learning from lidar inputs that are typically sparse and noisy in adverse conditions. Our method achieves state-of-the-art panoptic and semantic segmentation performance on the challenging MUSES and DeLiVER datasets. Code and models will be available at https://github.com/timbroed/DGFusion

