---
layout: default
title: "MesaTask: Towards Task-Driven Tabletop Scene Generation via 3D Spatial Reasoning"
---

# MesaTask: Towards Task-Driven Tabletop Scene Generation via 3D Spatial Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22281" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22281v1</a>
  <a href="https://arxiv.org/pdf/2509.22281.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22281v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22281v1', 'MesaTask: Towards Task-Driven Tabletop Scene Generation via 3D Spatial Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinkun Hao, Naifu Liang, Zhen Luo, Xudong Xu, Weipeng Zhong, Ran Yi, Yichen Jin, Zhaoyang Lyu, Feng Zheng, Lizhuang Ma, Jiangmiao Pang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-26

**备注**: Accepted by NeurIPS 2025; Project page: https://mesatask.github.io/

---

## 💡 一句话要点

**MesaTask：提出基于3D空间推理的任务驱动型桌面场景生成框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `桌面场景生成` `任务驱动` `3D空间推理` `大型语言模型` `机器人操作`

## 📋 核心要点

1. 现有桌面场景生成方法依赖于耗时的人工设计或纯随机布局，难以保证场景的合理性以及与任务的对齐。
2. 论文提出空间推理链，将场景生成分解为对象推理、空间关系推理和场景图构建，从而弥合任务指令和场景之间的差距。
3. 实验表明，MesaTask框架能够生成与任务描述对齐且物理上合理的桌面场景，性能优于现有基线方法。

## 📝 摘要（中文）

本文提出了一种新的任务：面向任务的桌面场景生成，旨在解决高层任务指令与桌面场景之间的巨大差距。为了支持该任务的研究，作者构建了一个大规模数据集MesaTask-10K，包含约10700个合成桌面场景，这些场景具有人工设计的布局，确保了布局的真实性和复杂的对象间关系。为了弥合任务和场景之间的差距，作者提出了一种空间推理链，将生成过程分解为对象推理、空间关系推理和场景图构建，最终生成3D布局。作者提出了一个基于LLM的框架MesaTask，该框架利用此推理链，并通过DPO算法进一步增强，以生成与给定任务描述对齐的、物理上合理的桌面场景。实验结果表明，与基线方法相比，MesaTask在生成符合任务的、具有真实布局的桌面场景方面表现出优越的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决任务驱动的桌面场景生成问题。现有方法，如人工设计或纯随机布局，无法有效生成既真实又与特定任务相关的场景。人工设计成本高昂，随机布局则缺乏合理性和任务相关性。因此，如何根据高层任务指令自动生成逼真的桌面场景是一个挑战。

**核心思路**：论文的核心思路是将场景生成过程分解为多个可控的步骤，通过空间推理链逐步构建场景。首先进行对象推理，确定场景中应包含哪些对象；然后进行空间关系推理，确定对象之间的相对位置和姿态；最后构建场景图，将对象及其关系整合为一个完整的场景。这种分解方法使得可以更好地控制场景的生成过程，并确保生成的场景与任务相关且物理上合理。

**技术框架**：MesaTask框架主要包含以下几个模块：1) 对象推理模块：根据任务描述，推断场景中需要包含哪些对象。2) 空间关系推理模块：基于对象推理的结果，推理对象之间的空间关系，例如相对位置、姿态等。3) 场景图构建模块：将对象及其空间关系整合为一个场景图，用于表示完整的3D场景布局。4) 3D布局生成模块：根据场景图生成最终的3D场景布局。框架使用LLM作为基础模型，并使用DPO算法进行微调，以提高生成场景的质量和任务相关性。

**关键创新**：论文的关键创新在于提出了空间推理链，将复杂的场景生成任务分解为多个可控的步骤。这种分解方法使得可以更好地利用LLM的推理能力，并确保生成的场景与任务相关且物理上合理。此外，论文还构建了一个大规模数据集MesaTask-10K，为该领域的研究提供了重要的数据支持。

**关键设计**：论文使用LLM作为基础模型，并使用DPO算法进行微调。DPO算法的目标是最大化生成场景与任务描述之间的对齐程度，同时最小化生成场景的不合理性。在空间关系推理模块中，论文使用了一组预定义的空间关系模板，例如“在...之上”、“在...旁边”等，用于描述对象之间的相对位置和姿态。这些模板可以帮助LLM更好地理解对象之间的空间关系，并生成更合理的场景布局。

## 📊 实验亮点

MesaTask框架在任务驱动的桌面场景生成任务上取得了显著的性能提升。通过与基线方法进行对比，MesaTask能够生成更符合任务描述、更具真实感的场景。实验结果表明，MesaTask在场景的合理性和任务相关性方面均优于现有方法，为机器人操作技能的学习和训练提供了更有效的场景生成方案。

## 🎯 应用场景

该研究成果可应用于机器人操作技能的学习和训练。通过自动生成各种任务相关的桌面场景，可以为机器人提供丰富的训练数据，提高其在真实世界中的操作能力。此外，该技术还可以应用于虚拟环境的创建、游戏开发等领域，例如快速生成符合特定任务或故事情节的场景。

## 📄 摘要（原文）

> The ability of robots to interpret human instructions and execute manipulation tasks necessitates the availability of task-relevant tabletop scenes for training. However, traditional methods for creating these scenes rely on time-consuming manual layout design or purely randomized layouts, which are limited in terms of plausibility or alignment with the tasks. In this paper, we formulate a novel task, namely task-oriented tabletop scene generation, which poses significant challenges due to the substantial gap between high-level task instructions and the tabletop scenes. To support research on such a challenging task, we introduce MesaTask-10K, a large-scale dataset comprising approximately 10,700 synthetic tabletop scenes with manually crafted layouts that ensure realistic layouts and intricate inter-object relations. To bridge the gap between tasks and scenes, we propose a Spatial Reasoning Chain that decomposes the generation process into object inference, spatial interrelation reasoning, and scene graph construction for the final 3D layout. We present MesaTask, an LLM-based framework that utilizes this reasoning chain and is further enhanced with DPO algorithms to generate physically plausible tabletop scenes that align well with given task descriptions. Exhaustive experiments demonstrate the superior performance of MesaTask compared to baselines in generating task-conforming tabletop scenes with realistic layouts. Project page is at https://mesatask.github.io/

