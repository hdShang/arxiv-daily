---
layout: default
title: Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning
---

# Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21302" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21302v1</a>
  <a href="https://arxiv.org/pdf/2510.21302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21302v1" onclick="toggleFavorite(this, '2510.21302v1', 'Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sanghyun Ahn, Wonje Choi, Junyong Lee, Jinwoo Park, Honguk Woo

**分类**: cs.AI, cs.RO

**发布日期**: 2025-10-24

**备注**: Accepted at NeurIPS 2025 Spotlight

---

## 💡 一句话要点

**提出神经符号框架，提升具身任务规划中代码策略的可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `任务规划` `神经符号` `代码策略` `大型语言模型` `环境感知` `交互式验证`

## 📋 核心要点

1. 基于LLM的代码策略在具身智能任务中表现出潜力，但其环境感知能力在动态环境中受限，导致任务成功率降低。
2. 论文提出一种神经符号框架，通过符号验证和交互式验证增强代码的环境感知，提升任务规划的可靠性。
3. 实验结果表明，该框架在RLBench和真实环境中，任务成功率显著提升，动作可执行性也得到提高。

## 📝 摘要（中文）

本文提出了一种神经符号具身任务规划框架，旨在解决基于大型语言模型（LLM）的代码策略在动态或部分可观察环境中环境感知不足的问题。该框架在代码生成过程中融入了显式的符号验证和交互式验证流程。在验证阶段，框架生成探索性代码，主动与环境交互以获取缺失的观察信息，同时保持与任务相关的状态。这种集成过程增强了生成代码的环境感知能力，从而提高了复杂环境中任务的可靠性和成功率。在RLBench和真实世界环境中的实验结果表明，该框架的任务成功率比代码策略基线提高了46.2%，并且任务相关动作的可执行性达到了86.8%以上，从而提高了动态环境中任务规划的可靠性。

## 🔬 方法详解

**问题定义**：现有基于大型语言模型的代码策略方法在具身任务规划中，尤其是在动态或部分可观察的环境中，存在环境感知不足的问题。这导致生成的代码不正确或不完整，最终影响任务的成功率。这些方法难以有效利用环境信息，无法应对环境变化带来的挑战。

**核心思路**：论文的核心思路是在代码生成过程中引入神经符号方法，结合符号验证和交互式验证。通过符号验证确保代码的逻辑正确性，并通过交互式验证让智能体主动探索环境，获取缺失的观察信息，从而增强代码的环境感知能力。这种结合符号推理和环境交互的方式，旨在提高代码策略的可靠性和鲁棒性。

**技术框架**：该框架包含代码生成、符号验证和交互式验证三个主要阶段。首先，利用大型语言模型生成初始代码。然后，通过符号验证模块检查代码的逻辑一致性和正确性。如果验证失败或需要更多环境信息，则进入交互式验证阶段，生成探索性代码与环境交互，获取缺失的观察信息并更新状态。最后，根据更新后的状态重新生成或修正代码，并再次进行验证，直至代码满足要求。

**关键创新**：该论文的关键创新在于将神经方法（LLM代码生成）与符号方法（代码验证）相结合，并引入了交互式验证机制。与传统的代码策略方法相比，该框架能够主动获取环境信息，并利用符号推理保证代码的正确性，从而显著提高了代码策略的可靠性和鲁棒性。

**关键设计**：交互式验证阶段是关键设计之一。该阶段设计了探索性代码生成策略，引导智能体主动探索环境，获取与任务相关的观察信息。具体实现细节（如探索策略、状态更新机制等）论文中可能有所描述，但摘要中未明确指出。损失函数和网络结构等细节也未在摘要中提及，属于未知信息。

## 📊 实验亮点

实验结果表明，该框架在RLBench和真实世界环境中，任务成功率比代码策略基线提高了46.2%，并且任务相关动作的可执行性达到了86.8%以上。这些数据表明，该框架能够显著提高代码策略的可靠性和鲁棒性，尤其是在动态和部分可观察的环境中。

## 🎯 应用场景

该研究成果可应用于机器人、自动驾驶、虚拟助手等领域，提升智能体在复杂、动态环境中的任务执行能力。通过提高代码策略的可靠性，可以减少人工干预，实现更自主、更智能的自动化系统。未来，该方法有望扩展到更广泛的具身智能任务中，例如家庭服务、工业自动化等。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have enabled the automatic generation of executable code for task planning and control in embodied agents such as robots, demonstrating the potential of LLM-based embodied intelligence. However, these LLM-based code-as-policies approaches often suffer from limited environmental grounding, particularly in dynamic or partially observable settings, leading to suboptimal task success rates due to incorrect or incomplete code generation. In this work, we propose a neuro-symbolic embodied task planning framework that incorporates explicit symbolic verification and interactive validation processes during code generation. In the validation phase, the framework generates exploratory code that actively interacts with the environment to acquire missing observations while preserving task-relevant states. This integrated process enhances the grounding of generated code, resulting in improved task reliability and success rates in complex environments. We evaluate our framework on RLBench and in real-world settings across dynamic, partially observable scenarios. Experimental results demonstrate that our framework improves task success rates by 46.2% over Code-as-Policies baselines and attains over 86.8% executability of task-relevant actions, thereby enhancing the reliability of task planning in dynamic environments.

