---
layout: default
title: Robotic Visual Instruction
---

# Robotic Visual Instruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00693" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00693v3</a>
  <a href="https://arxiv.org/pdf/2505.00693.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00693v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00693v3', 'Robotic Visual Instruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanbang Li, Ziyang Gong, Haoyang Li, Xiaoqi Huang, Haolan Kang, Guangping Bai, Xianzheng Ma

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-05-01 (更新: 2025-07-27)

**备注**: Project website: https://robotic-visual-instruction.github.io/

---

## 💡 一句话要点

**提出机器人视觉指令以解决自然语言交互的空间精度不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人视觉指令` `视觉-语言模型` `人机交互` `任务执行` `时空信息编码`

## 📋 核心要点

1. 现有的自然语言交互方式在空间精度上存在不足，导致机器人任务定义模糊且冗长。
2. 提出机器人视觉指令（RoVI），通过手绘符号表示来编码时空信息，指导机器人执行任务。
3. 在真实场景中，VIEW方法实现了87.5%的成功率，特别是在多步骤和轨迹跟随的任务中表现优异。

## 📝 摘要（中文）

近年来，自然语言成为人机交互的主要媒介。然而，其固有的空间精度不足导致机器人任务定义面临歧义和冗长的问题。此外，在需要安静的公共场所，如图书馆或医院，口头与机器人沟通并不合适。为了解决这些局限性，本文提出了机器人视觉指令（RoVI），通过物体中心的手绘符号表示来指导机器人任务。RoVI有效地将时空信息编码为人类可理解的视觉指令，利用箭头、圆圈、颜色和数字来引导3D机器人操作。为使机器人更好地理解RoVI并生成精确动作，本文提出了视觉指令体现工作流（VIEW），该流程为RoVI条件策略制定。通过关键点提取，VIEW利用视觉-语言模型（VLMs）解码2D像素空间中的时空约束，并将其转化为可执行的3D动作序列。我们还策划了一个包含15K实例的专用数据集，以微调小型VLMs，使其有效学习RoVI能力。我们的方案在11个新任务的真实和模拟环境中经过严格验证，显示出显著的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决自然语言在机器人任务定义中的空间精度不足问题，导致的歧义和冗长描述。现有方法在公共场所的应用也受到限制。

**核心思路**：提出机器人视觉指令（RoVI），通过手绘符号表示将时空信息转化为可理解的视觉指令，以提高机器人对任务的理解和执行能力。

**技术框架**：整体架构包括RoVI输入的解析、时空约束的解码和3D动作序列的生成。主要模块包括视觉-语言模型（VLMs）和关键点提取。

**关键创新**：RoVI通过物体中心的符号表示，克服了自然语言的模糊性，VIEW方法则利用VLMs实现了对视觉指令的高效解码和执行。

**关键设计**：在数据集构建中，策划了包含15K实例的专用数据集以微调VLMs，确保其能够有效学习RoVI的能力。

## 📊 实验亮点

在实验中，VIEW方法在真实场景中实现了87.5%的成功率，尤其是在涉及多步骤动作和轨迹跟随的任务中，表现出显著的泛化能力。这一结果相较于基线方法有明显提升，展示了RoVI的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、医疗辅助机器人和教育机器人等场景，能够在需要安静或高精度操作的环境中有效执行任务。未来，该方法有望推动人机交互的智能化和自然化，提升机器人在复杂环境中的适应能力。

## 📄 摘要（原文）

> Recently, natural language has been the primary medium for human-robot interaction. However, its inherent lack of spatial precision introduces challenges for robotic task definition such as ambiguity and verbosity. Moreover, in some public settings where quiet is required, such as libraries or hospitals, verbal communication with robots is inappropriate. To address these limitations, we introduce the Robotic Visual Instruction (RoVI), a novel paradigm to guide robotic tasks through an object-centric, hand-drawn symbolic representation. RoVI effectively encodes spatial-temporal information into human-interpretable visual instructions through 2D sketches, utilizing arrows, circles, colors, and numbers to direct 3D robotic manipulation. To enable robots to understand RoVI better and generate precise actions based on RoVI, we present Visual Instruction Embodied Workflow (VIEW), a pipeline formulated for RoVI-conditioned policies. This approach leverages Vision-Language Models (VLMs) to interpret RoVI inputs, decode spatial and temporal constraints from 2D pixel space via keypoint extraction, and then transform them into executable 3D action sequences. We additionally curate a specialized dataset of 15K instances to fine-tune small VLMs for edge deployment,enabling them to effectively learn RoVI capabilities. Our approach is rigorously validated across 11 novel tasks in both real and simulated environments, demonstrating significant generalization capability. Notably, VIEW achieves an 87.5% success rate in real-world scenarios involving unseen tasks that feature multi-step actions, with disturbances, and trajectory-following requirements. Project website: https://robotic-visual-instruction.github.io/

