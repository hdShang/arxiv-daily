---
layout: default
title: "ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation"
---

# ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20841" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20841v1</a>
  <a href="https://arxiv.org/pdf/2509.20841.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20841v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20841v1', 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dekun Lu, Wei Gao, Kui Jia

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-09-25

**备注**: First two authors contribute equally. Project page: https://sites.google.com/view/imaginationpolicy

---

## 💡 一句话要点

**提出基于运动导向关键点链的机器人操作端到端策略，提升泛化性与精度**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `端到端学习` `运动导向关键点` `动作表示` `策略学习`

## 📋 核心要点

1. 现有端到端机器人操作策略在泛化性、精度和可靠性方面存在不足，难以大规模实际部署。
2. 提出基于运动导向关键点链（CoMOK）的动作表示，用于端到端神经策略训练，提升通用性和精度。
3. 通过模拟和硬件实验验证了该方法的有效性，能够处理多阶段任务、多模态行为和可变形物体。

## 📝 摘要（中文）

本文旨在实现一种通用、精确且可靠的端到端机器人操作策略。与传统模块化流程不同，端到端学习减轻了模块间的信息损失以及孤立优化目标导致的不对齐问题。然而，现有的端到端神经网络，包括基于大型VLM/VLA模型的网络，在实际部署中性能仍然不足。为此，我们提出了一种新颖的运动导向关键点链（CoMOK）公式用于机器人操作。该公式作为神经策略的动作表示，可以进行端到端训练。这种动作表示具有通用性，扩展了标准的末端执行器姿态动作表示，并以统一的方式支持各种操作任务。我们方法中的导向关键点能够自然地泛化到不同形状和大小的物体，同时实现亚厘米级的精度。此外，我们的公式可以轻松处理多阶段任务、多模态机器人行为和可变形物体。大量的模拟和硬件实验证明了我们方法的有效性。

## 🔬 方法详解

**问题定义**：现有端到端机器人操作策略，即使是基于大型视觉语言模型的，仍然难以满足大规模实际部署的需求。主要痛点在于泛化性不足，难以适应不同形状、大小的物体，以及在复杂任务中的精度和可靠性较低。传统模块化方法虽然在特定任务上表现良好，但存在模块间信息损失和优化目标不一致的问题。

**核心思路**：论文的核心思路是设计一种通用的动作表示，能够自然地泛化到不同形状和大小的物体，并支持各种操作任务。通过引入运动导向的关键点链（CoMOK），将操作任务分解为一系列关键点的运动，从而实现对复杂操作的精确控制。这种表示方法允许端到端训练，避免了传统模块化方法的信息损失。

**技术框架**：整体框架是一个端到端的可学习策略网络，输入是场景的视觉信息（例如RGB图像或深度图像），输出是CoMOK表示的动作序列。该网络通过模仿学习或强化学习进行训练。在执行过程中，网络根据当前场景状态预测CoMOK动作序列，机器人控制器根据该序列执行操作。

**关键创新**：最重要的技术创新点在于CoMOK动作表示。与传统的末端执行器姿态表示相比，CoMOK更加灵活和通用，能够处理不同形状和大小的物体，以及多阶段任务和可变形物体。关键点的运动方向信息使得策略能够更好地理解操作的意图，从而提高精度和可靠性。

**关键设计**：CoMOK由一系列关键点及其运动方向组成。关键点的选择取决于具体的任务，例如，对于抓取任务，关键点可以是物体的角点或边缘点。运动方向可以是相对于物体的局部坐标系，也可以是全局坐标系。损失函数通常包括模仿损失（用于模仿专家轨迹）和奖励函数（用于强化学习）。网络结构可以是卷积神经网络（CNN）或Transformer网络，用于提取视觉特征并预测CoMOK动作序列。具体参数设置和网络结构的选择取决于具体的任务和数据集。

## 📊 实验亮点

论文通过大量的模拟和硬件实验验证了CoMOK方法的有效性。实验结果表明，该方法能够实现亚厘米级的操作精度，并且能够处理多阶段任务、多模态机器人行为和可变形物体。与传统的末端执行器姿态表示相比，CoMOK在泛化性和鲁棒性方面表现更优。

## 🎯 应用场景

该研究成果可广泛应用于各种机器人操作任务，例如工业自动化、家庭服务机器人、医疗机器人等。通过提高机器人操作的泛化性、精度和可靠性，可以使机器人更好地适应复杂和动态的环境，从而实现更高效、更安全的操作。未来，该方法有望应用于更复杂的任务，例如装配、拆卸、清洁等。

## 📄 摘要（原文）

> End-to-end robot manipulation policies offer significant potential for enabling embodied agents to understand and interact with the world. Unlike traditional modular pipelines, end-to-end learning mitigates key limitations such as information loss between modules and feature misalignment caused by isolated optimization targets. Despite these advantages, existing end-to-end neural networks for robotic manipulation--including those based on large VLM/VLA models--remain insufficiently performant for large-scale practical deployment. In this paper, we take a step towards an end-to-end manipulation policy that is generalizable, accurate and reliable. To achieve this goal, we propose a novel Chain of Moving Oriented Keypoints (CoMOK) formulation for robotic manipulation. Our formulation is used as the action representation of a neural policy, which can be trained in an end-to-end fashion. Such an action representation is general, as it extends the standard end-effector pose action representation and supports a diverse set of manipulation tasks in a unified manner. The oriented keypoint in our method enables natural generalization to objects with different shapes and sizes, while achieving sub-centimeter accuracy. Moreover, our formulation can easily handle multi-stage tasks, multi-modal robot behaviors, and deformable objects. Extensive simulated and hardware experiments demonstrate the effectiveness of our method.

