---
layout: default
title: "RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation"
---

# RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08820" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08820v1</a>
  <a href="https://arxiv.org/pdf/2509.08820.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08820v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08820v1', 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zongzheng Zhang, Chenghao Yue, Haobo Xu, Minwen Liao, Xianglin Qi, Huan-ang Gao, Ziwei Wang, Hao Zhao

**分类**: cs.RO

**发布日期**: 2025-09-10

**备注**: Accepted to CoRL 2025, Project Page: https://zzongzheng0918.github.io/RoboChemist.github.io/

---

## 💡 一句话要点

**RoboChemist：面向长期任务和安全合规的机器人化学实验框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人化学` `视觉语言模型` `视觉语言动作` `长期任务规划` `安全合规`

## 📋 核心要点

1. 现有机器人化学实验系统难以处理透明物体，且缺乏对复杂任务的语义理解和反馈。
2. RoboChemist利用VLM进行任务规划、视觉提示生成和合规性监控，实现更智能的控制。
3. 实验结果表明，RoboChemist在成功率和合规率上均优于现有VLA基线，并具有良好的泛化性。

## 📝 摘要（中文）

机器人化学家有望将人类专家从重复性任务中解放出来，并加速科学发现，但目前仍处于起步阶段。化学实验涉及对危险和可变形物质的长期操作，成功不仅需要完成任务，还需要严格遵守实验规范。为了应对这些挑战，我们提出了RoboChemist，一个双环框架，它集成了视觉-语言模型（VLM）和视觉-语言-动作（VLA）模型。与之前依赖深度感知且难以处理透明实验室设备的基于VLM的系统（如VoxPoser、ReKep）以及缺乏复杂任务语义级反馈的现有VLA系统（如RDT、pi0）不同，我们的方法利用VLM作为（1）将任务分解为原始动作的规划器，（2）引导VLA模型的视觉提示生成器，以及（3）评估任务成功和法规遵从性的监控器。值得注意的是，我们引入了一个VLA接口，该接口接受来自VLM的基于图像的视觉目标，从而实现精确的、目标条件控制。我们的系统成功地执行了原始动作和完整的多步骤化学协议。结果表明，与最先进的VLA基线相比，平均成功率提高了23.57%，合规率平均提高了0.298，同时也证明了对对象和任务的强大泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人化学实验中长期任务规划、安全合规以及对透明或半透明实验器材的处理问题。现有方法，如基于深度信息的系统，难以处理透明物体；而VLA系统缺乏对复杂任务的语义理解和反馈，难以保证实验的成功率和安全性。

**核心思路**：论文的核心思路是利用视觉-语言模型（VLM）的强大语义理解能力，将其作为任务规划器、视觉提示生成器和合规性监控器，从而指导视觉-语言-动作（VLA）模型执行化学实验。这种双环框架能够实现更精确、安全和智能的机器人化学实验。

**技术框架**：RoboChemist框架包含两个主要循环：一个由VLM驱动的高层规划循环，和一个由VLA模型驱动的底层执行循环。VLM首先将复杂任务分解为一系列原始动作，并生成视觉提示来指导VLA模型。VLA模型根据视觉提示执行动作，并将执行结果反馈给VLM。VLM评估任务的成功和合规性，并根据评估结果调整规划。

**关键创新**：该论文的关键创新在于将VLM集成到机器人化学实验系统中，并将其用作任务规划器、视觉提示生成器和合规性监控器。此外，论文还引入了一个VLA接口，该接口接受来自VLM的基于图像的视觉目标，从而实现精确的目标条件控制。

**关键设计**：VLM使用预训练的视觉-语言模型，并针对化学实验任务进行微调。VLA模型使用深度神经网络，并结合视觉和语言信息来预测动作。视觉提示生成器将VLM的语义理解转化为VLA模型可以理解的视觉目标。合规性监控器使用规则和约束来评估实验的安全性。

## 📊 实验亮点

RoboChemist在化学实验任务中取得了显著的性能提升。与最先进的VLA基线相比，平均成功率提高了23.57%，合规率平均提高了0.298。此外，该系统还表现出对不同对象和任务的强大泛化能力，证明了其在实际应用中的潜力。

## 🎯 应用场景

RoboChemist可应用于自动化化学合成、药物发现、材料科学等领域，加速科研进程，降低实验风险，并解放科研人员，使其能够专注于更具创造性的工作。该系统还可扩展到其他需要长期规划和安全合规的机器人任务中。

## 📄 摘要（原文）

> Robotic chemists promise to both liberate human experts from repetitive tasks and accelerate scientific discovery, yet remain in their infancy. Chemical experiments involve long-horizon procedures over hazardous and deformable substances, where success requires not only task completion but also strict compliance with experimental norms. To address these challenges, we propose \textit{RoboChemist}, a dual-loop framework that integrates Vision-Language Models (VLMs) with Vision-Language-Action (VLA) models. Unlike prior VLM-based systems (e.g., VoxPoser, ReKep) that rely on depth perception and struggle with transparent labware, and existing VLA systems (e.g., RDT, pi0) that lack semantic-level feedback for complex tasks, our method leverages a VLM to serve as (1) a planner to decompose tasks into primitive actions, (2) a visual prompt generator to guide VLA models, and (3) a monitor to assess task success and regulatory compliance. Notably, we introduce a VLA interface that accepts image-based visual targets from the VLM, enabling precise, goal-conditioned control. Our system successfully executes both primitive actions and complete multi-step chemistry protocols. Results show 23.57% higher average success rate and a 0.298 average increase in compliance rate over state-of-the-art VLA baselines, while also demonstrating strong generalization to objects and tasks.

