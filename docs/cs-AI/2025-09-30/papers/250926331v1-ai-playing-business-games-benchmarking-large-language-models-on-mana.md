---
layout: default
title: "AI Playing Business Games: Benchmarking Large Language Models on Managerial Decision-Making in Dynamic Simulations"
---

# AI Playing Business Games: Benchmarking Large Language Models on Managerial Decision-Making in Dynamic Simulations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26331" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26331v1</a>
  <a href="https://arxiv.org/pdf/2509.26331.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26331v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26331v1', 'AI Playing Business Games: Benchmarking Large Language Models on Managerial Decision-Making in Dynamic Simulations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Berdymyrat Ovezmyradov

**分类**: cs.AI

**发布日期**: 2025-09-30

**备注**: 34 pages, 7 figures, 3 tables

---

## 💡 一句话要点

**提出基于商业游戏模拟的LLM基准测试框架，评估其在动态管理决策中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `基准测试` `商业游戏` `管理决策` `动态模拟`

## 📋 核心要点

1. 现有LLM基准测试缺乏对长期战略业务决策能力的有效评估，尤其是在动态变化的环境中。
2. 提出一种基于商业游戏模拟的基准测试框架，通过模拟零售公司运营，评估LLM在多步骤决策中的表现。
3. 通过模拟12个月的业务运营，对比Gemini、ChatGPT等LLM在利润、市场份额等指标上的表现，分析其决策的连贯性和适应性。

## 📝 摘要（中文）

大型语言模型（LLM）的快速发展激发了人们对其增强或自动化管理职能的潜力的极大兴趣。AI基准测试的最新趋势之一是评估LLM在较长时间范围内的性能。虽然LLM擅长自然语言和模式识别任务，但它们在多步骤、战略性业务决策方面的能力在很大程度上仍未被探索。少数研究表明，结果可能与短期任务中的基准不同，正如Vending-Bench所揭示的那样。同时，长期连贯性的替代基准仍然短缺。本研究分析了一个使用商业游戏进行业务决策的新型基准。该研究通过为LLM基准测试提出一个可复现的、开放访问的管理模拟器，为人工智能领域的最新文献做出了贡献。这个新框架用于评估五种领先的LLM（Gemini、ChatGPT、Meta AI、Mistral AI和Grok）的性能。LLM为一个模拟零售公司做出决策。一个动态的、按月进行的管理模拟以电子表格模型形式提供，作为实验环境。在十二个月的每个月中，LLM都会收到一份包含上一时期完整业务报告的结构化提示，并负责做出关键的战略决策：定价、订单规模、营销预算、招聘、解雇、贷款、培训费用、研发费用、销售预测、收入预测。该方法旨在比较LLM的定量指标：利润、收入和市场份额，以及其他KPI。分析LLM决策的战略连贯性、对市场变化的适应性以及为其决策提供的理由。这种方法允许超越简单的性能指标来评估长期决策。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在自然语言处理和模式识别方面表现出色，但在复杂、动态的商业环境中进行长期战略决策的能力仍缺乏充分评估。现有的基准测试往往侧重于短期任务，无法有效衡量LLM在多步骤决策、适应市场变化以及保持战略连贯性方面的能力。因此，需要一种新的基准测试方法，能够更全面地评估LLM在长期商业决策中的表现。

**核心思路**：本研究的核心思路是利用商业游戏模拟作为LLM的基准测试环境。通过模拟一个零售公司的运营，LLM需要根据每个月的业务报告做出关键的战略决策，例如定价、订单规模、营销预算等。这种方法能够模拟真实商业环境的复杂性和动态性，从而更全面地评估LLM的长期决策能力。

**技术框架**：该研究的技术框架主要包括以下几个部分：1) **商业游戏模拟器**：使用电子表格模型构建一个动态的、按月进行的零售公司运营模拟器。2) **LLM接口**：设计一个结构化的提示，将每个月的业务报告提供给LLM，并接收LLM的决策作为输入。3) **决策评估模块**：根据LLM的决策，更新模拟器的状态，并计算关键的绩效指标（KPI），例如利润、收入和市场份额。4) **战略分析模块**：分析LLM决策的战略连贯性、对市场变化的适应性以及决策背后的理由。

**关键创新**：该研究的关键创新在于提出了一种基于商业游戏模拟的LLM基准测试框架，能够更全面地评估LLM在长期战略决策中的能力。与现有的基准测试相比，该框架具有以下优势：1) **动态性**：模拟真实商业环境的动态变化，要求LLM能够适应市场变化并做出相应的调整。2) **长期性**：通过模拟多个月的业务运营，评估LLM在长期决策中的战略连贯性。3) **可解释性**：分析LLM决策背后的理由，从而更好地理解其决策过程。

**关键设计**：在商业游戏模拟器中，关键的设计包括：1) **市场需求模型**：模拟市场需求对价格、营销等因素的敏感性。2) **竞争对手模型**：模拟竞争对手的定价和营销策略。3) **成本模型**：模拟各种运营成本，例如采购成本、营销成本和人力成本。在LLM接口中，关键的设计包括：1) **结构化提示**：将业务报告以结构化的方式呈现给LLM，以便其更好地理解。2) **决策格式**：定义LLM决策的格式，以便模拟器能够解析并执行。

## 📊 实验亮点

该研究通过实验对比了Gemini、ChatGPT、Meta AI、Mistral AI和Grok五种领先LLM在模拟零售公司运营中的表现。实验结果表明，不同LLM在利润、市场份额等指标上存在显著差异，并且LLM的决策质量受到市场变化的影响。该研究还发现，LLM的决策理由与实际效果之间存在一定的相关性，但仍有改进空间。

## 🎯 应用场景

该研究成果可应用于评估和改进LLM在商业决策领域的应用。企业可以利用该框架来测试和选择适合自身业务需求的LLM，从而提高决策效率和质量。此外，该框架还可以用于训练和微调LLM，使其更好地适应特定的商业环境和任务。

## 📄 摘要（原文）

> The rapid advancement of LLMs sparked significant interest in their potential to augment or automate managerial functions. One of the most recent trends in AI benchmarking is performance of Large Language Models (LLMs) over longer time horizons. While LLMs excel at tasks involving natural language and pattern recognition, their capabilities in multi-step, strategic business decision-making remain largely unexplored. Few studies demonstrated how results can be different from benchmarks in short-term tasks, as Vending-Bench revealed. Meanwhile, there is a shortage of alternative benchmarks for long-term coherence. This research analyses a novel benchmark using a business game for the decision making in business. The research contributes to the recent literature on AI by proposing a reproducible, open-access management simulator to the research community for LLM benchmarking. This novel framework is used for evaluating the performance of five leading LLMs available in free online interface: Gemini, ChatGPT, Meta AI, Mistral AI, and Grok. LLM makes decisions for a simulated retail company. A dynamic, month-by-month management simulation provides transparently in spreadsheet model as experimental environment. In each of twelve months, the LLMs are provided with a structured prompt containing a full business report from the previous period and are tasked with making key strategic decisions: pricing, order size, marketing budget, hiring, dismissal, loans, training expense, R&D expense, sales forecast, income forecast The methodology is designed to compare the LLMs on quantitative metrics: profit, revenue, and market share, and other KPIs. LLM decisions are analyzed in their strategic coherence, adaptability to market changes, and the rationale provided for their decisions. This approach allows to move beyond simple performance metrics for assessment of the long-term decision-making.

