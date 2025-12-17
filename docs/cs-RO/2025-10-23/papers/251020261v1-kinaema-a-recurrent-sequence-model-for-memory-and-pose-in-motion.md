---
layout: default
title: Kinaema: a recurrent sequence model for memory and pose in motion
---

# Kinaema: a recurrent sequence model for memory and pose in motion

**arXiv**: [2510.20261v1](https://arxiv.org/abs/2510.20261) | [PDF](https://arxiv.org/pdf/2510.20261.pdf)

**作者**: Mert Bulent Sariyildiz, Philippe Weinzaepfel, Guillaume Bono, Gianluca Monaci, Christian Wolf

---

## 💡 一句话要点

**提出Kinaema模型以解决机器人在连续操作中利用先前视觉信息定位自身的问题**

**关键词**: `机器人定位` `循环变换器` `隐式记忆` `视觉导航` `Mem-Nav任务`

## 📋 核心要点

1. 核心问题：机器人在先前见过的空间中如何高效定位自身，利用历史观测优化操作效率
2. 方法要点：使用循环变换器维护隐式潜在记忆，压缩传感器历史，无需显式存储观测
3. 实验或效果：在Mem-Nav任务中验证模型能导航至目标，保持场景表示，计算高效

## 📄 摘要（原文）

> One key aspect of spatially aware robots is the ability to "find their
> bearings", ie. to correctly situate themselves in previously seen spaces. In
> this work, we focus on this particular scenario of continuous robotics
> operations, where information observed before an actual episode start is
> exploited to optimize efficiency. We introduce a new model, Kinaema, and agent,
> capable of integrating a stream of visual observations while moving in a
> potentially large scene, and upon request, processing a query image and
> predicting the relative position of the shown space with respect to its current
> position. Our model does not explicitly store an observation history, therefore
> does not have hard constraints on context length. It maintains an implicit
> latent memory, which is updated by a transformer in a recurrent way,
> compressing the history of sensor readings into a compact representation. We
> evaluate the impact of this model in a new downstream task we call "Mem-Nav".
> We show that our large-capacity recurrent model maintains a useful
> representation of the scene, navigates to goals observed before the actual
> episode start, and is computationally efficient, in particular compared to
> classical transformers with attention over an observation history.

