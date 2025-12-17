---
layout: default
title: AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models
---

# AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models

**arXiv**: [2511.14148v1](https://arxiv.org/abs/2511.14148) | [PDF](https://arxiv.org/pdf/2511.14148.pdf)

**作者**: Yuhua Jiang, Shuang Cheng, Yan Ding, Feifei Gao, Biqing Qi

---

## 💡 一句话要点

**提出异步流匹配VLA以解决长视野任务中动作生成不稳定问题**

**关键词**: `视觉语言动作模型` `异步流匹配` `动作自校正` `机器人操作` `长视野任务` `置信度评估`

## 📋 核心要点

1. 传统VLA模型使用同步流匹配，缺乏动作上下文感知，易在长视野任务中失败
2. 引入异步流匹配和置信度评估器，实现非均匀时间调度和动作自校正
3. 在机器人操作基准测试中，数据高效且达到最先进性能，展示自校正能力

## 📄 摘要（原文）

> Vision-language-action (VLA) models have recently emerged as a powerful paradigm for building generalist robots. However, traditional VLA models that generate actions through flow matching (FM) typically rely on rigid and uniform time schedules, i.e., synchronous FM (SFM). Without action context awareness and asynchronous self-correction, SFM becomes unstable in long-horizon tasks, where a single action error can cascade into failure. In this work, we propose asynchronous flow matching VLA (AsyncVLA), a novel framework that introduces temporal flexibility in asynchronous FM (AFM) and enables self-correction in action generation. AsyncVLA breaks from the vanilla SFM in VLA models by generating the action tokens in a non-uniform time schedule with action context awareness. Besides, our method introduces the confidence rater to extract confidence of the initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution. Moreover, we propose a unified training procedure for SFM and AFM that endows a single model with both modes, improving KV-cache utilization. Extensive experiments on robotic manipulation benchmarks demonstrate that AsyncVLA is data-efficient and exhibits self-correction ability. AsyncVLA achieves state-of-the-art results across general embodied evaluations due to its asynchronous generation in AFM. Our code is available at https://github.com/YuhuaJiang2002/AsyncVLA.

