---
layout: default
title: "RaCalNet: Radar Calibration Network for Sparse-Supervised Metric Depth Estimation"
---

# RaCalNet: Radar Calibration Network for Sparse-Supervised Metric Depth Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15560" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15560v2</a>
  <a href="https://arxiv.org/pdf/2506.15560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15560v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15560v2', 'RaCalNet: Radar Calibration Network for Sparse-Supervised Metric Depth Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingrui Qin, Wentao Zhao, Chuan Cao, Yihe Niu, Tianchen Deng, Houcheng Jiang, Rui Guo, Jingchuan Wang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-06-18 (更新: 2025-07-05)

**备注**: 10 pages, 7 figures

**🔗 代码/项目**: [GITHUB](https://github.com/818slam/RaCalNet.git)

---

## 💡 一句话要点

**提出RaCalNet以解决稀疏监督下的深度估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `雷达校准` `深度估计` `稀疏监督` `多模态融合` `计算机视觉`

## 📋 核心要点

1. 现有的密集深度估计方法依赖于密集的LiDAR监督，导致高成本和数据需求。
2. RaCalNet通过稀疏LiDAR监督来学习精细化的雷达测量，显著降低了监督密度。
3. 在ZJU-4DRadarCam数据集上，RaCalNet的性能与现有方法相当，并在实际应用中实现了34.89%的RMSE降低。

## 📝 摘要（中文）

密集深度估计通常需要密集的LiDAR监督，这种方法成本高且数据密集。为了解决这一问题，本文提出了RaCalNet框架，通过稀疏LiDAR监督学习精细化雷达测量，监督密度仅为1%。RaCalNet由雷达重校准模块和度量深度优化模块组成，前者从稀疏雷达输入中生成准确的深度先验，后者则融合单目深度预测以实现度量准确的输出。尽管仅依赖稀疏监督，RaCalNet仍能生成清晰的物体轮廓和细致的纹理，展示出优于现有密集监督方法的视觉质量。

## 🔬 方法详解

**问题定义**：本文旨在解决密集深度估计中对密集LiDAR监督的依赖问题。现有方法不仅成本高，而且需要大量数据进行训练，限制了其应用场景。

**核心思路**：RaCalNet的核心思想是通过稀疏LiDAR监督来优化雷达测量，减少对密集监督的需求，从而降低成本和数据量。该方法通过生成精细的深度先验来提升深度估计的准确性。

**技术框架**：RaCalNet由两个主要模块组成：雷达重校准模块和度量深度优化模块。雷达重校准模块负责筛选雷达点并进行像素级位移优化，生成准确的深度先验；度量深度优化模块则学习场景级尺度先验，并将其与单目深度预测融合，以实现准确的深度输出。

**关键创新**：RaCalNet的主要创新在于其能够在仅依赖稀疏监督的情况下，生成高质量的深度图，显著提高了深度估计的视觉质量和结构一致性。这与传统方法依赖密集监督的本质区别在于监督密度的极大降低。

**关键设计**：在设计上，RaCalNet采用了特定的损失函数来优化深度预测，并通过网络结构的模块化设计增强了模型的可扩展性和灵活性。

## 📊 实验亮点

RaCalNet在ZJU-4DRadarCam数据集上的表现与现有密集监督方法相当，并在实际应用场景中实现了34.89%的均方根误差（RMSE）降低，展示了其在稀疏监督条件下的优越性能。

## 🎯 应用场景

RaCalNet的研究成果在自动驾驶、机器人导航和增强现实等领域具有广泛的应用潜力。通过降低对密集数据的依赖，该方法能够在资源受限的环境中实现高效的深度估计，推动相关技术的普及和发展。

## 📄 摘要（原文）

> Dense depth estimation using millimeter-wave radar typically requires dense LiDAR supervision, generated via multi-frame projection and interpolation, for guiding the learning of accurate depth from sparse radar measurements and RGB images. However, this paradigm is both costly and data-intensive. To address this, we propose RaCalNet, a novel framework that eliminates the need for dense supervision by using sparse LiDAR to supervise the learning of refined radar measurements, resulting in a supervision density of merely around 1\% compared to dense-supervised methods. RaCalNet is composed of two key modules. The Radar Recalibration module performs radar point screening and pixel-wise displacement refinement, producing accurate and reliable depth priors from sparse radar inputs. These priors are then used by the Metric Depth Optimization module, which learns to infer scene-level scale priors and fuses them with monocular depth predictions to achieve metrically accurate outputs. This modular design enhances structural consistency and preserves fine-grained geometric details. Despite relying solely on sparse supervision, RaCalNet produces depth maps with clear object contours and fine-grained textures, demonstrating superior visual quality compared to state-of-the-art dense-supervised methods. Quantitatively, it achieves performance comparable to existing methods on the ZJU-4DRadarCam dataset and yields a 34.89\% RMSE reduction in real-world deployment scenarios. We plan to gradually release the code and models in the future at https://github.com/818slam/RaCalNet.git.

