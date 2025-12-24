---
layout: default
title: Hallo4: High-Fidelity Dynamic Portrait Animation via Direct Preference Optimization
---

# Hallo4: High-Fidelity Dynamic Portrait Animation via Direct Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23525" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23525v4</a>
  <a href="https://arxiv.org/pdf/2505.23525.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23525v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23525v4', 'Hallo4: High-Fidelity Dynamic Portrait Animation via Direct Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Cui, Yan Chen, Mingwang Xu, Hanlin Shang, Yuxuan Chen, Yun Zhan, Zilong Dong, Yao Yao, Jingdong Wang, Siyu Zhu

**分类**: cs.CV

**发布日期**: 2025-05-29 (更新: 2025-11-30)

**🔗 代码/项目**: [GITHUB](https://github.com/fudan-generative-vision/hallo4)

---

## 💡 一句话要点

**提出人类偏好对齐的扩散框架以解决动态肖像动画问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `动态肖像动画` `人类偏好对齐` `扩散框架` `唇音同步` `面部表情` `高保真动态`

## 📋 核心要点

1. 现有方法在生成动态肖像动画时，难以实现精确的唇部同步和自然的面部表情，导致动画效果不理想。
2. 论文提出了一种人类偏好对齐的扩散框架，通过直接偏好优化和时间运动调制来提升动画的自然性和一致性。
3. 实验结果显示，所提方法在唇音同步、表情生动性和身体运动一致性上均显著优于基线方法，提升幅度明显。

## 📝 摘要（中文）

生成高动态和逼真的肖像动画，尤其是通过音频和骨骼运动驱动的动画，仍然面临着精确的唇部同步、自然的面部表情和高保真的身体运动动态等挑战。为此，本文提出了一种人类偏好对齐的扩散框架，主要通过两个创新点来解决这些问题。首先，引入了针对人类中心动画的直接偏好优化，利用经过精心策划的人类偏好数据集，使生成的输出与肖像运动视频对齐的感知指标相一致。其次，提出的时间运动调制通过时间通道重分配和比例特征扩展，将运动条件重塑为维度对齐的潜在特征，从而解决时空分辨率不匹配的问题，保持扩散合成中的高频运动细节的保真度。实验结果表明，与基线方法相比，唇音同步、表情生动性和身体运动一致性都有明显改善，同时在人类偏好指标上也取得了显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决生成动态肖像动画时，唇部同步、面部表情自然性和身体运动动态保真度等问题。现有方法在这些方面存在明显不足，导致生成效果不够真实。

**核心思路**：论文的核心思路是通过人类偏好对齐的扩散框架，结合直接偏好优化和时间运动调制，来提升生成动画的质量和自然性。这样的设计能够更好地反映人类的感知偏好，增强生成结果的真实感。

**技术框架**：整体架构包括两个主要模块：直接偏好优化模块和时间运动调制模块。前者通过人类偏好数据集优化生成结果，后者则通过重塑运动条件来解决时空分辨率不匹配的问题。

**关键创新**：最重要的技术创新在于直接偏好优化和时间运动调制的结合，前者使生成结果更符合人类的感知标准，后者则确保高频运动细节的保真度。这与现有的UNet和DiT基础的肖像扩散方法形成了明显的区别。

**关键设计**：在参数设置上，采用了经过精心策划的人类偏好数据集，并设计了特定的损失函数来优化生成效果。此外，网络结构上进行了时间通道重分配和比例特征扩展，以确保运动条件的维度对齐。

## 📊 实验亮点

实验结果表明，所提方法在唇音同步、表情生动性和身体运动一致性上均显著优于基线方法，具体提升幅度达到了XX%（具体数据未知），在人类偏好指标上也取得了显著的改善，显示出该方法的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括影视动画制作、游戏角色动画以及虚拟现实中的人机交互等。通过生成高质量的动态肖像动画，能够提升用户体验和视觉效果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Generating highly dynamic and photorealistic portrait animations driven by audio and skeletal motion remains challenging due to the need for precise lip synchronization, natural facial expressions, and high-fidelity body motion dynamics. We propose a human-preference-aligned diffusion framework that addresses these challenges through two key innovations. First, we introduce direct preference optimization tailored for human-centric animation, leveraging a curated dataset of human preferences to align generated outputs with perceptual metrics for portrait motion-video alignment and naturalness of expression. Second, the proposed temporal motion modulation resolves spatiotemporal resolution mismatches by reshaping motion conditions into dimensionally aligned latent features through temporal channel redistribution and proportional feature expansion, preserving the fidelity of high-frequency motion details in diffusion-based synthesis. The proposed mechanism is complementary to existing UNet and DiT-based portrait diffusion approaches, and experiments demonstrate obvious improvements in lip-audio synchronization, expression vividness, body motion coherence over baseline methods, alongside notable gains in human preference metrics. Our model and source code can be found at: https://github.com/fudan-generative-vision/hallo4.

