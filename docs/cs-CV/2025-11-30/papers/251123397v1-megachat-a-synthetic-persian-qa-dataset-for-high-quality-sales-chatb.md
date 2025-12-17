---
layout: default
title: MegaChat: A Synthetic Persian Q&A Dataset for High-Quality Sales Chatbot Evaluation
---

# MegaChat: A Synthetic Persian Q&A Dataset for High-Quality Sales Chatbot Evaluation

**arXiv**: [2511.23397v1](https://arxiv.org/abs/2511.23397) | [PDF](https://arxiv.org/pdf/2511.23397.pdf)

**作者**: Mahdi Rahmani, AmirHossein Saffari, Reyhane Rahmani

---

## 💡 一句话要点

**提出MegaChat合成波斯语问答数据集，以低成本评估Telegram销售聊天机器人。**

**关键词**: `合成数据集` `波斯语问答` `多智能体架构` `检索增强生成` `销售聊天机器人` `低资源语言`

## 📋 核心要点

1. 核心问题：波斯语等低资源语言缺乏高质量问答数据集，阻碍销售聊天机器人开发。
2. 方法要点：采用多智能体架构自动生成人物感知问答对，无需人工标注。
3. 实验或效果：代理系统在多数渠道优于传统检索增强生成模型，提升数据集质量。

## 📄 摘要（原文）

> Small and medium-sized enterprises (SMEs) in Iran increasingly leverage Telegram for sales, where real-time engagement is essential for conversion. However, developing AI-driven chatbots for this purpose requires large, high-quality question-and-answer (Q&A) datasets, which are typically expensive and resource-intensive to produce, especially for low-resource languages like Persian. In this paper, we introduce MegaChat, the first fully synthetic Persian Q&A dataset designed to evaluate intelligent sales chatbots in Telegram-based e-commerce. We propose a novel, automated multi-agent architecture that generates persona-aware Q&A pairs by collecting data from active Telegram shopping channels. The system employs specialized agents for question generation, validation, and refinement, ensuring the production of realistic and diverse conversational data. To evaluate answer generation, we compare three classic retrieval-augmented generation (RAG) models with our advanced agentic system, which features multi-query retrieval, reranking, and persona-aligned response synthesis. Using GPT-5.1 for evaluation across six quality dimensions, our results show that the agentic architecture outperformed traditional RAG models in 4 out of 5 diverse channels, demonstrating its ability to generate scalable, high-quality datasets without relying on expensive human annotation or complex fine-tuning. MegaChat provides SMEs with an efficient, cost-effective solution for building intelligent customer engagement systems in specialized commercial domains, enabling advancements in multilingual conversational AI for low-resource languages. Download: https://github.com/MegaChat-Tech/MegaChat-DataSet

