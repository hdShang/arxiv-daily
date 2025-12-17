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

🎯 **匹配领域**: **强化学习**

**关键词**: `推理风格投毒` `过程导向攻击` `生成式风格注入` `推理风格向量` `LLM代理安全` `实时监控` `对抗攻击` `检索增强生成`

## 📋 核心要点

1. 现有攻击主要针对内容伪造或指令注入，忽视了LLM代理推理过程本身的脆弱性。
2. 提出推理风格投毒攻击，通过生成式风格注入操纵推理风格而不改变事实内容。
3. 实验显示攻击显著降低性能，增加推理步骤或诱导错误，并成功绕过内容过滤器。

## 📝 摘要（中文）

大型语言模型（LLM）代理依赖外部检索，在高风险环境中部署日益增多。现有对抗攻击主要关注内容伪造或指令注入，而本文识别出一种新颖的、面向过程的攻击面：代理的推理风格。我们提出推理风格投毒（RSP），这是一种操纵代理处理信息方式而非处理内容的范式。我们引入生成式风格注入（GSI），一种攻击方法，将检索到的文档重写为病态语调——特别是“分析瘫痪”或“认知仓促”——而不改变基本事实或使用显式触发器。为了量化这些变化，我们开发了推理风格向量（RSV），一种跟踪验证深度、自信度和注意力焦点的指标。在HotpotQA和FEVER数据集上使用ReAct、Reflection和思维树（ToT）架构进行的实验表明，GSI显著降低了性能。它将推理步骤增加多达4.4倍或诱导过早错误，成功绕过最先进的内容过滤器。最后，我们提出RSP-M，一种轻量级运行时监控器，实时计算RSV指标并在值超过安全阈值时触发警报。我们的工作表明推理风格是一种独特、可利用的漏洞，需要超越静态内容分析的过程级防御。

## 🔬 方法详解

论文提出推理风格投毒（RSP）攻击范式，核心方法是生成式风格注入（GSI）。整体框架包括：攻击者将检索到的文档重写为“分析瘫痪”（过度谨慎）或“认知仓促”（草率决策）的病态风格，而不修改事实或使用显式触发器。关键技术创新是推理风格向量（RSV），它量化推理风格变化，通过验证深度、自信度和注意力焦点三个维度跟踪过程级异常。与现有方法的主要区别在于，RSP攻击的是代理的推理过程而非内容本身，属于过程导向攻击，而传统防御如内容过滤器难以检测这种风格转移。

## 📊 实验亮点

在HotpotQA和FEVER数据集上，GSI攻击使推理步骤增加高达4.4倍，或诱导过早错误，性能显著下降。攻击成功绕过最先进的内容过滤器，验证了推理风格作为独立攻击面的有效性。RSP-M监控器实时检测异常，为过程级防御提供了可行方案。

## 🎯 应用场景

该研究适用于高风险的LLM代理部署场景，如金融分析、医疗诊断或法律咨询，其中代理依赖外部检索进行决策。实际价值在于揭示了过程级安全漏洞，推动开发实时监控和防御机制，提升代理在对抗环境中的鲁棒性。

## 📄 摘要（原文）

> Large Language Model (LLM) agents relying on external retrieval are increasingly deployed in high-stakes environments. While existing adversarial attacks primarily focus on content falsification or instruction injection, we identify a novel, process-oriented attack surface: the agent's reasoning style. We propose Reasoning-Style Poisoning (RSP), a paradigm that manipulates how agents process information rather than what they process. We introduce Generative Style Injection (GSI), an attack method that rewrites retrieved documents into pathological tones--specifically "analysis paralysis" or "cognitive haste"--without altering underlying facts or using explicit triggers. To quantify these shifts, we develop the Reasoning Style Vector (RSV), a metric tracking Verification depth, Self-confidence, and Attention focus. Experiments on HotpotQA and FEVER using ReAct, Reflection, and Tree of Thoughts (ToT) architectures reveal that GSI significantly degrades performance. It increases reasoning steps by up to 4.4 times or induces premature errors, successfully bypassing state-of-the-art content filters. Finally, we propose RSP-M, a lightweight runtime monitor that calculates RSV metrics in real-time and triggers alerts when values exceed safety thresholds. Our work demonstrates that reasoning style is a distinct, exploitable vulnerability, necessitating process-level defenses beyond static content analysis.

