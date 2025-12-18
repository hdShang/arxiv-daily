---
layout: default
title: OmniMotion: Multimodal Motion Generation with Continuous Masked Autoregression
---

# OmniMotion: Multimodal Motion Generation with Continuous Masked Autoregression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14954" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14954v1</a>
  <a href="https://arxiv.org/pdf/2510.14954.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14954v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.14954v1', 'OmniMotion: Multimodal Motion Generation with Continuous Masked Autoregression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhe Li, Weihao Yuan, Weichao Shen, Siyu Zhu, Zilong Dong, Chang Xu

**分类**: cs.CV

**发布日期**: 2025-10-16

---

## 💡 一句话要点

**OmniMotion：提出连续掩码自回归Transformer，用于多模态全身人体运动生成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态运动生成` `连续掩码自回归` `运动Transformer` `因果注意力` `门控线性注意力` `DiT结构` `文本到运动` `语音到手势`

## 📋 核心要点

1. 现有方法在多模态人体运动生成中，缺乏有效的运动生成机制和模态融合方法，难以处理复杂和异构的数据。
2. 提出连续掩码自回归运动Transformer，利用因果注意力机制和门控线性注意力，关注关键动作并抑制不稳定性。
3. 实验结果表明，该框架在文本到运动、语音到手势和音乐到舞蹈等任务上，均优于现有方法，提升了生成质量。

## 📝 摘要（中文）

全身多模态人体运动生成面临两大挑战：一是构建有效的运动生成机制，二是将文本、语音和音乐等多种模态整合到一个统一的框架中。与以往通常采用离散掩码建模或自回归建模的方法不同，本文提出了一种连续掩码自回归运动Transformer，它在考虑人体运动的序列性质时执行因果注意力机制。在该Transformer中，引入了门控线性注意力和RMSNorm模块，以驱动Transformer关注关键动作，并抑制由异常运动或多模态中的异构分布引起的不稳定性。为了进一步增强运动生成和多模态泛化能力，本文采用DiT结构将Transformer中的条件扩散到目标。为了融合不同的模态，利用AdaLN和交叉注意力来注入文本、语音和音乐信号。实验结果表明，本文提出的框架在所有模态（包括文本到运动、语音到手势和音乐到舞蹈）上均优于以往的方法。该方法的代码将会开源。

## 🔬 方法详解

**问题定义**：论文旨在解决全身多模态人体运动生成问题。现有方法通常采用离散掩码建模或简单的自回归建模，无法充分利用人体运动的序列特性，并且在融合文本、语音和音乐等多种模态时，容易受到异构分布的影响，导致生成结果不稳定和质量不高。

**核心思路**：论文的核心思路是利用连续掩码自回归Transformer，结合因果注意力和门控机制，实现更有效的运动生成和多模态融合。通过连续掩码建模，可以更好地捕捉人体运动的连续性和依赖关系。门控线性注意力可以帮助模型关注关键动作，抑制噪声和不稳定性。

**技术框架**：整体框架包括以下几个主要模块：1) 连续掩码自回归运动Transformer：用于生成人体运动序列，采用因果注意力机制和门控线性注意力。2) DiT结构：将Transformer中的条件扩散到目标，增强运动生成和多模态泛化能力。3) 多模态融合模块：利用AdaLN和交叉注意力来注入文本、语音和音乐信号。

**关键创新**：论文的关键创新在于提出了连续掩码自回归运动Transformer，并结合了门控线性注意力和DiT结构。与传统的离散掩码建模和自回归建模相比，该方法能够更好地捕捉人体运动的连续性和依赖关系，并有效地融合多种模态的信息。

**关键设计**：在Transformer中，使用了门控线性注意力来关注关键动作，并使用RMSNorm模块来抑制不稳定性。为了融合不同的模态，使用了AdaLN和交叉注意力。此外，还采用了DiT结构来扩散条件，进一步增强了运动生成和多模态泛化能力。具体的参数设置和损失函数等细节将在代码开源后公开。

## 📊 实验亮点

实验结果表明，OmniMotion在文本到运动、语音到手势和音乐到舞蹈等任务上，均优于以往的方法。具体性能数据将在论文中详细展示，代码开源后可复现。该方法在多模态人体运动生成方面取得了显著的提升，为相关领域的研究提供了新的思路。

## 🎯 应用场景

该研究成果可应用于虚拟现实、游戏开发、动画制作、人机交互等领域。例如，可以根据用户的文本描述、语音指令或音乐节奏，自动生成逼真的人体运动动画，从而提升用户体验和创作效率。未来，该技术有望应用于更广泛的场景，如智能康复、运动训练等。

## 📄 摘要（原文）

> Whole-body multi-modal human motion generation poses two primary challenges: creating an effective motion generation mechanism and integrating various modalities, such as text, speech, and music, into a cohesive framework. Unlike previous methods that usually employ discrete masked modeling or autoregressive modeling, we develop a continuous masked autoregressive motion transformer, where a causal attention is performed considering the sequential nature within the human motion. Within this transformer, we introduce a gated linear attention and an RMSNorm module, which drive the transformer to pay attention to the key actions and suppress the instability caused by either the abnormal movements or the heterogeneous distributions within multi-modalities. To further enhance both the motion generation and the multimodal generalization, we employ the DiT structure to diffuse the conditions from the transformer towards the targets. To fuse different modalities, AdaLN and cross-attention are leveraged to inject the text, speech, and music signals. Experimental results demonstrate that our framework outperforms previous methods across all modalities, including text-to-motion, speech-to-gesture, and music-to-dance. The code of our method will be made public.

