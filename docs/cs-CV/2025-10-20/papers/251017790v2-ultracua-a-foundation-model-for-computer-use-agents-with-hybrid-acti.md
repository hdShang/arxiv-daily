---
layout: default
title: UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action
---

# UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.17790" target="_blank" class="toolbar-btn">arXiv: 2510.17790v2</a>
    <a href="https://arxiv.org/pdf/2510.17790.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17790v2" 
            onclick="toggleFavorite(this, '2510.17790v2', 'UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yuhao Yang, Zhen Yang, Zi-Yi Dou, Anh Nguyen, Keen You, Omar Attia, Andrew Szot, Michael Feng, Ram Ramrakhya, Alexander Toshev, Chao Huang, Yinfei Yang, Zhe Gan

**分类**: cs.CV, cs.CL

**发布日期**: 2025-10-20 (更新: 2025-12-10)

---

## 💡 一句话要点

**UltraCUA：融合GUI操作与高级工具的计算机使用Agent基础模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算机使用Agent` `混合动作` `基础模型` `强化学习` `GUI操作` `API调用` `自动化办公`

## 📋 核心要点

1. 现有计算机使用Agent过度依赖GUI操作，导致执行脆弱，易出错。
2. UltraCUA通过混合动作，融合GUI操作与高级工具调用，提升Agent能力。
3. 实验表明，UltraCUA在OSWorld和WindowsAgentArena上均取得显著性能提升。

## 📝 摘要（中文）

计算机使用Agent面临一个根本性限制：它们完全依赖于原始GUI操作（点击、输入、滚动），导致执行链脆弱且容易发生级联故障。虽然API驱动的Agent通过结构化接口和工具利用了丰富的功能，但计算机使用Agent仍然局限于低级视觉交互。我们提出了UltraCUA，一个通过混合动作超越这一限制的基础模型，它无缝地统一了原始GUI操作与高级工具执行。我们的创新基于四个关键进展。首先，一个自动化的pipeline从软件文档和代码仓库中提取并扩展工具能力。其次，一个合成数据引擎生成了17,000多个可验证的任务，捕捉了真实世界计算机使用的复杂性。第三，全面的混合动作轨迹收集包含了GUI原语和战略性工具调用。第四，一个两阶段训练方法结合了监督微调与在线强化学习，实现了GUI和API之间智能的动作选择。使用我们的7B和32B UltraCUA模型进行的评估显示了变革性的性能提升。在OSWorld上，UltraCUA实现了22%的相对改进，同时比现有方法平均快11%。在WindowsAgentArena上的跨域验证表明了强大的泛化能力，成功率为21.7%，超过了Windows训练的基线。混合动作范例被证明是必不可少的，减少了错误传播，同时提高了执行效率。这项工作建立了一个可扩展的范例，桥接了原始GUI交互和高级工具智能，为各种环境和复杂的真实世界任务实现了更具弹性和适应性的计算机使用Agent。

## 🔬 方法详解

**问题定义**：现有计算机使用Agent主要依赖于低级的GUI操作，例如点击、输入和滚动。这种方式导致执行流程非常脆弱，容易因为细微的环境变化而失败，从而产生级联错误。同时，它们无法有效利用软件本身提供的API和工具，限制了其解决复杂问题的能力。

**核心思路**：UltraCUA的核心思路是引入混合动作空间，将低级的GUI操作与高级的工具调用结合起来。Agent可以根据当前的任务和环境，智能地选择使用哪种动作。通过利用高级工具，可以减少对GUI操作的依赖，提高执行的效率和鲁棒性。

**技术框架**：UltraCUA的整体框架包含以下几个主要模块：1) **工具能力提取pipeline**：从软件文档和代码仓库中自动提取工具信息，构建工具库。2) **合成数据引擎**：生成包含复杂计算机使用场景的合成数据，用于训练Agent。3) **混合动作轨迹收集**：收集包含GUI操作和工具调用的混合动作轨迹，用于监督学习。4) **两阶段训练方法**：首先使用监督学习对Agent进行微调，然后使用在线强化学习进一步优化Agent的策略。

**关键创新**：UltraCUA最重要的创新在于混合动作空间的设计和两阶段训练方法。混合动作空间允许Agent在GUI操作和工具调用之间灵活切换，从而更好地适应不同的任务和环境。两阶段训练方法则可以有效地利用合成数据和真实数据，提高Agent的泛化能力。

**关键设计**：在工具能力提取pipeline中，使用了自然语言处理技术来解析软件文档和代码注释，提取工具的名称、参数和功能描述。在合成数据引擎中，使用了程序合成技术来生成包含复杂逻辑和约束的任务。在两阶段训练方法中，使用了Proximal Policy Optimization (PPO)算法进行在线强化学习，并设计了奖励函数来鼓励Agent使用高级工具。

## 📊 实验亮点

UltraCUA在OSWorld上实现了22%的相对改进，同时比现有方法平均快11%。在WindowsAgentArena上的跨域验证表明了强大的泛化能力，成功率为21.7%，超过了Windows训练的基线。这些结果表明，UltraCUA的混合动作范例能够显著提高计算机使用Agent的性能和鲁棒性。

## 🎯 应用场景

UltraCUA具有广泛的应用前景，可以用于自动化办公、软件测试、智能助手等领域。例如，它可以帮助用户自动完成重复性的计算机操作，提高工作效率；可以用于自动化测试软件的功能和性能，减少人工测试的成本；还可以作为智能助手的核心组件，帮助用户解决各种计算机使用问题。未来，UltraCUA有望成为通用计算机使用Agent的基础模型，推动相关领域的发展。

## 📄 摘要（原文）

> Computer-use agents face a fundamental limitation. They rely exclusively on primitive GUI actions (click, type, scroll), creating brittle execution chains prone to cascading failures. While API-driven agents harness rich capabilities through structured interfaces and tools, computer-use agents remain constrained to low-level visual interactions. We present UltraCUA, a foundation model that transcends this limitation through hybrid action-seamlessly unifying primitive GUI operations with high-level tool execution. Our innovation rests on four critical advances. First, an automated pipeline extracts and scales tool capabilities from software documentation and code repositories. Second, a synthetic data engine produces 17,000+ verifiable tasks capturing real-world computer-use complexity. Third, comprehensive hybrid action trajectory collection incorporates both GUI primitives and strategic tool calls. Fourth, a two-stage training methodology combines supervised fine-tuning with online reinforcement learning, enabling intelligent action selection between GUI and API. Evaluation with our 7B and 32B UltraCUA models reveals transformative performance gains. On OSWorld, UltraCUA achieves 22% relative improvement while executing 11% faster than existing approaches, averagely. Cross-domain validation on WindowsAgentArena demonstrates robust generalization with 21.7% success rate, surpassing Windows-trained baselines. The hybrid action paradigm proves essential, reducing error propagation while improving execution efficiency. This work establishes a scalable paradigm bridging primitive GUI interactions and high-level tool intelligence, enabling more resilient and adaptable computer use agents for diverse environments and complex real-world tasks.

