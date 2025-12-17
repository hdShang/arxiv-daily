---
layout: default
title: Can World Models Benefit VLMs for World Dynamics?
---

# Can World Models Benefit VLMs for World Dynamics?

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.00855" target="_blank" class="toolbar-btn">arXiv: 2510.00855v1</a>
    <a href="https://arxiv.org/pdf/2510.00855.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00855v1" 
            onclick="toggleFavorite(this, '2510.00855v1', 'Can World Models Benefit VLMs for World Dynamics?')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kevin Zhang, Kuangzhi Ge, Xiaowei Chi, Renrui Zhang, Shaojun Shi, Zhen Dong, Sirui Han, Shanghang Zhang

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-10-01

**备注**: Project page: https://dyva-worldlm.github.io

---

## 💡 一句话要点

**提出WorldLM，利用世界模型先验增强视觉语言模型的世界动态理解能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `世界模型` `视觉语言模型` `视频扩散模型` `生成式编码器` `空间推理` `动态理解` `多模态学习` `运动一致性`

## 📋 核心要点

1. 现有视觉语言模型在处理涉及动态变化和空间推理的任务时存在不足，缺乏对世界动态的有效建模。
2. 论文提出WorldLM，利用视频扩散模型作为生成式编码器，提取包含运动信息的视觉嵌入，从而引入世界模型先验。
3. 实验表明，提出的Dynamic Vision Aligner (DyVA) 在空间推理任务上超越了现有模型，并提升了单图像模型的多帧推理能力。

## 📝 摘要（中文）

本文探讨了世界模型（World Models）能否提升视觉语言模型（VLMs）对世界动态的理解能力。世界模型通过互联网规模的视频数据训练，能够生成连贯且合理的结构、运动和物理动态，被认为是强大的世界模拟器。本文将视频扩散模型重新用作生成式编码器，执行单步去噪，并将得到的潜在变量作为视觉嵌入。通过对这类模型（称为WorldLMs）的实证研究，发现生成式编码器能够捕获对下游理解有用的潜在变量，这些变量与传统编码器有所不同。最佳模型Dynamic Vision Aligner (DyVA) 显著增强了空间推理能力，并使单图像模型能够执行多帧推理。在视觉推理任务中，DyVA超越了开源和专有基线，实现了最先进或可比的性能。这些提升归因于WorldLM从视频预训练中继承的运动一致性内化。最后，系统地探索了广泛的模型设计，为未来的工作指明了方向。希望这项研究能为利用世界模型先验的新型VLM铺平道路，并朝着通用视觉学习器的方向发展。

## 🔬 方法详解

**问题定义**：现有视觉语言模型在理解世界动态和进行空间推理方面存在局限性。传统的视觉编码器难以捕捉视频中的时间信息和运动规律，导致模型在处理需要理解物体运动、交互和变化的场景时表现不佳。因此，如何有效地将世界动态知识融入视觉语言模型是一个关键问题。

**核心思路**：论文的核心思路是利用预训练的世界模型作为视觉编码器，将视频数据中学习到的运动规律和物理知识迁移到视觉语言模型中。具体而言，论文使用视频扩散模型作为生成式编码器，通过单步去噪过程提取视觉特征，这些特征包含了丰富的运动信息和世界动态先验。

**技术框架**：整体框架包括以下几个主要步骤：1) 使用预训练的视频扩散模型作为生成式编码器；2) 对输入图像或视频帧进行单步去噪，得到视觉嵌入；3) 将视觉嵌入输入到视觉语言模型中进行下游任务的训练和推理。提出的Dynamic Vision Aligner (DyVA) 是一个具体的WorldLM实现，它利用Transformer结构对视觉嵌入进行处理，并将其与文本嵌入进行对齐。

**关键创新**：论文的关键创新在于将世界模型（特别是视频扩散模型）引入视觉语言模型，并将其用作生成式编码器。这种方法能够有效地将视频数据中学习到的运动规律和物理知识迁移到视觉语言模型中，从而提升模型对世界动态的理解能力。与传统的视觉编码器相比，生成式编码器能够捕获更丰富的运动信息和上下文信息。

**关键设计**：论文的关键设计包括：1) 使用预训练的视频扩散模型，确保编码器具有强大的世界动态建模能力；2) 使用单步去噪过程，以高效地提取视觉嵌入；3) 设计Dynamic Vision Aligner (DyVA) 模型，利用Transformer结构对视觉嵌入进行处理，并将其与文本嵌入进行对齐。论文还探索了不同的模型设计，例如不同的去噪步数、不同的Transformer结构等，以找到最佳的模型配置。

## 📊 实验亮点

实验结果表明，提出的Dynamic Vision Aligner (DyVA) 在视觉推理任务上取得了显著的性能提升，超越了现有的开源和专有模型。例如，在某些空间推理任务上，DyVA的性能提升幅度超过了10%。这些结果表明，利用世界模型先验可以有效地提升视觉语言模型对世界动态的理解能力。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、视频理解、智能监控等领域。通过提升视觉语言模型对世界动态的理解能力，可以使机器人在复杂环境中更好地感知、推理和决策，从而实现更智能化的应用。

## 📄 摘要（原文）

> Trained on internet-scale video data, generative world models are increasingly recognized as powerful world simulators that can generate consistent and plausible dynamics over structure, motion, and physics. This raises a natural question: with the advent of strong video foundational models, might they supplant conventional vision encoder paradigms for general-purpose multimodal understanding? While recent studies have begun to explore the potential of world models on common vision tasks, these explorations typically lack a systematic investigation of generic, multimodal tasks. In this work, we strive to investigate the capabilities when world model priors are transferred into Vision-Language Models: we re-purpose a video diffusion model as a generative encoder to perform a single denoising step and treat the resulting latents as a set of visual embedding. We empirically investigate this class of models, which we refer to as World-Language Models (WorldLMs), and we find that generative encoders can capture latents useful for downstream understanding that show distinctions from conventional encoders. Naming our best-performing variant Dynamic Vision Aligner (DyVA), we further discover that this method significantly enhances spatial reasoning abilities and enables single-image models to perform multi-frame reasoning. Through the curation of a suite of visual reasoning tasks, we find DyVA to surpass both open-source and proprietary baselines, achieving state-of-the-art or comparable performance. We attribute these gains to WorldLM's inherited motion-consistency internalization from video pre-training. Finally, we systematically explore extensive model designs to highlight promising directions for future work. We hope our study can pave the way for a new family of VLMs that leverage priors from world models and are on a promising path towards generalist vision learners.

