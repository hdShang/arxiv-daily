---
layout: default
title: "Flowing from Reasoning to Motion: Learning 3D Hand Trajectory Prediction from Egocentric Human Interaction Videos"
---

# Flowing from Reasoning to Motion: Learning 3D Hand Trajectory Prediction from Egocentric Human Interaction Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16907" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16907v1</a>
  <a href="https://arxiv.org/pdf/2512.16907.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16907v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16907v1', 'Flowing from Reasoning to Motion: Learning 3D Hand Trajectory Prediction from Egocentric Human Interaction Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingfei Chen, Yifan Wang, Zhengqin Li, Homanga Bharadhwaj, Yujin Chen, Chuan Qin, Ziyi Kou, Yuan Tian, Eric Whitmire, Rajinder Sodhi, Hrvoje Benko, Eli Shlizerman, Yue Liu

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-12-18

**备注**: Project website: https://egoman-project.github.io

---

## 💡 一句话要点

**EgoMAN：基于自中心交互视频学习3D手部轨迹预测，实现推理到运动的衔接**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `3D手部轨迹预测` `自中心视频` `人机交互` `视觉语言推理` `运动生成`

## 📋 核心要点

1. 现有3D手部轨迹预测方法缺乏语义信息的有效利用，限制了预测的准确性和泛化能力。
2. EgoMAN模型通过轨迹-token接口，将视觉-语言推理与运动生成相结合，实现了推理到运动的有效衔接。
3. EgoMAN数据集和模型在真实场景中表现出良好的泛化能力，能够生成准确且阶段感知的轨迹。

## 📝 摘要（中文）

本文提出了一种基于自中心人类交互视频的3D手部轨迹预测方法。现有方法受限于缺乏语义监督的数据集以及推理和动作之间弱连接的模型。为了解决这些问题，我们首先提出了EgoMAN数据集，这是一个大规模的自中心数据集，用于交互阶段感知的3D手部轨迹预测，包含21.9万个6DoF轨迹和300万个结构化的QA对，用于语义、空间和运动推理。然后，我们介绍了EgoMAN模型，这是一个推理到运动的框架，通过轨迹-token接口连接视觉-语言推理和运动生成。通过逐步训练以使推理与运动动力学对齐，我们的方法产生了准确且阶段感知的轨迹，并在真实场景中具有泛化能力。

## 🔬 方法详解

**问题定义**：现有3D手部轨迹预测方法主要面临两个挑战：一是数据集的限制，现有数据集通常将运动与语义监督分离，缺乏丰富的交互信息；二是模型设计上的不足，现有模型通常难以有效地将推理过程与动作生成联系起来，导致预测结果不够准确和自然。

**核心思路**：本文的核心思路是通过构建一个大规模的自中心交互数据集EgoMAN，并设计一个推理到运动的框架EgoMAN模型，从而实现更准确和自然的3D手部轨迹预测。EgoMAN数据集提供了丰富的语义、空间和运动推理信息，EgoMAN模型则通过轨迹-token接口将视觉-语言推理与运动生成相结合。

**技术框架**：EgoMAN模型是一个推理到运动的框架，主要包含以下几个模块：首先，利用视觉和语言信息进行推理，提取场景的语义信息和交互意图；然后，将推理结果编码成轨迹-token，作为运动生成模块的输入；最后，运动生成模块根据轨迹-token生成3D手部轨迹。整个框架通过逐步训练，使推理与运动动力学对齐。

**关键创新**：本文的关键创新在于：1) 提出了EgoMAN数据集，这是一个大规模的自中心交互数据集，包含丰富的语义、空间和运动推理信息；2) 设计了EgoMAN模型，这是一个推理到运动的框架，通过轨迹-token接口将视觉-语言推理与运动生成相结合，实现了推理和动作之间的有效衔接。

**关键设计**：EgoMAN模型中的轨迹-token接口是关键设计之一，它将推理结果编码成一种紧凑的表示，作为运动生成模块的输入。此外，模型还采用了逐步训练的策略，通过逐步对齐推理和运动动力学，提高预测的准确性和自然性。具体的损失函数和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16907v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16907v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16907v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EgoMAN模型在EgoMAN数据集上取得了显著的性能提升。实验结果表明，该模型能够生成准确且阶段感知的轨迹，并在真实场景中具有良好的泛化能力。具体的性能数据和对比基线在论文中有详细描述，证明了EgoMAN数据集和模型的有效性。

## 🎯 应用场景

该研究成果可应用于人机交互、机器人控制、虚拟现实和增强现实等领域。例如，在机器人控制中，可以利用该模型预测人的手部运动轨迹，从而使机器人能够更好地理解人的意图并做出相应的动作。在虚拟现实和增强现实中，可以利用该模型生成更逼真的手部动画，提高用户的沉浸感。

## 📄 摘要（原文）

> Prior works on 3D hand trajectory prediction are constrained by datasets that decouple motion from semantic supervision and by models that weakly link reasoning and action. To address these, we first present the EgoMAN dataset, a large-scale egocentric dataset for interaction stage-aware 3D hand trajectory prediction with 219K 6DoF trajectories and 3M structured QA pairs for semantic, spatial, and motion reasoning. We then introduce the EgoMAN model, a reasoning-to-motion framework that links vision-language reasoning and motion generation via a trajectory-token interface. Trained progressively to align reasoning with motion dynamics, our approach yields accurate and stage-aware trajectories with generalization across real-world scenes.

