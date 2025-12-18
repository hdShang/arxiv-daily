---
layout: default
title: ReCAD: Reinforcement Learning Enhanced Parametric CAD Model Generation with Vision-Language Models
---

# ReCAD: Reinforcement Learning Enhanced Parametric CAD Model Generation with Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.06328" class="toolbar-btn" target="_blank">📄 arXiv: 2512.06328v1</a>
  <a href="https://arxiv.org/pdf/2512.06328.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06328v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.06328v1', 'ReCAD: Reinforcement Learning Enhanced Parametric CAD Model Generation with Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Li, Yusheng Luo, Yunzhong Lou, Xiangdong Zhou

**分类**: cs.CV

**发布日期**: 2025-12-06

**备注**: Accepted as an Oral presentation at AAAI 2026

---

## 💡 一句话要点

**ReCAD：利用强化学习增强的参数化CAD模型生成，结合视觉-语言模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `CAD模型生成` `强化学习` `视觉-语言模型` `参数化建模` `分层基元学习`

## 📋 核心要点

1. 现有CAD模型生成方法依赖监督微调，可编辑性差，未能充分利用预训练模型的生成能力。
2. ReCAD框架利用强化学习，结合参数化代码指导，增强模型推理能力，并采用分层基元学习。
3. 实验表明，ReCAD在文本到CAD和图像到CAD任务中显著提升了几何精度，优于现有方法。

## 📝 摘要（中文）

本文提出ReCAD，一个强化学习（RL）框架，它利用预训练大型模型（PLM）的固有生成能力，从多模态输入生成精确的参数化计算机辅助设计（CAD）模型。我们的方法仅需简单的功能接口（例如，点坐标），即可实现复杂的CAD操作（例如，图案复制和镜像）。这与以往的方法形成对比，以往的方法通常依赖于通过监督微调（SFT）注入的知识，对可编辑性的支持有限，并且未能利用PLM强大的生成先验。具体来说，ReCAD框架首先微调视觉-语言模型（VLM），使其具备基本的CAD模型生成能力，我们将CAD脚本重写为参数化代码，用于生成精确的文本描述以进行监督。然后，我们提出了一种新颖的RL策略，该策略结合参数化代码作为指导，以增强模型对具有挑战性问题的推理能力。此外，我们采用分层基元学习过程，在统一的奖励函数下逐步教授结构化和组合技能，该奖励函数可确保几何精度和语义保真度。ReCAD在文本到CAD和图像到CAD任务中均创下了新的技术水平，显着提高了分布内和分布外设置中的几何精度。例如，在图像到CAD任务中，它将平均Chamfer距离从73.47降低到29.61（分布内），从272.06降低到80.23（分布外），大大优于现有的基线。

## 🔬 方法详解

**问题定义**：论文旨在解决从多模态输入（文本或图像）精确生成参数化CAD模型的问题。现有方法主要依赖于监督微调，需要大量标注数据，且可编辑性较差，难以充分利用预训练视觉-语言模型（VLM）的强大生成能力。这些方法在处理复杂CAD操作（如图案复制和镜像）时也存在局限性。

**核心思路**：ReCAD的核心思路是利用强化学习（RL）来引导预训练的VLM生成CAD模型。通过将CAD脚本转换为参数化代码，并将其作为RL的指导信号，可以有效地利用VLM的生成先验知识，并学习复杂的CAD操作。此外，分层基元学习过程允许模型逐步学习结构化和组合技能，从而提高生成模型的几何精度和语义保真度。

**技术框架**：ReCAD框架包含以下主要阶段：1) VLM微调：首先，微调VLM，使其具备基本的CAD模型生成能力。CAD脚本被重写为参数化代码，用于生成精确的文本描述，作为监督信号。2) 强化学习：利用RL策略，将参数化代码作为指导，增强模型对复杂问题的推理能力。3) 分层基元学习：采用分层学习过程，逐步教授模型结构化和组合技能。整个框架使用统一的奖励函数，确保几何精度和语义保真度。

**关键创新**：ReCAD的关键创新在于：1) 利用强化学习来引导VLM生成CAD模型，避免了对大量标注数据的依赖。2) 引入参数化代码作为RL的指导信号，有效地利用了VLM的生成先验知识。3) 采用分层基元学习过程，逐步教授模型结构化和组合技能。与现有方法相比，ReCAD能够生成更精确、可编辑性更强的CAD模型。

**关键设计**：参数化代码的设计是关键。CAD脚本被转换为包含参数的程序代码，这些参数可以被RL智能体调整，从而控制CAD模型的生成过程。奖励函数的设计也至关重要，它需要同时考虑几何精度（例如，Chamfer距离）和语义保真度，以确保生成的CAD模型既准确又符合语义要求。分层基元学习过程通过逐步增加任务的复杂性，帮助模型学习复杂的CAD操作。

## 📊 实验亮点

ReCAD在文本到CAD和图像到CAD任务中均取得了显著的性能提升。在图像到CAD任务中，ReCAD将分布内的平均Chamfer距离从73.47降低到29.61，将分布外的平均Chamfer距离从272.06降低到80.23，大幅超越了现有基线方法。这些结果表明，ReCAD能够有效地提高CAD模型的几何精度，尤其是在处理分布外数据时。

## 🎯 应用场景

ReCAD具有广泛的应用前景，包括自动化产品设计、建筑设计、工业设计等领域。它可以帮助设计师快速生成CAD模型，提高设计效率，并降低设计成本。此外，ReCAD还可以用于逆向工程，从图像或文本描述中重建CAD模型，为产品修复和改进提供支持。未来，ReCAD有望成为智能制造和数字化设计的重要工具。

## 📄 摘要（原文）

> We present ReCAD, a reinforcement learning (RL) framework that bootstraps pretrained large models (PLMs) to generate precise parametric computer-aided design (CAD) models from multimodal inputs by leveraging their inherent generative capabilities. With just access to simple functional interfaces (e.g., point coordinates), our approach enables the emergence of complex CAD operations (e.g., pattern replication and mirror). This stands in contrast to previous methods, which typically rely on knowledge injected through supervised fine-tuning (SFT), offer limited support for editability, and fail to exploit the strong generative priors of PLMs. Specifically, the ReCAD framework begins by fine-tuning vision-language models (VLMs) to equip them with basic CAD model generation capabilities, where we rewrite CAD scripts into parameterized code that is leveraged to generate accurate textual descriptions for supervision. Then, we propose a novel RL strategy that incorporates parameterized code as guidance to enhance the model's reasoning on challenging questions. Furthermore, we employ a hierarchical primitive learning process to progressively teach structured and compositional skills under a unified reward function that ensures both geometric accuracy and semantic fidelity. ReCAD sets a new state-of-the-art in both text-to-CAD and image-to-CAD tasks, significantly improving geometric accuracy across in-distribution and out-of-distribution settings. In the image-to-CAD task, for instance, it reduces the mean Chamfer Distance from 73.47 to 29.61 (in-distribution) and from 272.06 to 80.23 (out-of-distribution), outperforming existing baselines by a substantial margin.

