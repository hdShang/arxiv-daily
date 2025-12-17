---
layout: default
title: Intent-Driven LLM Ensemble Planning for Flexible Multi-Robot Disassembly: Demonstration on EV Batteries
---

# Intent-Driven LLM Ensemble Planning for Flexible Multi-Robot Disassembly: Demonstration on EV Batteries

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.17576" target="_blank" class="toolbar-btn">arXiv: 2510.17576v1</a>
    <a href="https://arxiv.org/pdf/2510.17576.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17576v1" 
            onclick="toggleFavorite(this, '2510.17576v1', 'Intent-Driven LLM Ensemble Planning for Flexible Multi-Robot Disassembly: Demonstration on EV Batteries')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Cansu Erdogan, Cesar Alan Contreras, Alireza Rastegarpanah, Manolis Chiou, Rustam Stolkin

**分类**: cs.RO, cs.AI, cs.HC, cs.MA

**发布日期**: 2025-10-20

**备注**: This work is funded by the project called "Research and Development of a Highly Automated and Safe Streamlined Process for Increasing Lithium-ion Battery Repurposing and Recycling" (REBELION) under Grant 101104241, and partially supported by the Ministry of National Education, Republic of Turkey. Submitted to Frontiers for Review

---

## 💡 一句话要点

**提出意图驱动的LLM集成规划方法，用于柔性多机器人拆卸电动汽车电池。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多机器人协同` `拆卸规划` `大型语言模型` `意图驱动` `电动汽车电池回收`

## 📋 核心要点

1. 现有方法难以处理非结构化场景中多机器人协同拆卸任务，尤其是在任务顺序需要根据环境和人类意图动态调整时。
2. 提出一种意图驱动的规划流程，利用LLM集成生成候选方案，并通过验证器和过滤器确保方案的正确性和可行性。
3. 在电动汽车电池拆卸任务的真实场景中验证了该方法的有效性，结果表明该方法能够可靠地将人类意图转化为可执行的多机器人计划。

## 📝 摘要（中文）

本文提出了一种规划复杂操作任务的方法，其中多个具有不同末端执行器和能力的机器人，在计算机视觉的引导下，必须规划和执行连接的动作序列，处理出现在非结构化场景中任意位置和配置的各种对象。我们提出了一种意图驱动的规划流程，该流程可以通过简单的语言指令，在人类的不同程度的监督输入下，稳健地构建此类动作序列。该流程集成了：（i）感知到文本的场景编码，（ii）一个大型语言模型（LLM）集成，它根据操作员的意图生成候选移除序列，（iii）一个基于LLM的验证器，用于强制执行格式和优先级约束，以及（iv）一个确定性的连贯性过滤器，用于拒绝幻觉对象。该流程在一个示例任务中进行了评估，其中两个机器人手臂协同工作以拆卸电动汽车电池以进行回收应用。必须按照特定顺序抓取和移除各种组件，该顺序由人工指令和/或自主系统做出的任务顺序可行性决策决定。在包含五个组件类别的200个真实场景和600个操作员提示中，我们使用完整序列正确性和下一个任务正确性指标来评估和比较五个基于LLM的规划器（包括流程组件的消融分析）。我们还通过人类参与者实验，根据执行时间和NASA TLX评估了基于LLM的人机界面。结果表明，我们的集成验证方法能够可靠地将操作员意图映射到安全、可执行的多机器人计划，同时保持较低的用户工作量。

## 🔬 方法详解

**问题定义**：论文旨在解决多机器人协同拆卸任务中，如何在非结构化环境中，根据人类的意图和场景的实际情况，规划出合理的拆卸动作序列。现有方法通常依赖于预定义的规则或复杂的运动规划算法，难以适应环境变化和人类意图的动态调整。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的强大推理能力，将人类的意图转化为机器人可执行的动作序列。通过集成多个LLM，并引入验证器和过滤器，提高规划的鲁棒性和准确性。这种方法允许系统根据人类的指令和场景的感知信息，灵活地调整拆卸顺序和策略。

**技术框架**：该方法包含以下几个主要模块：1) **感知到文本的场景编码**：将计算机视觉获取的场景信息转化为LLM可以理解的文本描述。2) **LLM集成规划**：使用多个LLM生成候选的拆卸动作序列，每个LLM基于不同的知识和推理策略。3) **LLM验证器**：使用另一个LLM作为验证器，检查候选序列是否符合格式和优先级约束。4) **确定性连贯性过滤器**：过滤掉包含幻觉对象的序列，确保规划的可靠性。

**关键创新**：该方法最重要的创新点在于将LLM集成应用于多机器人拆卸任务规划。通过集成多个LLM，可以利用不同模型的优势，提高规划的鲁棒性和泛化能力。同时，引入LLM验证器和连贯性过滤器，可以有效减少LLM的幻觉问题，提高规划的可靠性。

**关键设计**：LLM集成中使用了多个预训练的LLM，并针对拆卸任务进行了微调。LLM验证器被设计成可以检查动作序列的格式是否正确，以及是否违反了任何优先级约束。连贯性过滤器使用确定性算法来识别和删除包含幻觉对象的序列。此外，该方法还设计了一个人机交互界面，允许用户通过简单的语言指令来指导机器人的拆卸过程。

## 📊 实验亮点

在包含五个组件类别的200个真实场景和600个操作员提示中，该方法在电动汽车电池拆卸任务中表现出色。通过与五个LLM-based planners对比，验证了ensemble-with-verification方法的有效性。实验结果表明，该方法能够可靠地将操作员意图映射到安全、可执行的多机器人计划，同时保持较低的用户工作量。

## 🎯 应用场景

该研究成果可广泛应用于自动化拆卸、回收和再制造领域，例如电动汽车电池回收、电子产品拆解等。通过结合计算机视觉和自然语言处理技术，可以实现更加灵活和智能的机器人拆卸系统，提高资源利用率，降低环境污染，并减少人工劳动强度。

## 📄 摘要（原文）

> This paper addresses the problem of planning complex manipulation tasks, in which multiple robots with different end-effectors and capabilities, informed by computer vision, must plan and execute concatenated sequences of actions on a variety of objects that can appear in arbitrary positions and configurations in unstructured scenes. We propose an intent-driven planning pipeline which can robustly construct such action sequences with varying degrees of supervisory input from a human using simple language instructions. The pipeline integrates: (i) perception-to-text scene encoding, (ii) an ensemble of large language models (LLMs) that generate candidate removal sequences based on the operator's intent, (iii) an LLM-based verifier that enforces formatting and precedence constraints, and (iv) a deterministic consistency filter that rejects hallucinated objects. The pipeline is evaluated on an example task in which two robot arms work collaboratively to dismantle an Electric Vehicle battery for recycling applications. A variety of components must be grasped and removed in specific sequences, determined by human instructions and/or by task-order feasibility decisions made by the autonomous system. On 200 real scenes with 600 operator prompts across five component classes, we used metrics of full-sequence correctness and next-task correctness to evaluate and compare five LLM-based planners (including ablation analyses of pipeline components). We also evaluated the LLM-based human interface in terms of time to execution and NASA TLX with human participant experiments. Results indicate that our ensemble-with-verification approach reliably maps operator intent to safe, executable multi-robot plans while maintaining low user effort.

