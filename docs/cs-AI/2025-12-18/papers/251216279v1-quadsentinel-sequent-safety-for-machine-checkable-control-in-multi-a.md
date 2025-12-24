---
layout: default
title: "QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems"
---

# QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16279" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16279v1</a>
  <a href="https://arxiv.org/pdf/2512.16279.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16279v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16279v1', 'QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiliu Yang, Yilei Jiang, Qunzhong Wang, Yingshui Tan, Xiaoyong Zhu, Sherman S. M. Chow, Bo Zheng, Xiangyu Yue

**分类**: cs.AI, cs.CL

**发布日期**: 2025-12-18

**备注**: Preprint

**🔗 代码/项目**: [GITHUB](https://github.com/yyiliu/QuadSentinel)

---

## 💡 一句话要点

**QuadSentinel：多智能体系统中基于时序逻辑的安全可验证控制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `安全控制` `大型语言模型` `时序逻辑` `机器可验证` `智能体安全` `运行时监控`

## 📋 核心要点

1. 基于LLM的智能体在复杂任务中存在安全风险，而自然语言策略难以转化为机器可验证规则，运行时强制执行不可靠。
2. QuadSentinel将安全策略表示为时序逻辑，编译为机器可检查规则，并通过四智能体守卫系统在线强制执行。
3. 实验表明，QuadSentinel提高了护栏准确率和规则召回率，减少误报，并优于单智能体基线。

## 📝 摘要（中文）

基于大型语言模型（LLM）的智能体在解决复杂任务时，会利用工具、多步计划和智能体间消息，从而产生安全风险。然而，部署者编写的自然语言策略具有模糊性和上下文依赖性，难以映射到机器可检查的规则，并且运行时强制执行也不可靠。本文提出	extsc{QuadSentinel}，一种四智能体守卫（状态跟踪器、策略验证器、威胁观察器和裁判）系统，它将安全策略表示为时序逻辑，并将其编译为基于可观察状态谓词的机器可检查规则，并在运行时强制执行。裁判逻辑加上高效的top-$k$谓词更新器，通过优先检查和分层解决冲突来降低成本。在ST-WebAgentBench和AgentHarm上的实验表明，	extsc{QuadSentinel}提高了护栏的准确性和规则召回率，同时减少了误报。与ShieldAgent等单智能体基线相比，它产生了更好的整体安全控制。无需修改核心智能体，即可通过保持策略分离和机器可检查性来采用此模式进行近期部署。代码将在https://github.com/yyiliu/QuadSentinel公开。

## 🔬 方法详解

**问题定义**：论文旨在解决多智能体系统中，基于大型语言模型的智能体在执行复杂任务时产生的安全风险问题。现有方法，如直接使用自然语言策略进行安全控制，存在模糊性、上下文依赖性以及难以进行机器验证的痛点，导致运行时强制执行的可靠性不足。

**核心思路**：论文的核心思路是将安全策略形式化为时序逻辑（sequents），并将其编译成机器可检查的规则。通过引入一个四智能体守卫系统，在线监控和强制执行这些规则，从而提高安全控制的准确性和可靠性。这种方法将安全策略与核心智能体分离，便于维护和更新。

**技术框架**：QuadSentinel 包含四个核心智能体：状态跟踪器（State Tracker）、策略验证器（Policy Verifier）、威胁观察器（Threat Watcher）和裁判（Referee）。状态跟踪器负责监控环境和智能体的状态；策略验证器将状态信息与预定义的安全策略进行比对；威胁观察器检测潜在的威胁行为；裁判根据前三个智能体的输出，做出最终的安全决策并采取相应的行动。整个系统通过一个高效的 top-$k$ 谓词更新器来优化性能，优先检查最重要的规则，并分层解决冲突。

**关键创新**：论文的关键创新在于将安全策略表示为时序逻辑，并将其编译为机器可检查的规则。这种形式化的表示方法克服了自然语言策略的模糊性和不确定性，使得安全策略能够被机器精确地理解和执行。此外，四智能体守卫系统的设计也提高了安全控制的鲁棒性和可靠性。

**关键设计**：裁判逻辑是 QuadSentinel 的关键设计之一，它负责整合来自其他三个智能体的输出，并做出最终的安全决策。为了降低计算成本，系统采用了一个高效的 top-$k$ 谓词更新器，优先检查最重要的规则。此外，系统还采用了分层冲突解决机制，以确保安全决策的一致性和有效性。具体的参数设置、损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16279v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16279v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16279v1/imgs/harmful_by_category.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

QuadSentinel 在 ST-WebAgentBench 和 AgentHarm 两个基准测试中进行了评估。实验结果表明，QuadSentinel 提高了护栏的准确性和规则召回率，同时减少了误报。与 ShieldAgent 等单智能体基线相比，QuadSentinel 取得了更好的整体安全控制效果。具体的性能提升数据在摘要中未给出，属于未知信息。

## 🎯 应用场景

QuadSentinel 可应用于各种多智能体系统，例如自动驾驶、机器人协作、智能家居等。通过提供可验证的安全控制，它可以降低智能体系统在复杂环境中运行的风险，提高系统的可靠性和安全性。该研究对于推动安全可靠的人工智能应用具有重要意义。

## 📄 摘要（原文）

> Safety risks arise as large language model-based agents solve complex tasks with tools, multi-step plans, and inter-agent messages. However, deployer-written policies in natural language are ambiguous and context dependent, so they map poorly to machine-checkable rules, and runtime enforcement is unreliable. Expressing safety policies as sequents, we propose \textsc{QuadSentinel}, a four-agent guard (state tracker, policy verifier, threat watcher, and referee) that compiles these policies into machine-checkable rules built from predicates over observable state and enforces them online. Referee logic plus an efficient top-$k$ predicate updater keeps costs low by prioritizing checks and resolving conflicts hierarchically. Measured on ST-WebAgentBench (ICML CUA~'25) and AgentHarm (ICLR~'25), \textsc{QuadSentinel} improves guardrail accuracy and rule recall while reducing false positives. Against single-agent baselines such as ShieldAgent (ICML~'25), it yields better overall safety control. Near-term deployments can adopt this pattern without modifying core agents by keeping policies separate and machine-checkable. Our code will be made publicly available at https://github.com/yyiliu/QuadSentinel.

