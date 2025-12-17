---
layout: default
title: In-Context Distillation with Self-Consistency Cascades: A Simple, Training-Free Way to Reduce LLM Agent Costs
---

# In-Context Distillation with Self-Consistency Cascades: A Simple, Training-Free Way to Reduce LLM Agent Costs

**arXiv**: [2512.02543v1](https://arxiv.org/abs/2512.02543) | [PDF](https://arxiv.org/pdf/2512.02543.pdf)

**作者**: Vishnu Sarukkai, Asanshay Gupta, James Hong, Michaël Gharbi, Kayvon Fatahalian

---

## 💡 一句话要点

**提出上下文蒸馏与自一致性级联方法，以降低LLM智能体推理成本，无需训练或手动提示工程。**

**关键词**: `LLM智能体` `上下文蒸馏` `自一致性级联` `推理成本优化` `无训练方法` `智能体基准`

## 📋 核心要点

1. 核心问题：LLM智能体大规模推理成本高，传统方法如微调或提示工程开发摩擦大。
2. 方法要点：引入上下文蒸馏，通过检索教师演示作为上下文示例，使低成本学生模型动态模仿教师行为；结合自一致性级联自适应信任学生。
3. 实验或效果：在ALFWorld基准上以2.5倍低成本匹配教师准确率，AppWorld上实现2倍成本降低，保持准确率。

## 📄 摘要（原文）

> The world currently has an abundance of ideas for how to use new LLM agents, and developers seek to rapidly prototype and test new agentic designs. However, executing agents at scale using high-capacity LLMs incurs high inference costs. We propose a simple method for reducing LLM agent inference costs without incurring the development friction costs associated with LLM fine-tuning (long training cycles, optimization hyperparameter tweaking loops) or manual prompt engineering (laborious trial and error). Most importantly, we introduce $\textit{in-context distillation}$, which adapts the idea of knowledge distillation (training a low cost-student model to mimic a high-cost teacher) to an in-context learning setting. Our approach retrieves relevant teacher demonstrations at each agent step and provides them to the student as in-context examples, enabling the student to imitate teacher behavior on-the-fly. We combine in-context distillation with the established idea of $\textit{self-consistency cascades}$ to know when the trust the student. This adaptive strategy realizes the cost benefits of model specialization while preserving the productivity of working with frozen models. On the multi-step embodied reasoning benchmark ALFWorld, our method matches teacher-level accuracy at $\textbf{2.5$\times$ lower cost}$, reducing per-episode costs from \$0.059 to \$0.024. The upfront demonstration cost amortizes after just 843 episodes, yielding cumulative savings exceeding \$34,900 at deployment scale (1M episodes). On AppWorld, a complex agent benchmark requiring multi-step API workflows, we shift the Pareto frontier by achieving a $\textbf{2$\times$ cost reduction}$ at iso-accuracy. By reducing operational costs while maintaining rapid experimentation cycles with frozen models, our approach makes advanced agentic systems economically viable for a broader range of applications.

