---
layout: default
title: "BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent"
---

# BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15566" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15566v4</a>
  <a href="https://arxiv.org/pdf/2509.15566.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15566v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15566v4', 'BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaojie Zhang, Ruoceng Zhang, Pei Fu, Shaokang Wang, Jiahui Yang, Xin Du, Shiqi Cui, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-19 (更新: 2025-10-27)

**备注**: Accepted at NeurIPS 2025

---

## 💡 一句话要点

**提出BTL-UI模型，模拟人脑认知过程，提升GUI智能体的交互能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GUI智能体` `人机交互` `认知模型` `强化学习` `多模态学习`

## 📋 核心要点

1. 现有多模态大语言模型和强化学习微调技术在GUI交互自动化中取得进展，但交互逻辑与人类自然模式存在偏差。
2. 提出BTL框架，模拟人脑“Blink-Think-Link”认知过程，将交互分解为快速检测、高层推理和命令生成三个阶段。
3. 构建BTL-UI模型，并在GUI理解和交互任务上验证了框架的有效性，证明其在开发高级GUI智能体方面的潜力。

## 📝 摘要（中文）

本文针对AI驱动的人机界面(GUI)交互自动化领域中，现有方法交互逻辑偏离自然人机通信模式的挑战，提出了“Blink-Think-Link”(BTL)框架。该框架模仿人脑认知过程，将交互分解为三个阶段：(1) Blink：快速检测和关注屏幕相关区域；(2) Think：高层次推理和决策；(3) Link：生成可执行命令以进行精确运动控制。此外，还提出了Blink数据生成自动化标注流程和BTL奖励机制，后者是一种基于规则的奖励机制，可实现过程和结果双驱动的强化学习。基于此框架，开发了GUI智能体模型BTL-UI，并在静态GUI理解和动态交互任务中表现出竞争优势，验证了该框架在开发高级GUI智能体方面的有效性。

## 🔬 方法详解

**问题定义**：现有GUI智能体在人机交互时，其交互逻辑与人类的自然交互模式存在显著差异，导致智能体难以像人类一样自然、高效地与GUI进行交互。现有方法通常依赖于端到端的学习，缺乏对人类认知过程的建模，因此难以泛化到复杂的GUI交互场景。

**核心思路**：本文的核心思路是模仿人脑在人机交互中的认知过程，将交互过程分解为三个阶段：Blink（快速关注）、Think（高层推理）和Link（命令生成）。通过模拟人脑的认知机制，使GUI智能体的交互逻辑更接近人类，从而提高交互的自然性和效率。

**技术框架**：BTL框架包含三个主要阶段：1) Blink阶段：快速检测屏幕上的相关区域，类似于人类的眼动；2) Think阶段：进行高层次的推理和决策，类似于人类的认知规划；3) Link阶段：生成可执行的命令，用于精确的动作控制，类似于人类的动作选择机制。BTL-UI模型基于该框架构建，利用深度学习模型实现各个阶段的功能。

**关键创新**：本文的关键创新在于：1) 提出了BTL框架，将人机交互过程分解为三个具有生物学意义的阶段，更符合人类的认知模式；2) 提出了Blink数据生成自动化标注流程，解决了Blink阶段数据稀缺的问题；3) 提出了BTL奖励机制，该机制基于规则，能够同时考虑过程和结果，从而更有效地指导强化学习。

**关键设计**：Blink阶段使用目标检测模型快速定位屏幕上的相关元素。Think阶段使用大型语言模型进行推理和决策，选择合适的交互动作。Link阶段将推理结果转化为可执行的命令。BTL奖励机制根据交互过程中的中间状态和最终结果进行奖励，鼓励智能体采取更符合人类认知模式的交互方式。具体参数设置、损失函数和网络结构等细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

BTL-UI模型在静态GUI理解和动态交互任务中表现出竞争优势，证明了BTL框架的有效性。摘要中未提供具体的性能数据和对比基线，属于未知信息。但结论表明，该模型在开发高级GUI智能体方面具有潜力。

## 🎯 应用场景

该研究成果可应用于各种人机交互场景，例如自动化测试、智能助手、无障碍辅助等。通过模拟人类的认知过程，可以开发出更加智能、自然、高效的GUI智能体，提升用户体验，降低使用门槛。未来，该技术有望应用于更复杂的交互场景，例如虚拟现实、增强现实等。

## 📄 摘要（原文）

> In the field of AI-driven human-GUI interaction automation, while rapid advances in multimodal large language models and reinforcement fine-tuning techniques have yielded remarkable progress, a fundamental challenge persists: their interaction logic significantly deviates from natural human-GUI communication patterns. To fill this gap, we propose "Blink-Think-Link" (BTL), a brain-inspired framework for human-GUI interaction that mimics the human cognitive process between users and graphical interfaces. The system decomposes interactions into three biologically plausible phases: (1) Blink - rapid detection and attention to relevant screen areas, analogous to saccadic eye movements; (2) Think - higher-level reasoning and decision-making, mirroring cognitive planning; and (3) Link - generation of executable commands for precise motor control, emulating human action selection mechanisms. Additionally, we introduce two key technical innovations for the BTL framework: (1) Blink Data Generation - an automated annotation pipeline specifically optimized for blink data, and (2) BTL Reward -- the first rule-based reward mechanism that enables reinforcement learning driven by both process and outcome. Building upon this framework, we develop a GUI agent model named BTL-UI, which demonstrates competitive performance across both static GUI understanding and dynamic interaction tasks in comprehensive benchmarks. These results provide conclusive empirical validation of the framework's efficacy in developing advanced GUI Agents.

