---
layout: default
title: Decoupled Q-Chunking
---

# Decoupled Q-Chunking

**arXiv**: [2512.10926v1](https://arxiv.org/abs/2512.10926) | [PDF](https://arxiv.org/pdf/2512.10926.pdf)

**作者**: Qiyang Li, Seohong Park, Sergey Levine

---

## 💡 一句话要点

**提出解耦Q分块算法，以解决分块评论家策略提取中的开环次优性和长动作块建模难题。**

**关键词**: `强化学习` `分块评论家` `值蒸馏` `离线策略优化` `长视界任务`

## 📋 核心要点

1. 核心问题：分块评论家虽加速值备份，但策略需开环输出长动作块，导致次优和建模困难。
2. 方法要点：解耦评论家与策略的分块长度，通过蒸馏评论家优化策略，近似部分动作块的最大值。
3. 实验或效果：在长视界离线目标导向任务中评估，性能优于先前方法。

## 📄 摘要（原文）

> Temporal-difference (TD) methods learn state and action values efficiently by bootstrapping from their own future value predictions, but such a self-bootstrapping mechanism is prone to bootstrapping bias, where the errors in the value targets accumulate across steps and result in biased value estimates. Recent work has proposed to use chunked critics, which estimate the value of short action sequences ("chunks") rather than individual actions, speeding up value backup. However, extracting policies from chunked critics is challenging: policies must output the entire action chunk open-loop, which can be sub-optimal for environments that require policy reactivity and also challenging to model especially when the chunk length grows. Our key insight is to decouple the chunk length of the critic from that of the policy, allowing the policy to operate over shorter action chunks. We propose a novel algorithm that achieves this by optimizing the policy against a distilled critic for partial action chunks, constructed by optimistically backing up from the original chunked critic to approximate the maximum value achievable when a partial action chunk is extended to a complete one. This design retains the benefits of multi-step value propagation while sidestepping both the open-loop sub-optimality and the difficulty of learning action chunking policies for long action chunks. We evaluate our method on challenging, long-horizon offline goal-conditioned tasks and show that it reliably outperforms prior methods. Code: github.com/ColinQiyangLi/dqc.

