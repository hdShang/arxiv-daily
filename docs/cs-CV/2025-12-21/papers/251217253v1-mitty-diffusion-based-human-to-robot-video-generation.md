---
layout: default
title: Mitty: Diffusion-based Human-to-Robot Video Generation
---

# Mitty: Diffusion-based Human-to-Robot Video Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17253" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17253v1</a>
  <a href="https://arxiv.org/pdf/2512.17253.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17253v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17253v1', 'Mitty: Diffusion-based Human-to-Robot Video Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiren Song, Cheng Liu, Weijia Mao, Mike Zheng Shou

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**Mitty：提出基于扩散模型的Human2Robot视频生成方法，实现端到端机器人学习。**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人学习` `视频生成` `扩散模型` `Human2Robot` `上下文学习` `Transformer` `端到端学习`

## 📋 核心要点

1. 现有机器人学习方法依赖中间表示，易造成信息损失和误差累积，影响视频一致性。
2. Mitty利用扩散Transformer，直接将人类演示视频转化为机器人执行视频，无需中间抽象。
3. 通过自动合成流程生成高质量人-机器人数据，实验证明Mitty具有优秀的泛化能力。

## 📝 摘要（中文）

本文提出Mitty，一种基于扩散Transformer的视频上下文学习方法，用于端到端的人类到机器人视频生成。现有方法依赖于关键点或轨迹等中间表示，导致信息损失和累积误差，影响时间和视觉一致性。Mitty建立在预训练的视频扩散模型之上，利用强大的视觉-时间先验，将人类演示转化为机器人执行视频，无需动作标签或中间抽象。演示视频被压缩成条件tokens，并通过扩散过程中的双向注意力与机器人去噪tokens融合。为了缓解配对数据稀缺问题，还开发了一种自动合成流程，从大型自我中心数据集中生成高质量的人-机器人对。在Human2Robot和EPIC-Kitchens上的实验表明，Mitty提供了最先进的结果，对未见环境的强大泛化能力，以及从人类观察中进行可扩展机器人学习的新见解。

## 🔬 方法详解

**问题定义**：现有机器人学习方法通常依赖于从人类演示视频中提取的中间表示，例如关键点或轨迹。这种方法存在两个主要问题：一是信息损失，中间表示无法完全捕捉原始视频中的所有信息；二是误差累积，中间表示的提取过程本身可能引入误差，这些误差会进一步影响后续的机器人控制。因此，需要一种能够直接从人类演示视频生成机器人执行视频的端到端方法。

**核心思路**：Mitty的核心思路是利用预训练的视频扩散模型强大的视觉-时间先验知识，将人类演示视频作为条件，引导扩散过程生成对应的机器人执行视频。通过这种方式，避免了中间表示的使用，从而减少了信息损失和误差累积。同时，利用扩散模型的生成能力，可以生成更加自然和真实的机器人视频。

**技术框架**：Mitty的整体框架包括两个主要部分：一是视频扩散模型，用于生成机器人执行视频；二是条件编码器，用于将人类演示视频编码成条件tokens。具体来说，首先使用预训练的视频扩散模型作为生成器，然后将人类演示视频通过条件编码器压缩成条件tokens。在扩散过程中，通过双向注意力机制将条件tokens与机器人去噪tokens融合，从而引导生成过程。此外，为了缓解配对数据稀缺问题，还设计了一个自动合成流程，用于生成高质量的人-机器人配对数据。

**关键创新**：Mitty的关键创新在于将视频扩散模型应用于Human2Robot视频生成任务，并提出了一种有效的条件融合方法。与现有方法相比，Mitty无需中间表示，可以直接从人类演示视频生成机器人执行视频，从而减少了信息损失和误差累积。此外，Mitty还提出了一种自动合成流程，用于生成高质量的人-机器人配对数据，进一步提高了模型的性能。

**关键设计**：Mitty的关键设计包括以下几个方面：一是使用预训练的视频扩散模型，利用其强大的视觉-时间先验知识；二是设计双向注意力机制，用于有效融合条件tokens和机器人去噪tokens；三是设计自动合成流程，用于生成高质量的人-机器人配对数据。在具体实现上，使用了Transformer作为扩散模型的基本架构，并采用了标准的扩散训练方法。损失函数主要包括扩散模型的重建损失和对抗损失，以提高生成视频的质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17253v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17253v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17253v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Mitty在Human2Robot和EPIC-Kitchens数据集上取得了state-of-the-art的结果。实验表明，Mitty能够生成高质量的机器人执行视频，并且具有很强的泛化能力，可以适应未见过的环境。相较于之前的中间表示方法，Mitty在视觉和时间一致性上都有显著提升。具体性能数据未知，但论文强调了其优于现有技术的表现。

## 🎯 应用场景

Mitty具有广泛的应用前景，例如可以通过学习人类的演示，使机器人能够执行各种复杂的任务，如烹饪、清洁、装配等。此外，Mitty还可以用于机器人教学，通过生成不同场景下的机器人执行视频，帮助人们更好地理解和学习机器人操作。未来，Mitty有望成为实现通用机器人学习的关键技术。

## 📄 摘要（原文）

> Learning directly from human demonstration videos is a key milestone toward scalable and generalizable robot learning. Yet existing methods rely on intermediate representations such as keypoints or trajectories, introducing information loss and cumulative errors that harm temporal and visual consistency. We present Mitty, a Diffusion Transformer that enables video In-Context Learning for end-to-end Human2Robot video generation. Built on a pretrained video diffusion model, Mitty leverages strong visual-temporal priors to translate human demonstrations into robot-execution videos without action labels or intermediate abstractions. Demonstration videos are compressed into condition tokens and fused with robot denoising tokens through bidirectional attention during diffusion. To mitigate paired-data scarcity, we also develop an automatic synthesis pipeline that produces high-quality human-robot pairs from large egocentric datasets. Experiments on Human2Robot and EPIC-Kitchens show that Mitty delivers state-of-the-art results, strong generalization to unseen environments, and new insights for scalable robot learning from human observations.

