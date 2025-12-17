---
layout: default
title: Zero-Knowledge Proof Based Verifiable Inference of Models
---

# Zero-Knowledge Proof Based Verifiable Inference of Models

**arXiv**: [2511.19902v1](https://arxiv.org/abs/2511.19902) | [PDF](https://arxiv.org/pdf/2511.19902.pdf)

**作者**: Yunxiao Wang

---

## 💡 一句话要点

**提出零知识证明框架以验证AI模型推理而不暴露参数**

**关键词**: `零知识证明` `模型推理验证` `zkSNARK` `深度学习` `知识产权保护`

## 📋 核心要点

1. 核心问题：AI模型推理正确性验证困难，因参数涉及知识产权
2. 方法要点：基于递归零知识证明，支持线性与非线性层，无需可信设置
3. 实验或效果：实现ZK-DeepSeek模型，展示高效灵活的实际验证性能

## 📄 摘要（原文）

> Recent advances in artificial intelligence (AI), particularly deep learning, have led to widespread adoption across various applications. Yet, a fundamental challenge persists: how can we verify the correctness of AI model inference when model owners cannot (or will not) reveal their parameters? These parameters represent enormous training costs and valuable intellectual property, making transparent verification difficult. In this paper, we introduce a zero-knowledge framework capable of verifying deep learning inference without exposing model internal parameters. Built on recursively composed zero-knowledge proofs and requiring no trusted setup, our framework supports both linear and nonlinear neural network layers, including matrix multiplication, normalization, softmax, and SiLU. Leveraging the Fiat-Shamir heuristic, we obtain a succinct non-interactive argument of knowledge (zkSNARK) with constant-size proofs. To demonstrate the practicality of our approach, we translate the DeepSeek model into a fully SNARK-verifiable version named ZK-DeepSeek and show experimentally that our framework delivers both efficiency and flexibility in real-world AI verification workloads.

