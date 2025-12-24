---
layout: default
title: "Occlusion Boundary and Depth: Mutual Enhancement via Multi-Task Learning"
---

# Occlusion Boundary and Depth: Mutual Enhancement via Multi-Task Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21231" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21231v3</a>
  <a href="https://arxiv.org/pdf/2505.21231.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21231v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21231v3', 'Occlusion Boundary and Depth: Mutual Enhancement via Multi-Task Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lintao Xu, Yinghao Wang, Chaohui Wang

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-11-26)

**备注**: WACV 2026

**🔗 代码/项目**: [GITHUB](https://github.com/xul-ops/MoDOT)

---

## 💡 一句话要点

**提出MoDOT框架以解决单目深度估计与遮挡边界估计的互补问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `遮挡边界估计` `单目深度估计` `多任务学习` `计算机视觉` `深度学习`

## 📋 核心要点

1. 现有方法在处理遮挡边界和深度估计时，往往无法有效利用两者之间的互补信息，导致性能不足。
2. 本文提出MoDOT框架，通过交叉注意力机制和约束损失函数，联合优化深度和遮挡边界，提高估计精度。
3. 实验结果显示，MoDOT在合成数据集和NYUD-v2上均表现优异，深度图的边界更加清晰，几何保真度显著提升。

## 📝 摘要（中文）

遮挡边界估计（OBE）识别由物体间遮挡和自遮挡引起的边界，与单目深度估计（MDE）密切相关。遮挡边界为解决深度模糊提供几何线索，而深度信息又能改善遮挡推理。本文提出MoDOT框架，通过交叉注意力条模块（CASM）和遮挡深度约束损失（OBDCL）联合估计深度和遮挡边界。我们还贡献了OB-Hypersim数据集，包含精确的深度和自遮挡处理的边界注释。实验结果表明，MoDOT在多个数据集上显著优于单任务和多任务基线，且在真实场景中表现出良好的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决单目深度估计与遮挡边界估计之间的互补性不足问题。现有方法往往忽视两者的关联，导致深度推理和遮挡边界识别的性能下降。

**核心思路**：论文提出MoDOT框架，通过引入交叉注意力条模块（CASM）和遮挡深度约束损失（OBDCL），实现深度和遮挡边界的联合估计，从而充分利用两者之间的几何关系。

**技术框架**：MoDOT框架包括两个主要模块：CASM用于提取中层遮挡边界特征以辅助深度预测，OBDCL用于确保深度估计与遮挡边界之间的几何一致性。整体流程为：输入图像→特征提取→联合估计→损失计算→优化。

**关键创新**：最重要的创新在于CASM和OBDCL的结合，前者通过注意力机制增强了特征的表达能力，后者则确保了深度和遮挡边界之间的几何一致性，这在现有方法中是未曾实现的。

**关键设计**：在网络结构上，CASM设计为多层次的注意力模块，以便更好地捕捉遮挡特征；OBDCL则通过引入几何约束，确保深度估计与遮挡边界的相互验证。

## 📊 实验亮点

在实验中，MoDOT在两个合成数据集和NYUD-v2上均取得了显著的性能提升，相较于单任务基线，深度估计的准确性提高了XX%，而在多任务竞争者中，性能提升幅度达到YY%。此外，模型在真实场景中的泛化能力强，无需微调即可生成更清晰的深度图。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和增强现实等场景。在这些应用中，准确的深度信息和遮挡边界识别对于环境理解和决策至关重要。未来，该方法有望推动更智能的视觉系统的发展，提升其在复杂环境中的表现。

## 📄 摘要（原文）

> Occlusion Boundary Estimation (OBE) identifies boundaries arising from both inter-object occlusions and self-occlusion within individual objects. This task is closely related to Monocular Depth Estimation (MDE), which infers depth from a single image, as Occlusion Boundaries (OBs) provide critical geometric cues for resolving depth ambiguities, while depth can conversely refine occlusion reasoning. In this paper, we aim to systematically model and exploit this mutually beneficial relationship. To this end, we propose MoDOT, a novel framework for joint estimation of depth and OBs, which incorporates a new Cross-Attention Strip Module (CASM) to leverage mid-level OB features for depth prediction, and a novel OB-Depth Constraint Loss (OBDCL) to enforce geometric consistency. To facilitate this study, we contribute OB-Hypersim, a large-scale photorealistic dataset with precise depth and self-occlusion-handled OB annotations. Extensive experiments on two synthetic datasets and NYUD-v2 demonstrate that MoDOT achieves significantly better performance than single-task baselines and multi-task competitors. Furthermore, models trained solely on our synthetic data demonstrate strong generalization to real-world scenes without fine-tuning, producing depth maps with sharper boundaries and improved geometric fidelity. Collectively, these results underscore the significant benefits of jointly modeling OBs and depth. Code and resources are available at https://github.com/xul-ops/MoDOT.

