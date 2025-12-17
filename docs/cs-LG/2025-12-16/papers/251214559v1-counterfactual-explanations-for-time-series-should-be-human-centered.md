---
layout: default
title: Counterfactual Explanations for Time Series Should be Human-Centered and Temporally Coherent in Interventions
---

# Counterfactual Explanations for Time Series Should be Human-Centered and Temporally Coherent in Interventions

**arXiv**: [2512.14559v1](https://arxiv.org/abs/2512.14559) | [PDF](https://arxiv.org/pdf/2512.14559.pdf)

**作者**: Emmanuel C. Chukwu, Rianne M. Schouten, Monique Tabak, Mykola Pechenizkiy

**分类**: cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出以人为中心且时间连贯的反事实解释方法，以解决临床推荐中现有方法的不足**

**关键词**: `反事实解释` `时间序列分类` `临床推荐系统` `可解释人工智能` `时间连贯性` `以人为中心设计` `算法追索` `鲁棒性分析`

## 📋 核心要点

1. 核心问题：现有反事实解释方法基于静态假设，忽略时间连贯性和临床可行性，导致干预不可靠。
2. 方法要点：倡导以人为中心的反事实解释，强调持续、目标导向的干预，需与临床推理和患者动态一致。
3. 实验或效果：通过鲁棒性分析发现现有方法对噪声敏感，突显其在真实临床环境中的局限性。

## 📝 摘要（中文）

反事实解释作为可解释机制被越来越多地提出，以实现算法追索。然而，当前针对时间序列分类的反事实技术主要基于静态数据假设设计，并侧重于生成最小输入扰动以翻转模型预测。本文认为，在临床推荐场景中，此类方法从根本上不足，因为干预措施随时间展开，必须具有因果合理性和时间连贯性。我们主张转向反映持续、目标导向干预的反事实解释，这些干预应与临床推理和患者特定动态保持一致。我们指出了现有方法在实践应用中的关键缺陷，特别是时间盲点以及在方法设计和评估指标中缺乏以用户为中心的考量。为支持我们的观点，我们对几种最先进的时间序列方法进行了鲁棒性分析，结果表明生成的反事实解释对随机噪声高度敏感。这一发现突显了它们在现实世界临床环境中的有限可靠性，因为微小的测量变化是不可避免的。最后，我们呼吁开发超越仅考虑预测变化而不考虑可行性或可操作性的方法和评估框架，强调需要可操作、目的驱动的干预措施，这些措施在现实世界中对应用用户是可行的。

## 🔬 方法详解

本文未提出具体的新模型架构，而是从方法论角度批判现有方法并倡导新方向。整体框架强调反事实解释应基于时间序列的动态特性，而非静态扰动。关键技术创新点在于将时间连贯性和因果合理性作为核心设计原则，要求干预措施在时间维度上持续且逻辑一致。与现有方法的主要区别在于：现有方法侧重于最小化输入扰动以改变预测，而本文主张反事实解释应反映现实世界中的可行干预，如临床治疗过程，从而提升可解释性和实用性。

## 📊 实验亮点

对多种最先进时间序列反事实方法进行鲁棒性分析，发现生成的反事实解释对随机噪声高度敏感，表明现有方法在真实临床环境中可靠性有限，因微小测量变化不可避免。

## 🎯 应用场景

该研究主要应用于临床推荐系统，如疾病预测和个性化治疗规划。通过提供以人为中心且时间连贯的反事实解释，可帮助医生理解模型决策，制定更可行、持续的干预措施，提升医疗AI的可信度和实用性。

## 📄 摘要（原文）

> Counterfactual explanations are increasingly proposed as interpretable mechanisms to achieve algorithmic recourse. However, current counterfactual techniques for time series classification are predominantly designed with static data assumptions and focus on generating minimal input perturbations to flip model predictions. This paper argues that such approaches are fundamentally insufficient in clinical recommendation settings, where interventions unfold over time and must be causally plausible and temporally coherent. We advocate for a shift towards counterfactuals that reflect sustained, goal-directed interventions aligned with clinical reasoning and patient-specific dynamics. We identify critical gaps in existing methods that limit their practical applicability, specifically, temporal blind spots and the lack of user-centered considerations in both method design and evaluation metrics. To support our position, we conduct a robustness analysis of several state-of-the-art methods for time series and show that the generated counterfactuals are highly sensitive to stochastic noise. This finding highlights their limited reliability in real-world clinical settings, where minor measurement variations are inevitable. We conclude by calling for methods and evaluation frameworks that go beyond mere prediction changes without considering feasibility or actionability. We emphasize the need for actionable, purpose-driven interventions that are feasible in real-world contexts for the users of such applications.

