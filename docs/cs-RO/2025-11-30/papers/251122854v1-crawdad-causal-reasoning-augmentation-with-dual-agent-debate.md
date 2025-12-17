---
layout: default
title: CRAwDAD: Causal Reasoning Augmentation with Dual-Agent Debate
---

# CRAwDAD: Causal Reasoning Augmentation with Dual-Agent Debate

**arXiv**: [2511.22854v1](https://arxiv.org/abs/2511.22854) | [PDF](https://arxiv.org/pdf/2511.22854.pdf)

**作者**: Finn G. Vamosi, Nils D. Forkert

---

## 💡 一句话要点

**提出双智能体辩论框架CRAwDAD，通过内部对话提升语言模型在因果推理中的准确性。**

**关键词**: `因果推理` `多智能体辩论` `语言模型` `反事实分析` `CLadder数据集`

## 📋 核心要点

1. 核心问题：因果推理常需考虑多种假设，类似内部对话，但现有方法未显式模拟此过程。
2. 方法要点：采用双智能体辩论框架，一智能体进行结构化因果推理，另一智能体批判性审查逻辑缺陷，通过辩论达成共识。
3. 实验或效果：在CLadder数据集上，使用Qwen3和DeepSeek-R1，辩论后模型整体准确率提升，反事实问题改进显著。

## 📄 摘要（原文）

> When people reason about cause and effect, they often consider many competing "what if" scenarios before deciding which explanation fits best. Analogously, advanced language models capable of causal inference can consider multiple interventions and counterfactuals to judge the validity of causal claims. Crucially, this type of reasoning is less like a single calculation and more like an internal dialogue between alternative hypotheses. In this paper, we make this dialogue explicit through a dual-agent debate framework where one model provides a structured causal inference, and the other critically examines this reasoning for logical flaws. When disagreements arise, agents attempt to persuade each other, challenging each other's logic and revising their conclusions until they converge on a mutually agreed answer. To take advantage of this deliberative process, we specifically use reasoning language models, whose strengths in both causal inference and adversarial debate remain under-explored relative to standard large language models. We evaluate our approach on the CLadder dataset, a benchmark linking natural language questions to formally defined causal graphs across all three rungs of Pearl's ladder of causation. With Qwen3 and DeepSeek-R1 as debater agents, we demonstrate that multi-agent debate improves DeepSeek-R1's overall accuracy in causal inference from 78.03% to 87.45%, with the counterfactual category specifically improving from 67.94% to 80.04% accuracy. Similarly, Qwen3's overall accuracy improves from 84.16% to 89.41%, and counterfactual questions from 71.53% to 80.35%, showing that strong models can still benefit greatly from debate with weaker agents. Our results highlight the potential of reasoning models as building blocks for multi-agent systems in causal inference, and demonstrate the importance of diverse perspectives in causal problem-solving.

