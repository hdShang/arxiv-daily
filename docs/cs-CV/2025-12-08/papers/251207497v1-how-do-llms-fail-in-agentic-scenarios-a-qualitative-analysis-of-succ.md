---
layout: default
title: How Do LLMs Fail In Agentic Scenarios? A Qualitative Analysis of Success and Failure Scenarios of Various LLMs in Agentic Simulations
---

# How Do LLMs Fail In Agentic Scenarios? A Qualitative Analysis of Success and Failure Scenarios of Various LLMs in Agentic Simulations

**arXiv**: [2512.07497v1](https://arxiv.org/abs/2512.07497) | [PDF](https://arxiv.org/pdf/2512.07497.pdf)

**作者**: JV Roig

---

## 💡 一句话要点

**分析大语言模型在代理场景中的失败模式，揭示策略与可靠性因素**

**关键词**: `大语言模型代理` `工具使用失败分析` `KAMI基准` `细粒度行为分析` `强化学习可靠性` `失败模式分类`

## 📋 核心要点

1. 研究大语言模型作为自主代理使用工具时的失败机制
2. 通过KAMI基准对三款模型进行细粒度行为分析，识别成功策略与失败模式
3. 发现模型规模非唯一决定因素，强化学习提升可靠性，并归纳四种常见失败类型

## 📄 摘要（原文）

> We investigate how large language models (LLMs) fail when operating as autonomous agents with tool-use capabilities. Using the Kamiwaza Agentic Merit Index (KAMI) v0.1 benchmark, we analyze 900 execution traces from three representative models - Granite 4 Small, Llama 4 Maverick, and DeepSeek V3.1 - across filesystem, text extraction, CSV analysis, and SQL scenarios. Rather than focusing on aggregate scores, we perform fine-grained, per-trial behavioral analysis to surface the strategies that enable successful multi-step tool execution and the recurrent failure modes that undermine reliability. Our findings show that model scale alone does not predict agentic robustness: Llama 4 Maverick (400B) performs only marginally better than Granite 4 Small (32B) in some uncertainty-driven tasks, while DeepSeek V3.1's superior reliability derives primarily from post-training reinforcement learning rather than architecture or size. Across models, we identify four recurring failure archetypes: premature action without grounding, over-helpfulness that substitutes missing entities, vulnerability to distractor-induced context pollution, and fragile execution under load. These patterns highlight the need for agentic evaluation methods that emphasize interactive grounding, recovery behavior, and environment-aware adaptation, suggesting that reliable enterprise deployment requires not just stronger models but deliberate training and design choices that reinforce verification, constraint discovery, and adherence to source-of-truth data.

