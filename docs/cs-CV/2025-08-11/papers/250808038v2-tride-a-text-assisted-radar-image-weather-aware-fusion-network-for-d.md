---
layout: default
title: "TRIDE: A Text-assisted Radar-Image weather-aware fusion network for Depth Estimation"
---

# TRIDE: A Text-assisted Radar-Image weather-aware fusion network for Depth Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08038" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08038v2</a>
  <a href="https://arxiv.org/pdf/2508.08038.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08038v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08038v2', 'TRIDE: A Text-assisted Radar-Image weather-aware fusion network for Depth Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huawei Sun, Zixu Wang, Hao Feng, Julius Ott, Lorenzo Servadei, Robert Wille

**分类**: cs.CV

**发布日期**: 2025-08-11 (更新: 2025-08-18)

**备注**: Accepted by TMLR (2025.08)

**🔗 代码/项目**: [GITHUB](https://github.com/harborsarah/TRIDE)

---

## 💡 一句话要点

**提出TRIDE以解决天气影响下的深度估计问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `深度估计` `雷达-相机融合` `天气感知` `文本生成` `多模态学习`

## 📋 核心要点

1. 现有深度估计方法未考虑天气对传感器性能的影响，导致在恶劣天气条件下表现不佳。
2. 论文提出TRIDE，通过结合文本生成策略与雷达信息，改进了深度估计的准确性。
3. 在nuScenes数据集上，TRIDE相较于现有方法在MAE和RMSE上分别提升了12.87%和9.08%。

## 📝 摘要（中文）

深度估计对于自动驾驶至关重要，旨在解析车辆周围的三维环境。雷达传感器因其成本效益和鲁棒性而受到关注，但现有算法在融合雷达与相机特征时未考虑天气条件。本文首先提出了一种文本生成策略和特征提取与融合技术，以辅助单目深度估计，提升了KITTI数据集上的准确性。基于此，我们提出了TRIDE，一种雷达-相机融合算法，通过引入雷达点信息增强文本特征提取。为应对天气对传感器性能的影响，我们引入了天气感知融合模块，根据当前天气条件自适应调整雷达权重。我们的算法在nuScenes数据集上进行基准测试，显示出相较于现有最先进方法的性能提升，MAE提高了12.87%，RMSE提高了9.08%。

## 🔬 方法详解

**问题定义**：本论文旨在解决在不同天气条件下深度估计的准确性问题。现有方法在融合雷达与相机特征时未考虑天气因素，导致在恶劣天气下性能下降。

**核心思路**：论文提出了一种新的雷达-相机融合算法TRIDE，通过引入文本生成策略和天气感知模块，增强了深度估计的鲁棒性和准确性。

**技术框架**：TRIDE的整体架构包括文本生成模块、特征提取模块、天气感知融合模块和深度估计模块。文本生成模块提供额外的上下文信息，特征提取模块从雷达和相机中提取重要特征，天气感知模块根据实时天气条件调整雷达权重。

**关键创新**：最重要的创新在于引入天气感知融合模块，使得算法能够根据当前天气条件自适应调整雷达与相机的特征融合权重，从而提升在不同天气下的深度估计性能。

**关键设计**：在设计中，采用了自适应权重调整机制，结合了多模态特征提取和深度学习网络结构，损失函数则考虑了不同天气条件下的传感器表现，以优化整体深度估计效果。

## 📊 实验亮点

TRIDE在nuScenes数据集上的实验结果显示，MAE提升了12.87%，RMSE提升了9.08%。这些结果表明，TRIDE在处理恶劣天气条件下的深度估计任务时，相较于现有最先进方法具有显著的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和智能交通系统等。通过提高在各种天气条件下的深度估计准确性，TRIDE能够显著提升自动驾驶系统的安全性和可靠性，推动智能交通技术的发展。

## 📄 摘要（原文）

> Depth estimation, essential for autonomous driving, seeks to interpret the 3D environment surrounding vehicles. The development of radar sensors, known for their cost-efficiency and robustness, has spurred interest in radar-camera fusion-based solutions. However, existing algorithms fuse features from these modalities without accounting for weather conditions, despite radars being known to be more robust than cameras under adverse weather. Additionally, while Vision-Language models have seen rapid advancement, utilizing language descriptions alongside other modalities for depth estimation remains an open challenge. This paper first introduces a text-generation strategy along with feature extraction and fusion techniques that can assist monocular depth estimation pipelines, leading to improved accuracy across different algorithms on the KITTI dataset. Building on this, we propose TRIDE, a radar-camera fusion algorithm that enhances text feature extraction by incorporating radar point information. To address the impact of weather on sensor performance, we introduce a weather-aware fusion block that adaptively adjusts radar weighting based on current weather conditions. Our method, benchmarked on the nuScenes dataset, demonstrates performance gains over the state-of-the-art, achieving a 12.87% improvement in MAE and a 9.08% improvement in RMSE. Code: https://github.com/harborsarah/TRIDE

