---
layout: default
title: BEAVER: An Efficient Deterministic LLM Verifier
---

# BEAVER: An Efficient Deterministic LLM Verifier

**arXiv**: [2512.05439v1](https://arxiv.org/abs/2512.05439) | [PDF](https://arxiv.org/pdf/2512.05439.pdf)

**作者**: Tarun Suresh, Nalin Wadhwa, Debangshu Banerjee, Gagandeep Singh

---

## 💡 一句话要点

**提出BEAVER框架以确定性验证大语言模型输出满足约束，提供概率保证。**

**关键词**: `大语言模型验证` `确定性概率界限` `前缀闭包约束` `令牌树数据结构` `安全代码生成`

## 📋 核心要点

1. 核心问题：大语言模型生产部署需可靠验证输出约束，采样方法无严格保证。
2. 方法要点：基于前缀闭包约束，使用令牌树和前沿数据结构系统探索生成空间，保持概率界限。
3. 实验或效果：在正确性、隐私和代码生成任务中，比基线方法界限更紧、高风险实例识别更多。

## 📄 摘要（原文）

> As large language models (LLMs) transition from research prototypes to production systems, practitioners often need reliable methods to verify that model outputs satisfy required constraints. While sampling-based estimates provide an intuition of model behavior, they offer no sound guarantees. We present BEAVER, the first practical framework for computing deterministic, sound probability bounds on LLM constraint satisfaction. Given any prefix-closed semantic constraint, BEAVER systematically explores the generation space using novel token trie and frontier data structures, maintaining provably sound bounds at every iteration. We formalize the verification problem, prove soundness of our approach, and evaluate BEAVER on correctness verification, privacy verification and secure code generation tasks across multiple state of the art LLMs. BEAVER achieves 6 to 8 times tighter probability bounds and identifies 3 to 4 times more high risk instances compared to baseline methods under identical computational budgets, enabling precise characterization and risk assessment that loose bounds or empirical evaluation cannot provide.

