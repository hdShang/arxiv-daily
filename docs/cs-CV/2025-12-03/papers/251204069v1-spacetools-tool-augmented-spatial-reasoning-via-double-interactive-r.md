---
layout: default
title: SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL
---

# SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04069" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04069v1</a>
  <a href="https://arxiv.org/pdf/2512.04069.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04069v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.04069v1', 'SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyi Chen, Mikaela Angelina Uy, Chan Hee Song, Faisal Ladhak, Adithyavairavan Murali, Qing Qu, Stan Birchfield, Valts Blukis, Jonathan Tremblay

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-03

**🔗 代码/项目**: [PROJECT_PAGE](https://spacetools.github.io/)

---

## 💡 一句话要点

**SpaceTools：通过双重交互强化学习增强工具辅助的空间推理能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `空间推理` `视觉语言模型` `强化学习` `工具学习` `机器人操作`

## 📋 核心要点

1. 现有视觉语言模型在精确空间推理方面存在不足，限制了其在具身智能应用中的潜力。
2. 提出双重交互强化学习(DIRL)框架，通过教学和探索两个阶段，使VLM能够协调使用多种工具。
3. SpaceTools模型在多个空间理解基准测试中取得SOTA性能，并在真实机器人操作中验证了有效性。

## 📝 摘要（中文）

视觉语言模型(VLM)在定性视觉理解方面表现出色，但在具身应用所需的精确空间推理方面存在困难。Agentic范式认为VLM可以使用各种工具来增强这些能力，例如深度估计器、分割模型和姿态估计器。然而，如何在不依赖手工设计的提示策略或强制执行固定的、预定义的工具管道（限制了VLM发现最佳工具使用模式的能力）的情况下实现这一愿景仍然是一个开放的挑战。强化学习可以弥补这一差距，但由于多工具推理中搜索空间巨大，因此迄今为止仅限于使用单个视觉工具进行推理。我们引入了双重交互强化学习(DIRL)，这是一个两阶段的训练框架，其中VLM通过交互式探索和反馈来学习协调多个工具。在教学阶段，我们将通过交互式强化学习训练的单个工具专家的演示与使用所有工具的前沿模型的轨迹相结合。在探索阶段，模型通过持续的强化学习进一步完善多工具协调。我们的模型SpaceTools具有工具增强的空间推理能力，在空间理解基准测试（RoboSpatial-Home、BLINK、BOP-ASK）上实现了最先进的性能，并展示了使用7自由度机器人作为工具的可靠的真实世界操作。DIRL比vanilla SFT（在RoboSpatial上+12%）和RL（在RoboSpatial上+16%）基线有了显著的改进。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉语言模型(VLM)在具身应用中进行精确空间推理的难题。现有方法要么依赖手工设计的提示，要么使用固定的工具流程，限制了VLM发现最优工具使用策略的能力。强化学习虽然有潜力，但由于多工具组合带来的巨大搜索空间，难以有效训练。

**核心思路**：论文的核心思路是利用双重交互强化学习(DIRL)框架，分阶段训练VLM学会协调使用多种工具。DIRL首先通过模仿学习（教学阶段）让VLM快速掌握工具的使用，然后通过强化学习（探索阶段）进一步优化工具的使用策略。

**技术框架**：DIRL框架包含两个主要阶段：教学阶段和探索阶段。在教学阶段，模型结合了单个工具专家的演示数据和使用所有工具的前沿模型的轨迹。单个工具专家通过交互式强化学习训练，能够熟练使用单个工具。前沿模型则尝试使用所有工具解决问题。在探索阶段，模型通过持续的强化学习，根据环境反馈进一步优化多工具协调策略。

**关键创新**：DIRL的关键创新在于其双阶段训练方式，有效地解决了多工具强化学习中的探索空间过大的问题。通过教学阶段的模仿学习，模型可以快速学习到有用的工具使用策略，从而缩小了探索空间。探索阶段的强化学习则进一步优化了这些策略，使模型能够更好地适应不同的环境和任务。

**关键设计**：论文使用了强化学习算法来训练工具专家和前沿模型。具体的算法选择和参数设置未知。损失函数的设计旨在鼓励模型模仿工具专家的行为，并根据环境反馈优化工具使用策略。网络结构方面，论文使用了视觉语言模型作为基础模型，并针对多工具推理任务进行了调整。具体调整细节未知。

## 📊 实验亮点

SpaceTools在RoboSpatial-Home数据集上相比vanilla SFT提升了12%，相比纯RL提升了16%，在BLINK和BOP-ASK数据集上也取得了SOTA性能。此外，该模型还成功应用于真实世界的7自由度机器人操作，验证了其在实际场景中的有效性。这些实验结果表明，DIRL框架能够有效地提升VLM的工具辅助空间推理能力。

## 🎯 应用场景

该研究成果可应用于机器人操作、自动驾驶、增强现实等领域。例如，机器人可以利用该技术理解周围环境，并使用各种工具完成复杂的任务，如物体抓取、场景导航等。在自动驾驶领域，车辆可以利用该技术进行更精确的环境感知和行为决策。在增强现实领域，用户可以通过语音或手势与虚拟环境进行交互，并使用虚拟工具完成各种任务。

## 📄 摘要（原文）

> Vision Language Models (VLMs) demonstrate strong qualitative visual understanding, but struggle with metrically precise spatial reasoning required for embodied applications. The agentic paradigm promises that VLMs can use a wide variety of tools that could augment these capabilities, such as depth estimators, segmentation models, and pose estimators. Yet it remains an open challenge how to realize this vision without solely relying on handcrafted prompting strategies or enforcing fixed, predefined tool pipelines that limit VLMs' ability to discover optimal tool-use patterns. Reinforcement Learning could overcome this gap, but has so far been limited to reasoning with a single visual tool due to the large search space in multi-tool reasoning. We introduce Double Interactive Reinforcement Learning (DIRL), a two-phase training framework where VLMs learn to coordinate multiple tools through interactive exploration and feedback. In the teaching phase, we combine demonstrations from a single tool specialist trained via interactive RL with traces from a frontier model using all tools. In the exploration phase, the model further refines multi-tool coordination through continued RL. Our model, SpaceTools, with tool-augmented spatial reasoning ability, achieves state-of-the-art performance on spatial understanding benchmarks (RoboSpatial-Home, BLINK, BOP-ASK) and demonstrates reliable real-world manipulation using a 7-DOF robot as a tool. DIRL provides substantial improvements over the vanilla SFT (+12% on RoboSpatial) and RL (+16% on RoboSpatial) baselines. Project page: https://spacetools.github.io/.

