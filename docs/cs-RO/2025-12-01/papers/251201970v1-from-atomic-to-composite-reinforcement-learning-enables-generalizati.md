---
layout: default
title: From Atomic to Composite: Reinforcement Learning Enables Generalization in Complementary Reasoning
---

# From Atomic to Composite: Reinforcement Learning Enables Generalization in Complementary Reasoning

**arXiv**: [2512.01970v1](https://arxiv.org/abs/2512.01970) | [PDF](https://arxiv.org/pdf/2512.01970.pdf)

**作者**: Sitao Cheng, Xunjian Yin, Ruiwen Zhou, Yuxuan Li, Xinyi Wang, Liangming Pan, William Yang Wang, Victor Zhong

---

## 💡 一句话要点

**提出原子技能分解与强化学习结合方法，以提升互补推理任务的泛化能力**

**关键词**: `互补推理` `强化学习` `泛化能力` `原子技能分解` `监督微调`

## 📋 核心要点

1. 核心问题：探究强化学习在推理能力中的作用，是合成新技能还是仅放大现有行为
2. 方法要点：将互补推理分解为参数推理和上下文推理原子技能，通过监督微调与强化学习结合训练
3. 实验或效果：发现强化学习能合成复杂推理策略，但需原子技能作为基础，显著提升零样本泛化性能

## 📄 摘要（原文）

> The mechanism by which RL contributes to reasoning capabilities-whether it incentivizes the synthesis of new skills or merely amplifies existing behaviors-remains a subject of intense debate. In this work, we investigate this question through the lens of Complementary Reasoning, a complex task that requires integrating internal parametric knowledge with external contextual information. Using a controlled synthetic dataset of human biographies, we strictly decouple this ability into two atomic skills: Parametric Reasoning (relying on internal knowledge) and Contextual Reasoning (depending on external information). To rigorously assess capability boundaries, we evaluate generalization across three distinct levels of difficulty: I.I.D., Composition, and Zero-shot settings. We find that while SFT is sufficient for in-distribution performance, it struggles with O.O.D. generalization, particularly in Zero-shot settings where relational combinations are novel. Crucially, we identify the SFT Generalization Paradox: Models supervised solely on the composite task achieve near-perfect in-distribution accuracy but collapse on out-of-distribution generalization, indicating their reliance on rote memorization of path shortcuts. In contrast, we find that RL acts as a reasoning synthesizer rather than a probability amplifier. However, we uncover a strict atomic prerequisite: RL can only synthesize these complex strategies if the base model has first mastered the independent atomic skills (Parametric and Contextual) via SFT. These findings challenge the view of RL as a mere amplifier, suggesting that given sufficient atomic foundations, RL can actively synthesize complex reasoning strategies from learned primitives without explicit supervision on such complex strategies. This indicates that decoupled atomic training followed by RL offers a scalable path to generalization for complex reasoning tasks.

