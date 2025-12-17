---
layout: default
title: RLHFSpec: Breaking the Efficiency Bottleneck in RLHF Training via Adaptive Drafting
---

# RLHFSpec: Breaking the Efficiency Bottleneck in RLHF Training via Adaptive Drafting

**arXiv**: [2512.04752v1](https://arxiv.org/abs/2512.04752) | [PDF](https://arxiv.org/pdf/2512.04752.pdf)

**作者**: Siqi Wang, Hailong Yang, Junjie Zhu, Xuezhu Wang, Yufan Xu, Depei Qian

---

## 💡 一句话要点

**提出RLHFSpec系统，通过自适应推测解码加速RLHF训练中的生成阶段瓶颈**

**关键词**: `强化学习人类反馈` `推测解码` `自适应策略` `GPU资源优化` `大语言模型微调`

## 📋 核心要点

1. RLHF训练中生成阶段是效率瓶颈，需优化以提升整体执行速度
2. 集成推测解码并采用自适应策略选择，结合样本重分配以充分利用GPU资源
3. 实验显示在生成阶段实现更高吞吐量，显著加速整个RLHF执行过程

## 📄 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) is an important fine-tuning technique for large language models (LLMs) and comprises three stages: generation, inference, and training. The generation stage generates samples that are then used to infer learnable experiences for training. We observe that the generation stage is the bottleneck of the entire execution process and consider it a key point for optimization. Specifically, we realize the first attempt to integrate speculative decoding into the RLHF generation stage and propose RLHFSpec, an RLHF system that accelerates generation execution with adaptive speculative decoding and sample reallocation. To fully exploit the performance potential provided by speculative decoding, especially dealing with the dynamic workload of the generation stage, RLHFSpec proposes a workload-aware drafting strategy selection mechanism, which selects the near-optimal strategy by jointly considering the verification cost and the number of accepted tokens. Moreover, RLHFSpec also proposes sample reallocation to fully utilize the GPU resources, and optimizes it with an efficient sample migration mechanism. The experimental results show that the RLHFSpec can achieve higher throughput in the generation stage compared to state-of-the-art works. Moreover, due to the effective alleviation of the generation bottleneck, RLHFSpec also shows significant performance speedup in the entire RLHF execution.

