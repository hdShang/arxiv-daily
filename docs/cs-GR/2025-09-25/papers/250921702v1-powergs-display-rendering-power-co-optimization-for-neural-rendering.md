---
layout: default
title: "PowerGS: Display-Rendering Power Co-Optimization for Neural Rendering in Power-Constrained XR Systems"
---

# PowerGS: Display-Rendering Power Co-Optimization for Neural Rendering in Power-Constrained XR Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21702" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21702v1</a>
  <a href="https://arxiv.org/pdf/2509.21702.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21702v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21702v1', 'PowerGS: Display-Rendering Power Co-Optimization for Neural Rendering in Power-Constrained XR Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weikai Lin, Sushant Kondguli, Carl Marshall, Yuhao Zhu

**分类**: cs.GR

**发布日期**: 2025-09-25

**备注**: 10 pages, Accepted to Siggraph Asia 2025

**🔗 代码/项目**: [GITHUB](https://github.com/horizon-research/PowerGS)

---

## 💡 一句话要点

**PowerGS：面向功率受限XR系统的神经渲染显示-渲染功率协同优化**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `神经渲染` `功率优化` `扩展现实` `注视点渲染`

## 📋 核心要点

1. 现有3DGS模型在功率受限的XR设备上效率不足，无法满足低功耗需求。
2. PowerGS通过联合优化渲染和显示功率，在保证质量的前提下，显著降低功耗。
3. 实验表明，PowerGS相比现有3DGS模型，总功耗降低高达86%，且主客观质量损失极小。

## 📝 摘要（中文）

3D高斯溅射(3DGS)结合了经典的基于图像的渲染、基于点的图形和现代可微技术，为传统的基于物理的渲染提供了一种有趣的替代方案。然而，3DGS系列模型对于需要在瓦特级别运行的功率受限的扩展现实(XR)设备来说效率远不够高。本文介绍了PowerGS，这是第一个在质量约束下联合最小化3DGS渲染和显示功率的框架。我们提出了一个通用的问题公式，并表明解决该问题相当于：1) 识别由显示和渲染功率所覆盖的景观中的等质量曲线；2) 识别给定曲线上功率最小的点，如果对曲线进行适当的参数化，则该点具有闭式解。PowerGS还支持注视点渲染，以进一步节省功耗。大量的实验和用户研究表明，与最先进的3DGS模型相比，PowerGS实现了高达86%的总功率降低，同时在主观和客观质量上的损失最小。代码可在https://github.com/horizon-research/PowerGS 获取。

## 🔬 方法详解

**问题定义**：论文旨在解决在功率受限的XR设备上，3DGS渲染功耗过高的问题。现有的3DGS模型没有充分考虑XR设备的功率限制，导致无法在低功耗下提供高质量的渲染效果。因此，如何在保证渲染质量的前提下，最小化渲染和显示功耗，是本研究要解决的核心问题。

**核心思路**：PowerGS的核心思路是联合优化渲染和显示功率，找到在满足特定渲染质量约束下的最小功率点。通过对渲染和显示功率之间的关系进行建模，并利用等质量曲线的概念，将问题转化为一个优化问题。通过对等质量曲线进行参数化，可以找到功率最小的闭式解。

**技术框架**：PowerGS框架主要包含以下几个阶段：1) 建立渲染和显示功率的数学模型；2) 定义渲染质量的度量标准；3) 确定等质量曲线，即在不同渲染和显示功率组合下，渲染质量保持不变的曲线；4) 在等质量曲线上寻找功率最小的点，该点对应于在给定质量约束下的最优渲染和显示功率分配。PowerGS还支持注视点渲染，通过降低非注视区域的渲染质量来进一步节省功耗。

**关键创新**：PowerGS的关键创新在于首次提出了渲染和显示功率的协同优化方法，并将其应用于3DGS渲染。与传统的渲染优化方法不同，PowerGS不仅考虑了渲染过程的功耗，还考虑了显示过程的功耗，从而实现了更全面的功率优化。此外，PowerGS还提出了基于等质量曲线的优化方法，能够有效地找到在给定质量约束下的最优功率分配方案。

**关键设计**：PowerGS的关键设计包括：1) 渲染和显示功率的精确建模，需要考虑硬件特性和渲染算法的复杂度；2) 渲染质量的客观度量，例如PSNR、SSIM等，以及主观用户体验评估；3) 等质量曲线的参数化方法，需要选择合适的参数化方式，以便能够有效地找到功率最小的闭式解；4) 注视点渲染的策略，需要根据用户的视线位置动态调整渲染质量。

## 📊 实验亮点

PowerGS通过联合优化渲染和显示功率，实现了显著的功耗降低。实验结果表明，与最先进的3DGS模型相比，PowerGS的总功耗降低高达86%，同时在主观和客观质量上的损失最小。这表明PowerGS在保证渲染质量的前提下，能够有效地降低XR设备的功耗，具有很高的实用价值。

## 🎯 应用场景

PowerGS在功率受限的XR设备（如AR/VR头显）上具有广泛的应用前景。它可以显著降低设备的功耗，延长电池续航时间，并提高用户体验。此外，PowerGS还可以应用于移动设备、嵌入式系统等其他需要低功耗3D渲染的场景。该研究成果有助于推动XR技术的普及和发展。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) combines classic image-based rendering, pointbased graphics, and modern differentiable techniques, and offers an interesting alternative to traditional physically-based rendering. 3DGS-family models are far from efficient for power-constrained Extended Reality (XR) devices, which need to operate at a Watt-level. This paper introduces PowerGS, the first framework to jointly minimize the rendering and display power in 3DGS under a quality constraint. We present a general problem formulation and show that solving the problem amounts to 1) identifying the iso-quality curve(s) in the landscape subtended by the display and rendering power and 2) identifying the power-minimal point on a given curve, which has a closed-form solution given a proper parameterization of the curves. PowerGS also readily supports foveated rendering for further power savings. Extensive experiments and user studies show that PowerGS achieves up to 86% total power reduction compared to state-of-the-art 3DGS models, with minimal loss in both subjective and objective quality. Code is available at https://github.com/horizon-research/PowerGS.

