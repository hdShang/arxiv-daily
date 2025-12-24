---
layout: default
title: "Towards Human-Centric Autonomous Driving: A Fast-Slow Architecture Integrating Large Language Model Guidance with Reinforcement Learning"
---

# Towards Human-Centric Autonomous Driving: A Fast-Slow Architecture Integrating Large Language Model Guidance with Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06875" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06875v1</a>
  <a href="https://arxiv.org/pdf/2505.06875.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06875v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06875v1', 'Towards Human-Centric Autonomous Driving: A Fast-Slow Architecture Integrating Large Language Model Guidance with Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengkai Xu, Jiaqi Liu, Yicheng Guo, Yuhang Zhang, Peng Hang, Jian Sun

**分类**: cs.RO

**发布日期**: 2025-05-11

---

## 💡 一句话要点

**提出快慢决策框架以解决人机交互不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `人机交互` `强化学习` `大型语言模型` `个性化驾驶` `决策框架` `安全性` `实时控制`

## 📋 核心要点

1. 现有自动驾驶方法常常忽视用户的个性化需求，导致交互和适应能力不足。
2. 本文提出了一种快慢决策框架，将大型语言模型与强化学习结合，实现高效的用户指令解析与实时决策。
3. 实验结果显示，该框架在降低碰撞率的同时，更好地符合用户的驾驶偏好，提升了安全性和可靠性。

## 📝 摘要（中文）

自动驾驶技术在数据驱动方法上取得了显著进展，但现有方法常常忽视用户特定偏好，缺乏与用户的互动和适应能力。为了解决这些挑战，本文提出了一种“快慢”决策框架，结合大型语言模型（LLM）进行高层指令解析和强化学习（RL）代理进行低层实时决策。在该双重系统中，LLM作为“慢”模块，将用户指令转化为结构化指导，而RL代理作为“快”模块，在严格的延迟约束下进行时间敏感的操作。实验评估表明，该方法在各种驾驶场景中有效降低了碰撞率，并更好地与用户偏好对齐，实现了以人为本的驾驶模式。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动驾驶系统在用户个性化需求和实时决策之间的矛盾，现有方法往往无法有效整合用户指令与驾驶行为。

**核心思路**：提出快慢决策框架，LLM负责高层指令解析，RL代理负责低层实时决策，从而实现个性化与安全性的平衡。

**技术框架**：整体架构分为两个主要模块：慢模块（LLM）用于解析用户指令并生成结构化指导，快模块（RL代理）负责在严格的时间限制下执行决策。

**关键创新**：通过将高层决策与快速控制解耦，本文的框架实现了个性化的用户中心操作，同时保持了安全边际，这与传统方法的集成式决策方式有本质区别。

**关键设计**：在设计中，LLM的输出结构化指导包括用户偏好的多样化表达，而RL代理则采用强化学习算法优化决策过程，确保在复杂交通环境中的实时响应能力。

## 📊 实验亮点

实验结果表明，所提框架在多种驾驶场景下有效降低了碰撞率，与基线算法相比，碰撞率降低了显著幅度，同时驾驶行为与用户偏好的契合度提高，展示了人机交互的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、自动驾驶汽车以及人机交互界面等。通过实现用户个性化的驾驶体验，未来可提升乘客的安全感和满意度，推动自动驾驶技术的广泛应用。

## 📄 摘要（原文）

> Autonomous driving has made significant strides through data-driven techniques, achieving robust performance in standardized tasks. However, existing methods frequently overlook user-specific preferences, offering limited scope for interaction and adaptation with users. To address these challenges, we propose a "fast-slow" decision-making framework that integrates a Large Language Model (LLM) for high-level instruction parsing with a Reinforcement Learning (RL) agent for low-level real-time decision. In this dual system, the LLM operates as the "slow" module, translating user directives into structured guidance, while the RL agent functions as the "fast" module, making time-critical maneuvers under stringent latency constraints. By decoupling high-level decision making from rapid control, our framework enables personalized user-centric operation while maintaining robust safety margins. Experimental evaluations across various driving scenarios demonstrate the effectiveness of our method. Compared to baseline algorithms, the proposed architecture not only reduces collision rates but also aligns driving behaviors more closely with user preferences, thereby achieving a human-centric mode. By integrating user guidance at the decision level and refining it with real-time control, our framework bridges the gap between individual passenger needs and the rigor required for safe, reliable driving in complex traffic environments.

