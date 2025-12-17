---
layout: default
title: Counteracting Matthew Effect in Self-Improvement of LVLMs through Head-Tail Re-balancing
---

# Counteracting Matthew Effect in Self-Improvement of LVLMs through Head-Tail Re-balancing

**arXiv**: [2510.26474v1](https://arxiv.org/abs/2510.26474) | [PDF](https://arxiv.org/pdf/2510.26474.pdf)

**作者**: Xin Guo, Zhiheng Xi, Yiwen Ding, Yitao Zhai, Xiaowei Shi, Xunliang Cai, Tao Gui, Qi Zhang, Xuanjing Huang

---

## 💡 一句话要点

**提出头尾重平衡策略以解决LVLM自改进中的马太效应问题**

**关键词**: `大型视觉语言模型` `自改进` `马太效应` `头尾重平衡` `视觉推理` `分布重塑`

## 📋 核心要点

1. LVLM自改进中模型对简单查询优化过度，复杂查询优化不足，导致马太效应。
2. 从分布重塑和轨迹重采样角度引入四种策略，实现头尾数据平衡优化。
3. 在视觉推理任务中，方法平均提升3.86分，优于基线自改进。

## 📄 摘要（原文）

> Self-improvement has emerged as a mainstream paradigm for advancing the
> reasoning capabilities of large vision-language models (LVLMs), where models
> explore and learn from successful trajectories iteratively. However, we
> identify a critical issue during this process: the model excels at generating
> high-quality trajectories for simple queries (i.e., head data) but struggles
> with more complex ones (i.e., tail data). This leads to an imbalanced
> optimization that drives the model to prioritize simple reasoning skills, while
> hindering its ability to tackle more complex reasoning tasks. Over iterations,
> this imbalance becomes increasingly pronounced--a dynamic we term the "Matthew
> effect"--which ultimately hinders further model improvement and leads to
> performance bottlenecks. To counteract this challenge, we introduce four
> efficient strategies from two perspectives: distribution-reshaping and
> trajectory-resampling, to achieve head-tail re-balancing during the
> exploration-and-learning self-improvement process. Extensive experiments on
> Qwen2-VL-7B-Instruct and InternVL2.5-4B models across visual reasoning tasks
> demonstrate that our methods consistently improve visual reasoning
> capabilities, outperforming vanilla self-improvement by 3.86 points on average.

