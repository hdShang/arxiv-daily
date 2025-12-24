---
layout: default
title: Harnessing Foundation Models for Robust and Generalizable 6-DOF Bronchoscopy Localization
---

# Harnessing Foundation Models for Robust and Generalizable 6-DOF Bronchoscopy Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24249" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24249v1</a>
  <a href="https://arxiv.org/pdf/2505.24249.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24249v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24249v1', 'Harnessing Foundation Models for Robust and Generalizable 6-DOF Bronchoscopy Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingyao Tian, Huai Liao, Xinyan Huang, Bingyu Yang, Hongbin Liu

**分类**: cs.CV

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出PANSv2以解决支气管镜定位的鲁棒性与泛化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `支气管镜定位` `深度估计` `地标检测` `姿态优化` `鲁棒性` `泛化能力` `内窥镜基础模型` `自动重初始化`

## 📋 核心要点

1. 现有支气管镜定位方法在患者案例间的泛化能力不足，且在视觉退化情况下表现不佳，影响临床应用。
2. 本文提出的PANSv2框架通过整合深度估计、地标检测和中心线约束，优化姿态评估，提升了鲁棒性和泛化能力。
3. 实验结果显示，PANSv2在10个患者案例的数据集上实现了最高的跟踪成功率，SR-5指标提升了18.1%。

## 📝 摘要（中文）

基于视觉的6自由度支气管镜定位为精准且经济的介入指导提供了有前景的解决方案。然而，现有方法在患者案例间的泛化能力有限，且在视觉退化情况下表现不佳。为了解决这些挑战，本文提出了PANSv2框架，集成了深度估计、地标检测和中心线约束，形成统一的姿态优化框架。通过利用预训练的内窥镜基础模型EndoOmni和视频基础模型EndoMamba，PANSv2在多种支气管镜场景中提供了稳定的视觉表示。此外，自动重初始化模块能够在跟踪失败时重新建立姿态。实验结果表明，PANSv2在10个患者案例的数据集上实现了最高的跟踪成功率，相较于现有方法在SR-5指标上提升了18.1%。

## 🔬 方法详解

**问题定义**：本文旨在解决支气管镜定位中存在的泛化能力不足和视觉退化下的鲁棒性差的问题。现有方法在不同患者案例中表现不佳，且在视觉信息受损时容易出现跟踪失败。

**核心思路**：PANSv2框架通过整合多种视觉线索（如深度估计和地标检测）来优化姿态评估，旨在提高定位的鲁棒性和泛化能力。该设计使得模型能够在多种临床场景中稳定运行。

**技术框架**：PANSv2的整体架构包括深度估计模块、地标检测模块和中心线约束模块，所有模块共同作用于姿态优化。通过评估姿态概率，模型能够计算出最优的支气管镜姿态。

**关键创新**：PANSv2的主要创新在于引入了内窥镜基础模型EndoOmni和视频基础模型EndoMamba，这些模型经过多样化内窥镜数据集的预训练，提供了稳定且可迁移的视觉表示，显著提升了模型的泛化能力。

**关键设计**：在模型设计中，采用了自动重初始化模块来检测跟踪失败，并在可用的清晰视图下重新建立姿态。此外，损失函数和网络结构经过精心设计，以确保模型在不同场景下的稳定性和准确性。

## 📊 实验亮点

实验结果显示，PANSv2在10个患者案例的数据集上实现了最高的跟踪成功率，相较于现有方法在SR-5指标上提升了18.1%。这一显著的性能提升表明PANSv2在实际临床应用中的潜力，尤其是在复杂和多变的医疗环境中。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像引导的介入手术，尤其是在支气管镜检查和治疗中。通过提高定位的鲁棒性和泛化能力，PANSv2有望在实际临床中提供更为精准的指导，从而提升患者的治疗效果和安全性。未来，该技术可能扩展到其他类型的内窥镜手术中，进一步推动医疗技术的发展。

## 📄 摘要（原文）

> Vision-based 6-DOF bronchoscopy localization offers a promising solution for accurate and cost-effective interventional guidance. However, existing methods struggle with 1) limited generalization across patient cases due to scarce labeled data, and 2) poor robustness under visual degradation, as bronchoscopy procedures frequently involve artifacts such as occlusions and motion blur that impair visual information. To address these challenges, we propose PANSv2, a generalizable and robust bronchoscopy localization framework. Motivated by PANS that leverages multiple visual cues for pose likelihood measurement, PANSv2 integrates depth estimation, landmark detection, and centerline constraints into a unified pose optimization framework that evaluates pose probability and solves for the optimal bronchoscope pose. To further enhance generalization capabilities, we leverage the endoscopic foundation model EndoOmni for depth estimation and the video foundation model EndoMamba for landmark detection, incorporating both spatial and temporal analyses. Pretrained on diverse endoscopic datasets, these models provide stable and transferable visual representations, enabling reliable performance across varied bronchoscopy scenarios. Additionally, to improve robustness to visual degradation, we introduce an automatic re-initialization module that detects tracking failures and re-establishes pose using landmark detections once clear views are available. Experimental results on bronchoscopy dataset encompassing 10 patient cases show that PANSv2 achieves the highest tracking success rate, with an 18.1% improvement in SR-5 (percentage of absolute trajectory error under 5 mm) compared to existing methods, showing potential towards real clinical usage.

