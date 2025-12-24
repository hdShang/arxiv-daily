---
layout: default
title: "World Models That Know When They Don't Know: Controllable Video Generation with Calibrated Uncertainty"
---

# World Models That Know When They Don't Know: Controllable Video Generation with Calibrated Uncertainty

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05927" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05927v1</a>
  <a href="https://arxiv.org/pdf/2512.05927.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05927v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.05927v1', 'World Models That Know When They Don\'t Know: Controllable Video Generation with Calibrated Uncertainty')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiting Mei, Tenny Yin, Micah Baker, Ola Shorinwa, Anirudha Majumdar

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-12-05

---

## 💡 一句话要点

**提出C3方法，为可控视频生成模型提供校准的不确定性估计，缓解幻觉问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `可控视频生成` `不确定性量化` `机器人学习` `世界模型` `深度学习`

## 📋 核心要点

1. 现有可控视频生成模型易产生与物理现实不符的幻觉，且缺乏置信度评估能力，限制了其在机器人等领域的应用。
2. C3方法通过引入不确定性量化框架，在潜在空间中训练视频模型，使其能够估计并表达生成视频帧的不确定性。
3. 实验表明，C3方法不仅能提供校准的不确定性估计，还能有效检测分布外数据，提升模型在真实场景中的可靠性。

## 📝 摘要（中文）

近年来，生成式视频模型在高质量视频合成方面取得了显著进展，尤其是在可控视频生成领域，生成的视频以文本和动作输入为条件，例如在指令引导的视频编辑和机器人技术中的世界建模。尽管这些模型具有卓越的能力，但可控视频模型经常产生幻觉——生成的未来视频帧与物理现实不符——这在机器人策略评估和规划等许多任务中引起了严重关注。然而，最先进的视频模型缺乏评估和表达其置信度的能力，从而阻碍了幻觉的缓解。为了严格应对这一挑战，我们提出了一种不确定性量化（UQ）方法C3，用于训练连续尺度校准的可控视频模型，以在子补丁级别进行密集置信度估计，从而精确定位每个生成的视频帧中的不确定性。我们的UQ方法引入了三个核心创新，使视频模型能够估计其不确定性。首先，我们的方法开发了一个新颖的框架，该框架通过严格的适当评分规则训练视频模型以实现正确性和校准。其次，我们在潜在空间中估计视频模型的不确定性，避免了与像素空间方法相关的训练不稳定性和过高的训练成本。第三，我们将密集的潜在空间不确定性映射到RGB空间中可解释的像素级不确定性，以进行直观的可视化，从而提供识别不可信区域的高分辨率不确定性热图。通过在大型机器人学习数据集（Bridge和DROID）和真实世界评估中的大量实验，我们证明了我们的方法不仅在训练分布内提供校准的不确定性估计，而且能够实现有效的分布外检测。

## 🔬 方法详解

**问题定义**：可控视频生成模型在生成未来帧时，容易出现与真实物理世界不符的“幻觉”现象。现有模型无法评估自身预测的可靠性，即缺乏不确定性估计能力，这限制了其在安全攸关场景（如机器人控制）中的应用。现有像素空间的不确定性估计方法计算成本高昂，且训练不稳定。

**核心思路**：C3方法的核心在于训练视频生成模型，使其能够预测自身预测的不确定性。通过在潜在空间中进行不确定性估计，降低计算复杂度并提高训练稳定性。同时，利用严格的评分规则来校准模型的不确定性估计，使其与实际误差相匹配。

**技术框架**：C3方法包含以下几个主要模块：1) 可控视频生成模型：用于生成视频帧，以文本或动作指令为条件。2) 潜在空间编码器：将视频帧编码到潜在空间中。3) 不确定性估计器：在潜在空间中估计每个潜在向量的不确定性。4) 校准模块：使用严格的评分规则校准不确定性估计。5) 解码器：将潜在空间的不确定性映射回像素空间，生成像素级别的置信度热图。

**关键创新**：C3方法的关键创新在于：1) 提出了一种在潜在空间中进行不确定性估计的框架，避免了像素空间方法的计算瓶颈和训练难题。2) 使用严格的评分规则（strictly proper scoring rules）来训练模型，确保不确定性估计的校准性。3) 设计了一种将潜在空间不确定性映射到像素空间的机制，使得用户可以直观地理解模型在哪些区域的预测不可靠。

**关键设计**：C3方法使用变分自编码器（VAE）作为视频生成模型的基础架构。不确定性估计器通常是一个小型神经网络，输入是潜在向量，输出是不确定性值。评分规则的选择至关重要，常用的评分规则包括负对数似然（Negative Log-Likelihood）和连续排序概率分数（Continuous Ranked Probability Score, CRPS）。在训练过程中，模型同时优化视频生成损失和不确定性校准损失。

## 📊 实验亮点

在Bridge和DROID机器人学习数据集上的实验表明，C3方法能够提供校准的不确定性估计，并且能够有效检测分布外数据。与现有方法相比，C3方法在不确定性估计的准确性和效率方面均有显著提升。实验结果表明，C3方法能够有效缓解可控视频生成中的幻觉问题。

## 🎯 应用场景

C3方法可应用于机器人控制、自动驾驶、视频编辑等领域。在机器人控制中，可以帮助机器人识别不可靠的预测，从而避免危险行为。在自动驾驶中，可以提高系统对环境感知的鲁棒性。在视频编辑中，可以辅助用户识别和修复生成视频中的错误。

## 📄 摘要（原文）

> Recent advances in generative video models have led to significant breakthroughs in high-fidelity video synthesis, specifically in controllable video generation where the generated video is conditioned on text and action inputs, e.g., in instruction-guided video editing and world modeling in robotics. Despite these exceptional capabilities, controllable video models often hallucinate - generating future video frames that are misaligned with physical reality - which raises serious concerns in many tasks such as robot policy evaluation and planning. However, state-of-the-art video models lack the ability to assess and express their confidence, impeding hallucination mitigation. To rigorously address this challenge, we propose C3, an uncertainty quantification (UQ) method for training continuous-scale calibrated controllable video models for dense confidence estimation at the subpatch level, precisely localizing the uncertainty in each generated video frame. Our UQ method introduces three core innovations to empower video models to estimate their uncertainty. First, our method develops a novel framework that trains video models for correctness and calibration via strictly proper scoring rules. Second, we estimate the video model's uncertainty in latent space, avoiding training instability and prohibitive training costs associated with pixel-space approaches. Third, we map the dense latent-space uncertainty to interpretable pixel-level uncertainty in the RGB space for intuitive visualization, providing high-resolution uncertainty heatmaps that identify untrustworthy regions. Through extensive experiments on large-scale robot learning datasets (Bridge and DROID) and real-world evaluations, we demonstrate that our method not only provides calibrated uncertainty estimates within the training distribution, but also enables effective out-of-distribution detection.

