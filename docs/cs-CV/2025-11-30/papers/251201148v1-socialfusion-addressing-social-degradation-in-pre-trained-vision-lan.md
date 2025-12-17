---
layout: default
title: SocialFusion: Addressing Social Degradation in Pre-trained Vision-Language Models
---

# SocialFusion: Addressing Social Degradation in Pre-trained Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.01148" class="toolbar-btn" target="_blank">📄 arXiv: 2512.01148v1</a>
  <a href="https://arxiv.org/pdf/2512.01148.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.01148v1" onclick="toggleFavorite(this, '2512.01148v1', 'SocialFusion: Addressing Social Degradation in Pre-trained Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hamza Tahboub, Weiyan Shi, Gang Hua, Huaizu Jiang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-30

**备注**: 22 pages, 10 figures

---

## 💡 一句话要点

**提出SocialFusion框架，解决预训练视觉-语言模型中的社会认知退化问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `视觉-语言模型` `社会认知` `负迁移` `正迁移` `多任务学习` `表征学习` `社会退化`

## 📋 核心要点

1. 现有预训练视觉-语言模型在处理社会感知任务时存在负迁移现象，无法有效学习多个相关任务。
2. 论文提出SocialFusion框架，通过学习视觉编码器和语言模型之间的最小连接来解决社会认知退化问题。
3. 实验表明，SocialFusion在多个社会任务上实现了正迁移，性能与特定任务的SOTA模型相当。

## 📝 摘要（中文）

理解视觉线索中的社会互动是具备社会能力的AI所面临的一项根本性挑战。尽管强大的预训练视觉-语言模型(VLMs)已经展现出卓越的通用能力，但令人惊讶的是，它们难以同时统一和学习多个社会感知任务，常常表现出负迁移。我们发现这种负迁移源于一个关键问题，我们称之为“社会退化”，即VLMs的通用视觉-语言预训练过程损害了视觉编码器表示细微社会信息的能力。我们通过线性表示探针的可解码性和梯度冲突分析的兼容性这两个角度进一步研究了这种行为，揭示了两者都在退化中发挥作用，尤其是前者在VLM预训练过程中受到了显著损害。为了解决这些问题，我们提出了SocialFusion，一个统一的框架，用于学习冻结的视觉编码器和语言模型之间的最小连接。与现有的VLM相比，它在所有五个社会任务中都表现出正迁移，利用它们之间的协同作用来提高整体性能，并在各种基准测试中实现了与特定任务的state-of-the-art模型相当的性能。我们的研究结果表明，当前的VLM预训练策略可能不利于获得通用的社会能力，并强调需要更多具有社会意识的训练范式。

## 🔬 方法详解

**问题定义**：现有的预训练视觉-语言模型(VLMs)在处理多个社会感知任务时，会发生“社会退化”现象，即模型在学习一个社会任务时，会损害其在其他社会任务上的表现，导致负迁移。这种现象表明，通用的视觉-语言预训练过程可能损害了视觉编码器捕捉细微社会信息的能力，阻碍了模型学习通用的社会认知能力。

**核心思路**：论文的核心思路是，通过解耦视觉编码器和语言模型，并学习它们之间的最小连接，来避免视觉编码器在预训练过程中受到过度干扰，从而保留其捕捉社会信息的能力。具体来说，论文冻结了预训练的视觉编码器，并训练一个轻量级的融合模块，将视觉特征和语言特征进行融合，从而实现跨任务的正迁移。

**技术框架**：SocialFusion框架主要包含两个模块：一个冻结的预训练视觉编码器和一个可训练的语言模型。视觉编码器负责提取图像的视觉特征，语言模型负责处理文本信息。框架的关键在于一个轻量级的融合模块，该模块学习视觉特征和语言特征之间的关联，并将它们融合在一起。融合后的特征被用于执行各种社会感知任务。

**关键创新**：SocialFusion的关键创新在于，它通过冻结视觉编码器并学习最小连接，有效地避免了预训练过程对视觉编码器的干扰，从而保留了其捕捉社会信息的能力。这种方法与传统的微调方法不同，后者通常会微调整个模型，从而可能导致社会退化现象。

**关键设计**：SocialFusion的关键设计包括：1) 使用预训练的视觉编码器，例如CLIP，以获得强大的视觉特征表示；2) 设计一个轻量级的融合模块，以减少训练参数和计算成本；3) 使用对比学习损失函数，以鼓励模型学习视觉特征和语言特征之间的关联；4) 在多个社会感知任务上进行联合训练，以提高模型的泛化能力。

## 📊 实验亮点

SocialFusion在五个社会感知任务上均实现了正迁移，显著优于直接微调的VLM模型。例如，在某些任务上，SocialFusion的性能提升超过5%。此外，SocialFusion在多个基准测试中取得了与特定任务的SOTA模型相当的性能，证明了其有效性和泛化能力。

## 🎯 应用场景

该研究成果可应用于社交机器人、智能监控、自动驾驶等领域，提升AI系统对人类社会行为的理解和交互能力。例如，社交机器人可以更好地理解人类的情绪和意图，从而进行更自然和有效的互动；智能监控系统可以识别异常的社会行为，从而提高安全性；自动驾驶系统可以理解行人的意图，从而做出更安全的决策。

## 📄 摘要（原文）

> Understanding social interactions from visual cues is a fundamental challenge for a socially competent AI. While powerful pre-trained vision-language models (VLMs) have shown remarkable general capabilities, they surprisingly struggle to unify and learn multiple social perception tasks simultaneously, often exhibiting negative transfer. We identify that this negative transfer stems from a critical issue we term "social degradation," whereby the general visual-linguistic pre-training process of VLMs impairs the visual encoder's ability to represent nuanced social information. We investigate this behavior further under two lenses: decodability through linear representation probing and compatibility through gradient conflict analysis, revealing that both play a role in the degradation, especially the former, which is significantly compromised in the VLM pre-training process. To address these issues, we propose SocialFusion, a unified framework that learns a minimal connection between a frozen visual encoder and a language model. Compared with existing VLMs, it exhibits positive transfer across all five social tasks, leveraging synergies between them to enhance overall performance and achieves comparable performance to task-specific state-of-the-art models on various benchmarks. Our findings suggest that current VLM pre-training strategies may be detrimental to acquiring general social competence and highlight the need for more socially-aware training paradigms.

