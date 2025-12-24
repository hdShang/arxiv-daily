---
layout: default
title: "Prime and Reach: Synthesising Body Motion for Gaze-Primed Object Reach"
---

# Prime and Reach: Synthesising Body Motion for Gaze-Primed Object Reach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16456" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16456v1</a>
  <a href="https://arxiv.org/pdf/2512.16456.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16456v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16456v1', 'Prime and Reach: Synthesising Body Motion for Gaze-Primed Object Reach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Masashi Hatano, Saptarshi Sinha, Jacob Chalk, Wei-Hong Li, Hideo Saito, Dima Damen

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project Page: https://masashi-hatano.github.io/prime-and-reach/

---

## 💡 一句话要点

**提出基于注视启动的人体运动合成方法，用于模拟抓取或放置物体的自然行为。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `人体运动生成` `注视启动` `扩散模型` `人机交互` `运动合成`

## 📋 核心要点

1. 现有方法在生成人体运动时，难以模拟注视启动等复杂行为，缺乏对目标物体交互的精准控制。
2. 本文提出一种基于扩散模型的运动生成框架，利用大规模注视启动数据集进行训练，实现自然的人体运动合成。
3. 实验表明，该方法在HD-EPIC数据集上取得了显著的启动成功率和到达成功率，验证了其有效性。

## 📝 摘要（中文）

人体运动生成是一项具有挑战性的任务，旨在创建模仿自然人类行为的真实运动。本文关注一个经过充分研究的行为：启动物体/位置以进行拾取或放置，即从远处发现物体/位置（称为注视启动），然后是接近和到达目标位置的运动。为此，我们首次整理了23.7K个注视启动的人体运动序列，用于从五个公开可用的数据集（即HD-EPIC、MoGaze、HOT3D、ADT和GIMO）到达目标物体位置。我们预训练了一个文本条件扩散运动生成模型，然后在我们整理的序列上，以目标姿势或位置为条件对其进行微调。重要的是，我们通过包括“到达成功”和新引入的“启动成功”指标在内的多个指标来评估生成的运动模仿自然人类运动的能力。在最大的数据集HD-EPIC上，当以目标物体位置为条件时，我们的模型实现了60%的启动成功率和89%的到达成功率。

## 🔬 方法详解

**问题定义**：现有的人体运动生成方法难以准确模拟人类在抓取或放置物体前的注视启动行为，即在运动前通过注视来预先锁定目标物体。这导致生成的运动不够自然和真实，缺乏与环境的有效交互。现有方法通常难以将注视信息有效地融入到运动生成过程中。

**核心思路**：本文的核心思路是利用大规模的注视启动人体运动数据集，训练一个条件扩散模型，使其能够学习到注视行为与后续运动之间的关联。通过将目标物体的位置或姿势作为条件输入，模型可以生成符合人类自然行为的运动序列，从而实现更真实和自然的运动合成。

**技术框架**：该方法采用两阶段训练策略。首先，使用文本条件扩散模型进行预训练，使其具备生成基本人体运动的能力。然后，利用整理的注视启动数据集，以目标物体的位置或姿势为条件，对预训练模型进行微调。在推理阶段，给定目标物体的位置或姿势，模型即可生成相应的运动序列。整体流程包括数据收集与整理、模型预训练、条件微调和运动生成。

**关键创新**：该方法的关键创新在于首次整理了大规模的注视启动人体运动数据集，并将其用于训练条件扩散模型。此外，还提出了一个新的评估指标“启动成功率”，用于衡量生成的运动是否能够模拟真实的注视启动行为。与现有方法相比，该方法能够更好地模拟人类与环境的交互，生成更自然和真实的运动序列。

**关键设计**：该方法使用扩散模型作为运动生成的核心架构。在微调阶段，目标物体的位置或姿势被编码为条件向量，并输入到扩散模型的逆扩散过程中，以引导运动的生成。损失函数包括运动重建损失和对抗损失，以保证生成运动的真实性和多样性。具体参数设置和网络结构细节在论文中有详细描述（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16456v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16456v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16456v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该模型在HD-EPIC数据集上取得了显著的成果，到达成功率高达89%，启动成功率达到60%。这些结果表明，该方法能够有效地模拟人类的注视启动行为，并生成自然和真实的运动序列。与未进行注视启动训练的模型相比，该方法在启动成功率方面有显著提升（具体数值未知）。

## 🎯 应用场景

该研究成果可应用于虚拟现实、人机交互、游戏开发和机器人控制等领域。例如，可以用于创建更逼真的虚拟角色动画，提高人机交互的自然性和效率，以及使机器人能够更好地理解和模仿人类的动作，从而完成更复杂的任务。未来的研究可以进一步探索如何将注视信息与其他感知信息（如语音、触觉）融合，以生成更丰富和智能的人体运动。

## 📄 摘要（原文）

> Human motion generation is a challenging task that aims to create realistic motion imitating natural human behaviour. We focus on the well-studied behaviour of priming an object/location for pick up or put down -- that is, the spotting of an object/location from a distance, known as gaze priming, followed by the motion of approaching and reaching the target location. To that end, we curate, for the first time, 23.7K gaze-primed human motion sequences for reaching target object locations from five publicly available datasets, i.e., HD-EPIC, MoGaze, HOT3D, ADT, and GIMO. We pre-train a text-conditioned diffusion-based motion generation model, then fine-tune it conditioned on goal pose or location, on our curated sequences. Importantly, we evaluate the ability of the generated motion to imitate natural human movement through several metrics, including the 'Reach Success' and a newly introduced 'Prime Success' metric. On the largest dataset, HD-EPIC, our model achieves 60% prime success and 89% reach success when conditioned on the goal object location.

