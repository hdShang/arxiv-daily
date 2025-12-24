---
layout: default
title: "AgentSwift: Efficient LLM Agent Design via Value-guided Hierarchical Search"
---

# AgentSwift: Efficient LLM Agent Design via Value-guided Hierarchical Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06017" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06017v2</a>
  <a href="https://arxiv.org/pdf/2506.06017.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06017v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06017v2', 'AgentSwift: Efficient LLM Agent Design via Value-guided Hierarchical Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Li, Lehui Li, Zhihao Wu, Qingmin Liao, Jianye Hao, Kun Shao, Fengli Xu, Yong Li

**分类**: cs.CL

**发布日期**: 2025-06-06 (更新: 2025-11-20)

**备注**: AAAI-2026

---

## 💡 一句话要点

**提出AgentSwift以解决自动化代理设计中的高成本与低效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动化代理设计` `层次化搜索` `价值模型` `蒙特卡洛树搜索` `大型语言模型` `性能提升` `智能系统`

## 📋 核心要点

1. 现有自动化代理设计方法受限于有限的搜索空间，无法有效整合关键的人类设计组件。
2. 本文提出AgentSwift，通过层次化搜索空间联合建模工作流和功能组件，提升代理设计的复杂性与有效性。
3. 在七个不同领域的基准测试中，AgentSwift发现的代理平均性能提升了8.34%，超越现有方法和手动设计的代理。

## 📝 摘要（中文）

大型语言模型（LLM）代理在多个领域展现出强大的能力，但自动化代理设计仍然面临重大挑战。现有方法往往受限于有限的搜索空间，主要优化工作流，却未能有效整合记忆、规划和工具使用等关键人类设计组件。此外，这些方法的评估成本高昂，评估一个新代理在基准测试上的费用可达数十美元。为了解决这些问题，本文提出了AgentSwift，一个新的自动化代理设计框架。我们形式化了一个层次化搜索空间，联合建模代理工作流和可组合功能组件，从而发现更复杂和有效的代理架构。通过在高质量数据集上训练价值模型，并结合组合覆盖和均衡贝叶斯采样的策略降低评估成本，AgentSwift在七个基准测试上发现的代理平均性能提升了8.34%。

## 🔬 方法详解

**问题定义**：本文旨在解决自动化代理设计中的高评估成本和低效率问题。现有方法往往仅优化工作流，未能有效整合记忆、规划等人类设计组件，导致探索过程缓慢且资源密集。

**核心思路**：AgentSwift通过引入层次化搜索空间，联合建模代理工作流和功能组件，突破了传统方法的局限性。这种设计使得代理架构的发现更加复杂和有效。

**技术框架**：AgentSwift的整体架构包括层次化搜索空间、价值模型训练和基于不确定性的层次化蒙特卡洛树搜索（MCTS）策略。首先，构建一个联合模型以优化工作流和功能组件；其次，利用价值模型降低评估成本；最后，通过MCTS策略高效导航搜索空间。

**关键创新**：最重要的技术创新在于层次化搜索空间的构建和价值模型的训练策略。这与现有方法的本质区别在于，AgentSwift不仅优化工作流，还同时优化功能组件，从而发现更复杂的代理架构。

**关键设计**：在设计中，采用了组合覆盖和均衡贝叶斯采样的策略生成高质量数据集，以训练价值模型。此外，MCTS策略的引入使得搜索过程能够更有效地应对不确定性，提升了整体探索效率。

## 📊 实验亮点

在七个不同领域的基准测试中，AgentSwift发现的代理平均性能提升了8.34%，显著超越了现有的自动化代理搜索方法和手动设计的代理。这一结果表明，AgentSwift在代理设计的效率和效果上均具有显著优势。

## 🎯 应用场景

AgentSwift的研究成果在多个领域具有广泛的应用潜力，包括智能助手、自动化决策系统和游戏AI等。其高效的代理设计方法可以帮助研究人员快速发现强大的代理架构，推动相关技术的发展与应用。未来，随着更多领域的探索，AgentSwift有望在智能系统的自动化设计中发挥更大作用。

## 📄 摘要（原文）

> Large language model (LLM) agents have demonstrated strong capabilities across diverse domains, yet automated agent design remains a significant challenge. Current automated agent design approaches are often constrained by limited search spaces that primarily optimize workflows but fail to integrate crucial human-designed components like memory, planning, and tool use. Furthermore, these methods are hampered by high evaluation costs, as evaluating even a single new agent on a benchmark can require tens of dollars. The difficulty of this exploration is further exacerbated by inefficient search strategies that struggle to navigate the large design space effectively, making the discovery of novel agents a slow and resource-intensive process. To address these challenges, we propose AgentSwift, a novel framework for automated agent design. We formalize a hierarchical search space that jointly models agentic workflow and composable functional components. This structure moves beyond optimizing workflows alone by co-optimizing functional components, which enables the discovery of more complex and effective agent architectures. To make exploration within this expansive space feasible, we mitigate high evaluation costs by training a value model on a high-quality dataset, generated via a novel strategy combining combinatorial coverage and balanced Bayesian sampling for low-cost evaluation. Guiding the entire process is a hierarchical MCTS strategy, which is informed by uncertainty to efficiently navigate the search space. Evaluated across a comprehensive set of seven benchmarks spanning embodied, math, web, tool, and game domains, AgentSwift discovers agents that achieve an average performance gain of 8.34\% over both existing automated agent search methods and manually designed agents. Our framework serves as a launchpad for researchers to rapidly discover powerful agent architectures.

