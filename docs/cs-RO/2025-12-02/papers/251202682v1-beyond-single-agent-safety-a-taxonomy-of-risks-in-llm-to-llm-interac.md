---
layout: default
title: Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions
---

# Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions

**arXiv**: [2512.02682v1](https://arxiv.org/abs/2512.02682) | [PDF](https://arxiv.org/pdf/2512.02682.pdf)

**作者**: Piercosma Bisconti, Marcello Galisai, Federico Pierucci, Marcantonio Bracale, Matteo Prandi

---

## 💡 一句话要点

**提出系统级安全框架以解决多LLM交互中的集体风险**

**关键词**: `多智能体交互` `系统级安全` `涌现风险` `制度性AI` `风险分类学`

## 📋 核心要点

1. 核心问题：单智能体安全机制在多LLM交互中失效，导致局部合规聚合为集体失败
2. 方法要点：引入涌现系统性风险视界框架，从交互结构分析风险，并提出制度性AI架构
3. 实验或效果：未知

## 📄 摘要（原文）

> This paper examines why safety mechanisms designed for human-model interaction do not scale to environments where large language models (LLMs) interact with each other. Most current governance practices still rely on single-agent safety containment, prompts, fine-tuning, and moderation layers that constrain individual model behavior but leave the dynamics of multi-model interaction ungoverned. These mechanisms assume a dyadic setting: one model responding to one user under stable oversight. Yet research and industrial development are rapidly shifting toward LLM-to-LLM ecosystems, where outputs are recursively reused as inputs across chains of agents. In such systems, local compliance can aggregate into collective failure even when every model is individually aligned. We propose a conceptual transition from model-level safety to system-level safety, introducing the framework of the Emergent Systemic Risk Horizon (ESRH) to formalize how instability arises from interaction structure rather than from isolated misbehavior. The paper contributes (i) a theoretical account of collective risk in interacting LLMs, (ii) a taxonomy connecting micro, meso, and macro-level failure modes, and (iii) a design proposal for InstitutionalAI, an architecture for embedding adaptive oversight within multi-agent systems.

