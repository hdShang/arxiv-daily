---
layout: default
title: Complex Instruction Following with Diverse Style Policies in Football Games
---

# Complex Instruction Following with Diverse Style Policies in Football Games

**arXiv**: [2511.19885v1](https://arxiv.org/abs/2511.19885) | [PDF](https://arxiv.org/pdf/2511.19885.pdf)

**作者**: Chenglu Sun, Shuo Shen, Haonan Hu, Wei Zhou, Chen Chen

---

## 💡 一句话要点

**提出LCDSP以解决复杂足球游戏中语言指令跟随问题**

**关键词**: `语言控制强化学习` `多样风格策略` `多智能体环境` `足球游戏` `风格参数调制`

## 📋 核心要点

1. 核心问题：LC-RL在复杂多智能体环境中难以理解高级抽象指令
2. 方法要点：结合多样风格训练和风格解释器，通过参数调制行为
3. 实验或效果：在5v5足球环境中验证指令理解和行为多样性执行

## 📄 摘要（原文）

> Despite advancements in language-controlled reinforcement learning (LC-RL) for basic domains and straightforward commands (e.g., object manipulation and navigation), effectively extending LC-RL to comprehend and execute high-level or abstract instructions in complex, multi-agent environments, such as football games, remains a significant challenge. To address this gap, we introduce Language-Controlled Diverse Style Policies (LCDSP), a novel LC-RL paradigm specifically designed for complex scenarios. LCDSP comprises two key components: a Diverse Style Training (DST) method and a Style Interpreter (SI). The DST method efficiently trains a single policy capable of exhibiting a wide range of diverse behaviors by modulating agent actions through style parameters (SP). The SI is designed to accurately and rapidly translate high-level language instructions into these corresponding SP. Through extensive experiments in a complex 5v5 football environment, we demonstrate that LCDSP effectively comprehends abstract tactical instructions and accurately executes the desired diverse behavioral styles, showcasing its potential for complex, real-world applications.

