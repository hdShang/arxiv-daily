---
layout: default
title: ViPER: Empowering the Self-Evolution of Visual Perception Abilities in Vision-Language Model
---

# ViPER: Empowering the Self-Evolution of Visual Perception Abilities in Vision-Language Model

**arXiv**: [2510.24285v1](https://arxiv.org/abs/2510.24285) | [PDF](https://arxiv.org/pdf/2510.24285.pdf)

**作者**: Juntian Zhang, Song Jin, Chuanqi Cheng, Yuhan Liu, Yankai Lin, Xun Zhang, Yufei Zhang, Fei Jiang, Guojun Yin, Wei Lin, Rui Yan

---

## 💡 一句话要点

**提出ViPER框架以增强视觉语言模型的细粒度视觉感知能力**

**关键词**: `视觉语言模型` `细粒度视觉感知` `自举框架` `两阶段强化学习` `图像重建` `自进化`

## 📋 核心要点

1. 核心问题：视觉语言模型在细粒度视觉感知方面存在瓶颈，影响实际应用。
2. 方法要点：设计两阶段任务和自举框架，通过自批判和自预测实现迭代进化。
3. 实验或效果：在多个基准测试中平均提升1.7%，细粒度感知最高提升6.0%。

## 📄 摘要（原文）

> The limited capacity for fine-grained visual perception presents a critical
> bottleneck for Vision-Language Models (VLMs) in real-world applications.
> Addressing this is challenging due to the scarcity of high-quality data and the
> limitations of existing methods: supervised fine-tuning (SFT) often compromises
> general capabilities, while reinforcement fine-tuning (RFT) prioritizes textual
> reasoning over visual perception. To bridge this gap, we propose a novel
> two-stage task that structures visual perception learning as a coarse-to-fine
> progressive process. Based on this task formulation, we develop ViPER, a
> self-bootstrapping framework specifically designed to enable iterative
> evolution through self-critiquing and self-prediction. By synergistically
> integrating image-level and instance-level reconstruction with a two-stage
> reinforcement learning strategy, ViPER establishes a closed-loop training
> paradigm, where internally synthesized data directly fuel the enhancement of
> perceptual ability. Applied to the Qwen2.5-VL family, ViPER produces the
> Qwen-Viper series. With an average gain of 1.7% on seven comprehensive
> benchmarks spanning various tasks and up to 6.0% on fine-grained perception,
> Qwen-Viper consistently demonstrates superior performance across different
> vision-language scenarios while maintaining generalizability. Beyond enabling
> self-improvement in perceptual capabilities, ViPER provides concrete evidence
> for the reciprocal relationship between generation and understanding, a
> breakthrough to developing more autonomous and capable VLMs.

