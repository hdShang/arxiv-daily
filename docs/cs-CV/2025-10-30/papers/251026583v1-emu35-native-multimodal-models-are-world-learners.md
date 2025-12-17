---
layout: default
title: Emu3.5: Native Multimodal Models are World Learners
---

# Emu3.5: Native Multimodal Models are World Learners

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26583" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26583v1</a>
  <a href="https://arxiv.org/pdf/2510.26583.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26583v1" onclick="toggleFavorite(this, '2510.26583v1', 'Emu3.5: Native Multimodal Models are World Learners')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yufeng Cui, Honghao Chen, Haoge Deng, Xu Huang, Xinghang Li, Jirong Liu, Yang Liu, Zhuoyan Luo, Jinsheng Wang, Wenxuan Wang, Yueze Wang, Chengyuan Wang, Fan Zhang, Yingli Zhao, Ting Pan, Xianduo Li, Zecheng Hao, Wenxuan Ma, Zhuo Chen, Yulong Ao, Tiejun Huang, Zhongyuan Wang, Xinlong Wang

**分类**: cs.CV

**发布日期**: 2025-10-30

**备注**: project page: https://emu.world

**🔗 代码/项目**: [GITHUB](https://github.com/baaivision/Emu3.5)

---

## 💡 一句话要点

**Emu3.5：原生多模态模型，通过预测视觉和语言的下一个状态实现世界理解。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `世界模型` `视觉语言模型` `长时程推理` `图像生成` `强化学习` `离散扩散` `具身智能`

## 📋 核心要点

1. 现有模型在处理长时程视觉-语言交互和复杂多模态推理方面存在挑战，难以实现对世界的深入理解和有效操作。
2. Emu3.5通过原生预测视觉和语言的下一个状态，并利用大规模视觉-语言交错数据进行端到端预训练，从而实现对世界的建模。
3. Emu3.5通过离散扩散适应（DiDA）加速推理，并在图像生成、编辑和交错生成任务上取得了与Gemini 2.5 Flash Image相当或更优越的性能。

## 📝 摘要（中文）

Emu3.5是一个大规模多模态世界模型，它原生预测视觉和语言的下一个状态。Emu3.5通过统一的下一个token预测目标，在包含超过10万亿token的视觉-语言交错数据语料库上进行端到端预训练，这些数据主要来自互联网视频的连续帧和文本记录。该模型自然地接受交错的视觉-语言输入，并生成交错的视觉-语言输出。Emu3.5通过大规模强化学习进一步进行后训练，以增强多模态推理和生成能力。为了提高推理效率，我们提出了离散扩散适应（DiDA），它将逐token解码转换为双向并行预测，在不牺牲性能的情况下，将每次图像推理加速约20倍。Emu3.5表现出强大的原生多模态能力，包括长时程视觉-语言生成、任意到图像（X2I）生成和复杂的富文本图像生成。它还表现出可泛化的世界建模能力，从而能够在各种场景和任务中实现时空一致的世界探索和开放世界具身操作。作为比较，Emu3.5在图像生成和编辑任务上达到了与Gemini 2.5 Flash Image (Nano Banana)相当的性能，并在一系列交错生成任务上表现出优越的结果。我们开源了Emu3.5，以支持社区研究。

## 🔬 方法详解

**问题定义**：现有的大型多模态模型通常难以处理长时程的视觉-语言交互，并且在理解和生成复杂的多模态内容时存在局限性。它们在世界建模和开放环境中的具身操作方面也面临挑战。现有方法的痛点在于缺乏对视觉和语言信息进行深度融合和推理的能力，以及推理效率较低。

**核心思路**：Emu3.5的核心思路是通过原生预测视觉和语言的下一个状态，从而学习世界模型。这种方法允许模型自然地处理交错的视觉-语言输入和输出，并能够进行长时程的推理和生成。通过大规模的预训练和强化学习，模型可以学习到丰富的世界知识和操作技能。DiDA的引入旨在加速推理过程，提高模型的实用性。

**技术框架**：Emu3.5的整体架构包括以下几个主要阶段：1) 大规模视觉-语言交错数据预训练：使用包含超过10万亿token的数据集，通过下一个token预测目标进行端到端训练。2) 强化学习后训练：利用强化学习进一步提升模型的多模态推理和生成能力。3) 离散扩散适应（DiDA）：将token-by-token解码转换为双向并行预测，加速推理过程。

**关键创新**：Emu3.5最重要的技术创新点在于其原生多模态建模方法，即通过预测视觉和语言的下一个状态来学习世界模型。与传统的先分别处理视觉和语言信息再进行融合的方法不同，Emu3.5从一开始就将视觉和语言视为统一的序列，从而能够更好地捕捉它们之间的依赖关系。DiDA也是一个重要的创新，它显著提高了推理效率。

**关键设计**：Emu3.5的关键设计包括：1) 使用大规模的视觉-语言交错数据集进行预训练，保证模型能够学习到丰富的世界知识。2) 采用Transformer架构作为模型的基础，使其能够处理长序列的视觉和语言信息。3) 使用强化学习来优化模型的多模态推理和生成能力。4) DiDA通过将自回归解码转化为并行预测，显著提升了推理速度。

## 📊 实验亮点

Emu3.5在图像生成和编辑任务上达到了与Gemini 2.5 Flash Image (Nano Banana)相当的性能，并在一系列交错生成任务上表现出优越的结果。通过DiDA，Emu3.5的推理速度提高了约20倍，而没有牺牲性能。这些结果表明Emu3.5具有强大的多模态能力和高效的推理能力。

## 🎯 应用场景

Emu3.5具有广泛的应用前景，包括智能助手、机器人控制、内容创作和教育等领域。它可以用于生成逼真的图像和视频，理解复杂的视觉-语言场景，并与用户进行自然的交互。在机器人领域，Emu3.5可以帮助机器人理解环境，执行复杂的任务，并与人类进行协作。此外，Emu3.5还可以用于开发新的教育工具，帮助学生更好地学习和理解知识。

## 📄 摘要（原文）

> We introduce Emu3.5, a large-scale multimodal world model that natively predicts the next state across vision and language. Emu3.5 is pre-trained end-to-end with a unified next-token prediction objective on a corpus of vision-language interleaved data containing over 10 trillion tokens, primarily derived from sequential frames and transcripts of internet videos. The model naturally accepts interleaved vision-language inputs and generates interleaved vision-language outputs. Emu3.5 is further post-trained with large-scale reinforcement learning to enhance multimodal reasoning and generation. To improve inference efficiency, we propose Discrete Diffusion Adaptation (DiDA), which converts token-by-token decoding into bidirectional parallel prediction, accelerating per-image inference by about 20x without sacrificing performance. Emu3.5 exhibits strong native multimodal capabilities, including long-horizon vision-language generation, any-to-image (X2I) generation, and complex text-rich image generation. It also exhibits generalizable world-modeling abilities, enabling spatiotemporally consistent world exploration and open-world embodied manipulation across diverse scenarios and tasks. For comparison, Emu3.5 achieves performance comparable to Gemini 2.5 Flash Image (Nano Banana) on image generation and editing tasks and demonstrates superior results on a suite of interleaved generation tasks. We open-source Emu3.5 at https://github.com/baaivision/Emu3.5 to support community research.

