---
layout: default
title: Beyond Frequency: Scoring-Driven Debiasing for Object Detection via Blueprint-Prompted Image Synthesis
---

# Beyond Frequency: Scoring-Driven Debiasing for Object Detection via Blueprint-Prompted Image Synthesis

**arXiv**: [2510.18229v1](https://arxiv.org/abs/2510.18229) | [PDF](https://arxiv.org/pdf/2510.18229.pdf)

**作者**: Xinhao Cai, Liulei Li, Gensheng Pei, Tao Chen, Jinshan Pan, Yazhou Yao, Wenguan Wang

---

## 💡 一句话要点

**提出基于表示分数和蓝图提示的图像合成框架，以解决目标检测中的表示偏差问题。**

**关键词**: `目标检测` `去偏方法` `图像合成` `表示分数` `生成对齐` `视觉蓝图`

## 📋 核心要点

1. 核心问题：现有去偏方法受限于样本多样性，且生成式增强易保留偏差；实例频率不足以反映模型真实需求。
2. 方法要点：引入表示分数诊断表示差距，使用视觉蓝图和生成对齐策略提升合成图像质量与控制。
3. 实验或效果：显著改善罕见对象检测性能，如大/稀有实例mAP提升4.4/3.6，布局精度超越先前模型15.9 mAP。

## 📄 摘要（原文）

> This paper presents a generation-based debiasing framework for object
> detection. Prior debiasing methods are often limited by the representation
> diversity of samples, while naive generative augmentation often preserves the
> biases it aims to solve. Moreover, our analysis reveals that simply generating
> more data for rare classes is suboptimal due to two core issues: i) instance
> frequency is an incomplete proxy for the true data needs of a model, and ii)
> current layout-to-image synthesis lacks the fidelity and control to generate
> high-quality, complex scenes. To overcome this, we introduce the representation
> score (RS) to diagnose representational gaps beyond mere frequency, guiding the
> creation of new, unbiased layouts. To ensure high-quality synthesis, we replace
> ambiguous text prompts with a precise visual blueprint and employ a generative
> alignment strategy, which fosters communication between the detector and
> generator. Our method significantly narrows the performance gap for
> underrepresented object groups, \eg, improving large/rare instances by 4.4/3.6
> mAP over the baseline, and surpassing prior L2I synthesis models by 15.9 mAP
> for layout accuracy in generated images.

