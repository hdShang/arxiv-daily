---
layout: default
title: Massive Activations are the Key to Local Detail Synthesis in Diffusion Transformers
---

# Massive Activations are the Key to Local Detail Synthesis in Diffusion Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11538" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11538v2</a>
  <a href="https://arxiv.org/pdf/2510.11538.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11538v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.11538v2', 'Massive Activations are the Key to Local Detail Synthesis in Diffusion Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaofan Gan, Zicheng Zhao, Yuanpeng Tu, Xi Chen, Ziran Qin, Tieyuan Chen, Mehrtash Harandi, Weiyao Lin

**分类**: cs.CV

**发布日期**: 2025-10-13 (更新: 2025-10-14)

---

## 💡 一句话要点

**提出Detail Guidance，通过调控Diffusion Transformer中的大规模激活提升图像细节生成质量**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `扩散模型` `Diffusion Transformer` `图像生成` `细节合成` `大规模激活`

## 📋 核心要点

1. 扩散模型在图像生成领域表现出色，但Diffusion Transformer中大规模激活的作用尚不明确。
2. 论文提出Detail Guidance策略，通过扰动大规模激活构建细节缺失模型，引导原始网络生成更精细的图像细节。
3. 实验表明，Detail Guidance能有效提升SD3、SD3.5和Flux等模型的细节生成质量，且无需额外训练。

## 📝 摘要（中文）

扩散Transformer（DiT）最近成为视觉生成领域一个强大的骨干网络。近期的研究表明，DiT的内部特征图中存在“大规模激活”（MAs），但其作用机制尚不明确。本文系统地研究了这些激活，以阐明它们在视觉生成中的作用。研究发现，这些大规模激活出现在所有空间token中，并且它们的分布受到输入时间步嵌入的调节。更重要的是，研究进一步表明，这些大规模激活在局部细节合成中起着关键作用，而对输出的整体语义内容影响甚微。基于这些发现，我们提出了一种名为“细节引导”（DG）的、由MAs驱动的、无需训练的自引导策略，以显式地增强DiT的局部细节保真度。具体来说，DG通过扰乱MAs构建了一个降级的“细节缺失”模型，并利用它来引导原始网络朝着更高质量的细节合成方向发展。我们的DG可以与无分类器引导（CFG）无缝集成，从而进一步改进精细细节。大量的实验表明，我们的DG能够持续提高各种预训练DiT（例如，SD3、SD3.5和Flux）的精细细节质量。

## 🔬 方法详解

**问题定义**：扩散模型在图像生成任务中取得了显著进展，但现有方法在生成图像的局部细节方面仍存在不足。Diffusion Transformer (DiT) 作为一种新兴的扩散模型架构，其内部特征图中存在大规模激活 (Massive Activations, MAs)，但这些激活在图像生成过程中的具体作用尚不明确，如何利用这些激活来提升图像细节生成质量是一个待解决的问题。

**核心思路**：论文的核心思路是，通过分析和调控DiT中的大规模激活，来提升生成图像的局部细节。具体来说，论文发现大规模激活在局部细节合成中起着关键作用，因此可以通过扰动这些激活来构建一个“细节缺失”的模型。然后，利用这个细节缺失的模型来引导原始模型，使其更加关注细节信息的生成。这种自引导的方式不需要额外的训练，可以方便地集成到现有的DiT模型中。

**技术框架**：Detail Guidance (DG) 策略主要包含以下几个步骤：1) 分析DiT模型中大规模激活的分布和作用；2) 通过扰动大规模激活构建一个“细节缺失”的模型；3) 利用细节缺失模型和原始模型之间的差异，设计一个引导信号；4) 将引导信号添加到原始模型的预测中，从而引导其生成更精细的细节。DG可以与Classifier-Free Guidance (CFG) 无缝集成，进一步提升细节生成效果。

**关键创新**：论文的关键创新在于发现了Diffusion Transformer中大规模激活在局部细节合成中的重要作用，并基于此提出了Detail Guidance策略。与现有方法相比，DG不需要额外的训练，可以直接应用于各种预训练的DiT模型，具有很强的通用性和实用性。此外，DG通过自引导的方式，避免了引入额外的噪声或伪影，从而保证了生成图像的质量。

**关键设计**：DG的关键设计包括：1) 如何有效地扰动大规模激活，以构建一个“细节缺失”的模型；2) 如何设计引导信号，以有效地引导原始模型生成更精细的细节。论文中采用了一种简单有效的扰动方法，即对大规模激活进行随机masking。引导信号的设计则基于细节缺失模型和原始模型之间的差异，通过加权的方式将差异添加到原始模型的预测中。具体的权重参数可以通过实验进行调整。

## 📊 实验亮点

实验结果表明，Detail Guidance (DG) 能够显著提升各种预训练DiT模型（如SD3、SD3.5和Flux）的细节生成质量。在定性结果上，DG能够生成更加清晰、锐利的图像细节，例如更逼真的纹理和边缘。在定量结果上，DG在多个指标上都取得了显著的提升，例如FID分数和LPIPS分数。此外，DG与Classifier-Free Guidance (CFG) 的集成能够进一步提升细节生成效果。

## 🎯 应用场景

该研究成果可广泛应用于图像生成、图像编辑、超分辨率重建等领域。通过提升生成图像的细节质量，可以改善用户体验，提高图像的真实感和可用性。例如，在游戏开发中，可以利用该技术生成更加精细的游戏场景和角色；在医学影像分析中，可以利用该技术提高医学图像的分辨率，从而辅助医生进行诊断。

## 📄 摘要（原文）

> Diffusion Transformers (DiTs) have recently emerged as a powerful backbone for visual generation. Recent observations reveal \emph{Massive Activations} (MAs) in their internal feature maps, yet their function remains poorly understood. In this work, we systematically investigate these activations to elucidate their role in visual generation. We found that these massive activations occur across all spatial tokens, and their distribution is modulated by the input timestep embeddings. Importantly, our investigations further demonstrate that these massive activations play a key role in local detail synthesis, while having minimal impact on the overall semantic content of output. Building on these insights, we propose \textbf{D}etail \textbf{G}uidance (\textbf{DG}), a MAs-driven, training-free self-guidance strategy to explicitly enhance local detail fidelity for DiTs. Specifically, DG constructs a degraded ``detail-deficient'' model by disrupting MAs and leverages it to guide the original network toward higher-quality detail synthesis. Our DG can seamlessly integrate with Classifier-Free Guidance (CFG), enabling further refinements of fine-grained details. Extensive experiments demonstrate that our DG consistently improves fine-grained detail quality across various pre-trained DiTs (\eg, SD3, SD3.5, and Flux).

