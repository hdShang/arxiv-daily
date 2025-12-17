---
layout: default
title: Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning
---

# Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning

**arXiv**: [2511.19900v1](https://arxiv.org/abs/2511.19900) | [PDF](https://arxiv.org/pdf/2511.19900.pdf)

**作者**: Jiaqi Liu, Kaiwen Xiong, Peng Xia, Yiyang Zhou, Haonian Ji, Lu Feng, Siwei Han, Mingyu Ding, Huaxiu Yao

---

## 💡 一句话要点

**提出Agent0-VL自进化视觉语言代理，通过工具集成推理解决视觉推理自监督学习问题**

**关键词**: `视觉语言代理` `工具集成推理` `自进化学习` `自监督评估` `多模态推理` `强化学习`

## 📋 核心要点

1. 核心问题：视觉语言代理依赖人工标注，文本自评估易产生幻觉，难以验证复杂视觉推理
2. 方法要点：集成工具用于推理、自评估和自修复，通过求解器和验证器角色实现自进化循环
3. 实验或效果：在几何问题解决和视觉科学分析中，比基础模型提升12.5%，无需外部奖励

## 📄 摘要（原文）

> Vision-language agents have achieved remarkable progress in a variety of multimodal reasoning tasks; however, their learning remains constrained by the limitations of human-annotated supervision. Recent self-rewarding approaches attempt to overcome this constraint by allowing models to act as their own critics or reward providers. Yet, purely text-based self-evaluation struggles to verify complex visual reasoning steps and often suffers from evaluation hallucinations. To address these challenges, inspired by recent advances in tool-integrated reasoning, we propose Agent0-VL, a self-evolving vision-language agent that achieves continual improvement with tool-integrated reasoning. Agent0-VL incorporates tool usage not only into reasoning but also into self-evaluation and self-repair, enabling the model to introspect, verify, and refine its reasoning through evidence-grounded analysis. It unifies two synergistic roles within a single LVLM: a Solver that performs multi-turn tool-integrated reasoning, and a Verifier that generates structured feedback and fine-grained self-rewards through tool-grounded critique. These roles interact through a Self-Evolving Reasoning Cycle, where tool-based verification and reinforcement learning jointly align the reasoning and evaluation distributions for stable self-improvement. Through this zero-external-reward evolution, Agent0-VL aligns its reasoning and verification behaviors without any human annotation or external reward models, achieving continual self-improvement. Experiments on geometric problem solving and visual scientific analysis show that Agent0-VL achieves an 12.5% improvement over the base model. Our code is available at \href{https://github.com/aiming-lab/Agent0/Agent0-VL}{this https URL}.

