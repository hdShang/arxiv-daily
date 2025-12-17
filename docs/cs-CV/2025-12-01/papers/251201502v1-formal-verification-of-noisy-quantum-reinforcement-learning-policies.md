---
layout: default
title: Formal Verification of Noisy Quantum Reinforcement Learning Policies
---

# Formal Verification of Noisy Quantum Reinforcement Learning Policies

**arXiv**: [2512.01502v1](https://arxiv.org/abs/2512.01502) | [PDF](https://arxiv.org/pdf/2512.01502.pdf)

**作者**: Dennis Gross

---

## 💡 一句话要点

**提出QVerifier以验证含噪声量子强化学习策略的安全性**

**关键词**: `量子强化学习` `形式化验证` `概率模型检验` `量子噪声` `安全验证` `策略分析`

## 📋 核心要点

1. 量子强化学习策略面临量子测量和硬件噪声带来的不确定性风险
2. QVerifier将量子不确定性融入概率模型检验，通过Storm模型检查器验证安全属性
3. 实验表明该方法能精确测量不同噪声模型对安全性的影响

## 📄 摘要（原文）

> Quantum reinforcement learning (QRL) aims to use quantum effects to create sequential decision-making policies that achieve tasks more effectively than their classical counterparts. However, QRL policies face uncertainty from quantum measurements and hardware noise, such as bit-flip, phase-flip, and depolarizing errors, which can lead to unsafe behavior. Existing work offers no systematic way to verify whether trained QRL policies meet safety requirements under specific noise conditions.
>   We introduce QVerifier, a formal verification method that applies probabilistic model checking to analyze trained QRL policies with and without modeled quantum noise. QVerifier builds a complete model of the policy-environment interaction, incorporates quantum uncertainty directly into the transition probabilities, and then checks safety properties using the Storm model checker.
>   Experiments across multiple QRL environments show that QVerifier precisely measures how different noise models influence safety, revealing both performance degradation and cases where noise can help. By enabling rigorous safety verification before deployment, QVerifier addresses a critical need: because access to quantum hardware is expensive, pre-deployment verification is essential for any safety-critical use of QRL. QVerifier targets a potential classical-quantum sweet spot: trained QRL policies that execute efficiently on quantum hardware, yet remain tractable for classical probabilistic model checking despite being too slow for real-time classical deployment.

