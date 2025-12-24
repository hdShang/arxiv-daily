---
layout: default
title: "MinD: Learning A Dual-System World Model for Real-Time Planning and Implicit Risk Analysis"
---

# MinD: Learning A Dual-System World Model for Real-Time Planning and Implicit Risk Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18897" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18897v2</a>
  <a href="https://arxiv.org/pdf/2506.18897.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18897v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18897v2', 'MinD: Learning A Dual-System World Model for Real-Time Planning and Implicit Risk Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaowei Chi, Kuangzhi Ge, Jiaming Liu, Siyuan Zhou, Peidong Jia, Zichen He, Yuzhen Liu, Tingguang Li, Lei Han, Sirui Han, Shanghang Zhang, Yike Guo

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-23 (更新: 2025-08-20)

---

## 💡 一句话要点

**提出MinD以解决实时规划与隐式风险分析问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成模型` `实时规划` `风险分析` `双系统模型` `机器人操作` `潜变量` `异步扩散` `动作预测`

## 📋 核心要点

1. 现有视频生成模型在未来状态预测方面的分布建模能力未得到充分利用，且实时机器人应用中逐帧视频扩散计算效率低下。
2. 提出MinD，通过低频视觉生成器和高频扩散策略的双系统模型，实现实时规划与隐式风险分析，提升了决策效率。
3. MinD在RL-Bench和真实世界任务中的成功率分别为63%和60%，并以11.3 FPS的速度运行，展示了其在控制信号中的高效性。

## 📝 摘要（中文）

视频生成模型（VGM）已成为视觉-语言-动作（VLA）模型的重要基础，但现有方法未充分利用其分布建模能力来预测未来状态。本文提出Manipulate in Dream（MinD），一种双系统世界模型，旨在实现实时、风险感知的规划。MinD采用两种异步扩散过程：低频视觉生成器（LoDiff）预测未来场景，高频扩散策略（HiDiff）输出动作。关键在于机器人策略不需要完全去噪的帧，而是依赖于单次去噪步骤生成的低分辨率潜变量。通过引入DiffMatcher模块，论文实现了视频与动作的对齐。实验结果表明，MinD在RL-Bench上成功率达到63%，在真实世界的Franka任务中为60%，且以11.3 FPS的速度运行，展示了单步潜变量在控制信号中的高效性。此外，MinD能够提前识别74%的潜在任务失败，为实时监控和干预提供安全信号。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频生成模型在未来状态预测中的不足，尤其是在实时机器人应用中的计算效率问题。现有方法在生成过程中未能有效整合生成过程与特征学习，导致实时性不足。

**核心思路**：论文提出的MinD模型通过引入低频和高频的双系统扩散过程，分别用于场景预测和动作输出，从而实现高效的实时规划。关键在于机器人策略可以依赖于低分辨率的潜变量，而非完全去噪的帧。

**技术框架**：MinD的整体架构包括两个主要模块：低频视觉生成器（LoDiff）用于生成未来场景，高频扩散策略（HiDiff）用于生成控制动作。此外，DiffMatcher模块用于实现视频与动作的对齐，确保两者之间的同步。

**关键创新**：MinD的主要创新在于其双系统模型的设计，尤其是通过低分辨率潜变量实现的高效决策过程。这一设计与传统方法的逐帧生成方式形成鲜明对比，显著提升了计算效率。

**关键设计**：在模型设计中，采用了异步扩散过程和共训练策略，确保LoDiff和HiDiff之间的有效协同。此外，DiffMatcher模块的引入使得视频与动作的对齐更加精准，提升了整体系统的性能。实验中，MinD在不同任务上表现出色，验证了其设计的有效性。

## 📊 实验亮点

MinD在RL-Bench任务中的成功率达到63%，在真实世界Franka任务中为60%，并以11.3 FPS的速度运行，展示了其在控制信号中的高效性。此外，MinD能够提前识别74%的潜在任务失败，为实时监控提供了重要的安全信号。

## 🎯 应用场景

MinD模型在机器人操作、自动驾驶、智能监控等领域具有广泛的应用潜力。其高效的实时规划能力和风险分析功能能够显著提升机器人在复杂环境中的决策能力，未来可能推动智能机器人技术的进一步发展与应用。

## 📄 摘要（原文）

> Video Generation Models (VGMs) have become powerful backbones for Vision-Language-Action (VLA) models, leveraging large-scale pretraining for robust dynamics modeling. However, current methods underutilize their distribution modeling capabilities for predicting future states. Two challenges hinder progress: integrating generative processes into feature learning is both technically and conceptually underdeveloped, and naive frame-by-frame video diffusion is computationally inefficient for real-time robotics. To address these, we propose Manipulate in Dream (MinD), a dual-system world model for real-time, risk-aware planning. MinD uses two asynchronous diffusion processes: a low-frequency visual generator (LoDiff) that predicts future scenes and a high-frequency diffusion policy (HiDiff) that outputs actions. Our key insight is that robotic policies do not require fully denoised frames but can rely on low-resolution latents generated in a single denoising step. To connect early predictions to actions, we introduce DiffMatcher, a video-action alignment module with a novel co-training strategy that synchronizes the two diffusion models. MinD achieves a 63% success rate on RL-Bench, 60% on real-world Franka tasks, and operates at 11.3 FPS, demonstrating the efficiency of single-step latent features for control signals. Furthermore, MinD identifies 74% of potential task failures in advance, providing real-time safety signals for monitoring and intervention. This work establishes a new paradigm for efficient and reliable robotic manipulation using generative world models.

