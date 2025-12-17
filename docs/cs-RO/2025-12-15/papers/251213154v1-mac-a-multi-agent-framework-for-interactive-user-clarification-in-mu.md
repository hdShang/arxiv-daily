---
layout: default
title: MAC: A Multi-Agent Framework for Interactive User Clarification in Multi-turn Conversations
---

# MAC: A Multi-Agent Framework for Interactive User Clarification in Multi-turn Conversations

**arXiv**: [2512.13154v1](https://arxiv.org/abs/2512.13154) | [PDF](https://arxiv.org/pdf/2512.13154.pdf)

**作者**: Emre Can Acikgoz, Jinoh Oh, Joo Hyuk Jeon, Jie Hao, Heng Ji, Dilek Hakkani-Tür, Gokhan Tur, Xiang Li, Chengyuan Ma, Xing Fan

---

## 💡 一句话要点

**提出多智能体框架MAC，通过协同交互解决多轮对话中用户请求的歧义问题。**

**关键词**: `多智能体对话` `歧义澄清` `交互框架` `任务导向对话` `协同协调`

## 📋 核心要点

1. 核心问题：多智能体对话中，如何协调智能体以最优方式发起和制定澄清查询，解决用户歧义。
2. 方法要点：引入歧义分类法，设计MAC框架，使多智能体协同管理澄清对话，主动交互用户。
3. 实验或效果：在MultiWOZ 2.4上评估，任务成功率提升7.8%，平均对话轮数减少，提高通信可靠性。

## 📄 摘要（原文）

> Conversational agents often encounter ambiguous user requests, requiring an effective clarification to successfully complete tasks. While recent advancements in real-world applications favor multi-agent architectures to manage complex conversational scenarios efficiently, ambiguity resolution remains a critical and underexplored challenge--particularly due to the difficulty of determining which agent should initiate a clarification and how agents should coordinate their actions when faced with uncertain or incomplete user input. The fundamental questions of when to interrupt a user and how to formulate the optimal clarification query within the most optimal multi-agent settings remain open. In this paper, we propose MAC (Multi-Agent Clarification), an interactive multi-agent framework specifically optimized to resolve user ambiguities by strategically managing clarification dialogues. We first introduce a novel taxonomy categorizing user ambiguities to systematically guide clarification strategies. Then, we present MAC that autonomously coordinates multiple agents to interact synergistically with users. Empirical evaluations on MultiWOZ 2.4 demonstrate that enabling clarification at both levels increases task success rate 7.8\% (54.5 to 62.3) and reduces the average number of dialogue turns (6.53 to 4.86) by eliciting all required user information up front and minimizing repetition. Our findings highlight the importance of active user interaction and role-aware clarification for more reliable human-agent communication.

