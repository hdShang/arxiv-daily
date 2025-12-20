---
layout: default
title: Flowing from Reasoning to Motion: Learning 3D Hand Trajectory Prediction from Egocentric Human Interaction Videos
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

**EgoMAN：基于自中心交互视频，学习3D手部轨迹预测，实现从推理到运动的生成**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `3D手部轨迹预测` `自中心视角` `人机交互` `视觉语言推理` `运动生成`

## 📋 核心要点

1. 现有3D手部轨迹预测方法缺乏语义信息的有效利用，且推理与动作生成之间联系薄弱。
2. EgoMAN模型通过轨迹-token接口，将视觉-语言推理与运动生成连接，实现从推理到运动的轨迹预测。
3. EgoMAN数据集和模型的结合，实现了准确且具有阶段感知的3D手部轨迹预测，并具备良好的泛化性。

## 📝 摘要（中文）

本文提出了一种基于自中心视角的交互场景下，进行阶段感知的3D手部轨迹预测方法。为了解决现有方法缺乏语义监督以及推理与动作弱连接的问题，作者首先构建了EgoMAN数据集，这是一个大规模的自中心数据集，包含21.9万条6DoF轨迹和300万个结构化的问答对，用于语义、空间和运动推理。然后，作者提出了EgoMAN模型，这是一个推理到运动的框架，通过轨迹-token接口连接视觉-语言推理和运动生成。该方法通过逐步训练，使推理与运动动态对齐，从而生成准确且具有阶段感知的轨迹，并具有跨真实世界场景的泛化能力。

## 🔬 方法详解

**问题定义**：现有3D手部轨迹预测方法主要面临两个挑战：一是数据集层面，缺乏与语义信息强关联的大规模数据集；二是模型层面，推理（reasoning）过程与动作生成（motion generation）过程联系不够紧密，导致预测精度和泛化能力受限。现有数据集通常将运动与语义监督解耦，模型也难以有效利用语义信息指导运动生成。

**核心思路**：本文的核心思路是通过构建一个大规模的、包含丰富语义信息的数据集（EgoMAN），并设计一个能够有效连接视觉-语言推理和运动生成的模型（EgoMAN模型），从而实现从推理到运动的3D手部轨迹预测。通过显式地将推理过程与运动生成过程联系起来，模型可以更好地理解场景语义，并生成更准确、更自然的轨迹。

**技术框架**：EgoMAN模型的整体框架是一个推理到运动的流程。首先，利用视觉和语言信息进行推理，提取场景的语义信息和运动意图。然后，通过一个轨迹-token接口，将推理结果转换为运动生成的输入。最后，利用运动生成模块，生成3D手部轨迹。整个框架通过逐步训练的方式，使推理过程与运动动态对齐，从而提高预测精度和泛化能力。

**关键创新**：本文的关键创新在于以下两点：一是EgoMAN数据集的构建，该数据集包含大量的6DoF手部轨迹和结构化的问答对，为模型提供了丰富的语义信息和运动监督信号；二是EgoMAN模型的提出，该模型通过轨迹-token接口，将视觉-语言推理与运动生成连接起来，实现了从推理到运动的轨迹预测。这种推理到运动的框架能够更好地利用场景语义信息，并生成更准确、更自然的轨迹。

**关键设计**：EgoMAN模型中的轨迹-token接口是关键设计之一，它将推理结果转换为一系列轨迹token，这些token包含了运动的起始位置、方向、速度等信息。运动生成模块利用这些token作为输入，生成最终的3D手部轨迹。此外，模型还采用了逐步训练的策略，首先训练推理模块，然后训练运动生成模块，最后将两个模块联合训练，从而使推理过程与运动动态对齐。

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

EgoMAN数据集包含21.9万条6DoF轨迹和300万个结构化的问答对，是目前最大的自中心手部轨迹预测数据集之一。EgoMAN模型在EgoMAN数据集上取得了显著的性能提升，相较于现有方法，在轨迹预测精度和阶段感知能力方面均有明显优势。实验结果表明，该模型具有良好的泛化能力，可以应用于不同的真实世界场景。

## 🎯 应用场景

该研究成果可应用于人机交互、机器人操作、虚拟现实/增强现实等领域。例如，机器人可以根据人类的意图预测其手部运动轨迹，从而更好地辅助人类完成任务。在VR/AR中，可以根据用户与虚拟环境的交互，预测用户的手部运动，从而提供更自然、更沉浸式的体验。该研究的未来影响在于提升人机交互的智能化和自然化水平。

## 📄 摘要（原文）

> Prior works on 3D hand trajectory prediction are constrained by datasets that decouple motion from semantic supervision and by models that weakly link reasoning and action. To address these, we first present the EgoMAN dataset, a large-scale egocentric dataset for interaction stage-aware 3D hand trajectory prediction with 219K 6DoF trajectories and 3M structured QA pairs for semantic, spatial, and motion reasoning. We then introduce the EgoMAN model, a reasoning-to-motion framework that links vision-language reasoning and motion generation via a trajectory-token interface. Trained progressively to align reasoning with motion dynamics, our approach yields accurate and stage-aware trajectories with generalization across real-world scenes.

