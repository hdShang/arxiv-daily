---
layout: default
title: "RobotxR1: Enabling Embodied Robotic Intelligence on Large Language Models through Closed-Loop Reinforcement Learning"
---

# RobotxR1: Enabling Embodied Robotic Intelligence on Large Language Models through Closed-Loop Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03238" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03238v2</a>
  <a href="https://arxiv.org/pdf/2505.03238.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03238v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03238v2', 'RobotxR1: Enabling Embodied Robotic Intelligence on Large Language Models through Closed-Loop Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liam Boyle, Nicolas Baumann, Paviththiren Sivasothilingam, Michele Magno, Luca Benini

**分类**: cs.RO

**发布日期**: 2025-05-06 (更新: 2025-08-30)

---

## 💡 一句话要点

**提出基于闭环强化学习的R1-Zero方法以提升机器人智能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `闭环强化学习` `嵌入式智能` `小型语言模型` `自主驾驶` `机器人推理`

## 📋 核心要点

1. 现有方法在机器人智能中依赖于大型模型，导致计算和内存需求高，限制了其在嵌入式系统中的应用。
2. 本文提出了一种新的闭环强化学习框架，结合低参数量的LLMs，增强了机器人在动态环境中的推理能力。
3. 实验结果显示，Qwen2.5-1.5B模型在自主驾驶任务中比基线提升20.2%，而Qwen2.5-3B模型的控制适应性得分达到63.3%，超越了更大的GPT-4o。

## 📝 摘要（中文）

未来的机器人系统需要在没有持续云连接的情况下具备嵌入式智能，同时平衡计算能力和内存的限制。本文扩展了R1-Zero方法，使低参数量的大型语言模型（LLMs）能够在机器人领域应用。通过将其集成到闭环强化学习框架中，增强了嵌入式人工智能的推理能力，而不再单纯依赖于大模型的蒸馏和监督微调。实验表明，小规模LLMs通过与环境的闭环交互能够实现有效的推理性能，甚至在自主驾驶场景中超越了基于监督微调的基线，展示了小型LLMs在实际应用中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有机器人系统在嵌入式环境中对大型语言模型的依赖问题，现有方法在计算和内存方面存在显著限制，影响了智能推理能力的发挥。

**核心思路**：通过将R1-Zero方法扩展到闭环强化学习框架，允许小规模LLMs通过与环境的交互进行学习，从而提升推理能力，而不依赖于传统的监督微调。

**技术框架**：整体架构包括环境交互模块、反馈学习模块和推理模块。机器人通过与环境的闭环交互获取反馈，进而调整其行为策略，提升智能决策能力。

**关键创新**：最重要的创新在于通过闭环强化学习实现小型LLMs的有效推理，突破了传统依赖大型模型的局限，展示了小模型在实际应用中的潜力。

**关键设计**：在训练过程中，采用了特定的损失函数来优化模型的反馈学习能力，并设计了适合小规模模型的网络结构，以确保在资源受限的情况下仍能实现高效的推理。

## 📊 实验亮点

实验结果显示，Qwen2.5-1.5B模型在自主驾驶任务中相比基线提升了20.2个百分点，而Qwen2.5-3B模型的控制适应性得分为63.3%，超越了云端大型模型GPT-4o的58.5%。这些结果表明小型LLMs在环境反馈学习中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自主驾驶、智能家居机器人和服务机器人等。通过实现小型LLMs的嵌入式智能，机器人能够在复杂的现实环境中自主决策，提升其适应性和实用性，未来可能在各类机器人应用中发挥重要作用。

## 📄 摘要（原文）

> Future robotic systems operating in real-world environments will require on-board embodied intelligence without continuous cloud connection, balancing capabilities with constraints on computational power and memory. This work presents an extension of the R1-zero approach, which enables the usage of low parameter-count Large Language Models (LLMs) in the robotic domain. The R1-Zero approach was originally developed to enable mathematical reasoning in LLMs using static datasets. We extend it to the robotics domain through integration in a closed-loop Reinforcement Learning (RL) framework. This extension enhances reasoning in Embodied Artificial Intelligence (Embodied AI) settings without relying solely on distillation of large models through Supervised Fine-Tuning (SFT). We show that small-scale LLMs can achieve effective reasoning performance by learning through closed-loop interaction with their environment, which enables tasks that previously required significantly larger models. In an autonomous driving setting, a performance gain of 20.2%-points over the SFT-based baseline is observed with a Qwen2.5-1.5B model. Using the proposed training procedure, Qwen2.5-3B achieves a 63.3% control adaptability score, surpassing the 58.5% obtained by the much larger, cloud-bound GPT-4o. These results highlight that practical, on-board deployment of small LLMs is not only feasible but can outperform larger models if trained through environmental feedback, underscoring the importance of an interactive learning framework for robotic Embodied AI, one grounded in practical experience rather than static supervision.

