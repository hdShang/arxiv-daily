---
layout: default
title: SpeakRL: Synergizing Reasoning, Speaking, and Acting in Language Models with Reinforcement Learning
---

# SpeakRL: Synergizing Reasoning, Speaking, and Acting in Language Models with Reinforcement Learning

**arXiv**: [2512.13159v1](https://arxiv.org/abs/2512.13159) | [PDF](https://arxiv.org/pdf/2512.13159.pdf)

**作者**: Emre Can Acikgoz, Jinoh Oh, Jie Hao, Joo Hyuk Jeon, Heng Ji, Dilek Hakkani-Tür, Gokhan Tur, Xiang Li, Chengyuan Ma, Xing Fan

---

## 💡 一句话要点

**提出SpeakRL强化学习方法，通过奖励主动交互提升语言模型在任务导向对话中的协作能力。**

**关键词**: `强化学习` `任务导向对话` `主动交互` `语言模型优化` `合成数据集`

## 📋 核心要点

1. 核心问题：现有语言模型在协作中多为被动响应，缺乏主动澄清用户意图的能力。
2. 方法要点：使用强化学习奖励模型主动提问，平衡询问与行动，并构建SpeakER合成数据集支持训练。
3. 实验或效果：在任务完成率上比基础模型提升20.14%，对话轮次未增加，优于更大专有模型。

## 📄 摘要（原文）

> Effective human-agent collaboration is increasingly prevalent in real-world applications. Current trends in such collaborations are predominantly unidirectional, with users providing instructions or posing questions to agents, where agents respond directly without seeking necessary clarifications or confirmations. However, the evolving capabilities of these agents require more proactive engagement, where agents should dynamically participate in conversations to clarify user intents, resolve ambiguities, and adapt to changing circumstances. Existing prior work under-utilize the conversational capabilities of language models (LMs), thereby optimizing agents as better followers rather than effective speakers. In this work, we introduce SpeakRL, a reinforcement learning (RL) method that enhances agents' conversational capabilities by rewarding proactive interactions with users, such as asking right clarification questions when necessary. To support this, we curate SpeakER, a synthetic dataset that includes diverse scenarios from task-oriented dialogues, where tasks are resolved through interactive clarification questions. We present a systematic analysis of reward design for conversational proactivity and propose a principled reward formulation for teaching agents to balance asking with acting. Empirical evaluations demonstrate that our approach achieves a 20.14% absolute improvement in task completion over base models without increasing conversation turns even surpassing even much larger proprietary models, demonstrating the promise of clarification-centric user-agent interactions.

