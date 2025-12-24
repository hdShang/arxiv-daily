---
layout: default
title: "The Personality Illusion: Revealing Dissociation Between Self-Reports & Behavior in LLMs"
---

# The Personality Illusion: Revealing Dissociation Between Self-Reports & Behavior in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03730" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03730v2</a>
  <a href="https://arxiv.org/pdf/2509.03730.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03730v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03730v2', 'The Personality Illusion: Revealing Dissociation Between Self-Reports & Behavior in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengrui Han, Rafal Kocielnik, Peiyang Song, Ramit Debnath, Dean Mobbs, Anima Anandkumar, R. Michael Alvarez

**分类**: cs.AI, cs.CL, cs.CY, cs.LG, stat.ML

**发布日期**: 2025-09-03 (更新: 2025-09-05)

**备注**: We make public all code and source data at https://github.com/psychology-of-AI/Personality-Illusion for full reproducibility

---

## 💡 一句话要点

**揭示LLM人格幻觉：自述与行为之间的解离现象**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `人格特质` `自我报告` `行为预测` `角色扮演` `指令对齐` `RLHF`

## 📋 核心要点

1. 现有研究主要依赖LLM的自我报告来推断其人格特质，缺乏充分的行为验证，难以判断其真实性。
2. 该研究通过系统性实验，考察LLM在不同训练阶段的人格特质演变，以及自我报告与实际行为之间的关系。
3. 实验发现，指令对齐能稳定LLM的特质表达，但自我报告的特质并不能可靠预测行为，角色注入对行为影响有限。

## 📝 摘要（中文）

人格特质长期以来被认为是人类行为的预测指标。大型语言模型（LLM）的最新进展表明，类似模式可能出现在人工智能系统中，高级LLM表现出与人类特质（如宜人性和自我调节）相似的一致行为倾向。理解这些模式至关重要，但先前的工作主要依赖于简化的自我报告和启发式提示，缺乏行为验证。本研究系统地描述了LLM人格的三个维度：（1）在训练阶段中特质概况的动态出现和演变；（2）自我报告特质在行为任务中的预测有效性；（3）目标干预（如角色注入）对自我报告和行为的影响。研究结果表明，指令对齐（例如，RLHF、指令微调）显著稳定了特质表达并加强了特质相关性，这与人类数据相似。然而，这些自我报告的特质并不能可靠地预测行为，并且观察到的关联通常与人类模式不同。虽然角色注入成功地将自我报告引导到预期方向，但它对实际行为的影响很小或不一致。通过区分表面层面的特质表达与行为一致性，我们的发现挑战了关于LLM人格的假设，并强调需要在对齐和可解释性方面进行更深入的评估。

## 🔬 方法详解

**问题定义**：现有研究主要通过LLM的自我报告来评估其人格特质，但这种方法缺乏行为验证，无法确定LLM的自我报告是否与其行为一致。此外，现有方法对LLM人格的理解不够深入，未能充分考察训练过程对人格的影响，以及外部干预（如角色扮演）对人格的影响。因此，该研究旨在揭示LLM人格的真实性，以及自我报告与行为之间的关系。

**核心思路**：该研究的核心思路是通过系统性的实验，对比LLM的自我报告和实际行为，从而揭示LLM人格的幻觉。具体来说，研究人员首先评估LLM在不同训练阶段的人格特质，然后考察这些特质在预测行为任务中的有效性，最后研究角色注入等干预手段对LLM人格的影响。通过这种多维度的分析，研究人员旨在揭示LLM人格的真实面貌。

**技术框架**：该研究的技术框架主要包括以下几个部分：1) 人格评估：使用标准的人格测试量表（例如，Big Five）来评估LLM的自我报告人格特质。2) 行为任务：设计一系列行为任务，用于评估LLM在不同情境下的行为表现。3) 角色注入：通过指令微调，让LLM扮演特定角色，从而考察角色扮演对LLM人格的影响。4) 数据分析：使用统计方法分析LLM的自我报告和行为数据，从而揭示LLM人格的特征和规律。

**关键创新**：该研究的关键创新在于：1) 系统性地考察了LLM人格的多个维度，包括训练阶段、行为预测和外部干预。2) 揭示了LLM人格的幻觉，即自我报告的特质并不能可靠地预测行为。3) 强调了在评估LLM人格时，需要进行更深入的行为验证。

**关键设计**：该研究的关键设计包括：1) 使用多种人格测试量表，以确保人格评估的准确性。2) 设计多样化的行为任务，以覆盖不同情境下的行为表现。3) 使用不同的角色注入方法，以考察角色扮演对LLM人格的影响。4) 使用严格的统计方法，以确保数据分析的可靠性。

## 📊 实验亮点

研究发现，指令对齐（如RLHF）能显著稳定LLM的特质表达，并加强特质相关性，但自我报告的特质并不能可靠预测行为。角色注入能改变LLM的自我报告，但对实际行为影响很小或不一致。这些结果表明，LLM的“人格”更多是表面现象，而非内在行为驱动力。

## 🎯 应用场景

该研究成果可应用于LLM的对齐和可解释性研究，帮助开发者更好地理解和控制LLM的行为。例如，可以利用该研究的发现，设计更有效的对齐方法，避免LLM产生不符合人类价值观的行为。此外，该研究还可以用于评估LLM在特定应用场景下的可靠性，例如，在医疗、金融等领域，需要确保LLM的行为与自我报告一致，避免产生误导或错误决策。

## 📄 摘要（原文）

> Personality traits have long been studied as predictors of human behavior. Recent advances in Large Language Models (LLMs) suggest similar patterns may emerge in artificial systems, with advanced LLMs displaying consistent behavioral tendencies resembling human traits like agreeableness and self-regulation. Understanding these patterns is crucial, yet prior work primarily relied on simplified self-reports and heuristic prompting, with little behavioral validation. In this study, we systematically characterize LLM personality across three dimensions: (1) the dynamic emergence and evolution of trait profiles throughout training stages; (2) the predictive validity of self-reported traits in behavioral tasks; and (3) the impact of targeted interventions, such as persona injection, on both self-reports and behavior. Our findings reveal that instructional alignment (e.g., RLHF, instruction tuning) significantly stabilizes trait expression and strengthens trait correlations in ways that mirror human data. However, these self-reported traits do not reliably predict behavior, and observed associations often diverge from human patterns. While persona injection successfully steers self-reports in the intended direction, it exerts little or inconsistent effect on actual behavior. By distinguishing surface-level trait expression from behavioral consistency, our findings challenge assumptions about LLM personality and underscore the need for deeper evaluation in alignment and interpretability.

