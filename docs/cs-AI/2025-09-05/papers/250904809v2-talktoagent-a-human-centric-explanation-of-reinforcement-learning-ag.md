---
layout: default
title: "TalkToAgent: A Human-centric Explanation of Reinforcement Learning Agents with Large Language Models"
---

# TalkToAgent: A Human-centric Explanation of Reinforcement Learning Agents with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04809" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04809v2</a>
  <a href="https://arxiv.org/pdf/2509.04809.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04809v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04809v2', 'TalkToAgent: A Human-centric Explanation of Reinforcement Learning Agents with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haechang Kim, Hao Chen, Can Li, Jong Min Lee

**分类**: cs.AI, cs.HC

**发布日期**: 2025-09-05 (更新: 2025-09-08)

**备注**: 31 pages total

---

## 💡 一句话要点

**提出TalkToAgent，利用LLM实现人机交互式强化学习智能体解释**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可解释强化学习` `大型语言模型` `人机交互` `反事实解释` `多智能体系统`

## 📋 核心要点

1. 现有可解释强化学习方法难以被领域专家理解，且工具覆盖范围有限，用户难以选择。
2. TalkToAgent利用多智能体LLM框架，将用户查询映射到XRL工具，并提供自然语言解释。
3. 实验表明，TalkToAgent能准确映射用户查询，有效解释智能体行为，并减少反事实生成失败。

## 📝 摘要（中文）

可解释强化学习(XRL)在提高强化学习(RL)智能体的透明度方面展现出巨大潜力。然而，由于XRL结果的理解难度以及现有XRL方法覆盖范围的局限性，复杂的RL策略与领域专家之间仍然存在差距，用户不确定该使用哪种工具。为了解决这些挑战，我们提出了TalkToAgent，一个多智能体大型语言模型(LLM)框架，它为RL策略提供交互式的自然语言解释。该架构包含五个专门的LLM智能体（协调器、解释器、编码器、评估器和调试器），使TalkToAgent能够自动将用户查询映射到相关的XRL工具，并根据关键状态变量、预期结果或反事实解释来阐明智能体的行为。此外，我们的方法通过从定性的行为描述甚至新的基于规则的策略中推导出替代方案，扩展了先前的反事实解释。我们在四罐过程控制问题（一个著名的非线性控制基准）上验证了TalkToAgent。结果表明，TalkToAgent成功地将用户查询映射到XRL任务，并具有很高的准确性，并且编码器-调试器交互最大限度地减少了反事实生成的失败。此外，定性评估证实了TalkToAgent有效地解释了智能体的行为，并在问题领域内对其含义进行了情境化。

## 🔬 方法详解

**问题定义**：现有的可解释强化学习(XRL)方法生成的解释难以被领域专家理解，并且各种XRL工具之间缺乏整合，用户难以选择合适的工具来理解强化学习智能体的行为。这导致了RL策略的透明度不足，阻碍了其在实际场景中的应用。

**核心思路**：TalkToAgent的核心思路是利用大型语言模型(LLM)的强大自然语言处理能力，构建一个多智能体系统，该系统能够理解用户的查询，自动选择合适的XRL工具，并以自然语言的形式向用户解释强化学习智能体的行为。通过这种方式，弥合了RL策略与领域专家之间的鸿沟，提高了RL策略的可理解性和可信度。

**技术框架**：TalkToAgent的整体架构包含五个主要的LLM智能体：协调器(Coordinator)、解释器(Explainer)、编码器(Coder)、评估器(Evaluator)和调试器(Debugger)。协调器负责接收用户查询，并将其分配给合适的智能体进行处理。解释器负责根据智能体的行为生成自然语言解释。编码器负责将自然语言描述转换为可执行的代码或策略。评估器负责评估生成的代码或策略的性能。调试器负责修复编码器生成的代码中的错误。这些智能体协同工作，共同完成用户提出的XRL任务。

**关键创新**：TalkToAgent的关键创新在于其多智能体LLM框架，该框架能够自动将用户查询映射到相关的XRL工具，并以自然语言的形式提供解释。此外，该方法还扩展了先前的反事实解释，能够从定性的行为描述甚至新的基于规则的策略中推导出替代方案。这种交互式的解释方式使得用户能够更深入地理解强化学习智能体的行为。

**关键设计**：TalkToAgent的关键设计包括：(1) 五个LLM智能体的角色定义和协作机制；(2) 用户查询到XRL工具的映射策略；(3) 自然语言解释的生成方法；(4) 反事实解释的推导方法；(5) 编码器和调试器之间的迭代优化过程。具体的参数设置、损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，TalkToAgent能够以高准确率将用户查询映射到XRL任务。编码器-调试器交互显著减少了反事实生成的失败。定性评估证实，TalkToAgent能够有效地解释智能体的行为，并在问题领域内对其含义进行情境化。具体的性能数据和对比基线在摘要中未提供，属于未知信息。

## 🎯 应用场景

TalkToAgent可应用于各种需要人机协作的强化学习场景，例如机器人控制、自动驾驶、智能推荐系统等。通过提供可解释的智能体行为，可以提高用户对系统的信任度，并促进人与智能体之间的有效协作。该研究的未来影响在于推动可解释人工智能的发展，使AI系统更加透明、可信和易于理解。

## 📄 摘要（原文）

> Explainable Reinforcement Learning (XRL) has emerged as a promising approach in improving the transparency of Reinforcement Learning (RL) agents. However, there remains a gap between complex RL policies and domain experts, due to the limited comprehensibility of XRL results and isolated coverage of current XRL approaches that leave users uncertain about which tools to employ. To address these challenges, we introduce TalkToAgent, a multi-agent Large Language Models (LLM) framework that delivers interactive, natural language explanations for RL policies. The architecture with five specialized LLM agents (Coordinator, Explainer, Coder, Evaluator, and Debugger) enables TalkToAgent to automatically map user queries to relevant XRL tools and clarify an agent's actions in terms of either key state variables, expected outcomes, or counterfactual explanations. Moreover, our approach extends previous counterfactual explanations by deriving alternative scenarios from qualitative behavioral descriptions, or even new rule-based policies. We validated TalkToAgent on quadruple-tank process control problem, a well-known nonlinear control benchmark. Results demonstrated that TalkToAgent successfully mapped user queries into XRL tasks with high accuracy, and coder-debugger interactions minimized failures in counterfactual generation. Furthermore, qualitative evaluation confirmed that TalkToAgent effectively interpreted agent's actions and contextualized their meaning within the problem domain.

