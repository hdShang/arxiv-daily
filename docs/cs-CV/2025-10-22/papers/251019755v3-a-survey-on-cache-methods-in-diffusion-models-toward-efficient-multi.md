---
layout: default
title: A Survey on Cache Methods in Diffusion Models: Toward Efficient Multi-Modal Generation
---

# A Survey on Cache Methods in Diffusion Models: Toward Efficient Multi-Modal Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19755" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19755v3</a>
  <a href="https://arxiv.org/pdf/2510.19755.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19755v3" onclick="toggleFavorite(this, '2510.19755v3', 'A Survey on Cache Methods in Diffusion Models: Toward Efficient Multi-Modal Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiacheng Liu, Xinyu Wang, Yuqi Lin, Zhikai Wang, Peiru Wang, Peiliang Cai, Qinming Zhou, Zhengan Yan, Zexuan Yan, Zhengyi Shi, Chang Zou, Yue Ma, Linfeng Zhang

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-10-22 (更新: 2025-11-01)

**备注**: 22 pages,2 figures

---

## 💡 一句话要点

**综述扩散模型缓存方法，加速高效多模态生成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `缓存技术` `模型加速` `多模态生成` `高效推理`

## 📋 核心要点

1. 扩散模型计算开销大、推理延迟高，限制了其在实时应用中的发展。
2. 扩散缓存通过重用扩散过程中的计算冗余，实现免训练、架构无关的高效推理。
3. 扩散缓存从静态复用发展到动态预测，提升了灵活性，并可与其他加速技术集成。

## 📝 摘要（中文）

扩散模型以其卓越的生成质量和可控性，已成为现代生成式人工智能的基石。然而，其固有的多步迭代和复杂的骨干网络导致了过高的计算开销和生成延迟，成为实时应用的主要瓶颈。尽管现有的加速技术取得了一些进展，但它们仍然面临着适用性有限、训练成本高或质量下降等挑战。在此背景下，扩散缓存提供了一种有前景的免训练、架构无关和高效的推理范式。其核心机制是识别和重用扩散过程中的内在计算冗余。通过实现特征级跨步复用和层间调度，它可以在不修改模型参数的情况下减少计算。本文系统地回顾了扩散缓存的理论基础和演变，并提出了一个统一的框架对其进行分类和分析。通过对代表性方法的比较分析，我们表明扩散缓存从静态重用到动态预测演变。这种趋势增强了缓存跨不同任务的灵活性，并能够与其他加速技术（如采样优化和模型蒸馏）集成，从而为未来的多模态和交互式应用构建一个统一、高效的推理框架。我们认为这种范式将成为实时和高效生成式人工智能的关键推动力，为高效生成智能的理论和实践注入新的活力。

## 🔬 方法详解

**问题定义**：扩散模型在生成高质量图像的同时，也面临着计算量大、推理速度慢的问题。现有的加速方法通常需要额外的训练，或者会牺牲生成质量，难以满足实时应用的需求。因此，如何降低扩散模型的计算复杂度，同时保持其生成质量，是一个重要的研究问题。

**核心思路**：论文的核心思路是利用扩散过程中存在的计算冗余，通过缓存中间特征并进行复用，从而减少重复计算。这种方法不需要重新训练模型，并且可以灵活地应用于不同的扩散模型架构。通过智能地管理和调度缓存，可以有效地降低计算成本，提高推理速度。

**技术框架**：扩散缓存的整体框架主要包括以下几个阶段：1) 特征提取：从扩散模型的中间层提取特征；2) 缓存管理：将提取的特征存储在缓存中，并根据一定的策略进行更新和替换；3) 特征复用：在后续的扩散步骤中，从缓存中检索相关的特征，并将其用于计算；4) 融合：将复用的特征与当前步骤的特征进行融合，得到最终的输出。

**关键创新**：最重要的技术创新点在于提出了一个统一的框架来分析和分类不同的扩散缓存方法，并指出了扩散缓存从静态复用到动态预测的演变趋势。静态复用方法简单直接，但灵活性较差；动态预测方法则可以根据当前的状态预测需要复用的特征，从而提高缓存的利用率和生成质量。

**关键设计**：关键设计包括缓存的容量、更新策略、检索方法和融合方式等。缓存容量决定了可以存储的特征数量，更新策略决定了何时以及如何替换缓存中的特征，检索方法决定了如何找到与当前状态相关的特征，融合方式决定了如何将复用的特征与当前步骤的特征进行结合。这些设计都需要根据具体的应用场景进行调整和优化。

## 📊 实验亮点

论文通过对代表性方法的比较分析，展示了扩散缓存从静态重用到动态预测的演变趋势。这种演变增强了缓存跨不同任务的灵活性，并能够与其他加速技术（如采样优化和模型蒸馏）集成。实验结果表明，扩散缓存可以在不牺牲生成质量的前提下，显著降低计算成本，提高推理速度。

## 🎯 应用场景

扩散缓存技术可以广泛应用于各种需要实时生成图像或视频的场景，例如：在线游戏、虚拟现实、视频会议、图像编辑等。通过降低计算成本和提高推理速度，可以使得这些应用更加流畅和高效。此外，扩散缓存还可以与其他加速技术相结合，进一步提高生成效率，为未来的多模态和交互式应用提供更强大的支持。

## 📄 摘要（原文）

> Diffusion Models have become a cornerstone of modern generative AI for their exceptional generation quality and controllability. However, their inherent \textit{multi-step iterations} and \textit{complex backbone networks} lead to prohibitive computational overhead and generation latency, forming a major bottleneck for real-time applications. Although existing acceleration techniques have made progress, they still face challenges such as limited applicability, high training costs, or quality degradation.
>   Against this backdrop, \textbf{Diffusion Caching} offers a promising training-free, architecture-agnostic, and efficient inference paradigm. Its core mechanism identifies and reuses intrinsic computational redundancies in the diffusion process. By enabling feature-level cross-step reuse and inter-layer scheduling, it reduces computation without modifying model parameters. This paper systematically reviews the theoretical foundations and evolution of Diffusion Caching and proposes a unified framework for its classification and analysis.
>   Through comparative analysis of representative methods, we show that Diffusion Caching evolves from \textit{static reuse} to \textit{dynamic prediction}. This trend enhances caching flexibility across diverse tasks and enables integration with other acceleration techniques such as sampling optimization and model distillation, paving the way for a unified, efficient inference framework for future multimodal and interactive applications. We argue that this paradigm will become a key enabler of real-time and efficient generative AI, injecting new vitality into both theory and practice of \textit{Efficient Generative Intelligence}.

