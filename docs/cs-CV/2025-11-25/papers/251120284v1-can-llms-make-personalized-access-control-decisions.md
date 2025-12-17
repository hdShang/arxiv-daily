---
layout: default
title: Can LLMs Make (Personalized) Access Control Decisions?
---

# Can LLMs Make (Personalized) Access Control Decisions?

**arXiv**: [2511.20284v1](https://arxiv.org/abs/2511.20284) | [PDF](https://arxiv.org/pdf/2511.20284.pdf)

**作者**: Friederike Groschupp, Daniele Lain, Aritra Dhar, Lara Magdalena Lazier, Srdjan Čapkun

---

## 💡 一句话要点

**提出利用LLM进行动态访问控制决策以减轻用户认知负担。**

**关键词**: `访问控制决策` `大型语言模型` `用户隐私偏好` `安全权衡` `自然语言处理`

## 📋 核心要点

1. 系统复杂性增加导致用户访问控制决策认知负担过重。
2. 利用LLM处理自然语言偏好，实现动态、上下文感知决策。
3. 用户研究显示LLM决策准确率达86%，但个性化可能违反安全最佳实践。

## 📄 摘要（原文）

> Precise access control decisions are crucial to the security of both traditional applications and emerging agent-based systems. Typically, these decisions are made by users during app installation or at runtime. Due to the increasing complexity and automation of systems, making these access control decisions can add a significant cognitive load on users, often overloading them and leading to suboptimal or even arbitrary access control decisions. To address this problem, we propose to leverage the processing and reasoning capabilities of large language models (LLMs) to make dynamic, context-aware decisions aligned with the user's security preferences. For this purpose, we conducted a user study, which resulted in a dataset of 307 natural-language privacy statements and 14,682 access control decisions made by users. We then compare these decisions against those made by two versions of LLMs: a general and a personalized one, for which we also gathered user feedback on 1,446 of its decisions.
>   Our results show that in general, LLMs can reflect users' preferences well, achieving up to 86\% accuracy when compared to the decision made by the majority of users. Our study also reveals a crucial trade-off in personalizing such a system: while providing user-specific privacy preferences to the LLM generally improves agreement with individual user decisions, adhering to those preferences can also violate some security best practices. Based on our findings, we discuss design and risk considerations for implementing a practical natural-language-based access control system that balances personalization, security, and utility.

