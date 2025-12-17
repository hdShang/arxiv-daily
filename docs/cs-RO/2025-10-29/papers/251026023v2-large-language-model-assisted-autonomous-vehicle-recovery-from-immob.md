---
layout: default
title: Large Language Model-assisted Autonomous Vehicle Recovery from Immobilization
---

# Large Language Model-assisted Autonomous Vehicle Recovery from Immobilization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26023" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26023v2</a>
  <a href="https://arxiv.org/pdf/2510.26023.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26023v2" onclick="toggleFavorite(this, '2510.26023v2', 'Large Language Model-assisted Autonomous Vehicle Recovery from Immobilization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhipeng Bao, Qianwen Li

**分类**: cs.AI, cs.RO

**发布日期**: 2025-10-29 (更新: 2025-11-14)

**备注**: 7 pages

---

## 💡 一句话要点

**提出StuckSolver，利用大语言模型辅助自动驾驶车辆脱困**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `大语言模型` `脱困` `自主推理` `乘客引导` `环境感知` `运动规划`

## 📋 核心要点

1. 现有自动驾驶车辆在复杂交通场景中易陷入困境，远程干预成本高，人工接管限制了车辆可访问性。
2. StuckSolver利用大语言模型进行推理，无需修改现有自动驾驶系统，通过插件式模块实现自主或乘客引导的脱困。
3. 实验表明，StuckSolver在Bench2Drive基准测试中表现出色，结合乘客指导后性能进一步提升。

## 📝 摘要（中文）

尽管近年来自动驾驶车辆取得了显著进展，但在某些人类驾驶员擅长的交通场景中，自动驾驶车辆仍然面临挑战。在这些情况下，自动驾驶车辆经常会陷入无法行驶的状态，扰乱整体交通流畅性。现有的解决方案，如远程干预（成本高且效率低）和人工接管（将非驾驶员排除在外并限制了自动驾驶车辆的可访问性）并不完善。本文介绍了一种新颖的基于大语言模型（LLM）的脱困框架StuckSolver，使自动驾驶车辆能够通过自我推理和/或乘客引导的决策来解决无法行驶的场景。StuckSolver被设计为一个插件式附加模块，运行在自动驾驶车辆现有的感知-规划-控制堆栈之上，无需修改其内部架构。相反，它与标准传感器数据流交互以检测无法行驶的状态，解释环境上下文，并生成可由自动驾驶车辆原生规划器执行的高级恢复命令。我们在Bench2Drive基准测试和自定义设计的不确定性场景中评估了StuckSolver。结果表明，StuckSolver仅通过自主自我推理就实现了接近最先进的性能，并且在结合乘客指导后表现出进一步的改进。

## 🔬 方法详解

**问题定义**：自动驾驶车辆在复杂或未知的交通场景中容易出现“immobilization”问题，即车辆无法继续行驶，阻碍交通。现有的远程干预方案成本高昂，人工接管方案则依赖于驾驶员，限制了自动驾驶技术的应用范围。因此，需要一种能够自主或在乘客辅助下解决自动驾驶车辆脱困问题的方案。

**核心思路**：利用大语言模型（LLM）的强大推理能力，使自动驾驶车辆能够理解当前环境，分析导致immobilization的原因，并生成合理的脱困策略。通过与乘客的交互，进一步提升决策的准确性和安全性。核心在于将LLM作为高级决策者，指导车辆的底层控制系统。

**技术框架**：StuckSolver作为一个插件式模块，位于自动驾驶车辆的感知-规划-控制堆栈之上。它接收来自传感器的数据流，检测immobilization状态。一旦检测到，StuckSolver会利用LLM分析环境上下文，生成高级恢复命令。这些命令随后被传递给车辆的原生规划器，由规划器生成具体的行驶轨迹并控制车辆执行。整体流程包括：感知 -> 状态检测 -> LLM推理 -> 命令生成 -> 规划 -> 控制。

**关键创新**：StuckSolver的关键创新在于将大语言模型引入到自动驾驶车辆的脱困过程中，实现了自主推理和决策。与传统的基于规则或强化学习的方法相比，StuckSolver具有更强的泛化能力和适应性，能够处理更复杂的交通场景。此外，乘客引导机制的引入进一步提升了系统的鲁棒性和安全性。

**关键设计**：StuckSolver的设计重点在于LLM的prompt设计和命令接口的设计。Prompt需要包含足够的环境信息和约束条件，以便LLM能够生成合理的脱困策略。命令接口需要与车辆的原生规划器兼容，能够将LLM生成的高级命令转化为具体的行驶轨迹。具体的参数设置和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，StuckSolver在Bench2Drive基准测试中取得了接近最先进的性能，证明了其自主推理能力。当结合乘客指导时，StuckSolver的性能得到了进一步提升，表明乘客的反馈能够有效提高脱困决策的准确性。具体的性能数据和提升幅度在论文中未详细给出，属于未知信息。

## 🎯 应用场景

StuckSolver可应用于各种自动驾驶车辆，提高其在复杂交通环境下的适应性和可靠性。该技术能够减少对远程干预的需求，降低运营成本，并提升自动驾驶车辆的可用性。未来，该技术有望扩展到其他类型的机器人系统，例如无人机和移动机器人，使其能够在复杂环境中自主完成任务。

## 📄 摘要（原文）

> Despite significant advancements in recent decades, autonomous vehicles (AVs) continue to face challenges in navigating certain traffic scenarios where human drivers excel. In such situations, AVs often become immobilized, disrupting overall traffic flow. Current recovery solutions, such as remote intervention (which is costly and inefficient) and manual takeover (which excludes non-drivers and limits AV accessibility), are inadequate. This paper introduces StuckSolver, a novel Large Language Model (LLM) driven recovery framework that enables AVs to resolve immobilization scenarios through self-reasoning and/or passenger-guided decision-making. StuckSolver is designed as a plug-in add-on module that operates on top of the AV's existing perception-planning-control stack, requiring no modification to its internal architecture. Instead, it interfaces with standard sensor data streams to detect immobilization states, interpret environmental context, and generate high-level recovery commands that can be executed by the AV's native planner. We evaluate StuckSolver on the Bench2Drive benchmark and in custom-designed uncertainty scenarios. Results show that StuckSolver achieves near-state-of-the-art performance through autonomous self-reasoning alone and exhibits further improvements when passenger guidance is incorporated.

