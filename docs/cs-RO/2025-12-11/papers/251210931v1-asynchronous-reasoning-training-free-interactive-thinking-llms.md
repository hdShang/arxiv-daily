---
layout: default
title: Asynchronous Reasoning: Training-Free Interactive Thinking LLMs
---

# Asynchronous Reasoning: Training-Free Interactive Thinking LLMs

**arXiv**: [2512.10931v1](https://arxiv.org/abs/2512.10931) | [PDF](https://arxiv.org/pdf/2512.10931.pdf)

**作者**: George Yakushev, Nataliia Babina, Masoud Vahid Dastgerdi, Vyacheslav Zhdanovskiy, Alina Shutova, Denis Kuznedelev

---

## 💡 一句话要点

**提出异步推理方法，使LLM无需训练即可实时交互思考与响应。**

**关键词**: `异步推理` `实时交互` `旋转嵌入` `LLM增强` `训练免费`

## 📋 核心要点

1. 核心问题：LLM推理需顺序交互，不适用于实时响应场景如语音助手。
2. 方法要点：利用旋转嵌入特性，使LLM能同时思考、监听和生成输出。
3. 实验或效果：在数学、常识和安全推理中，实时延迟降低6-11倍，首非思考令牌时间≤5秒。

## 📄 摘要（原文）

> Many state-of-the-art LLMs are trained to think before giving their answer. Reasoning can greatly improve language model capabilities and safety, but it also makes them less interactive: given a new input, a model must stop thinking before it can respond. Real-world use cases such as voice-based or embedded assistants require an LLM agent to respond and adapt to additional information in real time, which is incompatible with sequential interactions. In contrast, humans can listen, think, and act asynchronously: we begin thinking about the problem while reading it and continue thinking while formulating the answer. In this work, we augment LLMs capable of reasoning to operate in a similar way without additional training. Our method uses the properties of rotary embeddings to enable LLMs built for sequential interactions to simultaneously think, listen, and generate outputs. We evaluate our approach on math, commonsense, and safety reasoning and find that it can generate accurate thinking-augmented answers in real time, reducing time to first non-thinking token from minutes to <= 5s. and the overall real-time delays by 6-11x.

