---
layout: default
title: ASTRIDE: A Security Threat Modeling Platform for Agentic-AI Applications
---

# ASTRIDE: A Security Threat Modeling Platform for Agentic-AI Applications

**arXiv**: [2512.04785v1](https://arxiv.org/abs/2512.04785) | [PDF](https://arxiv.org/pdf/2512.04785.pdf)

**作者**: Eranga Bandara, Amin Hass, Ross Gore, Sachin Shetty, Ravi Mukkamala, Safdar H. Bouk, Xueping Liang, Ng Wee Keong, Kasun De Zoysa, Aruna Withanage, Nilaan Loganathan

---

## 💡 一句话要点

**提出ASTRIDE平台以解决AI代理应用中的安全威胁建模问题**

**关键词**: `AI代理安全` `威胁建模自动化` `视觉语言模型` `推理大语言模型` `STRIDE扩展`

## 📋 核心要点

1. AI代理系统面临提示注入等新型安全挑战，传统威胁建模框架难以覆盖
2. ASTRIDE扩展STRIDE框架，新增AI代理特定攻击类别，并集成视觉语言模型与推理大语言模型实现自动化
3. 评估显示ASTRIDE能提供准确、可扩展和可解释的威胁建模，适用于下一代智能系统

## 📄 摘要（原文）

> AI agent-based systems are becoming increasingly integral to modern software architectures, enabling autonomous decision-making, dynamic task execution, and multimodal interactions through large language models (LLMs). However, these systems introduce novel and evolving security challenges, including prompt injection attacks, context poisoning, model manipulation, and opaque agent-to-agent communication, that are not effectively captured by traditional threat modeling frameworks. In this paper, we introduce ASTRIDE, an automated threat modeling platform purpose-built for AI agent-based systems. ASTRIDE extends the classical STRIDE framework by introducing a new threat category, A for AI Agent-Specific Attacks, which encompasses emerging vulnerabilities such as prompt injection, unsafe tool invocation, and reasoning subversion, unique to agent-based applications. To automate threat modeling, ASTRIDE combines a consortium of fine-tuned vision-language models (VLMs) with the OpenAI-gpt-oss reasoning LLM to perform end-to-end analysis directly from visual agent architecture diagrams, such as data flow diagrams(DFDs). LLM agents orchestrate the end-to-end threat modeling automation process by coordinating interactions between the VLM consortium and the reasoning LLM. Our evaluations demonstrate that ASTRIDE provides accurate, scalable, and explainable threat modeling for next-generation intelligent systems. To the best of our knowledge, ASTRIDE is the first framework to both extend STRIDE with AI-specific threats and integrate fine-tuned VLMs with a reasoning LLM to fully automate diagram-driven threat modeling in AI agent-based applications.

