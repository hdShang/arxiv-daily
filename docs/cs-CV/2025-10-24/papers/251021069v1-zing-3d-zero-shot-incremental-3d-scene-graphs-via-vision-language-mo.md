---
layout: default
title: ZING-3D: Zero-shot Incremental 3D Scene Graphs via Vision-Language Models
---

# ZING-3D: Zero-shot Incremental 3D Scene Graphs via Vision-Language Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.21069" target="_blank" class="toolbar-btn">arXiv: 2510.21069v1</a>
    <a href="https://arxiv.org/pdf/2510.21069.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21069v1" 
            onclick="toggleFavorite(this, '2510.21069v1', 'ZING-3D: Zero-shot Incremental 3D Scene Graphs via Vision-Language Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Pranav Saxena, Jimmy Chiun

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-24

---

## 💡 一句话要点

**ZING-3D：利用视觉-语言模型实现零样本增量式3D场景图构建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D场景图` `视觉-语言模型` `零样本学习` `增量学习` `具身智能` `开放词汇识别` `几何定位`

## 📋 核心要点

1. 现有3D场景图生成方法主要局限于单视角，缺乏增量更新能力，且缺乏明确的3D几何定位，难以应用于具身智能任务。
2. ZING-3D利用预训练VLM的知识，以零样本方式进行开放词汇识别，并构建具有几何定位和增量更新能力的3D场景图。
3. 在Replica和HM3D数据集上的实验表明，ZING-3D能够有效捕获空间和关系知识，无需特定任务训练。

## 📝 摘要（中文）

本文提出ZING-3D框架，利用预训练的视觉-语言模型（VLM）的强大知识，以零样本方式实现开放词汇识别，并生成场景的丰富语义表示。该框架支持增量式更新和3D空间中的几何定位，适用于具身智能场景。ZING-3D利用VLM推理生成丰富的2D场景图，并使用深度信息将其定位到3D空间中。节点表示具有特征、3D位置和语义上下文的开放词汇对象，边表示具有对象间距离的空间和语义关系。在Replica和HM3D数据集上的实验表明，ZING-3D能够有效地捕获空间和关系知识，而无需特定于任务的训练。

## 🔬 方法详解

**问题定义**：现有3D场景图生成方法在具身智能场景中存在局限性。它们通常依赖于单视角数据，无法随着新观测的到来进行增量更新，并且缺乏在3D空间中的明确几何定位。这限制了它们在需要持续感知和交互的机器人应用中的应用。

**核心思路**：ZING-3D的核心思路是利用预训练的视觉-语言模型（VLM）的强大语义理解能力，结合深度信息，将2D场景图转化为具有几何信息的3D场景图。通过VLM的零样本学习能力，实现开放词汇的场景理解，并支持增量式更新，从而适应动态环境。

**技术框架**：ZING-3D框架主要包含以下几个阶段：1) 利用VLM对单视角图像进行分析，生成2D场景图，节点包含对象类别和特征，边包含对象间的语义关系；2) 利用深度信息将2D场景图中的对象定位到3D空间中，为每个节点赋予3D坐标；3) 构建3D场景图，节点表示3D对象，边表示对象间的空间和语义关系，包括距离等几何信息；4) 当新的观测数据到来时，利用VLM和深度信息对新观测进行分析，并将新对象和关系增量式地添加到现有的3D场景图中。

**关键创新**：ZING-3D的关键创新在于：1) 利用VLM进行零样本开放词汇识别，无需特定任务的训练数据；2) 将2D场景图与深度信息融合，实现3D场景图的几何定位；3) 支持增量式更新，能够适应动态变化的场景。与现有方法相比，ZING-3D更具通用性和适应性。

**关键设计**：ZING-3D的关键设计包括：1) 选择合适的VLM模型，例如CLIP等，以获得良好的语义理解能力；2) 设计有效的深度信息融合策略，将2D对象准确地定位到3D空间中；3) 设计增量式更新机制，避免重复计算和信息冗余。具体的参数设置和网络结构取决于所选的VLM模型和深度估计方法。

## 📊 实验亮点

ZING-3D在Replica和HM3D数据集上进行了实验，结果表明，该方法能够有效地捕获场景中的空间和关系知识，而无需进行特定于任务的训练。虽然论文中没有给出具体的性能指标，但强调了ZING-3D在零样本学习和增量式更新方面的优势，使其在动态环境中具有更强的适应性。

## 🎯 应用场景

ZING-3D在机器人导航、场景理解、虚拟现实等领域具有广泛的应用前景。它可以帮助机器人理解周围环境，进行自主导航和物体交互。在虚拟现实中，ZING-3D可以用于构建逼真的3D场景，并支持用户进行交互。此外，该技术还可以应用于智能家居、自动驾驶等领域，提升系统的智能化水平。

## 📄 摘要（原文）

> Understanding and reasoning about complex 3D environments requires structured scene representations that capture not only objects but also their semantic and spatial relationships. While recent works on 3D scene graph generation have leveraged pretrained VLMs without task-specific fine-tuning, they are largely confined to single-view settings, fail to support incremental updates as new observations arrive and lack explicit geometric grounding in 3D space, all of which are essential for embodied scenarios. In this paper, we propose, ZING-3D, a framework that leverages the vast knowledge of pretrained foundation models to enable open-vocabulary recognition and generate a rich semantic representation of the scene in a zero-shot manner while also enabling incremental updates and geometric grounding in 3D space, making it suitable for downstream robotics applications. Our approach leverages VLM reasoning to generate a rich 2D scene graph, which is grounded in 3D using depth information. Nodes represent open-vocabulary objects with features, 3D locations, and semantic context, while edges capture spatial and semantic relations with inter-object distances. Our experiments on scenes from the Replica and HM3D dataset show that ZING-3D is effective at capturing spatial and relational knowledge without the need of task-specific training.

