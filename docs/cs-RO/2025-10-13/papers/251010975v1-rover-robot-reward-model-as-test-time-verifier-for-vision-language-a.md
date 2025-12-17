---
layout: default
title: RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model
---

# RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model

**arXiv**: [2510.10975v1](https://arxiv.org/abs/2510.10975) | [PDF](https://arxiv.org/pdf/2510.10975.pdf)

**作者**: Mingtong Dai, Lingbo Liu, Yongjie Bai, Yang Liu, Zhouxia Wang, Rui SU, Chunjie Chen, Liang Lin, Xinyu Wu

---

## 💡 一句话要点

**提出RoVer框架，通过测试时验证增强视觉-语言-动作模型性能**

**关键词**: `视觉-语言-动作模型` `测试时缩放` `过程奖励模型` `动作空间方向` `共享感知缓存` `机器人决策`

## 📋 核心要点

1. 核心问题：VLA模型性能提升依赖数据与模型规模扩展，成本高昂且受限。
2. 方法要点：使用机器人过程奖励模型验证候选动作，并预测动作空间方向进行扩展。
3. 实验或效果：通过共享感知特征缓存，在相同计算预算下评估更多候选动作。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have become a prominent paradigm for
> embodied intelligence, yet further performance improvements typically rely on
> scaling up training data and model size -- an approach that is prohibitively
> expensive for robotics and fundamentally limited by data collection costs.We
> address this limitation with $\mathbf{RoVer}$, an embodied test-time scaling
> framework that uses a $\mathbf{Ro}$bot Process Reward Model (PRM) as a
> Test-Time $\mathbf{Ver}$ifier to enhance the capabilities of existing VLA
> models without modifying their architectures or weights. Specifically, RoVer
> (i) assigns scalar-based process rewards to evaluate the reliability of
> candidate actions, and (ii) predicts an action-space direction for candidate
> expansion/refinement. During inference, RoVer generates multiple candidate
> actions concurrently from the base policy, expands them along PRM-predicted
> directions, and then scores all candidates with PRM to select the optimal
> action for execution. Notably, by caching shared perception features, it can
> amortize perception cost and evaluate more candidates under the same test-time
> computational budget. Essentially, our approach effectively transforms
> available computing resources into better action decision-making, realizing the
> benefits of test-time scaling without extra training overhead. Our
> contributions are threefold: (1) a general, plug-and-play test-time scaling
> framework for VLAs; (2) a PRM that jointly provides scalar process rewards and
> an action-space direction to guide exploration; and (3) an efficient
> direction-guided sampling strategy that leverages a shared perception cache to
> enable scalable candidate generation and selection during inference.

