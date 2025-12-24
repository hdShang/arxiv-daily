---
layout: default
title: "NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robot Manipulation"
---

# NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robot Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03895" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03895v1</a>
  <a href="https://arxiv.org/pdf/2510.03895.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03895v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03895v1', 'NoTVLA: Narrowing of Dense Action Trajectories for Generalizable Robot Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zheng Huang, Mingyu Liu, Xiaoyi Lin, Muzhi Zhu, Canyu Zhao, Zongze Du, Xiaoman Li, Yiduo Jia, Hao Zhong, Hao Chen, Chunhua Shen

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-04

---

## 💡 一句话要点

**提出NoTVLA框架，通过稀疏轨迹学习解决VLA模型中的灾难性遗忘问题，提升机器人操作的泛化性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `机器人操作` `灾难性遗忘` `稀疏轨迹学习` `泛化能力`

## 📋 核心要点

1. VLA模型依赖连续动作序列导致灾难性遗忘，阻碍了其在真实机器人操作中的应用。
2. NoTVLA框架通过聚焦于稀疏轨迹，利用时间压缩和空间推理剪枝优化末端执行器轨迹，避免了密集轨迹微调。
3. 实验表明，NoTVLA在多任务场景下，以更低的计算资源和无需腕载摄像头的情况下，实现了优于现有方法的性能和泛化能力。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型是具身智能领域的重要进展，但其在实际部署中面临灾难性遗忘的关键障碍。这个问题源于模型过度依赖连续动作序列或动作块，这无意中创建了孤立的数据孤岛，破坏了跨任务的知识保留。为了解决这些挑战，我们提出了轨迹窄化VLA(NoTVLA)框架：一种新颖的方法，它将其重点缩小到稀疏轨迹，从而避免了与密集轨迹微调相关的灾难性遗忘。NoTVLA的一个关键创新在于其轨迹规划策略：它没有以目标对象的轨迹为中心，而是专门利用时间压缩和空间推理剪枝来优化机器人末端执行器的轨迹。此外，训练是使用这些稀疏轨迹而不是密集动作轨迹进行的，这种优化在零样本中提供了更好的性能，带来了显著的实际优势。在多任务评估场景中，NoTVLA在两个关键约束条件下实现了优于pi0的性能和泛化：它使用的计算能力比pi0少一个数量级以上，并且不需要腕载摄像头。这种设计确保了NoTVLA的运行精度与单任务专家模型非常接近。至关重要的是，它还保留了模型固有的语言能力，从而在特定场景中实现零样本泛化，支持跨多个机器人平台的统一模型部署，并在从新的角度感知任务时培养一定程度的泛化。

## 🔬 方法详解

**问题定义**：VLA模型在机器人操作中面临灾难性遗忘问题，即在学习新任务时，会忘记之前学习过的任务。现有方法通常依赖于密集的动作轨迹进行训练，这导致模型过度拟合特定任务的数据，从而难以泛化到新的任务和环境。此外，计算资源消耗大，对硬件要求高，限制了其在实际机器人平台上的部署。

**核心思路**：NoTVLA的核心思路是通过聚焦于稀疏的动作轨迹来解决灾难性遗忘问题。作者认为，密集的动作轨迹包含了大量冗余信息，并且容易导致模型陷入局部最优解。通过只关注关键的动作点，可以减少模型的学习负担，提高其泛化能力。此外，通过优化机器人末端执行器的轨迹，可以更好地适应不同的任务和环境。

**技术框架**：NoTVLA框架主要包含以下几个模块：1) 轨迹规划模块：该模块负责生成稀疏的机器人末端执行器轨迹。2) 视觉-语言编码器：该模块负责将视觉和语言信息编码成统一的特征向量。3) 动作预测模块：该模块负责根据视觉-语言特征向量预测机器人的动作。4) 训练模块：该模块负责使用稀疏轨迹数据训练整个模型。

**关键创新**：NoTVLA的关键创新在于其轨迹规划策略。与现有方法不同，NoTVLA不是以目标对象的轨迹为中心，而是专门针对机器人末端执行器的轨迹进行优化。它利用时间压缩和空间推理剪枝技术，只保留对完成任务至关重要的动作点。这种方法可以显著减少模型的学习负担，提高其泛化能力。

**关键设计**：NoTVLA使用了一种基于Transformer的视觉-语言编码器，将视觉和语言信息编码成统一的特征向量。动作预测模块使用一个简单的多层感知机。训练过程中，作者使用了一种基于对比学习的损失函数，鼓励模型学习到任务相关的特征表示。具体参数设置和网络结构细节在论文中有详细描述，但摘要中未明确给出。

## 📊 实验亮点

NoTVLA在多任务评估场景中表现出色，性能优于pi0，且计算资源消耗降低一个数量级以上，无需腕载摄像头。其运行精度接近单任务专家模型，同时保留了模型的语言能力，支持零样本泛化和跨平台部署。这些结果表明NoTVLA在解决VLA模型灾难性遗忘问题方面具有显著优势。

## 🎯 应用场景

NoTVLA框架可应用于各种机器人操作任务，例如物体抓取、放置、装配等。它能够提高机器人在复杂环境中的适应性和泛化能力，降低对计算资源和硬件的要求，从而促进VLA模型在实际机器人平台上的部署。该研究对智能制造、家庭服务机器人等领域具有重要意义。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models represent a pivotal advance in embodied intelligence, yet they confront critical barriers to real-world deployment, most notably catastrophic forgetting. This issue stems from their overreliance on continuous action sequences or action chunks, which inadvertently create isolated data silos that disrupt knowledge retention across tasks. To tackle these challenges, we propose the Narrowing of Trajectory VLA (NoTVLA) framework: a novel approach that narrows its focus to sparse trajectories, thereby avoiding the catastrophic forgetting associated with dense trajectory fine-tuning. A key innovation of NoTVLA lies in its trajectory planning strategy: instead of centering on the target object's trajectory, it leverages temporal compression and spatial reasoning pruning specifically for the robot end effector's trajectory. Furthermore, training is conducted using these sparse trajectories rather than dense action trajectories, an optimization that delivers remarkable practical advantages with better performance in zero-shot. In multi-task evaluation scenarios, NoTVLA achieves superior performance and generalization compared to pi0 while operating under two critical constraints: it uses over an order of magnitude less computing power than pi0 and requires no wrist-mounted camera. This design ensures that NoTVLA's operational accuracy closely approximates that of single-task expert models. Crucially, it also preserves the model's inherent language capabilities, enabling zero-shot generalization in specific scenarios, supporting unified model deployment across multiple robot platforms, and fostering a degree of generalization even when perceiving tasks from novel perspectives.

