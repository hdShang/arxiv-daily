---
layout: default
title: "Normalized Attention Guidance: Universal Negative Guidance for Diffusion Models"
---

# Normalized Attention Guidance: Universal Negative Guidance for Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21179" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21179v3</a>
  <a href="https://arxiv.org/pdf/2505.21179.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21179v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21179v3', 'Normalized Attention Guidance: Universal Negative Guidance for Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dar-Yen Chen, Hmrishav Bandyopadhyay, Kai Zou, Yi-Zhe Song

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-06-03)

---

## 💡 一句话要点

**提出归一化注意力引导以解决扩散模型中的负引导问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `负引导` `扩散模型` `注意力机制` `无训练方法` `图像生成` `视频合成` `模型泛化`

## 📋 核心要点

1. 现有的无分类器引导方法在激进的采样步骤压缩下表现不佳，导致负引导效果不理想。
2. 提出的归一化注意力引导（NAG）通过在注意力空间中进行L1归一化和外推，提供了一种高效的负引导机制。
3. 实验结果显示，NAG在文本对齐、保真度和人类感知质量上均有显著提升，用户研究也表明对NAG引导输出的偏好。

## 📝 摘要（中文）

负引导，即明确抑制不需要的属性，仍然是扩散模型中的一个基本挑战，尤其是在少步采样的情况下。尽管无分类器引导（CFG）在标准设置中表现良好，但在激进的采样步骤压缩下，由于正负分支之间的预测偏差，它的效果却不理想。本文提出了归一化注意力引导（NAG），这是一种高效的、无训练的机制，通过在注意力空间中应用基于L1的归一化和精炼来实现外推。NAG在CFG失效的情况下恢复了有效的负引导，同时保持了保真度。与现有方法不同，NAG能够跨架构（如UNet、DiT）、采样模式（少步、多步）和模态（图像、视频）进行泛化，作为一种通用的插件，计算开销极小。通过广泛的实验，我们展示了在文本对齐（CLIP评分）、保真度（FID、PFID）和人类感知质量（ImageReward）方面的一致提升。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散模型中的负引导问题，尤其是在少步采样情况下，现有的无分类器引导方法（CFG）由于正负分支预测的偏差，导致负引导效果不佳。

**核心思路**：归一化注意力引导（NAG）通过在注意力空间中应用L1归一化和外推，提供了一种无需训练的高效负引导机制，旨在恢复在CFG失效情况下的有效负引导。

**技术框架**：NAG的整体架构包括注意力机制的归一化处理和外推过程，能够适应不同的模型架构（如UNet、DiT）和采样模式（少步、多步），并支持多种模态（图像、视频）。

**关键创新**：NAG的核心创新在于其无训练的特性和跨架构的适用性，使其成为一种通用的负引导插件，显著降低了计算开销。

**关键设计**：NAG采用L1归一化来处理注意力权重，并通过精炼过程增强负引导效果，确保在不同的模型和采样条件下均能保持高效的性能。具体的参数设置和损失函数设计在附录中提供了伪代码。

## 📊 实验亮点

实验结果表明，NAG在文本对齐（CLIP评分）、保真度（FID、PFID）和人类感知质量（ImageReward）上均有显著提升，具体提升幅度在各项指标上均超过了现有基线，用户研究显示对NAG引导输出的偏好显著。

## 🎯 应用场景

该研究的潜在应用领域包括图像生成、视频合成以及其他需要控制生成内容属性的扩散模型。NAG的无训练特性使其能够轻松集成到现有的扩散框架中，提升生成质量，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Negative guidance -- explicitly suppressing unwanted attributes -- remains a fundamental challenge in diffusion models, particularly in few-step sampling regimes. While Classifier-Free Guidance (CFG) works well in standard settings, it fails under aggressive sampling step compression due to divergent predictions between positive and negative branches. We present Normalized Attention Guidance (NAG), an efficient, training-free mechanism that applies extrapolation in attention space with L1-based normalization and refinement. NAG restores effective negative guidance where CFG collapses while maintaining fidelity. Unlike existing approaches, NAG generalizes across architectures (UNet, DiT), sampling regimes (few-step, multi-step), and modalities (image, video), functioning as a \textit{universal} plug-in with minimal computational overhead. Through extensive experimentation, we demonstrate consistent improvements in text alignment (CLIP Score), fidelity (FID, PFID), and human-perceived quality (ImageReward). Our ablation studies validate each design component, while user studies confirm significant preference for NAG-guided outputs. As a model-agnostic inference-time approach requiring no retraining, NAG provides effortless negative guidance for all modern diffusion frameworks -- pseudocode in the Appendix!

