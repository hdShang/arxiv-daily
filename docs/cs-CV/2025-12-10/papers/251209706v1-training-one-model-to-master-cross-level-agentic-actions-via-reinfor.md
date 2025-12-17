---
layout: default
title: Training One Model to Master Cross-Level Agentic Actions via Reinforcement Learning
---

# Training One Model to Master Cross-Level Agentic Actions via Reinforcement Learning

**arXiv**: [2512.09706v1](https://arxiv.org/abs/2512.09706) | [PDF](https://arxiv.org/pdf/2512.09706.pdf)

**作者**: Kaichen He, Zihao Wang, Muyao Li, Anji Liu, Yitao Liang

---

## 💡 一句话要点

**提出CrossAgent统一智能体模型，通过强化学习掌握跨层级异构动作空间以提升动态环境适应性。**

**关键词**: `智能体模型` `强化学习` `异构动作空间` `自适应交互` `Minecraft环境` `策略优化`

## 📋 核心要点

1. 现有智能体受限于静态预定义动作空间，难以适应动态环境中交互粒度变化。
2. 采用监督微调与多轮组相对策略优化算法，实现自适应动作切换，无需人工规则。
3. 在Minecraft开放世界800多个任务上验证，性能超越固定动作基线，展现优越泛化与长时推理效率。

## 📄 摘要（原文）

> The paradigm of agentic AI is shifting from engineered complex workflows to post-training native models. However, existing agents are typically confined to static, predefined action spaces--such as exclusively using APIs, GUI events, or robotic commands. This rigidity limits their adaptability in dynamic environments where the optimal granularity of interaction varies contextually. To bridge this gap, we propose CrossAgent, a unified agentic model that masters heterogeneous action spaces and autonomously selects the most effective interface for each step of a trajectory. We introduce a comprehensive training pipeline that integrates cold-start supervised fine-tuning with a Multi-Turn Group Relative Policy Optimization (GRPO) algorithm. This approach enables the agent to learn adaptive action switching--balancing high-level efficiency with low-level precision--without human-specified rules. Extensive experiments on over 800 tasks in the open-world Minecraft environment demonstrate that CrossAgent achieves state-of-the-art performance. By dynamically leveraging the strengths of diverse action spaces, our model significantly outperforms fixed-action baselines, exhibiting superior generalization and efficiency in long-horizon reasoning. All code and models are available at https://github.com/CraftJarvis/OpenHA

