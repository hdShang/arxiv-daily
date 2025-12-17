---
layout: default
title: Pessimistic Verification for Open Ended Math Questions
---

# Pessimistic Verification for Open Ended Math Questions

**arXiv**: [2511.21522v1](https://arxiv.org/abs/2511.21522) | [PDF](https://arxiv.org/pdf/2511.21522.pdf)

**作者**: Yanxing Huang, Zihan Tang, Zejin Lin, Peng Li, Yang Liu

---

## 💡 一句话要点

**提出悲观验证方法以提升开放数学问题验证性能**

**关键词**: `悲观验证` `数学问题验证` `错误检测` `并行验证` `语言模型可靠性`

## 📋 核心要点

1. 核心问题：现有验证方法在错误检测能力上存在局限，影响开放数学问题验证效果。
2. 方法要点：设计多并行验证流程，任一验证报告错误即判定证明错误，提升准确性。
3. 实验或效果：在多个数学基准测试中显著提升性能，且计算资源消耗低，优于扩展长链思维。

## 📄 摘要（原文）

> The key limitation of the verification performance lies in the ability of error detection. With this intuition we designed several variants of pessimistic verification, which are simple workflows that could significantly improve the verification of open-ended math questions. In pessimistic verification we construct multiple parallel verifications for the same proof, and the proof is deemed incorrect if any one of them reports an error. This simple technique significantly improves the performance across many math verification benchmarks without incurring substantial computational resources. Its token efficiency even surpassed extended long-CoT in test-time scaling. Our case studies further indicate that the majority of false negatives in stronger models are actually caused by annotation errors in the original dataset, so our method's performance is in fact underestimated. Self-verification for mathematical problems can effectively improve the reliability and performance of language model outputs, and it also plays a critical role in enabling long-horizon mathematical tasks. We believe that research on pessimistic verification will help enhance the mathematical capabilities of language models across a wide range of tasks.

