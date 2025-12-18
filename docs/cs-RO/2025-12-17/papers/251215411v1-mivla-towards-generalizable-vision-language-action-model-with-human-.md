---
layout: default
title: MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training
---

# MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15411" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15411v1</a>
  <a href="https://arxiv.org/pdf/2512.15411.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15411v1" onclick="toggleFavorite(this, '2512.15411v1', 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenhan Yin, Xuanhan Wang, Jiahao Jiang, Kaiyuan Deng, Pengqi Chen, Shuangle Li, Chong Liu, Xing Xu, ingkuan Song, Lianli Gao, Heng Tao Shen

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**MiVLA：基于人-机互模仿预训练的通用视觉-语言-动作模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `机器人控制` `互模仿学习` `预训练` `泛化能力` `人机协作` `行为预测`

## 📋 核心要点

1. 现有VLA模型在泛化能力上存在不足，主要原因是人类视频和模拟机器人数据之间存在视角、外观和形态上的差异。
2. MiVLA的核心思想是利用人手和机器人手臂的行为相似性，通过互模仿预训练，学习通用的行为先验知识。
3. 实验结果表明，MiVLA在模拟和真实机器人控制任务中，泛化能力显著优于现有VLA模型，提升幅度分别达到25%和14%。

## 📝 摘要（中文）

现有视觉-语言-动作模型(VLA)在利用大量人类视频和模拟机器人数据时，其泛化能力受到相机视角、视觉外观和机器人形态差异的限制。为了克服这一限制，我们提出了MiVLA，一种通过人-机互模仿预训练增强的通用VLA。MiVLA利用人类手部和机器人手臂之间固有的行为相似性，为人类动作和机器人控制构建强大的行为先验基础。具体而言，我们的方法利用运动学规则和左右手坐标系，实现人与机器人动作空间之间的双向对齐。给定人类或模拟机器人演示，MiVLA被训练来预测一种形态的行为轨迹，并模仿另一种在演示中未见过的形态的行为。基于这种互模仿，它将真实世界人类数据的行为保真度与模拟机器人数据的操作多样性集成到一个统一的模型中，从而增强了下游任务的泛化能力。在模拟和真实平台上的大量实验表明，MiVLA实现了显著提高的泛化能力，在模拟中优于最先进的VLA（例如$oldsymbolπ_{0}$，$oldsymbolπ_{0.5}$和H-RDT）25％，在真实机器人控制任务中优于14％。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作模型(VLA)在机器人控制任务中，面临着泛化能力不足的问题。主要原因是训练数据（通常是人类视频或模拟数据）与真实机器人环境存在差异，包括相机视角、视觉外观和机器人形态等。现有方法难以有效弥合这些差异，导致模型在真实机器人上的表现不佳。

**核心思路**：MiVLA的核心思路是利用人类手部动作和机器人手臂动作之间的内在相似性，通过互模仿学习，让模型同时学习人类和机器人的行为模式。通过这种方式，模型可以更好地理解不同形态之间的行为映射关系，从而提高泛化能力。

**技术框架**：MiVLA的整体框架包括以下几个主要模块：1) 数据收集模块：收集人类视频数据和模拟机器人数据。2) 动作空间对齐模块：利用运动学规则和左右手坐标系，将人类和机器人的动作空间进行对齐。3) 互模仿学习模块：训练模型预测一种形态的行为轨迹，并模仿另一种形态的行为。4) 下游任务微调模块：将预训练好的模型在具体的机器人控制任务上进行微调。

**关键创新**：MiVLA最重要的创新点在于提出了人-机互模仿预训练方法。与传统的单向模仿学习不同，MiVLA通过双向的模仿学习，让模型同时学习人类和机器人的行为模式，从而更好地理解不同形态之间的行为映射关系。这种互模仿学习的方式可以有效地提高模型的泛化能力。

**关键设计**：在动作空间对齐方面，MiVLA利用了运动学规则和左右手坐标系，将人类手部的动作转换为机器人手臂的动作。在互模仿学习方面，MiVLA使用了Transformer网络来预测行为轨迹，并设计了相应的损失函数来鼓励模型学习人类和机器人的行为模式。具体的损失函数包括行为预测损失、模仿学习损失和正则化损失等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15411v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15411v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15411v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MiVLA在模拟和真实机器人控制任务中都取得了显著的性能提升。在模拟环境中，MiVLA的性能优于最先进的VLA模型（例如$oldsymbolπ_{0}$，$oldsymbolπ_{0.5}$和H-RDT）25％。在真实机器人控制任务中，MiVLA的性能优于现有方法14％。这些实验结果表明，MiVLA具有很强的泛化能力和实用价值。

## 🎯 应用场景

MiVLA具有广泛的应用前景，可以应用于各种机器人控制任务，例如家庭服务机器人、工业机器人和医疗机器人等。通过学习人类的行为模式，机器人可以更好地理解人类的意图，从而更安全、更有效地完成任务。此外，MiVLA还可以用于机器人技能学习，帮助机器人快速掌握新的技能。

## 📄 摘要（原文）

> While leveraging abundant human videos and simulated robot data poses a scalable solution to the scarcity of real-world robot data, the generalization capability of existing vision-language-action models (VLAs) remains limited by mismatches in camera views, visual appearance, and embodiment morphologies. To overcome this limitation, we propose MiVLA, a generalizable VLA empowered by human-robot mutual imitation pre-training, which leverages inherent behavioral similarity between human hands and robotic arms to build a foundation of strong behavioral priors for both human actions and robotic control. Specifically, our method utilizes kinematic rules with left/right hand coordinate systems for bidirectional alignment between human and robot action spaces. Given human or simulated robot demonstrations, MiVLA is trained to forecast behavior trajectories for one embodiment, and imitate behaviors for another one unseen in the demonstration. Based on this mutual imitation, it integrates the behavioral fidelity of real-world human data with the manipulative diversity of simulated robot data into a unified model, thereby enhancing the generalization capability for downstream tasks. Extensive experiments conducted on both simulation and real-world platforms with three robots (ARX, PiPer and LocoMan), demonstrate that MiVLA achieves strong improved generalization capability, outperforming state-of-the-art VLAs (e.g., $\boldsymbolπ_{0}$, $\boldsymbolπ_{0.5}$ and H-RDT) by 25% in simulation, and 14% in real-world robot control tasks.

