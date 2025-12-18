---
layout: default
title: ARRC: Advanced Reasoning Robot Control - Knowledge-Driven Autonomous Manipulation Using Retrieval-Augmented Generation
---

# ARRC: Advanced Reasoning Robot Control - Knowledge-Driven Autonomous Manipulation Using Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.05547" class="toolbar-btn" target="_blank">📄 arXiv: 2510.05547v1</a>
  <a href="https://arxiv.org/pdf/2510.05547.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05547v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.05547v1', 'ARRC: Advanced Reasoning Robot Control - Knowledge-Driven Autonomous Manipulation Using Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eugene Vorobiov, Ammar Jaleel Mahmood, Salim Rezvani, Robin Chhabra

**分类**: cs.RO

**发布日期**: 2025-10-07

---

## 💡 一句话要点

**ARRC：基于检索增强生成实现知识驱动的自主机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人控制` `检索增强生成` `大型语言模型` `自主操作` `RGB-D感知`

## 📋 核心要点

1. 现有机器人控制方法在处理复杂指令和环境变化时缺乏灵活性和泛化能力。
2. ARRC利用RAG框架，通过检索相关知识并结合LLM生成行动计划，提升机器人对指令的理解和执行能力。
3. 实验表明，ARRC在桌面扫描、接近和拾取放置任务中表现出良好的有效性和适应性。

## 📝 摘要（中文）

ARRC（高级推理机器人控制）是一个实用的系统，它通过结合检索增强生成（RAG）与RGB-D感知和受保护的执行，将自然语言指令连接到安全的局部机器人控制，并应用于经济实惠的机器人手臂。该系统在向量数据库中索引精心设计的机器人知识（运动模式、任务模板和安全启发式方法），为每个指令检索任务相关的上下文，并调节大型语言模型（LLM）以生成JSON结构化的行动计划。计划在配备Dynamixel驱动的平行夹爪和Intel RealSense D435相机的UFactory xArm 850上执行。感知使用AprilTag检测与深度信息融合，以生成以对象为中心的度量姿势。执行通过软件安全门强制执行：工作空间边界、速度和力上限、超时和有界重试。我们描述了架构、知识设计、集成选择以及用于桌面扫描、接近和拾取放置任务的可重复评估协议。实验结果证明了该方法的有效性。我们的设计表明，基于RAG的规划可以显著提高计划的有效性和适应性，同时保持感知和低级控制在机器人本地。

## 🔬 方法详解

**问题定义**：现有机器人控制系统难以将自然语言指令转化为可靠的机器人动作，尤其是在复杂环境和任务中。痛点在于缺乏对任务上下文的理解和灵活的规划能力，以及保证安全执行的机制。

**核心思路**：ARRC的核心在于利用检索增强生成（RAG）框架，将自然语言指令转化为机器人可执行的动作序列。通过检索与指令相关的机器人知识（运动模式、任务模板、安全规则），并结合大型语言模型（LLM）进行推理和规划，从而提高机器人对指令的理解和执行的可靠性。

**技术框架**：ARRC系统包含以下主要模块：1) **知识库**：存储机器人运动模式、任务模板和安全启发式规则。2) **检索模块**：根据自然语言指令，从知识库中检索相关信息。3) **LLM规划器**：利用检索到的信息，生成JSON格式的行动计划。4) **感知模块**：使用RGB-D相机和AprilTag检测，获取环境信息和物体姿态。5) **执行模块**：在软件安全门的保护下，执行行动计划。

**关键创新**：ARRC的关键创新在于将RAG框架应用于机器人控制，实现了知识驱动的自主操作。与传统的基于规则或学习的方法相比，ARRC能够更好地理解自然语言指令，并根据环境变化进行灵活的规划。此外，软件安全门的引入保证了机器人操作的安全性。

**关键设计**：知识库的设计至关重要，需要精心选择和组织机器人知识，以便检索模块能够快速准确地找到相关信息。LLM规划器的训练需要大量的机器人操作数据，以提高其生成有效行动计划的能力。软件安全门的设计需要考虑各种可能的安全风险，并设置相应的保护措施，例如工作空间限制、速度和力限制、超时和重试机制。

## 📊 实验亮点

实验结果表明，ARRC系统在桌面扫描、接近和拾取放置任务中表现出良好的性能。通过RAG框架，ARRC能够显著提高计划的有效性和适应性，同时保持感知和低级控制在机器人本地。具体性能数据和对比基线未在摘要中明确给出，需要查阅论文全文。

## 🎯 应用场景

ARRC系统可应用于各种机器人自动化场景，例如智能制造、仓储物流、家庭服务等。通过自然语言指令，用户可以轻松地控制机器人完成复杂的任务，而无需专业的编程知识。该研究有助于推动机器人技术的普及和应用，提高生产效率和服务质量。

## 📄 摘要（原文）

> We present ARRC (Advanced Reasoning Robot Control), a practical system that connects natural-language instructions to safe local robotic control by combining Retrieval-Augmented Generation (RAG) with RGB-D perception and guarded execution on an affordable robot arm. The system indexes curated robot knowledge (movement patterns, task templates, and safety heuristics) in a vector database, retrieves task-relevant context for each instruction, and conditions a large language model (LLM) to produce JSON-structured action plans. Plans are executed on a UFactory xArm 850 fitted with a Dynamixel-driven parallel gripper and an Intel RealSense D435 camera. Perception uses AprilTag detections fused with depth to produce object-centric metric poses. Execution is enforced via software safety gates: workspace bounds, speed and force caps, timeouts, and bounded retries. We describe the architecture, knowledge design, integration choices, and a reproducible evaluation protocol for tabletop scan, approach, and pick-place tasks. Experimental results demonstrate the efficacy of the proposed approach. Our design shows that RAG-based planning can substantially improve plan validity and adaptability while keeping perception and low-level control local to the robot.

