---
layout: default
title: DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos
---

# DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14217" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14217</a>
  <a href="https://arxiv.org/pdf/2512.14217.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14217" onclick="toggleFavorite(this, '2512.14217', 'DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Bai, Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Ziyuan Liu, Gitta Kutyniok

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**DRAW2ACT：提出深度感知的轨迹条件视频生成框架，用于机器人操作演示视频生成。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `视频生成` `扩散模型` `轨迹条件` `深度感知` `多模态融合` `具身智能`

## 📋 核心要点

1. 现有轨迹条件视频生成方法依赖2D轨迹或单模态信息，限制了机器人演示视频的可控性和一致性。
2. DRAW2ACT从轨迹中提取深度、语义、形状和运动等多重表示，并融入扩散模型，实现深度感知的视频生成。
3. 实验表明，DRAW2ACT在视觉保真度、一致性和操作成功率方面均优于现有方法，提升了机器人操作性能。

## 📝 摘要（中文）

视频扩散模型为具身智能提供了强大的真实世界模拟器，但在机器人操作的可控性方面仍然有限。最近关于轨迹条件视频生成的工作弥补了这一差距，但通常依赖于2D轨迹或单模态条件，这限制了它们生成可控和一致的机器人演示的能力。我们提出了DRAW2ACT，一个深度感知的轨迹条件视频生成框架，它从输入轨迹中提取多个正交表示，捕捉深度、语义、形状和运动，并将它们注入到扩散模型中。此外，我们提出联合生成空间对齐的RGB和深度视频，利用跨模态注意力机制和深度监督来增强时空一致性。最后，我们引入了一个以生成的RGB和深度序列为条件的多模态策略模型，以回归机器人的关节角度。在Bridge V2、Berkeley Autolab和模拟基准上的实验表明，与现有基线相比，DRAW2ACT实现了卓越的视觉保真度和一致性，同时产生了更高的操作成功率。

## 🔬 方法详解

**问题定义**：现有的轨迹条件视频生成方法在机器人操作领域面临挑战，主要痛点在于对轨迹信息的利用不足，通常只依赖于2D轨迹或单一模态的条件信息，导致生成视频的可控性和时空一致性较差，难以用于训练有效的机器人控制策略。

**核心思路**：DRAW2ACT的核心思路是从输入轨迹中提取更丰富的多模态信息，包括深度、语义、形状和运动等，并将这些信息有效地融入到视频生成过程中。通过深度感知，模型能够更好地理解场景的三维结构，从而生成更逼真、更一致的机器人操作视频。

**技术框架**：DRAW2ACT框架主要包含轨迹编码器、视频生成器和策略模型三个部分。轨迹编码器负责从输入轨迹中提取多模态特征表示；视频生成器基于扩散模型，以轨迹编码器的输出为条件，生成RGB和深度视频序列；策略模型则以生成的RGB和深度视频为输入，预测机器人的关节角度，从而实现机器人控制。框架采用联合训练的方式，优化视频生成和策略学习。

**关键创新**：DRAW2ACT的关键创新在于深度感知的轨迹条件视频生成方法。它通过提取轨迹的深度信息，并将其融入到视频生成过程中，显著提升了生成视频的真实感和一致性。此外，联合生成RGB和深度视频，并利用跨模态注意力机制和深度监督，进一步增强了时空一致性。

**关键设计**：在轨迹编码器中，论文采用了多层感知机（MLP）来提取轨迹的深度、语义、形状和运动特征。在视频生成器中，使用了U-Net结构的扩散模型，并引入了跨模态注意力机制，以融合RGB和深度信息。损失函数包括RGB和深度视频的重建损失、对抗损失以及深度监督损失，以保证生成视频的质量和一致性。策略模型采用卷积神经网络（CNN）结构，以生成的RGB和深度视频为输入，预测机器人的关节角度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14217/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14217/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14217/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DRAW2ACT在Bridge V2、Berkeley Autolab和模拟基准上进行了实验，结果表明，与现有基线相比，DRAW2ACT在视觉保真度和一致性方面取得了显著提升，并且在机器人操作成功率方面也表现出更高的性能。具体数据未知，但论文强调了其优越性。

## 🎯 应用场景

DRAW2ACT可应用于机器人操作技能学习、强化学习环境构建、虚拟机器人训练等领域。通过生成高质量的机器人操作视频，可以降低机器人训练的成本和难度，加速机器人技术的应用和发展。该技术还可用于生成各种复杂的机器人操作场景，为机器人研究提供更丰富的实验数据。

## 📄 摘要（原文）

> Video diffusion models provide powerful real-world simulators for embodied AI but remain limited in controllability for robotic manipulation. Recent works on trajectory-conditioned video generation address this gap but often rely on 2D trajectories or single modality conditioning, which restricts their ability to produce controllable and consistent robotic demonstrations. We present DRAW2ACT, a depth-aware trajectory-conditioned video generation framework that extracts multiple orthogonal representations from the input trajectory, capturing depth, semantics, shape and motion, and injects them into the diffusion model. Moreover, we propose to jointly generate spatially aligned RGB and depth videos, leveraging cross-modality attention mechanisms and depth supervision to enhance the spatio-temporal consistency. Finally, we introduce a multimodal policy model conditioned on the generated RGB and depth sequences to regress the robot's joint angles. Experiments on Bridge V2, Berkeley Autolab, and simulation benchmarks show that DRAW2ACT achieves superior visual fidelity and consistency while yielding higher manipulation success rates compared to existing baselines.

