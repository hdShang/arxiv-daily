---
layout: default
title: MagicTryOn: Harnessing Diffusion Transformer for Garment-Preserving Video Virtual Try-on
---

# MagicTryOn: Harnessing Diffusion Transformer for Garment-Preserving Video Virtual Try-on

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21325" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21325v3</a>
  <a href="https://arxiv.org/pdf/2505.21325.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21325v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21325v3', 'MagicTryOn: Harnessing Diffusion Transformer for Garment-Preserving Video Virtual Try-on')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangyuan Li, Siming Zheng, Hao Zhang, Jinwei Chen, Junsheng Luan, Binkai Ou, Lei Zhao, Bo Li, Peng-Tao Jiang

**分类**: cs.CV

**发布日期**: 2025-05-27 (更新: 2025-09-27)

---

## 💡 一句话要点

**提出MagicTryOn以解决视频虚拟试穿中的服装保留问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `视频虚拟试穿` `扩散变换器` `细粒度保留` `时空一致性` `掩码感知损失` `实时推理` `服装合成`

## 📋 核心要点

1. 现有视频虚拟试穿方法在服装细节保真度和时空一致性方面存在不足，导致合成效果不理想。
2. 本文提出MagicTryOn，通过细粒度服装保留策略和时空旋转位置嵌入，增强服装细节和时序一致性。
3. 实验结果表明，MagicTryOn在服装细节保真度和时序稳定性方面显著优于现有方法，表现出色。

## 📝 摘要（中文）

视频虚拟试穿（VVT）旨在合成在连续视频帧中自然出现的服装，捕捉其动态和与人类动作的交互。尽管已有进展，现有VVT方法仍面临服装保真度不足和时空一致性有限的问题。为此，本文提出MagicTryOn，一个基于扩散变换器的框架，采用细粒度服装保留策略和服装感知时空旋转位置嵌入（RoPE），以提高服装细节和时序一致性。通过分布匹配蒸馏，压缩采样轨迹至四步，实现实时推理。大量实验表明，MagicTryOn在无约束环境下优于现有方法，提供更高的服装细节保真度和时序稳定性。

## 🔬 方法详解

**问题定义**：本文旨在解决视频虚拟试穿中服装细节保真度不足和时空一致性差的问题。现有方法未能充分利用服装信息，导致细节表现不佳，同时缺乏有效的时空建模，造成跨帧身份一致性不足和外观漂移。

**核心思路**：MagicTryOn的核心思路是通过细粒度服装保留策略和服装感知时空旋转位置嵌入（RoPE）来提升服装细节和时序一致性。通过将服装线索解耦并注入去噪过程，增强细节表现，同时利用RoPE调节服装标记的时空相对位置。

**技术框架**：MagicTryOn的整体架构包括细粒度服装保留模块、时空旋转位置嵌入模块和掩码感知损失模块。首先，通过细粒度策略提取服装信息，然后利用RoPE增强时序一致性，最后通过掩码感知损失提升服装区域的保真度。

**关键创新**：本文的关键创新在于提出了细粒度服装保留策略和服装感知时空旋转位置嵌入（RoPE），这两者有效解决了现有方法在细节保真度和时序一致性方面的不足。

**关键设计**：在训练过程中，采用掩码感知损失函数以增强服装区域的保真度，同时通过分布匹配蒸馏将采样轨迹压缩至四步，实现实时推理而不降低服装保真度。整体网络结构设计上，充分考虑了服装信息的解耦与注入。

## 📊 实验亮点

实验结果显示，MagicTryOn在服装细节保真度和时序稳定性方面显著优于现有方法，具体表现为在多个基准测试中，细节保真度提升幅度达到XX%，时序一致性提升幅度达到YY%。这些结果表明，MagicTryOn在无约束环境下的表现极为出色。

## 🎯 应用场景

MagicTryOn的研究成果在时尚电商、虚拟试衣间和增强现实等领域具有广泛的应用潜力。通过提供高保真度的虚拟试穿体验，可以帮助消费者在购买前更好地评估服装效果，从而提升用户满意度和购买转化率。此外，该技术还可用于影视制作和游戏开发，增强角色服装的真实感。

## 📄 摘要（原文）

> Video Virtual Try-On (VVT) aims to synthesize garments that appear natural across consecutive video frames, capturing both their dynamics and interactions with human motion. Despite recent progress, existing VVT methods still suffer from inadequate garment fidelity and limited spatiotemporal consistency. The reasons are: (1) under-exploitation of garment information, with limited garment cues being injected, resulting in weaker fine-detail fidelity; and (2) a lack of spatiotemporal modeling, which hampers cross-frame identity consistency and causes temporal jitter and appearance drift. In this paper, we present MagicTryOn, a diffusion-transformer based framework for garment-preserving video virtual try-on. To preserve fine-grained garment details, we propose a fine-grained garment-preservation strategy that disentangles garment cues and injects these decomposed priors into the denoising process. To improve temporal garment consistency and suppress jitter, we introduce a garment-aware spatiotemporal rotary positional embedding (RoPE) that extends RoPE within full self-attention, using spatiotemporal relative positions to modulate garment tokens. We further impose a mask-aware loss during training to enhance fidelity within garment regions. Moreover, we adopt distribution-matching distillation to compress the sampling trajectory to four steps, enabling real-time inference without degrading garment fidelity. Extensive quantitative and qualitative experiments demonstrate that MagicTryOn outperforms existing methods, delivering superior garment-detail fidelity and temporal stability in unconstrained settings.

