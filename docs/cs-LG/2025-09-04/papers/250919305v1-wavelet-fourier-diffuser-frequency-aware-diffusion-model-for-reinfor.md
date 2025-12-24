---
layout: default
title: "Wavelet Fourier Diffuser: Frequency-Aware Diffusion Model for Reinforcement Learning"
---

# Wavelet Fourier Diffuser: Frequency-Aware Diffusion Model for Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19305" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19305v1</a>
  <a href="https://arxiv.org/pdf/2509.19305.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19305v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19305v1', 'Wavelet Fourier Diffuser: Frequency-Aware Diffusion Model for Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifu Luo, Yongzhe Chang, Xueqian Wang

**分类**: cs.LG, cs.AI, eess.SP

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**提出Wavelet Fourier Diffuser，解决离线强化学习中轨迹频率偏移问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `扩散模型` `频率分析` `小波变换` `傅里叶变换` `轨迹生成` `频率偏移`

## 📋 核心要点

1. 现有离线强化学习方法主要关注轨迹的时域特征，忽略了频域特征，导致轨迹频率偏移，影响性能。
2. WFDiffuser通过离散小波变换将轨迹分解为低频和高频分量，并利用短时傅里叶变换提取频域特征。
3. 在D4RL基准测试中，WFDiffuser有效缓解了频率偏移，生成更平滑稳定的轨迹，提升了决策性能。

## 📝 摘要（中文）

扩散概率模型在离线强化学习中通过直接建模轨迹序列展现出巨大潜力。然而，现有方法主要关注时域特征，忽略了频域特征，导致频率偏移和性能下降。本文从频域角度研究强化学习问题，观察到仅关注时域的方法会引入低频分量的偏移，导致轨迹不稳定和性能下降。为解决此问题，我们提出Wavelet Fourier Diffuser (WFDiffuser)，一种基于扩散的新型强化学习框架，它集成了离散小波变换，将轨迹分解为低频和高频分量。为了进一步增强每个分量的扩散建模，WFDiffuser采用短时傅里叶变换和交叉注意力机制来提取频域特征并促进跨频率交互。在D4RL基准上的大量实验结果表明，WFDiffuser有效地缓解了频率偏移，从而产生更平滑、更稳定的轨迹，并提高了决策性能。

## 🔬 方法详解

**问题定义**：现有基于扩散模型的离线强化学习方法在建模轨迹序列时，主要关注时域特征，忽略了轨迹在频域上的特性。这导致模型在生成轨迹时，容易出现低频分量的偏移，使得生成的轨迹不稳定，最终影响强化学习的性能。因此，论文旨在解决离线强化学习中由于忽略频域信息而导致的轨迹频率偏移问题。

**核心思路**：论文的核心思路是将轨迹分解到频域进行分析和建模，通过关注轨迹的频率特性来提升强化学习的性能。具体来说，利用离散小波变换将轨迹分解为低频和高频分量，分别进行建模，并利用短时傅里叶变换提取频域特征，从而更准确地捕捉轨迹的动态特性。

**技术框架**：WFDiffuser框架主要包含以下几个阶段：1) 轨迹分解：使用离散小波变换将轨迹分解为低频和高频分量。2) 频域特征提取：对分解后的低频和高频分量，使用短时傅里叶变换提取频域特征。3) 扩散模型建模：使用扩散模型分别对低频和高频分量进行建模，并利用交叉注意力机制促进跨频率交互。4) 轨迹生成：通过逆扩散过程生成新的轨迹。

**关键创新**：WFDiffuser的关键创新在于将频域分析引入到基于扩散模型的离线强化学习中。通过离散小波变换和短时傅里叶变换，模型能够更好地捕捉轨迹的频率特性，从而缓解频率偏移问题，生成更稳定和高质量的轨迹。与现有方法相比，WFDiffuser不仅关注时域信息，还充分利用了频域信息，从而提升了强化学习的性能。

**关键设计**：在轨迹分解阶段，选择了合适的离散小波变换基函数。在频域特征提取阶段，短时傅里叶变换的窗口大小和步长需要仔细调整，以平衡时间和频率分辨率。在扩散模型建模阶段，交叉注意力机制的设计需要考虑如何有效地融合低频和高频分量的信息。损失函数的设计也需要考虑如何惩罚频率偏移，保证生成轨迹的频率特性。

## 📊 实验亮点

在D4RL基准测试中，WFDiffuser在多个任务上都取得了显著的性能提升。例如，在hopper-medium-replay任务上，WFDiffuser的性能超过了现有最佳基线方法，证明了其有效性。实验结果表明，WFDiffuser能够有效缓解频率偏移，生成更平滑、更稳定的轨迹，从而提高决策性能。

## 🎯 应用场景

WFDiffuser可应用于各种需要稳定轨迹生成的强化学习任务，例如机器人控制、自动驾驶、游戏AI等。通过缓解轨迹频率偏移，可以提高智能体在复杂环境中的稳定性和可靠性，从而实现更安全、更高效的决策。

## 📄 摘要（原文）

> Diffusion probability models have shown significant promise in offline reinforcement learning by directly modeling trajectory sequences. However, existing approaches primarily focus on time-domain features while overlooking frequency-domain features, leading to frequency shift and degraded performance according to our observation. In this paper, we investigate the RL problem from a new perspective of the frequency domain. We first observe that time-domain-only approaches inadvertently introduce shifts in the low-frequency components of the frequency domain, which results in trajectory instability and degraded performance. To address this issue, we propose Wavelet Fourier Diffuser (WFDiffuser), a novel diffusion-based RL framework that integrates Discrete Wavelet Transform to decompose trajectories into low- and high-frequency components. To further enhance diffusion modeling for each component, WFDiffuser employs Short-Time Fourier Transform and cross attention mechanisms to extract frequency-domain features and facilitate cross-frequency interaction. Extensive experiment results on the D4RL benchmark demonstrate that WFDiffuser effectively mitigates frequency shift, leading to smoother, more stable trajectories and improved decision-making performance over existing methods.

