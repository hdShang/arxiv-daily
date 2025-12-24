---
layout: default
title: "E3-Rewrite: Learning to Rewrite SQL for Executability, Equivalence,and Efficiency"
---

# E3-Rewrite: Learning to Rewrite SQL for Executability, Equivalence,and Efficiency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09023" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09023v2</a>
  <a href="https://arxiv.org/pdf/2508.09023.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09023v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09023v2', 'E3-Rewrite: Learning to Rewrite SQL for Executability, Equivalence,and Efficiency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongjie Xu, Yue Cui, Weijie Shi, Qingzhi Ma, Hanghui Guo, Jiaming Li, Yao Zhao, Ruiyuan Zhang, Shimin Di, Jia Zhu, Kai Zheng, Jiajie Xu

**分类**: cs.DB, cs.AI, cs.CL

**发布日期**: 2025-08-12 (更新: 2025-08-15)

---

## 💡 一句话要点

**提出E3-Rewrite以解决SQL重写的执行性、等价性和效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `SQL重写` `大型语言模型` `强化学习` `查询优化` `数据库技术` `执行效率` `等价性验证`

## 📋 核心要点

1. 现有的SQL重写方法依赖于固定的重写规则，无法有效处理新查询模式和复杂查询，导致性能下降。
2. E3-Rewrite通过使用大型语言模型生成重写，结合上下文构建模块和强化学习框架，克服了执行意识和语义基础不足的问题。
3. 实验结果显示，E3-Rewrite在多个基准测试中显著提高了查询执行效率和等价性，表现优于现有方法。

## 📝 摘要（中文）

SQL查询重写旨在在保持等价性的同时，将查询重构为更高效的形式。现有方法大多依赖于预定义的重写规则，但这些规则在处理新查询模式和复杂查询时存在固有局限性。为了解决这些问题，本文提出了E3-Rewrite，一个基于大型语言模型（LLMs）的SQL重写框架。该框架通过构建上下文模块和强化学习框架，生成可执行、等价且高效的查询。实验结果表明，E3-Rewrite在多个SQL基准测试中，相较于领先基线，查询执行时间缩短了最多25.6%，同时生成了多达24.4%符合严格等价标准的重写。

## 🔬 方法详解

**问题定义**：本文旨在解决SQL查询重写中的执行性、等价性和效率问题。现有方法依赖于固定的重写规则，导致在处理复杂查询时性能不足，且无法捕捉到多样化的重写策略。

**核心思路**：E3-Rewrite利用大型语言模型生成SQL重写，能够捕捉复杂的重写策略，如评估重排序和公共表表达式重写。通过构建上下文和强化学习，确保生成的查询具备执行性和等价性。

**技术框架**：E3-Rewrite框架包含两个核心模块：上下文构建模块和强化学习框架。上下文模块利用执行计划和检索的示例构建瓶颈感知的提示，指导推理时的重写；强化学习框架则通过设计奖励函数，评估生成查询的执行性、等价性和效率。

**关键创新**：E3-Rewrite的创新在于将大型语言模型与强化学习相结合，克服了传统方法的局限性，能够生成更复杂的重写策略，并确保生成的查询在执行时的有效性和效率。

**关键设计**：在设计中，采用了分阶段的课程学习，首先强调执行性和等价性，随后逐步引入效率评估。奖励函数通过语法检查、等价验证和成本估算来评估生成查询的质量。实验中，E3-Rewrite在多个基准测试中表现出色，验证了其设计的有效性。

## 📊 实验亮点

E3-Rewrite在多个SQL基准测试中表现优异，查询执行时间相比于领先基线缩短了最多25.6%，同时生成的符合严格等价标准的重写数量增加了24.4%。这些结果表明，E3-Rewrite在处理复杂查询模式方面的优势，超越了现有的重写方法。

## 🎯 应用场景

E3-Rewrite的研究成果在数据库优化、数据分析和大数据处理等领域具有广泛的应用潜力。通过提高SQL查询的执行效率和等价性，该框架可以显著提升数据处理的性能，帮助企业在数据驱动决策中获得更快的响应时间和更高的准确性。未来，E3-Rewrite还可能扩展到其他类型的查询优化和自动化数据处理任务中。

## 📄 摘要（原文）

> SQL query rewriting aims to reformulate a query into a more efficient form while preserving equivalence. Most existing methods rely on predefined rewrite rules. However, such rule-based approaches face fundamental limitations: (1) fixed rule sets generalize poorly to novel query patterns and struggle with complex queries; (2) a wide range of effective rewriting strategies cannot be fully captured by declarative rules. To overcome these issues, we propose using large language models (LLMs) to generate rewrites. LLMs can capture complex strategies, such as evaluation reordering and CTE rewriting. Despite this potential, directly applying LLMs often results in performance regressions or non-equivalent rewrites due to a lack of execution awareness and semantic grounding. To address these challenges, We present E3-Rewrite, an LLM-based SQL rewriting framework that produces executable, equivalent, and efficient queries. It integrates two core components: a context construction module and a reinforcement learning framework. First, the context module leverages execution plans and retrieved demonstrations to build bottleneck-aware prompts that guide inference-time rewriting. Second, we design a reward function targeting executability, equivalence, and efficiency, evaluated via syntax checks, equivalence verification, and cost estimation. Third, to ensure stable multi-objective learning, we adopt a staged curriculum that first emphasizes executability and equivalence, then gradually incorporates efficiency. Across multiple SQL benchmarks, our experiments demonstrate that E3-Rewrite can shorten query execution time by as much as 25.6% relative to leading baselines, while also producing up to 24.4% more rewrites that meet strict equivalence criteria. These gains extend to challenging query patterns that prior approaches could not effectively optimize.

