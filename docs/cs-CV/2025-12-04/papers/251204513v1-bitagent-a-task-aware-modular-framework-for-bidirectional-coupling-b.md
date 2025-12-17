---
layout: default
title: BiTAgent: A Task-Aware Modular Framework for Bidirectional Coupling between Multimodal Large Language Models and World Models
---

# BiTAgent: A Task-Aware Modular Framework for Bidirectional Coupling between Multimodal Large Language Models and World Models

**arXiv**: [2512.04513v1](https://arxiv.org/abs/2512.04513) | [PDF](https://arxiv.org/pdf/2512.04513.pdf)

**作者**: Yu-Wei Zhan, Xin Wang, Pengzhe Mao, Tongtong Feng, Ren Wang, Wenwu Zhu

---

## 💡 一句话要点

**提出BiTAgent框架，通过双向耦合多模态大语言模型与世界模型，解决开放世界具身智能中的语义与动态对齐挑战。**

**关键词**: `具身智能` `多模态大语言模型` `世界模型` `双向耦合` `任务感知学习` `跨环境泛化`

## 📋 核心要点

1. 核心问题：多模态大语言模型与世界模型结合时，语义意图与动态状态表示难以紧密耦合，且缺乏任务感知的适应性。
2. 方法要点：设计前向路径注入语义指导想象，后向路径通过密集文本条件奖励优化语义空间，实现双向交互。
3. 实验或效果：在多任务和跨环境设置中，表现出优于基线的稳定性和泛化能力，推动开放世界具身学习。

## 📄 摘要（原文）

> Building generalist embodied agents requires a unified system that can interpret multimodal goals, model environment dynamics, and execute reliable actions across diverse real-world tasks. Multimodal large language models (MLLMs) offer strong semantic priors and cross-modal generalization, while world models (WMs) provide actionable latent dynamics for prediction and control. Their combination holds promise for open-ended embodied intelligence, yet introduces two key challenges: (1) establishing a tight coupling between the semantic intent from MLLMs and the dynamic state representations within the WM's latent space, and (2) achieving task-aware adaptability that supports multi-task learning and cross-environment generalization. To address these limitations, we propose BiTAgent, a task-aware dynamic joint framework that enables bidirectional coupling between MLLMs and WMs. BiTAgent establishes two complementary pathways: a forward path that injects MLLM representations into the WM's latent space for semantically guided imagination, and a backward path where WM-generated feedback refines the MLLM's semantic space via dense text-conditioned rewards. This bidirectional interaction is realized through three synergistic components: Task-Aware Dynamic Joint Learning, Task-Aware Behavior Learning, and MLLM-WM Joint Optimization, which together harmonize semantic reasoning and dynamic prediction. Extensive experiments across multi-task and cross-environment settings demonstrate superior stability and generalization over state-of-the-art baselines, marking a step toward open-ended embodied learning.

