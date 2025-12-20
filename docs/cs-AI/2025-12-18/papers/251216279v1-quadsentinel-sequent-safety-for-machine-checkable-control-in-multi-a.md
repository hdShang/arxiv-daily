---
layout: default
title: QuadSentinel: Sequent Safety for Machine-Checkable Control in Multi-agent Systems
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

**QuadSentinel：多智能体系统中基于时序的安全策略可验证控制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `安全策略` `机器可验证控制` `时序逻辑` `智能体架构`

## 📋 核心要点

1. 现有方法难以将自然语言安全策略转化为机器可验证规则，导致运行时强制执行不可靠。
2. QuadSentinel 提出四智能体守卫架构，将安全策略编译为基于状态谓词的机器可检查规则，并在线执行。
3. 实验表明，QuadSentinel 提高了护栏精度和规则召回率，减少了误报，并优于单智能体基线。

## 📝 摘要（中文）

当基于大型语言模型的智能体使用工具、多步计划和智能体间消息解决复杂任务时，会产生安全风险。然而，部署者编写的自然语言策略是模糊且依赖上下文的，因此它们很难映射到机器可检查的规则，并且运行时强制执行是不可靠的。本文将安全策略表示为时序逻辑，提出了	extsc{QuadSentinel}，一个四智能体守卫（状态跟踪器、策略验证器、威胁观察器和裁判），它将这些策略编译成由可观察状态上的谓词构建的机器可检查规则，并在在线强制执行它们。裁判逻辑加上高效的 top-$k$ 谓词更新器，通过优先检查和分层解决冲突来降低成本。在 ST-WebAgentBench (ICML CUA~'25) 和 AgentHarm (ICLR~'25) 上的测量表明，	extsc{QuadSentinel} 提高了护栏精度和规则召回率，同时减少了误报。与 ShieldAgent (ICML~'25) 等单智能体基线相比，它产生了更好的整体安全控制。通过保持策略分离和机器可检查，近期部署可以在不修改核心智能体的情况下采用这种模式。我们的代码将在 https://github.com/yyiliu/QuadSentinel 上公开。

## 🔬 方法详解

**问题定义**：论文旨在解决多智能体系统中，基于大型语言模型的智能体在执行复杂任务时产生的安全风险问题。现有方法依赖自然语言描述的安全策略，这些策略模糊且依赖上下文，难以转化为机器可验证的规则，导致运行时安全控制效果不佳。现有方法缺乏一种有效的机制，能够将高层次的安全策略转化为可执行的、机器可验证的规则，并在运行时进行可靠的强制执行。

**核心思路**：论文的核心思路是将安全策略表示为时序逻辑，并设计一个四智能体守卫架构（QuadSentinel），将这些策略编译成基于可观察状态谓词的机器可检查规则。通过在线强制执行这些规则，实现对多智能体系统的安全控制。这种设计旨在解决自然语言策略的模糊性和不可靠性问题，提供一种更精确、可验证的安全保障机制。

**技术框架**：QuadSentinel 包含四个主要智能体：状态跟踪器（State Tracker）、策略验证器（Policy Verifier）、威胁观察器（Threat Watcher）和裁判（Referee）。状态跟踪器负责监控和记录系统的状态信息；策略验证器将安全策略编译成机器可检查的规则；威胁观察器检测潜在的威胁和违规行为；裁判负责仲裁冲突，并根据策略验证器的结果执行相应的安全措施。整个流程是：状态跟踪器提供状态信息，策略验证器验证策略，威胁观察器检测威胁，最后裁判根据前三者的信息做出决策。

**关键创新**：论文的关键创新在于提出了 QuadSentinel 架构，将安全策略的制定、验证和执行分离到不同的智能体中，实现了模块化和可验证的安全控制。此外，论文还引入了裁判逻辑和高效的 top-$k$ 谓词更新器，用于降低计算成本，并优先检查和分层解决冲突。这种架构能够有效地将高层次的安全策略转化为可执行的、机器可验证的规则，并在运行时进行可靠的强制执行。

**关键设计**：论文的关键设计包括：1) 将安全策略表示为时序逻辑，使其更易于形式化验证；2) 设计了四智能体架构，实现了安全控制的模块化和可扩展性；3) 引入了裁判逻辑和 top-$k$ 谓词更新器，用于降低计算成本和提高效率。具体的参数设置、损失函数和网络结构等技术细节在论文中未详细描述，属于未知信息。

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

实验结果表明，QuadSentinel 在 ST-WebAgentBench 和 AgentHarm 数据集上，提高了护栏精度和规则召回率，同时减少了误报。与 ShieldAgent 等单智能体基线相比，QuadSentinel 实现了更好的整体安全控制，验证了其有效性。

## 🎯 应用场景

该研究成果可应用于各种多智能体系统，例如自动驾驶、机器人协作、智能家居等领域。通过部署 QuadSentinel，可以有效提高系统的安全性，防止潜在的风险和违规行为。该方法具有广泛的应用前景，有助于构建更安全、可靠的智能系统。

## 📄 摘要（原文）

> Safety risks arise as large language model-based agents solve complex tasks with tools, multi-step plans, and inter-agent messages. However, deployer-written policies in natural language are ambiguous and context dependent, so they map poorly to machine-checkable rules, and runtime enforcement is unreliable. Expressing safety policies as sequents, we propose \textsc{QuadSentinel}, a four-agent guard (state tracker, policy verifier, threat watcher, and referee) that compiles these policies into machine-checkable rules built from predicates over observable state and enforces them online. Referee logic plus an efficient top-$k$ predicate updater keeps costs low by prioritizing checks and resolving conflicts hierarchically. Measured on ST-WebAgentBench (ICML CUA~'25) and AgentHarm (ICLR~'25), \textsc{QuadSentinel} improves guardrail accuracy and rule recall while reducing false positives. Against single-agent baselines such as ShieldAgent (ICML~'25), it yields better overall safety control. Near-term deployments can adopt this pattern without modifying core agents by keeping policies separate and machine-checkable. Our code will be made publicly available at https://github.com/yyiliu/QuadSentinel.

