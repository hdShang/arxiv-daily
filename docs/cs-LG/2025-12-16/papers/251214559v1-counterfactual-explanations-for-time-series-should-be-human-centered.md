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

**提出以人为中心且时间连贯的反事实解释方法，以解决临床推荐系统中现有方法的不足。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `反事实解释` `时间序列分类` `临床推荐系统` `可解释人工智能` `时间连贯性` `以人为中心设计` `鲁棒性分析` `算法追索`

## 📋 核心要点

1. 现有反事实方法基于静态假设，忽略时间连贯性和临床可行性，导致干预不切实际。
2. 提出以人为中心的反事实解释，强调持续、目标导向的干预，与临床推理和患者动态保持一致。
3. 鲁棒性分析显示现有方法对噪声敏感，突显其在真实临床环境中的可靠性不足，需改进评估框架。

## 📝 摘要（中文）

反事实解释作为可解释机制被越来越多地用于实现算法追索。然而，当前针对时间序列分类的反事实技术主要基于静态数据假设，侧重于生成最小输入扰动以翻转模型预测。本文认为，在临床推荐场景中，此类方法从根本上不足，因为干预措施随时间展开，必须具有因果合理性和时间连贯性。我们主张转向反映持续、目标导向干预的反事实解释，这些干预应与临床推理和患者特定动态保持一致。我们指出了现有方法在实践应用中的关键缺陷，特别是时间盲点以及在方法设计和评估指标中缺乏以用户为中心的考虑。为支持我们的观点，我们对几种最先进的时间序列方法进行了鲁棒性分析，结果表明生成的反事实解释对随机噪声高度敏感。这一发现突显了它们在现实世界临床环境中的有限可靠性，因为微小的测量变化不可避免。最后，我们呼吁开发超越仅考虑预测变化而不考虑可行性或可操作性的方法和评估框架。我们强调需要可操作、目的驱动的干预措施，这些措施在现实世界中对应用用户是可行的。

## 🔬 方法详解

本文未提出具体的新模型架构，而是从方法论角度批判现有反事实解释技术，并倡导一种以人为中心、时间连贯的框架。整体框架强调反事实解释应反映持续干预，而非仅最小扰动。关键技术创新点在于将时间连贯性和因果合理性纳入反事实生成过程，与现有方法主要区别在于：现有方法聚焦静态数据扰动，而本文主张动态、目标导向的干预，考虑临床场景中的用户需求和可行性。这涉及重新设计评估指标，以超越预测翻转，纳入可操作性和现实世界适用性。

## 📊 实验亮点

对多种最先进时间序列反事实方法进行鲁棒性分析，发现生成的反事实对随机噪声高度敏感，表明现有方法在真实临床环境中可靠性有限，这突显了开发更稳健、以用户为中心方法的紧迫性。

## 🎯 应用场景

该研究主要应用于临床推荐系统，如疾病预测、治疗规划等时间序列分类任务。潜在价值在于提升医疗AI的可解释性和实用性，通过生成更合理、可行的反事实解释，帮助医生和患者理解模型决策，实现个性化干预，从而提高医疗决策的透明度和信任度。

## 📄 摘要（原文）

> Counterfactual explanations are increasingly proposed as interpretable mechanisms to achieve algorithmic recourse. However, current counterfactual techniques for time series classification are predominantly designed with static data assumptions and focus on generating minimal input perturbations to flip model predictions. This paper argues that such approaches are fundamentally insufficient in clinical recommendation settings, where interventions unfold over time and must be causally plausible and temporally coherent. We advocate for a shift towards counterfactuals that reflect sustained, goal-directed interventions aligned with clinical reasoning and patient-specific dynamics. We identify critical gaps in existing methods that limit their practical applicability, specifically, temporal blind spots and the lack of user-centered considerations in both method design and evaluation metrics. To support our position, we conduct a robustness analysis of several state-of-the-art methods for time series and show that the generated counterfactuals are highly sensitive to stochastic noise. This finding highlights their limited reliability in real-world clinical settings, where minor measurement variations are inevitable. We conclude by calling for methods and evaluation frameworks that go beyond mere prediction changes without considering feasibility or actionability. We emphasize the need for actionable, purpose-driven interventions that are feasible in real-world contexts for the users of such applications.

