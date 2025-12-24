---
layout: default
title: "NovaFlow: Zero-Shot Manipulation via Actionable Flow from Generated Videos"
---

# NovaFlow: Zero-Shot Manipulation via Actionable Flow from Generated Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08568" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08568v1</a>
  <a href="https://arxiv.org/pdf/2510.08568.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08568v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.08568v1', 'NovaFlow: Zero-Shot Manipulation via Actionable Flow from Generated Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyu Li, Lingfeng Sun, Yafei Hu, Duy Ta, Jennifer Barry, George Konidaris, Jiahui Fu

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-10-09

---

## 💡 一句话要点

**NovaFlow：通过生成视频中的可执行光流实现机器人零样本操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人操作` `零样本学习` `视频生成` `光流估计` `动作规划`

## 📋 核心要点

1. 现有机器人操作方法依赖于同分布任务或特定机器人数据微调，限制了跨平台迁移能力。
2. NovaFlow通过生成视频并提取可执行光流，将任务描述转化为机器人可执行的动作计划，无需演示。
3. 实验表明，NovaFlow在刚性、铰接和可变形对象操作任务中，实现了Franka机械臂和Spot机器人的零样本有效执行。

## 📝 摘要（中文）

本文提出NovaFlow，一个自主操作框架，旨在使机器人能够零样本执行新的操作任务。现有方法通常假设任务是同分布的，或者依赖于与具体机器人匹配的数据进行微调，限制了跨平台迁移。NovaFlow将任务描述转换为目标机器人的可执行计划，无需任何演示。给定任务描述，NovaFlow使用视频生成模型合成视频，并使用现成的感知模块将其提炼成3D可执行对象光流。从对象光流中，它计算刚性对象的相对姿势，并通过抓取建议和轨迹优化将其实现为机器人动作。对于可变形对象，此光流作为基于粒子动力学模型的模型预测控制的跟踪目标。通过将任务理解与底层控制解耦，NovaFlow自然地跨机器人平台迁移。在桌面Franka机械臂和Spot四足移动机器人上，对刚性、铰接和可变形对象的操作任务进行了验证，实现了有效的零样本执行，无需演示或特定于机器人的训练。

## 🔬 方法详解

**问题定义**：现有机器人操作方法在零样本泛化能力上存在不足。它们通常依赖于特定环境或机器人的数据进行训练或微调，难以适应新的任务和平台。这限制了机器人在真实世界复杂环境中的应用。

**核心思路**：NovaFlow的核心思想是将任务理解与底层控制解耦。通过生成视频来模拟任务执行过程，并从中提取可执行的光流信息，从而指导机器人的动作规划。这种方法避免了直接学习复杂的控制策略，提高了泛化能力。

**技术框架**：NovaFlow框架主要包含以下几个阶段：1) 视频生成：根据任务描述，使用视频生成模型合成任务执行的视频。2) 光流提取：使用现成的感知模块，从生成的视频中提取3D可执行对象光流。3) 动作规划：根据提取的光流信息，针对刚性对象计算相对姿势，并通过抓取建议和轨迹优化生成机器人动作；针对可变形对象，将光流作为模型预测控制的跟踪目标。

**关键创新**：NovaFlow的关键创新在于利用生成视频作为中间表示，将任务理解与机器人控制解耦。通过光流提取，将视频中的视觉信息转化为机器人可执行的动作指令。这种方法避免了直接学习复杂的控制策略，提高了泛化能力和跨平台迁移能力。

**关键设计**：在视频生成阶段，使用了预训练的视频生成模型，并根据任务描述进行prompting。在光流提取阶段，使用了现成的3D光流估计方法。在动作规划阶段，针对刚性对象，使用了基于抓取建议和轨迹优化的方法；针对可变形对象，使用了基于粒子动力学模型的模型预测控制方法。

## 📊 实验亮点

NovaFlow在Franka机械臂和Spot机器人上进行了实验验证，实现了刚性、铰接和可变形对象的零样本操作。实验结果表明，NovaFlow无需任何演示或特定于机器人的训练，即可有效地完成各种操作任务，证明了其良好的泛化能力和跨平台迁移能力。

## 🎯 应用场景

NovaFlow具有广泛的应用前景，例如在家庭服务机器人、工业自动化、医疗机器人等领域。它可以使机器人在没有人工干预的情况下，自主完成各种操作任务，提高生产效率和服务质量。未来，该技术可以进一步扩展到更复杂的任务和环境，例如在灾难救援、太空探索等领域发挥作用。

## 📄 摘要（原文）

> Enabling robots to execute novel manipulation tasks zero-shot is a central goal in robotics. Most existing methods assume in-distribution tasks or rely on fine-tuning with embodiment-matched data, limiting transfer across platforms. We present NovaFlow, an autonomous manipulation framework that converts a task description into an actionable plan for a target robot without any demonstrations. Given a task description, NovaFlow synthesizes a video using a video generation model and distills it into 3D actionable object flow using off-the-shelf perception modules. From the object flow, it computes relative poses for rigid objects and realizes them as robot actions via grasp proposals and trajectory optimization. For deformable objects, this flow serves as a tracking objective for model-based planning with a particle-based dynamics model. By decoupling task understanding from low-level control, NovaFlow naturally transfers across embodiments. We validate on rigid, articulated, and deformable object manipulation tasks using a table-top Franka arm and a Spot quadrupedal mobile robot, and achieve effective zero-shot execution without demonstrations or embodiment-specific training. Project website: https://novaflow.lhy.xyz/.

