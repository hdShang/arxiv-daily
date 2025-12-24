---
layout: default
title: DriveMoE: Mixture-of-Experts for Vision-Language-Action Model in End-to-End Autonomous Driving
---

# DriveMoE: Mixture-of-Experts for Vision-Language-Action Model in End-to-End Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.16278" class="toolbar-btn" target="_blank">📄 arXiv: 2505.16278v1</a>
  <a href="https://arxiv.org/pdf/2505.16278.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.16278v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.16278v1', 'DriveMoE: Mixture-of-Experts for Vision-Language-Action Model in End-to-End Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenjie Yang, Yilin Chai, Xiaosong Jia, Qifeng Li, Yuqian Shao, Xuekai Zhu, Haisheng Su, Junchi Yan

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-05-22

**备注**: Project Page: https://thinklab-sjtu.github.io/DriveMoE/

---

## 💡 一句话要点

**提出DriveMoE以解决端到端自动驾驶中的复杂场景处理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `端到端自动驾驶` `混合专家` `视觉-语言-动作` `动态路由` `行为专门化` `复杂场景处理` `智能交通`

## 📋 核心要点

1. 现有的端到端自动驾驶方法在处理复杂驾驶场景时存在不足，尤其是在应对稀有和激进的驾驶行为时。
2. 论文提出的DriveMoE框架通过引入视觉和动作的混合专家机制，动态选择相关信息以提高决策效率。
3. 在Bench2Drive评估实验中，DriveMoE达到了最先进的性能，显示出其在多样化场景处理上的优势。

## 📝 摘要（中文）

端到端自动驾驶（E2E-AD）需要有效处理多视角传感器数据，并稳健应对多样且复杂的驾驶场景，尤其是稀有的激进转弯等动作。本文提出DriveMoE，一个基于混合专家（MoE）的E2E-AD框架，包含场景专用的视觉MoE和技能专用的动作MoE。DriveMoE在我们的$π_0$视觉-语言-动作（VLA）基线Drive-$π_0$基础上构建，通过训练路由器动态选择与驾驶上下文相关的摄像头，模拟人类驾驶认知。通过明确的行为专门化，DriveMoE能够处理多样场景，而不受现有模型的模式平均影响。在Bench2Drive闭环评估实验中，DriveMoE实现了最先进的性能，展示了视觉和动作MoE结合在自动驾驶任务中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决端到端自动驾驶中对复杂多样驾驶场景的处理问题，现有方法在面对稀有驾驶行为时容易出现模式平均现象，导致性能下降。

**核心思路**：DriveMoE通过引入混合专家架构，分别针对视觉和动作进行专门化处理，动态选择与当前驾驶情境相关的专家模块，以模拟人类驾驶者的选择性注意机制。

**技术框架**：DriveMoE框架包括两个主要模块：场景专用的视觉MoE和技能专用的动作MoE。视觉MoE通过路由器选择合适的摄像头输入，而动作MoE则通过另一个路由器激活不同的专家模块以应对特定的驾驶行为。

**关键创新**：DriveMoE的核心创新在于通过明确的行为专门化，避免了传统模型的模式平均问题，从而提升了在复杂场景下的决策能力。

**关键设计**：在模型设计中，路由器的训练策略和专家模块的选择机制是关键，确保系统能够根据实时驾驶上下文动态调整其决策过程。

## 📊 实验亮点

在Bench2Drive闭环评估实验中，DriveMoE实现了最先进的性能，显著优于基线模型Drive-$π_0$，具体性能数据未披露，但实验结果表明其在复杂驾驶场景中的处理能力得到了显著提升。

## 🎯 应用场景

DriveMoE的研究成果在自动驾驶领域具有广泛的应用潜力，能够提升自动驾驶系统在复杂和动态环境中的表现。未来，该框架可扩展至其他需要实时决策的领域，如机器人导航和智能交通管理，推动智能交通系统的发展。

## 📄 摘要（原文）

> End-to-end autonomous driving (E2E-AD) demands effective processing of multi-view sensory data and robust handling of diverse and complex driving scenarios, particularly rare maneuvers such as aggressive turns. Recent success of Mixture-of-Experts (MoE) architecture in Large Language Models (LLMs) demonstrates that specialization of parameters enables strong scalability. In this work, we propose DriveMoE, a novel MoE-based E2E-AD framework, with a Scene-Specialized Vision MoE and a Skill-Specialized Action MoE. DriveMoE is built upon our $π_0$ Vision-Language-Action (VLA) baseline (originally from the embodied AI field), called Drive-$π_0$. Specifically, we add Vision MoE to Drive-$π_0$ by training a router to select relevant cameras according to the driving context dynamically. This design mirrors human driving cognition, where drivers selectively attend to crucial visual cues rather than exhaustively processing all visual information. In addition, we add Action MoE by training another router to activate specialized expert modules for different driving behaviors. Through explicit behavioral specialization, DriveMoE is able to handle diverse scenarios without suffering from modes averaging like existing models. In Bench2Drive closed-loop evaluation experiments, DriveMoE achieves state-of-the-art (SOTA) performance, demonstrating the effectiveness of combining vision and action MoE in autonomous driving tasks. We will release our code and models of DriveMoE and Drive-$π_0$.

