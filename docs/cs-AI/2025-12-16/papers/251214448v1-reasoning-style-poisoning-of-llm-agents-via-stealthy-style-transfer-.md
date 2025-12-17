---
layout: default
title: Reasoning-Style Poisoning of LLM Agents via Stealthy Style Transfer: Process-Level Attacks and Runtime Monitoring in RSV Space
---

# Reasoning-Style Poisoning of LLM Agents via Stealthy Style Transfer: Process-Level Attacks and Runtime Monitoring in RSV Space

**arXiv**: [2512.14448v1](https://arxiv.org/abs/2512.14448) | [PDF](https://arxiv.org/pdf/2512.14448.pdf)

**作者**: Xingfu Zhou, Pengfei Wang

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出推理风格投毒攻击与实时监控方法，揭示LLM代理在过程层面的安全漏洞。**

**关键词**: `推理风格投毒` `生成式风格注入` `推理风格向量` `过程级攻击` `LLM代理安全` `实时监控` `对抗攻击` `检索增强生成`

## 📋 核心要点

1. 现有攻击多聚焦内容伪造或指令注入，忽视LLM代理推理过程本身的脆弱性，导致安全防护存在盲区。
2. 提出推理风格投毒攻击，通过生成式风格注入操纵文档语调，在不改变事实下诱导病态推理，并开发推理风格向量进行量化评估。
3. 实验显示攻击显著降低代理性能，推理步骤最多增加4.4倍，且能绕过先进内容过滤器，验证了过程级攻击的有效性。

## 📝 摘要（中文）

大型语言模型（LLM）代理依赖外部检索，在高风险环境中部署日益增多。现有对抗攻击主要关注内容伪造或指令注入，而本文识别出一种新颖的、面向过程的攻击面：代理的推理风格。我们提出推理风格投毒（RSP），这是一种操纵代理如何处理信息而非处理什么信息的范式。我们引入生成式风格注入（GSI），这是一种攻击方法，将检索到的文档重写为病态语调——特别是“分析瘫痪”或“认知仓促”——而不改变基本事实或使用显式触发器。为了量化这些变化，我们开发了推理风格向量（RSV），这是一种跟踪验证深度、自信度和注意力焦点的指标。在HotpotQA和FEVER数据集上使用ReAct、Reflection和思维树（ToT）架构进行的实验表明，GSI显著降低了性能。它使推理步骤增加多达4.4倍或导致过早错误，成功绕过最先进的内容过滤器。最后，我们提出RSP-M，一种轻量级运行时监控器，实时计算RSV指标并在值超过安全阈值时触发警报。我们的工作表明，推理风格是一种独特、可利用的漏洞，需要超越静态内容分析的过程级防御。

## 🔬 方法详解

论文提出推理风格投毒（RSP）整体框架，包括攻击和防御两部分。核心创新点在于生成式风格注入（GSI）攻击方法，它通过重写检索文档为“分析瘫痪”或“认知仓促”等病态语调，在不改变事实内容下操纵LLM代理的推理风格；同时开发推理风格向量（RSV）作为量化指标，基于验证深度、自信度和注意力焦点跟踪风格变化。与现有方法的主要区别在于，传统攻击侧重于内容或指令层面，而RSP专注于过程层面的推理风格操纵，这是一种新颖的攻击范式，强调“如何推理”而非“推理什么”，从而能绕过基于内容的静态防御。

## 📊 实验亮点

在HotpotQA和FEVER数据集上，使用ReAct、Reflection和ToT架构的实验表明，GSI攻击使推理步骤增加高达4.4倍或诱导过早错误，显著降低代理性能；攻击成功绕过最先进的内容过滤器，验证了过程级攻击的隐蔽性和有效性。

## 🎯 应用场景

该研究主要应用于LLM代理的安全防护领域，特别是在高风险环境如金融决策、医疗诊断或法律咨询中，代理依赖外部检索进行推理。潜在价值在于揭示过程级安全漏洞，推动开发实时监控和动态防御机制，提升代理在对抗环境下的鲁棒性和可靠性。

## 📄 摘要（原文）

> Large Language Model (LLM) agents relying on external retrieval are increasingly deployed in high-stakes environments. While existing adversarial attacks primarily focus on content falsification or instruction injection, we identify a novel, process-oriented attack surface: the agent's reasoning style. We propose Reasoning-Style Poisoning (RSP), a paradigm that manipulates how agents process information rather than what they process. We introduce Generative Style Injection (GSI), an attack method that rewrites retrieved documents into pathological tones--specifically "analysis paralysis" or "cognitive haste"--without altering underlying facts or using explicit triggers. To quantify these shifts, we develop the Reasoning Style Vector (RSV), a metric tracking Verification depth, Self-confidence, and Attention focus. Experiments on HotpotQA and FEVER using ReAct, Reflection, and Tree of Thoughts (ToT) architectures reveal that GSI significantly degrades performance. It increases reasoning steps by up to 4.4 times or induces premature errors, successfully bypassing state-of-the-art content filters. Finally, we propose RSP-M, a lightweight runtime monitor that calculates RSV metrics in real-time and triggers alerts when values exceed safety thresholds. Our work demonstrates that reasoning style is a distinct, exploitable vulnerability, necessitating process-level defenses beyond static content analysis.

