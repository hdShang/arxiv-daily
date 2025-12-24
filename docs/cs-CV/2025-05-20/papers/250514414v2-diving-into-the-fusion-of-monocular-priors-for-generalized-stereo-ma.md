---
layout: default
title: Diving into the Fusion of Monocular Priors for Generalized Stereo Matching
---

# Diving into the Fusion of Monocular Priors for Generalized Stereo Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14414" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14414v2</a>
  <a href="https://arxiv.org/pdf/2505.14414.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14414v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14414v2', 'Diving into the Fusion of Monocular Priors for Generalized Stereo Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengtang Yao, Lidong Yu, Zhidan Liu, Jiaxi Zeng, Yuwei Wu, Yunde Jia

**分类**: cs.CV

**发布日期**: 2025-05-20 (更新: 2025-08-18)

**备注**: Code: https://github.com/YaoChengTang/Diving-into-the-Fusion-of-Monocular-Priors-for-Generalized-Stereo-Matching

**期刊**: ICCV 2025 Oral

---

## 💡 一句话要点

**提出二元局部排序图以解决立体匹配中的单目先验融合问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `立体匹配` `单目先验` `深度学习` `计算机视觉` `图像处理` `视觉基础模型` `局部排序图`

## 📋 核心要点

1. 现有立体匹配方法在处理遮挡和非朗伯表面等不良区域时表现不佳，导致匹配结果不准确。
2. 本文提出通过二元局部排序图来指导单目先验的融合，解决了深度图与视差之间的对齐问题。
3. 实验结果显示，该方法在多个数据集上显著提升了立体匹配的性能，验证了其有效性和高效性。

## 📝 摘要（中文）

立体匹配在处理遮挡和非朗伯表面等不良区域时面临挑战。融合单目先验已被证明对解决这些问题有帮助，但从小型立体数据集中学习的偏置单目先验限制了其泛化能力。本文深入探讨了从视觉基础模型中获取的无偏单目先验在不良区域的应用，识别出影响融合的三个主要问题。我们提出了一种二元局部排序图来指导融合，将深度图转换为二元相对格式，统一相对和绝对深度表示，并通过重加权初始视差更新来解决局部最优和噪声问题。最终，我们将单目深度的直接融合形式化为一个注册问题，利用像素级线性回归模块进行全局和自适应对齐。实验表明，该方法在从SceneFlow泛化到Middlebury和Booster数据集时显著提高了性能，同时几乎没有降低效率。

## 🔬 方法详解

**问题定义**：本文旨在解决立体匹配中因遮挡和非朗伯表面导致的匹配困难，现有方法因偏置单目先验的限制而难以泛化。

**核心思路**：我们提出了一种二元局部排序图，通过将深度图转换为二元相对格式，统一相对和绝对深度表示，从而指导单目先验的有效融合。

**技术框架**：整体流程包括三个主要阶段：首先，计算单目深度图；其次，利用二元局部排序图重加权初始视差更新；最后，将单目深度与视差的直接融合形式化为注册问题，使用线性回归模块进行对齐。

**关键创新**：最重要的创新在于提出了二元局部排序图，这一方法有效解决了深度图与视差之间的对齐问题，并缓解了局部最优和噪声影响。

**关键设计**：在参数设置上，采用了适应性重加权机制，并设计了像素级线性回归模块，以确保深度与视差的全局对齐。

## 📊 实验亮点

实验结果表明，所提方法在SceneFlow到Middlebury和Booster数据集的泛化过程中，性能显著提升，具体提升幅度达到XX%，同时保持了高效性，几乎没有降低计算速度。

## 🎯 应用场景

该研究在计算机视觉领域具有广泛的应用潜力，尤其是在自动驾驶、机器人导航和增强现实等场景中，能够提高立体视觉系统的准确性和鲁棒性。未来，该方法的推广可能会推动更多基于视觉的智能系统的发展。

## 📄 摘要（原文）

> The matching formulation makes it naturally hard for the stereo matching to handle ill-posed regions like occlusions and non-Lambertian surfaces. Fusing monocular priors has been proven helpful for ill-posed matching, but the biased monocular prior learned from small stereo datasets constrains the generalization. Recently, stereo matching has progressed by leveraging the unbiased monocular prior from the vision foundation model (VFM) to improve the generalization in ill-posed regions. We dive into the fusion process and observe three main problems limiting the fusion of the VFM monocular prior. The first problem is the misalignment between affine-invariant relative monocular depth and absolute depth of disparity. Besides, when we use the monocular feature in an iterative update structure, the over-confidence in the disparity update leads to local optima results. A direct fusion of a monocular depth map could alleviate the local optima problem, but noisy disparity results computed at the first several iterations will misguide the fusion. In this paper, we propose a binary local ordering map to guide the fusion, which converts the depth map into a binary relative format, unifying the relative and absolute depth representation. The computed local ordering map is also used to re-weight the initial disparity update, resolving the local optima and noisy problem. In addition, we formulate the final direct fusion of monocular depth to the disparity as a registration problem, where a pixel-wise linear regression module can globally and adaptively align them. Our method fully exploits the monocular prior to support stereo matching results effectively and efficiently. We significantly improve the performance from the experiments when generalizing from SceneFlow to Middlebury and Booster datasets while barely reducing the efficiency.

