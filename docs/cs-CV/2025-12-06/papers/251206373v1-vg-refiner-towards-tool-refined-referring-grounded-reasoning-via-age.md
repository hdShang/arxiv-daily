---
layout: default
title: VG-Refiner: Towards Tool-Refined Referring Grounded Reasoning via Agentic Reinforcement Learning
---

# VG-Refiner: Towards Tool-Refined Referring Grounded Reasoning via Agentic Reinforcement Learning

**arXiv**: [2512.06373v1](https://arxiv.org/abs/2512.06373) | [PDF](https://arxiv.org/pdf/2512.06373.pdf)

**作者**: Yuji Wang, Wenlong Liu, Jingxuan Niu, Haoji Zhang, Yansong Tang

**分类**: cs.CV

**发布日期**: 2025-12-06

**备注**: The project page is [this url](https://github.com/VoyageWang/VG-Refiner)

---

## 💡 一句话要点

**提出VG-Refiner，通过Agent强化学习优化工具反馈，提升指代 grounding 推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `指代 grounding` `视觉推理` `工具集成` `强化学习` `反馈优化`

## 📋 核心要点

1. 现有工具集成视觉推理方法忽略了对不可靠工具输出的有效响应，导致指代 grounding 任务中出现幻觉推理。
2. VG-Refiner 引入“思考-反思”机制，显式分析工具反馈并进行纠正，同时设计精炼奖励鼓励有效修正。
3. 实验表明，VG-Refiner 在指代和推理 grounding 基准测试中显著提升了准确性和纠正能力，并保留了预训练模型的能力。

## 📝 摘要（中文）

本文提出VG-Refiner，旨在解决工具集成视觉推理（TiVR）中，对不可靠或错误的工具输出缺乏有效响应机制的问题，尤其是在指代和 grounding 任务中，不准确的检测工具预测会导致幻觉推理。VG-Refiner是首个面向工具优化指代 grounding 推理的框架，引入了两阶段的“思考-反思”机制，使模型能够显式地分析和响应工具反馈，并设计了精炼奖励，鼓励模型根据不良工具结果进行有效纠正。此外，本文提出了两个新的评估指标，并建立了公平的评估协议，以系统地衡量当前模型的精炼能力。通过少量特定任务数据增强VG-Refiner的精炼能力，在指代和推理 grounding 基准测试中，实现了显著的准确性和纠正能力提升，同时保留了预训练模型的一般能力。

## 🔬 方法详解

**问题定义**：现有工具集成视觉推理（TiVR）方法在处理指代 grounding 任务时，容易受到不准确的检测工具预测的影响，导致模型产生幻觉推理。现有的 TiVR 范式主要关注通过强化学习集成各种视觉工具，而忽略了设计有效的响应机制来处理不可靠或错误的工具输出。

**核心思路**：VG-Refiner 的核心思路是引入一个两阶段的“思考-反思”机制，使模型能够显式地分析和响应工具的反馈。通过这种方式，模型可以识别并纠正由不准确的工具预测引起的错误，从而提高指代 grounding 推理的准确性。

**技术框架**：VG-Refiner 框架包含两个主要阶段：思考阶段和反思阶段。在思考阶段，模型首先利用视觉工具进行初步的推理和 grounding。然后，在反思阶段，模型分析工具的反馈，并根据反馈结果对推理过程进行修正。整个过程通过强化学习进行训练，目标是最大化模型的准确性和纠正能力。

**关键创新**：VG-Refiner 的关键创新在于其“思考-反思”机制和精炼奖励的设计。该机制使模型能够主动地识别和纠正工具带来的错误，而精炼奖励则鼓励模型在面对不良工具结果时进行有效的修正。与现有方法相比，VG-Refiner 更加关注工具输出的可靠性，并能够根据工具反馈进行自适应的调整。

**关键设计**：VG-Refiner 使用强化学习进行训练，其中奖励函数包括一个准确性奖励和一个精炼奖励。准确性奖励用于鼓励模型生成正确的推理结果，而精炼奖励则用于鼓励模型根据不良工具结果进行有效的修正。此外，论文还提出了两个新的评估指标，用于系统地衡量模型的精炼能力。具体网络结构和参数设置在论文中有详细描述，使用了少量特定任务数据进行微调。

## 📊 实验亮点

VG-Refiner 在指代和推理 grounding 基准测试中取得了显著的性能提升。通过少量特定任务数据增强，VG-Refiner 在准确性和纠正能力方面均优于现有方法，同时保留了预训练模型的一般能力。具体实验数据在论文中有详细展示，表明了 VG-Refiner 在工具优化指代 grounding 推理方面的有效性。

## 🎯 应用场景

VG-Refiner 可应用于各种需要指代 grounding 和视觉推理的场景，例如智能客服、机器人导航、图像编辑等。通过提高模型对工具输出的可靠性判断和纠错能力，可以显著提升这些应用的用户体验和智能化水平。未来，该研究可以扩展到更复杂的视觉推理任务和更多的工具集成场景。

## 📄 摘要（原文）

> Tool-integrated visual reasoning (TiVR) has demonstrated great potential in enhancing multimodal problem-solving. However, existing TiVR paradigms mainly focus on integrating various visual tools through reinforcement learning, while neglecting to design effective response mechanisms for handling unreliable or erroneous tool outputs. This limitation is particularly pronounced in referring and grounding tasks, where inaccurate detection tool predictions often mislead TiVR models into generating hallucinated reasoning. To address this issue, we propose the VG-Refiner, the first framework aiming at the tool-refined referring grounded reasoning. Technically, we introduce a two-stage think-rethink mechanism that enables the model to explicitly analyze and respond to tool feedback, along with a refinement reward that encourages effective correction in response to poor tool results. In addition, we propose two new metrics and establish fair evaluation protocols to systematically measure the refinement ability of current models. We adopt a small amount of task-specific data to enhance the refinement capability of VG-Refiner, achieving a significant improvement in accuracy and correction ability on referring and reasoning grounding benchmarks while preserving the general capabilities of the pretrained model.

