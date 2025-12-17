---
layout: default
title: Objects in Generated Videos Are Slower Than They Appear: Models Suffer Sub-Earth Gravity and Don't Know Galileo's Principle...for now
---

# Objects in Generated Videos Are Slower Than They Appear: Models Suffer Sub-Earth Gravity and Don't Know Galileo's Principle...for now

**arXiv**: [2512.02016v1](https://arxiv.org/abs/2512.02016) | [PDF](https://arxiv.org/pdf/2512.02016.pdf)

**作者**: Varun Varma Thozhiyoor, Shivam Tripathi, Venkatesh Babu Radhakrishnan, Anand Bhattad

---

## 💡 一句话要点

**提出无单位双物体协议以揭示视频生成模型违反伽利略等效原理，并通过轻量适配器部分纠正重力表示错误。**

**关键词**: `视频生成模型` `物理世界建模` `重力表示` `伽利略等效原理` `低秩适配器` `零样本泛化`

## 📋 核心要点

1. 核心问题：视频生成模型在重力表示上存在错误，物体下落加速度显著低于地球重力，且物理测试受度量尺度模糊性干扰。
2. 方法要点：引入无单位双物体协议，基于时间平方比与高度比的关系独立测试重力，隔离尺度混淆因素，揭示模型违反伽利略等效原理。
3. 实验或效果：使用仅100个单球下落视频微调轻量低秩适配器，将有效重力从1.81 m/s²提升至6.43 m/s²，并零样本泛化到双球下落和斜面场景。

## 📄 摘要（原文）

> Video generators are increasingly evaluated as potential world models, which requires them to encode and understand physical laws. We investigate their representation of a fundamental law: gravity. Out-of-the-box video generators consistently generate objects falling at an effectively slower acceleration. However, these physical tests are often confounded by ambiguous metric scale. We first investigate if observed physical errors are artifacts of these ambiguities (e.g., incorrect frame rate assumptions). We find that even temporal rescaling cannot correct the high-variance gravity artifacts. To rigorously isolate the underlying physical representation from these confounds, we introduce a unit-free, two-object protocol that tests the timing ratio $t_1^2/t_2^2 = h_1/h_2$, a relationship independent of $g$, focal length, and scale. This relative test reveals violations of Galileo's equivalence principle. We then demonstrate that this physical gap can be partially mitigated with targeted specialization. A lightweight low-rank adaptor fine-tuned on only 100 single-ball clips raises $g_{\mathrm{eff}}$ from $1.81\,\mathrm{m/s^2}$ to $6.43\,\mathrm{m/s^2}$ (reaching $65\%$ of terrestrial gravity). This specialist adaptor also generalizes zero-shot to two-ball drops and inclined planes, offering initial evidence that specific physical laws can be corrected with minimal data.

