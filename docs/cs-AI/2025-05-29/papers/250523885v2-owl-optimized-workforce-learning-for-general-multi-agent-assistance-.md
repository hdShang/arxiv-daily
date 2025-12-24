---
layout: default
title: OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation
---

# OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23885" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23885v2</a>
  <a href="https://arxiv.org/pdf/2505.23885.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23885v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23885v2', 'OWL: Optimized Workforce Learning for General Multi-Agent Assistance in Real-World Task Automation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mengkang Hu, Yuhang Zhou, Wendong Fan, Yuzhou Nie, Bowei Xia, Tao Sun, Ziyu Ye, Zhaoxuan Jin, Yingru Li, Qiguang Chen, Zeyu Zhang, Yifeng Wang, Qianshuo Ye, Bernard Ghanem, Ping Luo, Guohao Li

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-29 (更新: 2025-06-11)

**备注**: Project Page: https://github.com/camel-ai/owl

---

## 💡 一句话要点

**提出优化工作学习框架以解决多领域任务自动化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `任务自动化` `领域迁移` `强化学习` `模块化架构` `优化工作学习` `智能助手`

## 📋 核心要点

1. 现有的多智能体系统在跨领域迁移时面临架构重构和全量重训练的挑战，限制了其应用范围。
2. 本文提出了Workforce框架，通过解耦战略规划与执行，实现了领域无关的任务处理和高效的跨领域适应。
3. 实验结果显示，Workforce在GAIA基准测试中达到了69.70%的性能，超越了OpenAI的Deep Research系统，并且在复杂任务上与GPT-4o的表现相当。

## 📝 摘要（中文）

基于大型语言模型的多智能体系统在自动化现实任务方面展现出潜力，但由于其领域特定的特性，跨领域迁移存在困难。现有方法面临两个主要短板：在应用于新领域时需要完全重构架构和重新训练所有组件。为此，本文提出了Workforce，一个层次化的多智能体框架，通过模块化架构将战略规划与专业执行解耦。该框架包括：一个领域无关的规划器用于任务分解，一个协调器用于子任务管理，以及具有领域特定工具调用能力的专业工作者。通过这种解耦，Workforce在推理和训练阶段均能实现跨领域迁移。实验结果表明，Workforce在GAIA基准测试中达到了开源的最先进性能，超越了商业系统。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多智能体系统在跨领域任务自动化中的迁移困难，尤其是架构重构和全量重训练的问题。

**核心思路**：通过引入Workforce框架，将战略规划与执行解耦，使得系统能够在不同领域中灵活适应，提升任务处理的效率和效果。

**技术框架**：Workforce框架由三个主要模块组成：领域无关的规划器负责任务分解，协调器管理子任务，而专业工作者则具备领域特定的工具调用能力。这样的设计使得系统在推理时可以根据需要添加或修改工作者。

**关键创新**：最重要的创新在于引入了优化工作学习（OWL），通过强化学习从现实反馈中优化领域无关的规划器，从而提升了跨领域的泛化能力。

**关键设计**：在训练过程中，OWL通过实时反馈调整规划器的策略，确保其能够适应不同领域的任务需求。具体的参数设置和损失函数设计尚未详细披露，属于未知领域。

## 📊 实验亮点

实验结果显示，Workforce在GAIA基准测试中达到了69.70%的性能，超越了OpenAI的Deep Research系统2.34%。此外，经过OWL训练的32B模型在复杂任务上达到了52.73%的准确率，相较于之前提升了16.37%。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化客服、智能家居等多个场景，能够显著提升多智能体系统在不同领域的适应能力和任务执行效率。未来，该框架可能推动更广泛的通用人工智能助手的发展，满足多样化的用户需求。

## 📄 摘要（原文）

> Large Language Model (LLM)-based multi-agent systems show promise for automating real-world tasks but struggle to transfer across domains due to their domain-specific nature. Current approaches face two critical shortcomings: they require complete architectural redesign and full retraining of all components when applied to new domains. We introduce Workforce, a hierarchical multi-agent framework that decouples strategic planning from specialized execution through a modular architecture comprising: (i) a domain-agnostic Planner for task decomposition, (ii) a Coordinator for subtask management, and (iii) specialized Workers with domain-specific tool-calling capabilities. This decoupling enables cross-domain transferability during both inference and training phases: During inference, Workforce seamlessly adapts to new domains by adding or modifying worker agents; For training, we introduce Optimized Workforce Learning (OWL), which improves generalization across domains by optimizing a domain-agnostic planner with reinforcement learning from real-world feedback. To validate our approach, we evaluate Workforce on the GAIA benchmark, covering various realistic, multi-domain agentic tasks. Experimental results demonstrate Workforce achieves open-source state-of-the-art performance (69.70%), outperforming commercial systems like OpenAI's Deep Research by 2.34%. More notably, our OWL-trained 32B model achieves 52.73% accuracy (+16.37%) and demonstrates performance comparable to GPT-4o on challenging tasks. To summarize, by enabling scalable generalization and modular domain transfer, our work establishes a foundation for the next generation of general-purpose AI assistants.

