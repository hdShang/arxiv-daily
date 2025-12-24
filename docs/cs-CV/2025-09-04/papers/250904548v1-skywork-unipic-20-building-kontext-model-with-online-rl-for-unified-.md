---
layout: default
title: "Skywork UniPic 2.0: Building Kontext Model with Online RL for Unified Multimodal Model"
---

# Skywork UniPic 2.0: Building Kontext Model with Online RL for Unified Multimodal Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04548" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04548v1</a>
  <a href="https://arxiv.org/pdf/2509.04548.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04548v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04548v1', 'Skywork UniPic 2.0: Building Kontext Model with Online RL for Unified Multimodal Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyang Wei, Baixin Xu, Hongbo Liu, Cyrus Wu, Jie Liu, Yi Peng, Peiyu Wang, Zexiang Liu, Jingwen He, Yidan Xietian, Chuanxin Tang, Zidong Wang, Yichen Wei, Liang Hu, Boyi Jiang, William Li, Ying He, Yang Liu, Xuchen Song, Eric Li, Yahui Zhou

**分类**: cs.CV

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**UniPic 2.0：通过在线强化学习构建Kontext模型，实现统一多模态图像生成与编辑**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `图像生成` `图像编辑` `强化学习` `扩散模型` `预训练` `指令遵循`

## 📋 核心要点

1. 现有开源多模态模型侧重于扩展模型参数，而忽略了训练策略的优化，导致效率和性能受限。
2. UniPic 2.0通过架构修改、大规模预训练和渐进式双任务强化学习（PDTR）策略，提升图像生成和编辑能力。
3. UniPic2-SD3.5M-Kontext在图像生成和编辑方面优于参数量更大的模型，UniPic2-Metaquery在多模态任务中表现出色。

## 📝 摘要（中文）

本文提出了UniPic2-SD3.5M-Kontext，一个基于SD3.5-Medium的20亿参数DiT模型，在图像生成和编辑方面达到了最先进的水平，并无缝扩展到统一的多模态框架中。该方法首先对SD3.5-Medium进行架构修改，并在高质量数据上进行大规模预训练，从而实现联合文本到图像的生成和编辑能力。为了增强指令遵循和编辑一致性，提出了一种新的渐进式双任务强化策略（PDTR），有效地分阶段加强了这两项任务。实验验证了不同任务的强化阶段是互利的，不会引起负面干扰。经过预训练和强化策略后，UniPic2-SD3.5M-Kontext展示了比具有更大生成参数的模型（包括BAGEL (7B) 和 Flux-Kontext (12B)）更强的图像生成和编辑能力。此外，遵循MetaQuery，通过连接器将UniPic2-SD3.5M-Kontext和Qwen2.5-VL-7B连接起来，并进行联合训练，推出了统一的多模态模型UniPic2-Metaquery。UniPic2-Metaquery集成了理解、生成和编辑，通过简单且可扩展的训练范式，在各种任务中实现了顶级的性能。这始终验证了所提出的训练范式的有效性和泛化性，并将其形式化为Skywork UniPic 2.0。

## 🔬 方法详解

**问题定义**：论文旨在解决现有开源多模态模型在图像生成和编辑任务中，由于过度关注模型参数规模而忽略训练策略优化，导致效率和性能瓶颈的问题。现有方法难以在参数效率和性能之间取得平衡，并且在指令遵循和编辑一致性方面存在不足。

**核心思路**：论文的核心思路是通过优化训练策略，而非单纯增加模型参数，来提升多模态模型的图像生成和编辑能力。具体而言，通过架构改进、大规模预训练以及创新的渐进式双任务强化学习（PDTR）策略，实现更高效、更一致的图像生成和编辑。

**技术框架**：UniPic 2.0的技术框架主要包含三个阶段：首先，对SD3.5-Medium模型进行架构修改，以适应多模态任务；其次，在大规模高质量数据集上进行预训练，使模型具备基本的文本到图像生成和编辑能力；最后，采用PDTR策略进行强化学习，提升模型在指令遵循和编辑一致性方面的表现。UniPic2-Metaquery则进一步将UniPic2-SD3.5M-Kontext与Qwen2.5-VL-7B通过连接器连接，进行联合训练，形成统一的多模态模型。

**关键创新**：论文最重要的技术创新点是提出的渐进式双任务强化学习（PDTR）策略。PDTR策略通过分阶段的方式，分别对图像生成和编辑任务进行强化学习，避免了两种任务之间的负面干扰，实现了互利共赢的效果。这种策略能够有效地提升模型在指令遵循和编辑一致性方面的表现。

**关键设计**：PDTR策略的关键设计在于其渐进式的训练方式。首先，对模型进行预训练，使其具备基本的生成和编辑能力。然后，分别针对生成和编辑任务，设计相应的奖励函数，并使用强化学习算法进行训练。在训练过程中，逐步增加奖励函数的权重，使模型逐渐适应指令的要求。此外，论文还采用了MetaQuery方法，将UniPic2-SD3.5M-Kontext与Qwen2.5-VL-7B连接，并通过联合训练，实现了多模态信息的融合。

## 📊 实验亮点

UniPic2-SD3.5M-Kontext在图像生成和编辑方面优于参数量更大的模型，例如BAGEL (7B) 和 Flux-Kontext (12B)。UniPic2-Metaquery通过简单的训练范式，在各种多模态任务中实现了顶级的性能，验证了所提出的训练范式的有效性和泛化性。

## 🎯 应用场景

该研究成果可广泛应用于图像生成、图像编辑、内容创作、虚拟现实、游戏开发等领域。通过提升图像生成和编辑的质量和效率，可以为用户提供更丰富的视觉体验，并降低内容创作的门槛。未来，该技术有望应用于智能设计、自动化内容生成等更广泛的领域。

## 📄 摘要（原文）

> Recent advances in multimodal models have demonstrated impressive capabilities in unified image generation and editing. However, many prominent open-source models prioritize scaling model parameters over optimizing training strategies, limiting their efficiency and performance. In this work, we present UniPic2-SD3.5M-Kontext, a 2B-parameter DiT model based on SD3.5-Medium, which achieves state-of-the-art image generation and editing while extending seamlessly into a unified multimodal framework. Our approach begins with architectural modifications to SD3.5-Medium and large-scale pre-training on high-quality data, enabling joint text-to-image generation and editing capabilities. To enhance instruction following and editing consistency, we propose a novel Progressive Dual-Task Reinforcement strategy (PDTR), which effectively strengthens both tasks in a staged manner. We empirically validate that the reinforcement phases for different tasks are mutually beneficial and do not induce negative interference. After pre-training and reinforcement strategies, UniPic2-SD3.5M-Kontext demonstrates stronger image generation and editing capabilities than models with significantly larger generation parameters-including BAGEL (7B) and Flux-Kontext (12B). Furthermore, following the MetaQuery, we connect the UniPic2-SD3.5M-Kontext and Qwen2.5-VL-7B via a connector and perform joint training to launch a unified multimodal model UniPic2-Metaquery. UniPic2-Metaquery integrates understanding, generation, and editing, achieving top-tier performance across diverse tasks with a simple and scalable training paradigm. This consistently validates the effectiveness and generalizability of our proposed training paradigm, which we formalize as Skywork UniPic 2.0.

