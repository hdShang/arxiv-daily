---
layout: default
title: Architecting Large Action Models for Human-in-the-Loop Intelligent Robots
---

# Architecting Large Action Models for Human-in-the-Loop Intelligent Robots

**arXiv**: [2512.11620v1](https://arxiv.org/abs/2512.11620) | [PDF](https://arxiv.org/pdf/2512.11620.pdf)

**作者**: Kanisorn Sangchai, Methasit Boonpun, Withawin Kraipetchara, Paulo Garcia

---

## 💡 一句话要点

**提出基于现成基础模型组合构建大型动作模型，通过符号包装和验证实现人机协作智能机器人。**

**关键词**: `大型动作模型` `神经符号系统` `人机协作` `PDDL规划` `机器人智能` `模型组合`

## 📋 核心要点

1. 核心问题：大型动作模型训练成本高且可靠性不足，难以控制与解释。
2. 方法要点：组合现成基础模型，集成符号包装和PDDL代码生成以支持人机验证。
3. 实验或效果：多模态机器人实验显示无需大规模端到端训练，可有效减少动作幻觉。

## 📄 摘要（原文）

> The realization of intelligent robots, operating autonomously and interacting with other intelligent agents, human or artificial, requires the integration of environment perception, reasoning, and action. Classic Artificial Intelligence techniques for this purpose, focusing on symbolic approaches, have long-ago hit the scalability wall on compute and memory costs. Advances in Large Language Models in the past decade (neural approaches) have resulted in unprecedented displays of capability, at the cost of control, explainability, and interpretability. Large Action Models aim at extending Large Language Models to encompass the full perception, reasoning, and action cycle; however, they typically require substantially more comprehensive training and suffer from the same deficiencies in reliability. Here, we show it is possible to build competent Large Action Models by composing off-the-shelf foundation models, and that their control, interpretability, and explainability can be effected by incorporating symbolic wrappers and associated verification on their outputs, achieving verifiable neuro-symbolic solutions for intelligent robots. Our experiments on a multi-modal robot demonstrate that Large Action Model intelligence does not require massive end-to-end training, but can be achieved by integrating efficient perception models with a logic-driven core. We find that driving action execution through the generation of Planning Domain Definition Language (PDDL) code enables a human-in-the-loop verification stage that effectively mitigates action hallucinations. These results can support practitioners in the design and development of robotic Large Action Models across novel industries, and shed light on the ongoing challenges that must be addressed to ensure safety in the field.

