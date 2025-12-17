---
layout: default
title: The AI Consumer Index (ACE)
---

# The AI Consumer Index (ACE)

**arXiv**: [2512.04921v1](https://arxiv.org/abs/2512.04921) | [PDF](https://arxiv.org/pdf/2512.04921.pdf)

**作者**: Julien Benchek, Rohit Shetty, Benjamin Hunsberger, Ajay Arun, Zach Richards, Brendan Foody, Osvald Nitski, Bertie Vidgen

---

## 💡 一句话要点

**提出AI消费者指数以评估前沿模型在消费任务中的表现**

**关键词**: `AI基准测试` `消费任务评估` `幻觉检测` `前沿模型比较` `网络检索验证`

## 📋 核心要点

1. 核心问题：评估前沿AI模型能否执行高价值消费任务，如购物、饮食、游戏和DIY。
2. 方法要点：采用动态检查响应是否基于检索网络来源的新颖评分方法，并包含隐藏测试集。
3. 实验或效果：GPT 5（Thinking = High）以56.1%得分领先，但模型在购物等领域表现不足，存在幻觉问题。

## 📄 摘要（原文）

> We introduce the first version of the AI Consumer Index (ACE), a benchmark for assessing whether frontier AI models can perform high-value consumer tasks. ACE contains a hidden heldout set of 400 test cases, split across four consumer activities: shopping, food, gaming, and DIY. We are also open sourcing 80 cases as a devset with a CC-BY license. For the ACE leaderboard we evaluated 10 frontier models (with websearch turned on) using a novel grading methodology that dynamically checks whether relevant parts of the response are grounded in the retrieved web sources. GPT 5 (Thinking = High) is the top-performing model, scoring 56.1%, followed by o3 Pro (Thinking = On) (55.2%) and GPT 5.1 (Thinking = High) (55.1%). Models differ across domains, and in Shopping the top model scores under 50%. For some requests (such as giving the correct price or providing working links), models are highly prone to hallucination. Overall, ACE shows a substantial gap between the performance of even the best models and consumers' AI needs.

