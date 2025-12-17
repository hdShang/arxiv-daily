---
layout: default
title: LLM Rationalis? Measuring Bargaining Capabilities of AI Negotiators
---

# LLM Rationalis? Measuring Bargaining Capabilities of AI Negotiators

**arXiv**: [2512.13063v1](https://arxiv.org/abs/2512.13063) | [PDF](https://arxiv.org/pdf/2512.13063.pdf)

**作者**: Cheril Shah, Akshit Agarwal, Kanak Garg, Mourad Heddaya

---

## 💡 一句话要点

**提出双曲正切框架与CRI指标，量化LLM在双边谈判中的锚定与僵化行为。**

**关键词**: `双边谈判` `让步动态建模` `LLM评估` `锚定行为` `策略多样性`

## 📋 核心要点

1. 核心问题：双边谈判中LLM缺乏人类般的动态适应与情境推理能力。
2. 方法要点：基于双曲正切曲线建模让步动态，引入爆发性τ和CRI指标。
3. 实验或效果：大规模比较人类与LLM，揭示LLM锚定极端、策略单一且能力不随模型提升。

## 📄 摘要（原文）

> Bilateral negotiation is a complex, context-sensitive task in which human negotiators dynamically adjust anchors, pacing, and flexibility to exploit power asymmetries and informal cues. We introduce a unified mathematical framework for modeling concession dynamics based on a hyperbolic tangent curve, and propose two metrics burstiness tau and the Concession-Rigidity Index (CRI) to quantify the timing and rigidity of offer trajectories. We conduct a large-scale empirical comparison between human negotiators and four state-of-the-art large language models (LLMs) across natural-language and numeric-offers settings, with and without rich market context, as well as six controlled power-asymmetry scenarios. Our results reveal that, unlike humans who smoothly adapt to situations and infer the opponents position and strategies, LLMs systematically anchor at extremes of the possible agreement zone for negotiations and optimize for fixed points irrespective of leverage or context. Qualitative analysis further shows limited strategy diversity and occasional deceptive tactics used by LLMs. Moreover the ability of LLMs to negotiate does not improve with better models. These findings highlight fundamental limitations in current LLM negotiation capabilities and point to the need for models that better internalize opponent reasoning and context-dependent strategy.

