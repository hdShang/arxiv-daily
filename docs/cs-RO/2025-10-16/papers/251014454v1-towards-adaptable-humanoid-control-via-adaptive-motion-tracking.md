---
layout: default
title: Towards Adaptable Humanoid Control via Adaptive Motion Tracking
---

# Towards Adaptable Humanoid Control via Adaptive Motion Tracking

**arXiv**: [2510.14454v1](https://arxiv.org/abs/2510.14454) | [PDF](https://arxiv.org/pdf/2510.14454.pdf)

**作者**: Tao Huang, Huayi Wang, Junli Ren, Kangning Yin, Zirui Wang, Xiao Chen, Feiyu Jia, Wentao Zhang, Junfeng Long, Jingbo Wang, Jiangmiao Pang

---

## 💡 一句话要点

**提出AdaMimic算法，实现从单一参考运动进行可适应人形机器人控制。**

**关键词**: `人形机器人控制` `运动跟踪` `自适应算法` `关键帧稀疏化` `时间扭曲`

## 📋 核心要点

1. 核心问题：现有方法在运动适应性和模仿精度间存在权衡，难以从单一运动实现高精度适应。
2. 方法要点：通过稀疏化参考运动为关键帧，训练策略生成密集运动，并使用适配器调整速度和动作。
3. 实验或效果：在仿真和真实人形机器人上验证，在多种适应条件下提升模仿精度和适应性。

## 📄 摘要（原文）

> Humanoid robots are envisioned to adapt demonstrated motions to diverse
> real-world conditions while accurately preserving motion patterns. Existing
> motion prior approaches enable well adaptability with a few motions but often
> sacrifice imitation accuracy, whereas motion-tracking methods achieve accurate
> imitation yet require many training motions and a test-time target motion to
> adapt. To combine their strengths, we introduce AdaMimic, a novel motion
> tracking algorithm that enables adaptable humanoid control from a single
> reference motion. To reduce data dependence while ensuring adaptability, our
> method first creates an augmented dataset by sparsifying the single reference
> motion into keyframes and applying light editing with minimal physical
> assumptions. A policy is then initialized by tracking these sparse keyframes to
> generate dense intermediate motions, and adapters are subsequently trained to
> adjust tracking speed and refine low-level actions based on the adjustment,
> enabling flexible time warping that further improves imitation accuracy and
> adaptability. We validate these significant improvements in our approach in
> both simulation and the real-world Unitree G1 humanoid robot in multiple tasks
> across a wide range of adaptation conditions. Videos and code are available at
> https://taohuang13.github.io/adamimic.github.io/.

