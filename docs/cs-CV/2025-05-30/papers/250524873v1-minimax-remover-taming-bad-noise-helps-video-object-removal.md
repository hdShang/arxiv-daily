---
layout: default
title: MiniMax-Remover: Taming Bad Noise Helps Video Object Removal
---

# MiniMax-Remover: Taming Bad Noise Helps Video Object Removal

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24873" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24873v1</a>
  <a href="https://arxiv.org/pdf/2505.24873.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24873v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24873v1', 'MiniMax-Remover: Taming Bad Noise Helps Video Object Removal')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bojia Zi, Weixuan Peng, Xianbiao Qi, Jianan Wang, Shihao Zhao, Rong Xiao, Kam-Fai Wong

**分类**: cs.CV

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出MiniMax-Remover以解决视频对象移除中的噪声问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `视频对象移除` `噪声处理` `最小最大优化` `视频编辑` `高效推理`

## 📋 核心要点

1. 现有视频对象移除方法面临虚幻对象和视觉伪影等挑战，且推理速度慢。
2. MiniMax-Remover通过去除文本输入和交叉注意力层，简化模型架构，提高效率。
3. 实验显示该方法在6次采样步骤下实现了最先进的移除效果，显著提升了推理效率。

## 📝 摘要（中文）

近年来，视频扩散模型的进步推动了视频编辑技术的快速发展。然而，视频对象移除作为视频编辑的一个关键子任务，仍然面临诸如虚幻对象和视觉伪影等挑战。此外，现有方法通常依赖于计算开销大的采样过程和无分类器引导（CFG），导致推理速度缓慢。为了解决这些问题，本文提出了一种新颖的两阶段视频对象移除方法MiniMax-Remover。我们通过去除文本输入和交叉注意力层，简化了预训练的视频生成模型，从而在第一阶段实现了更轻量高效的模型架构。在第二阶段，我们在第一阶段模型生成的成功视频上进行蒸馏，并通过最小最大优化策略进一步提高编辑质量和推理速度。实验结果表明，MiniMax-Remover在仅需6次采样步骤的情况下，达到了最先进的视频对象移除效果，显著提高了推理效率。

## 🔬 方法详解

**问题定义**：本文旨在解决视频对象移除中的噪声问题，现有方法存在虚幻对象和视觉伪影，且推理速度较慢，影响实际应用。

**核心思路**：MiniMax-Remover通过去除文本输入和交叉注意力层，简化了视频生成模型，采用两阶段策略以提高移除质量和推理速度。第一阶段生成基础视频，第二阶段通过最小最大优化进一步提升效果。

**技术框架**：整体架构分为两个阶段。第一阶段为简化模型架构，去除不必要的输入和层，第二阶段则在第一阶段成功生成的视频上进行蒸馏，利用最小最大优化策略进行训练。

**关键创新**：最重要的创新在于通过最小最大优化策略识别并处理“坏噪声”，使得模型在困难条件下仍能生成高质量的移除结果。这一方法与现有依赖CFG的技术有本质区别。

**关键设计**：在模型设计中，去除了文本输入和交叉注意力层，降低了计算复杂度。损失函数设计上，内层最大化识别对移除失败有影响的噪声，外层最小化则训练模型生成高质量结果。

## 📊 实验亮点

实验结果表明，MiniMax-Remover在仅需6次采样步骤的情况下，达到了最先进的视频对象移除效果，显著提高了推理效率。与现有方法相比，推理速度提升显著，且不依赖于计算开销大的CFG，展示了其在实际应用中的优势。

## 🎯 应用场景

MiniMax-Remover的研究成果在视频编辑、电影制作、虚拟现实等领域具有广泛的应用潜力。其高效的视频对象移除能力可以帮助创作者更快速地处理视频内容，提升制作效率，并为用户提供更流畅的观看体验。未来，该技术可能在实时视频处理和增强现实应用中发挥重要作用。

## 📄 摘要（原文）

> Recent advances in video diffusion models have driven rapid progress in video editing techniques. However, video object removal, a critical subtask of video editing, remains challenging due to issues such as hallucinated objects and visual artifacts. Furthermore, existing methods often rely on computationally expensive sampling procedures and classifier-free guidance (CFG), resulting in slow inference. To address these limitations, we propose MiniMax-Remover, a novel two-stage video object removal approach. Motivated by the observation that text condition is not best suited for this task, we simplify the pretrained video generation model by removing textual input and cross-attention layers, resulting in a more lightweight and efficient model architecture in the first stage. In the second stage, we distilled our remover on successful videos produced by the stage-1 model and curated by human annotators, using a minimax optimization strategy to further improve editing quality and inference speed. Specifically, the inner maximization identifies adversarial input noise ("bad noise") that makes failure removals, while the outer minimization step trains the model to generate high-quality removal results even under such challenging conditions. As a result, our method achieves a state-of-the-art video object removal results with as few as 6 sampling steps and doesn't rely on CFG, significantly improving inference efficiency. Extensive experiments demonstrate the effectiveness and superiority of MiniMax-Remover compared to existing methods. Codes and Videos are available at: https://minimax-remover.github.io.

