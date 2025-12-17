---
layout: default
title: ThinkTrap: Denial-of-Service Attacks against Black-box LLM Services via Infinite Thinking
---

# ThinkTrap: Denial-of-Service Attacks against Black-box LLM Services via Infinite Thinking

**arXiv**: [2512.07086v1](https://arxiv.org/abs/2512.07086) | [PDF](https://arxiv.org/pdf/2512.07086.pdf)

**作者**: Yunzhe Li, Jianan Wang, Hongzi Zhu, James Lin, Shan Chang, Minyi Guo

---

## 💡 一句话要点

**提出ThinkTrap框架，在黑盒环境中通过无限思考对LLM服务进行拒绝服务攻击**

**关键词**: `拒绝服务攻击` `黑盒优化` `LLM安全` `无限推理` `嵌入空间`

## 📋 核心要点

1. 核心问题：黑盒LLM服务面临通过无限推理循环的拒绝服务攻击风险
2. 方法要点：将离散令牌映射到连续嵌入空间，在低维子空间进行高效黑盒优化
3. 实验或效果：在请求频率限制下，攻击可将服务吞吐量降至1%或导致完全失效

## 📄 摘要（原文）

> Large Language Models (LLMs) have become foundational components in a wide range of applications, including natural language understanding and generation, embodied intelligence, and scientific discovery. As their computational requirements continue to grow, these models are increasingly deployed as cloud-based services, allowing users to access powerful LLMs via the Internet. However, this deployment model introduces a new class of threat: denial-of-service (DoS) attacks via unbounded reasoning, where adversaries craft specially designed inputs that cause the model to enter excessively long or infinite generation loops. These attacks can exhaust backend compute resources, degrading or denying service to legitimate users. To mitigate such risks, many LLM providers adopt a closed-source, black-box setting to obscure model internals. In this paper, we propose ThinkTrap, a novel input-space optimization framework for DoS attacks against LLM services even in black-box environments. The core idea of ThinkTrap is to first map discrete tokens into a continuous embedding space, then undertake efficient black-box optimization in a low-dimensional subspace exploiting input sparsity. The goal of this optimization is to identify adversarial prompts that induce extended or non-terminating generation across several state-of-the-art LLMs, achieving DoS with minimal token overhead. We evaluate the proposed attack across multiple commercial, closed-source LLM services. Our results demonstrate that, even far under the restrictive request frequency limits commonly enforced by these platforms, typically capped at ten requests per minute (10 RPM), the attack can degrade service throughput to as low as 1% of its original capacity, and in some cases, induce complete service failure.

