---
layout: default
title: Soft Adaptive Policy Optimization
---

# Soft Adaptive Policy Optimization

**arXiv**: [2511.20347v1](https://arxiv.org/abs/2511.20347) | [PDF](https://arxiv.org/pdf/2511.20347.pdf)

**作者**: Chang Gao, Chujie Zheng, Xiong-Hui Chen, Kai Dang, Shixuan Liu, Bowen Yu, An Yang, Shuai Bai, Jingren Zhou, Junyang Lin

---

## 💡 一句话要点

**提出软自适应策略优化以解决强化学习中策略更新不稳定问题**

**关键词**: `强化学习` `策略优化` `大语言模型` `训练稳定性` `软门机制`

## 📋 核心要点

1. 强化学习中令牌级重要性比率方差高，导致策略更新不稳定
2. 使用温度控制软门自适应衰减离策略更新，保留有用学习信号
3. 在数学推理基准上提升训练稳定性和Pass@1性能，并在Qwen3-VL系列中验证有效性

## 📄 摘要（原文）

> Reinforcement learning (RL) plays an increasingly important role in enhancing the reasoning capabilities of large language models (LLMs), yet stable and performant policy optimization remains challenging. Token-level importance ratios often exhibit high variance-a phenomenon exacerbated in Mixture-of-Experts models-leading to unstable updates. Existing group-based policy optimization methods, such as GSPO and GRPO, alleviate this problem via hard clipping, making it difficult to maintain both stability and effective learning. We propose Soft Adaptive Policy Optimization (SAPO), which replaces hard clipping with a smooth, temperature-controlled gate that adaptively attenuates off-policy updates while preserving useful learning signals. Compared with GSPO and GRPO, SAPO is both sequence-coherent and token-adaptive. Like GSPO, SAPO maintains sequence-level coherence, but its soft gating forms a continuous trust region that avoids the brittle hard clipping band used in GSPO. When a sequence contains a few highly off-policy tokens, GSPO suppresses all gradients for that sequence, whereas SAPO selectively down-weights only the offending tokens and preserves the learning signal from the near-on-policy ones, improving sample efficiency. Relative to GRPO, SAPO replaces hard token-level clipping with smooth, temperature-controlled scaling, enabling more informative and stable updates. Empirical results on mathematical reasoning benchmarks indicate that SAPO exhibits improved training stability and higher Pass@1 performance under comparable training budgets. Moreover, we employ SAPO to train the Qwen3-VL model series, demonstrating that SAPO yields consistent performance gains across diverse tasks and different model sizes. Overall, SAPO provides a more reliable, scalable, and effective optimization strategy for RL training of LLMs.

