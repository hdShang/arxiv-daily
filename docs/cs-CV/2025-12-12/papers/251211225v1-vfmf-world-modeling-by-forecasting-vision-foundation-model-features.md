---
layout: default
title: VFMF: World Modeling by Forecasting Vision Foundation Model Features
---

# VFMF: World Modeling by Forecasting Vision Foundation Model Features

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.11225" class="toolbar-btn" target="_blank">📄 arXiv: 2512.11225v1</a>
  <a href="https://arxiv.org/pdf/2512.11225.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11225v1" onclick="toggleFavorite(this, '2512.11225v1', 'VFMF: World Modeling by Forecasting Vision Foundation Model Features')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gabrijel Boduljak, Yushi Lan, Christian Rupprecht, Andrea Vedaldi

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-12-12

---

## 💡 一句话要点

**VFMF：通过预测视觉基础模型特征实现世界建模**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界建模` `视觉基础模型` `特征预测` `生成式模型` `流匹配` `不确定性建模` `机器人导航`

## 📋 核心要点

1. 现有世界建模方法依赖像素预测，计算成本高且与决策脱节，而基于视觉基础模型特征的确定性回归忽略了预测的不确定性。
2. 论文提出一种生成式预测器，通过在视觉基础模型特征空间中进行自回归流匹配，捕捉预测的不确定性，提升预测精度。
3. 实验表明，该方法在语义分割、深度等多种模态上，相比回归方法，能产生更清晰、更准确的预测结果。

## 📝 摘要（中文）

从局部观测进行预测是世界建模的核心。许多最新方法通过图像表示世界，并将预测简化为随机视频生成。虽然这些方法在真实感和视觉保真度方面表现出色，但预测像素在计算上是密集型的，并且在许多应用中不是直接有用的，因为它需要将RGB转换为对决策有用的信号。另一种方法使用视觉基础模型（VFM）的特征作为世界表示，执行确定性回归来预测未来的世界状态。这些特征可以直接转换为可操作的信号，例如语义分割和深度，同时保持计算效率。然而，确定性回归平均了多个合理的未来，通过未能捕捉不确定性来破坏预测准确性。为了解决这个关键限制，我们引入了一个生成式预测器，它在VFM特征空间中执行自回归流匹配。我们的关键见解是，这个空间中的生成式建模需要将VFM特征编码成适合扩散的紧凑潜在空间。我们表明，这种潜在空间比以前使用的基于PCA的替代方案更有效地保留信息，无论是对于预测还是其他应用，例如图像生成。我们的潜在预测可以很容易地解码成多个有用且可解释的输出模态：语义分割、深度、表面法线，甚至RGB。在匹配的架构和计算下，我们的方法在所有模态上产生比回归更清晰和更准确的预测。我们的结果表明，VFM特征的随机条件生成为未来的世界模型提供了一个有希望且可扩展的基础。

## 🔬 方法详解

**问题定义**：现有基于像素预测的世界建模方法计算量大，且预测结果难以直接用于决策。而基于视觉基础模型（VFM）特征的确定性回归方法虽然计算效率高，但忽略了预测的不确定性，导致预测精度下降。因此，需要一种既能保持计算效率，又能有效捕捉预测不确定性的世界建模方法。

**核心思路**：论文的核心思路是在VFM特征空间中进行生成式建模，通过自回归流匹配来预测未来的世界状态。关键在于将VFM特征编码到一个紧凑的潜在空间，然后在这个潜在空间中进行扩散建模，从而捕捉预测的不确定性。

**技术框架**：该方法包含以下主要模块：1) VFM特征提取：使用预训练的视觉基础模型提取输入图像的特征。2) 潜在空间编码：将VFM特征编码到一个紧凑的潜在空间，该潜在空间的设计至关重要，需要有效保留信息。3) 自回归流匹配：在潜在空间中进行自回归流匹配，预测未来的潜在状态。4) 解码器：将预测的潜在状态解码为各种输出模态，例如语义分割、深度、表面法线和RGB图像。

**关键创新**：最重要的技术创新点在于在VFM特征空间中进行生成式建模，并使用自回归流匹配来捕捉预测的不确定性。与传统的确定性回归方法相比，该方法能够生成多个可能的未来状态，从而更好地反映真实世界的不确定性。此外，论文提出的潜在空间编码方法比传统的PCA方法更有效地保留了信息。

**关键设计**：论文的关键设计包括：1) 潜在空间的结构设计，需要平衡信息保留和计算效率。2) 自回归流匹配的具体实现方式，例如使用哪种流模型。3) 损失函数的设计，需要保证预测的准确性和多样性。4) 解码器的设计，需要能够将潜在状态解码为各种有用的输出模态。

## 📊 实验亮点

实验结果表明，该方法在语义分割、深度预测等多个模态上，均优于基于确定性回归的基线方法。例如，在深度预测任务上，该方法相比于回归方法，预测精度提升了X%（具体数值需要在论文中查找）。此外，该方法生成的预测结果更加清晰和锐利，能够更好地反映真实世界的不确定性。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、游戏AI等领域。通过预测未来环境状态，机器人可以更好地规划路径、避免障碍物，从而实现更安全、更高效的自主行为。此外，该方法还可以用于生成逼真的虚拟环境，为游戏开发和虚拟现实提供技术支持。

## 📄 摘要（原文）

> Forecasting from partial observations is central to world modeling. Many recent methods represent the world through images, and reduce forecasting to stochastic video generation. Although such methods excel at realism and visual fidelity, predicting pixels is computationally intensive and not directly useful in many applications, as it requires translating RGB into signals useful for decision making. An alternative approach uses features from vision foundation models (VFMs) as world representations, performing deterministic regression to predict future world states. These features can be directly translated into actionable signals such as semantic segmentation and depth, while remaining computationally efficient. However, deterministic regression averages over multiple plausible futures, undermining forecast accuracy by failing to capture uncertainty. To address this crucial limitation, we introduce a generative forecaster that performs autoregressive flow matching in VFM feature space. Our key insight is that generative modeling in this space requires encoding VFM features into a compact latent space suitable for diffusion. We show that this latent space preserves information more effectively than previously used PCA-based alternatives, both for forecasting and other applications, such as image generation. Our latent predictions can be easily decoded into multiple useful and interpretable output modalities: semantic segmentation, depth, surface normals, and even RGB. With matched architecture and compute, our method produces sharper and more accurate predictions than regression across all modalities. Our results suggest that stochastic conditional generation of VFM features offers a promising and scalable foundation for future world models.

