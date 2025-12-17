---
layout: default
title: OmniMotion-X: Versatile Multimodal Whole-Body Motion Generation
---

# OmniMotion-X: Versatile Multimodal Whole-Body Motion Generation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.19789" target="_blank" class="toolbar-btn">arXiv: 2510.19789v1</a>
    <a href="https://arxiv.org/pdf/2510.19789.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19789v1" 
            onclick="toggleFavorite(this, '2510.19789v1', 'OmniMotion-X: Versatile Multimodal Whole-Body Motion Generation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Guowei Xu, Yuxuan Bian, Ailing Zeng, Mingyi Shi, Shaoli Huang, Wen Li, Lixin Duan, Qiang Xu

**分类**: cs.CV

**发布日期**: 2025-10-22

---

## 💡 一句话要点

**OmniMotion-X：多功能多模态全身运动生成框架，实现逼真可控的交互式长时运动。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态运动生成` `扩散模型` `Transformer` `参考运动` `SMPL-X` `运动预测` `动作捕捉`

## 📋 核心要点

1. 现有方法在多模态全身运动生成中，难以兼顾多种模态输入和保证生成运动的连贯性与真实感。
2. OmniMotion-X利用自回归扩散Transformer，并引入参考运动作为条件信号，增强生成运动的一致性和风格。
3. OmniMotion-X在多项多模态任务上超越现有方法，并构建了大规模多模态运动数据集OmniMoCap-X。

## 📝 摘要（中文）

本文提出OmniMotion-X，一个多功能多模态全身人体运动生成框架，它以统一的序列到序列方式利用自回归扩散Transformer。OmniMotion-X高效地支持各种多模态任务，包括文本到运动、音乐到舞蹈、语音到手势，以及全局时空控制场景（例如，运动预测、中间帧生成、运动补全和关节/轨迹引导的合成），以及这些任务的灵活组合。具体来说，我们提出使用参考运动作为一种新的条件信号，从而显著增强了生成内容、风格和时间动态的一致性，这对于逼真的动画至关重要。为了处理多模态冲突，我们引入了一种渐进的由弱到强的混合条件训练策略。为了实现高质量的多模态训练，我们构建了迄今为止最大的统一多模态运动数据集OmniMoCap-X，整合了来自10个不同任务的28个公开MoCap资源，并以30 fps标准化为SMPL-X格式。为了确保详细和一致的注释，我们将序列渲染成视频，并使用GPT-4o自动生成结构化和分层字幕，捕捉低级动作和高级语义。广泛的实验评估证实，OmniMotion-X显著超越了现有方法，在多个多模态任务中展示了最先进的性能，并实现了逼真、连贯和可控的长时间运动的交互式生成。

## 🔬 方法详解

**问题定义**：现有方法在多模态全身运动生成任务中，难以同时处理多种模态的输入，并且生成的运动在连贯性、风格一致性和时间动态方面存在不足，导致生成的动画不够真实。此外，多模态输入之间可能存在冲突，进一步增加了生成高质量运动的难度。

**核心思路**：OmniMotion-X的核心思路是利用自回归扩散Transformer，并引入参考运动作为一种新的条件信号。参考运动能够提供关于运动风格、时间动态和整体结构的先验知识，从而引导生成器生成更连贯、更真实的运动。此外，采用渐进的由弱到强的混合条件训练策略，以解决多模态输入之间的冲突。

**技术框架**：OmniMotion-X采用序列到序列的框架，使用自回归扩散Transformer作为生成器。整体流程如下：首先，将各种模态的输入（例如，文本、音乐、语音、参考运动）编码成统一的特征表示。然后，将这些特征表示输入到自回归扩散Transformer中，逐步生成人体运动序列。最后，通过后处理步骤，将生成的运动序列转换为SMPL-X格式，以便进行可视化和评估。

**关键创新**：OmniMotion-X的关键创新点在于：1) 引入参考运动作为条件信号，显著提升了生成运动的连贯性和真实感；2) 提出渐进的由弱到强的混合条件训练策略，有效解决了多模态输入之间的冲突；3) 构建了大规模多模态运动数据集OmniMoCap-X，为多模态运动生成的研究提供了丰富的数据资源。

**关键设计**：OmniMotion-X的关键设计包括：1) 使用SMPL-X格式作为人体运动的统一表示；2) 采用自回归扩散Transformer作为生成器，能够逐步生成高质量的运动序列；3) 设计了专门的损失函数，以鼓励生成运动与参考运动在风格和时间动态上保持一致；4) 使用GPT-4o自动生成结构化和分层字幕，以确保数据集具有详细和一致的注释。

## 📊 实验亮点

OmniMotion-X在多个多模态任务上取得了显著的性能提升，超越了现有的最先进方法。例如，在文本到运动任务中，OmniMotion-X生成的运动在连贯性和真实感方面均优于现有方法。通过引入参考运动作为条件信号，OmniMotion-X能够生成更具风格化和个性化的运动，从而更好地满足用户的需求。OmniMoCap-X数据集的构建也为多模态运动生成的研究提供了重要的数据支持。

## 🎯 应用场景

OmniMotion-X具有广泛的应用前景，包括虚拟现实、游戏开发、动画制作、康复训练等领域。它可以用于生成逼真的人体动画，创建沉浸式的虚拟体验，辅助游戏角色设计，加速动画制作流程，以及为康复患者提供个性化的运动指导。该研究的成果将推动人机交互技术的发展，并为人们的生活带来更多便利和乐趣。

## 📄 摘要（原文）

> This paper introduces OmniMotion-X, a versatile multimodal framework for whole-body human motion generation, leveraging an autoregressive diffusion transformer in a unified sequence-to-sequence manner. OmniMotion-X efficiently supports diverse multimodal tasks, including text-to-motion, music-to-dance, speech-to-gesture, and global spatial-temporal control scenarios (e.g., motion prediction, in-betweening, completion, and joint/trajectory-guided synthesis), as well as flexible combinations of these tasks. Specifically, we propose the use of reference motion as a novel conditioning signal, substantially enhancing the consistency of generated content, style, and temporal dynamics crucial for realistic animations. To handle multimodal conflicts, we introduce a progressive weak-to-strong mixed-condition training strategy. To enable high-quality multimodal training, we construct OmniMoCap-X, the largest unified multimodal motion dataset to date, integrating 28 publicly available MoCap sources across 10 distinct tasks, standardized to the SMPL-X format at 30 fps. To ensure detailed and consistent annotations, we render sequences into videos and use GPT-4o to automatically generate structured and hierarchical captions, capturing both low-level actions and high-level semantics. Extensive experimental evaluations confirm that OmniMotion-X significantly surpasses existing methods, demonstrating state-of-the-art performance across multiple multimodal tasks and enabling the interactive generation of realistic, coherent, and controllable long-duration motions.

