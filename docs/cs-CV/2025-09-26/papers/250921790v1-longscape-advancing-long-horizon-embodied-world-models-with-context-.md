---
layout: default
title: "LongScape: Advancing Long-Horizon Embodied World Models with Context-Aware MoE"
---

# LongScape: Advancing Long-Horizon Embodied World Models with Context-Aware MoE

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21790" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21790v1</a>
  <a href="https://arxiv.org/pdf/2509.21790.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21790v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21790v1', 'LongScape: Advancing Long-Horizon Embodied World Models with Context-Aware MoE')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Shang, Lei Jin, Yiding Ma, Xin Zhang, Chen Gao, Wei Wu, Yong Li

**分类**: cs.CV

**发布日期**: 2025-09-26

**备注**: 13 pages, 8 figures

**🔗 代码/项目**: [GITHUB](https://github.com/tsinghua-fib-lab/Longscape)

---

## 💡 一句话要点

**LongScape：提出上下文感知MoE的长时程具身世界模型，解决视频生成中的时序不一致问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长时程生成` `具身世界模型` `视频生成` `扩散模型` `自回归模型` `混合专家模型` `动作引导` `机器人操作`

## 📋 核心要点

1. 现有基于扩散的视频生成方法在长时程生成中存在时间不一致和视觉漂移问题，自回归方法则牺牲了视觉细节。
2. LongScape通过动作引导的分块机制和上下文感知的混合专家模型，自适应地结合扩散模型和自回归模型，实现稳定长时程生成。
3. 实验表明，LongScape在长时间rollout中实现了稳定和一致的生成效果，克服了现有方法的局限性。

## 📝 摘要（中文）

本文提出LongScape，一个混合框架，用于生成高质量的具身操作数据。该框架自适应地结合了块内扩散去噪和块间自回归因果生成。核心创新是动作引导的可变长度分块机制，它基于机器人动作的语义上下文来分割视频，确保每个块代表一个完整的、连贯的动作，从而使模型能够灵活地生成多样化的动态。此外，引入了上下文感知混合专家(CMoE)框架，在生成过程中自适应地激活每个块的专门专家，保证了高质量的视觉效果和无缝的块过渡。实验结果表明，该方法在长时间的rollout中实现了稳定和一致的长时程生成。

## 🔬 方法详解

**问题定义**：现有基于视频的世界模型在长时程生成任务中面临挑战。基于扩散的模型容易出现时间不一致性和视觉漂移，而自回归模型则往往牺牲视觉细节以保证连贯性。因此，如何实现既具有高视觉质量又保持时间一致性的长时程视频生成是一个关键问题。

**核心思路**：LongScape的核心思路是将视频分割成具有语义意义的动作块，并结合扩散模型和自回归模型的优势。通过动作引导的分块机制，确保每个块内部的连贯性，并利用自回归模型在块间建立因果关系，从而实现长时程的稳定生成。上下文感知的混合专家模型则用于提升每个块的视觉质量和保证块之间的平滑过渡。

**技术框架**：LongScape的整体框架包含以下几个主要模块：1) **动作引导的分块机制**：根据机器人动作的语义上下文将视频分割成可变长度的块。2) **块内扩散去噪**：使用扩散模型对每个块进行去噪，提升视觉质量。3) **块间自回归生成**：使用自回归模型在块之间建立因果关系，保证时间一致性。4) **上下文感知混合专家(CMoE)**：根据上下文信息，自适应地选择不同的专家模型来处理每个块，提升视觉质量和保证块之间的平滑过渡。

**关键创新**：LongScape的关键创新在于以下两点：1) **动作引导的可变长度分块机制**：与固定长度分块相比，能够更好地捕捉视频中的语义信息，确保每个块代表一个完整的动作。2) **上下文感知混合专家(CMoE)**：能够根据上下文信息自适应地选择不同的专家模型，从而提升视觉质量和保证块之间的平滑过渡。

**关键设计**：动作引导分块机制依赖于对机器人动作的准确识别，具体实现细节未知。CMoE框架中，专家模型的数量和结构需要根据具体任务进行调整。损失函数的设计需要平衡视觉质量和时间一致性，具体形式未知。

## 📊 实验亮点

论文通过实验验证了LongScape在长时程视频生成任务中的有效性。实验结果表明，LongScape能够生成比现有方法更稳定、更一致的视频序列。具体的性能数据和对比基线未知，但论文强调了LongScape在长时间rollout中的优势。

## 🎯 应用场景

LongScape在机器人操作、自动驾驶、游戏AI等领域具有广泛的应用前景。它可以用于生成高质量的训练数据，提升机器人操作的性能和泛化能力。在自动驾驶领域，可以用于生成各种复杂的驾驶场景，提升自动驾驶系统的鲁棒性。在游戏AI领域，可以用于生成更加逼真的游戏环境和角色行为。

## 📄 摘要（原文）

> Video-based world models hold significant potential for generating high-quality embodied manipulation data. However, current video generation methods struggle to achieve stable long-horizon generation: classical diffusion-based approaches often suffer from temporal inconsistency and visual drift over multiple rollouts, while autoregressive methods tend to compromise on visual detail. To solve this, we introduce LongScape, a hybrid framework that adaptively combines intra-chunk diffusion denoising with inter-chunk autoregressive causal generation. Our core innovation is an action-guided, variable-length chunking mechanism that partitions video based on the semantic context of robotic actions. This ensures each chunk represents a complete, coherent action, enabling the model to flexibly generate diverse dynamics. We further introduce a Context-aware Mixture-of-Experts (CMoE) framework that adaptively activates specialized experts for each chunk during generation, guaranteeing high visual quality and seamless chunk transitions. Extensive experimental results demonstrate that our method achieves stable and consistent long-horizon generation over extended rollouts. Our code is available at: https://github.com/tsinghua-fib-lab/Longscape.

