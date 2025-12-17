---
layout: default
title: Motus: A Unified Latent Action World Model
---

# Motus: A Unified Latent Action World Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13030" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13030v1</a>
  <a href="https://arxiv.org/pdf/2512.13030.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13030v1" onclick="toggleFavorite(this, '2512.13030v1', 'Motus: A Unified Latent Action World Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongzhe Bi, Hengkai Tan, Shenghao Xie, Zeyuan Wang, Shuhe Huang, Haitian Liu, Ruowen Zhao, Yao Feng, Chendong Xiang, Yinze Rong, Hongyan Zhao, Hanyu Liu, Zhizhong Su, Lei Ma, Hang Su, Jun Zhu

**分类**: cs.CV, cs.LG, cs.RO

**发布日期**: 2025-12-15

---

## 💡 一句话要点

**提出Motus以解决多模态生成能力统一问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多模态生成` `机器人控制` `混合变换器` `光流学习` `统一建模` `动作预训练` `视频生成` `智能体系统`

## 📋 核心要点

1. 现有方法在理解、世界建模和控制方面存在碎片化，限制了多模态生成能力的统一。
2. Motus通过混合变换器架构整合多个专家，并采用灵活的调度器，实现不同建模模式的切换。
3. 实验表明，Motus在仿真中相较于X-VLA提升15%，相较于Pi0.5提升45%，在现实场景中提升11%至48%。

## 📝 摘要（中文）

在当前的智能体研究中，理解、世界建模和控制方法往往是孤立的，这种碎片化阻碍了多模态生成能力的统一和从大规模异构数据中学习。本文提出了Motus，一个统一的潜在动作世界模型，利用现有的通用预训练模型和丰富的可共享运动信息。Motus引入了混合变换器（MoT）架构，整合理解、视频生成和动作三个专家，并采用UniDiffuser风格的调度器，实现不同建模模式之间的灵活切换。通过光流学习潜在动作，Motus采用三阶段训练流程和六层数据金字塔，提取像素级“增量动作”，实现大规模动作预训练。实验结果表明，Motus在仿真和现实场景中均优于现有最先进方法，显著提升了机器人任务的性能。

## 🔬 方法详解

**问题定义**：当前的智能体方法往往是孤立的，导致理解、世界建模和控制之间缺乏有效的整合，限制了多模态生成能力的发挥。

**核心思路**：Motus通过引入混合变换器架构，将理解、视频生成和动作三个专家整合为一个统一的系统，利用丰富的运动信息和现有的预训练模型，提升模型的学习能力和生成能力。

**技术框架**：Motus的整体架构包括三个主要模块：理解模块、视频生成模块和动作模块。通过UniDiffuser风格的调度器，模型可以在不同的建模模式之间灵活切换，适应不同的任务需求。

**关键创新**：Motus的核心创新在于其混合变换器架构和三阶段训练流程，能够有效整合多种功能和先验知识，显著提升模型的整体性能。

**关键设计**：Motus采用六层数据金字塔结构，提取像素级“增量动作”，并通过光流学习潜在动作，设计了适应不同任务的损失函数和网络结构，确保模型的高效训练和性能提升。

## 📊 实验亮点

Motus在实验中表现出色，在仿真环境中相较于X-VLA提升了15%，相较于Pi0.5提升了45%。在真实场景中，性能提升幅度在11%至48%之间，展示了其在机器人任务中的显著优势。

## 🎯 应用场景

Motus的研究成果在多个领域具有潜在应用价值，包括机器人控制、自动驾驶、虚拟现实等。通过统一的多模态生成能力，Motus能够提升智能体在复杂环境中的决策和执行能力，推动智能系统的进一步发展。

## 📄 摘要（原文）

> While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios(improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

