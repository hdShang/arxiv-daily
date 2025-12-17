---
layout: default
title: Beyond Single Models: Mitigating Multimodal Hallucinations via Adaptive Token Ensemble Decoding
---

# Beyond Single Models: Mitigating Multimodal Hallucinations via Adaptive Token Ensemble Decoding

**arXiv**: [2510.18321v1](https://arxiv.org/abs/2510.18321) | [PDF](https://arxiv.org/pdf/2510.18321.pdf)

**作者**: Jinlin Li, Yuran Wang, Yifei Yuan, Xiao Zhou, Yingying Zhang, Xixian Yong, Yefeng Zheng, Xian Wu

---

## 💡 一句话要点

**提出自适应令牌集成解码以缓解多模态大模型中的物体幻觉问题**

**关键词**: `多模态大模型` `物体幻觉` `集成解码` `自适应权重` `推理优化` `语义一致性`

## 📋 核心要点

1. 核心问题：多模态大模型在图像描述等任务中易产生物体幻觉，生成不存在或误识别对象。
2. 方法要点：采用无需训练的令牌级集成框架，动态加权聚合多个模型预测以提升可靠性。
3. 实验或效果：在标准基准测试中显著减少幻觉，保持流畅性和相关性，优于现有方法。

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) have recently achieved impressive
> results in multimodal tasks such as image captioning and visual question
> answering. However, they remain prone to object hallucination -- generating
> descriptions of nonexistent or misidentified objects. Prior work has partially
> mitigated this via auxiliary training objectives or external modules, but
> challenges remain in terms of scalability, adaptability, and model
> independence. To address these limitations, we propose Adaptive Token Ensemble
> Decoding (ATED), a training-free, token-level ensemble framework that mitigates
> hallucination by aggregating predictions from multiple LVLMs during inference.
> ATED dynamically computes uncertainty-based weights for each model, reflecting
> their reliability at each decoding step. It also integrates diverse decoding
> paths to improve contextual grounding and semantic consistency. Experiments on
> standard hallucination detection benchmarks demonstrate that ATED significantly
> outperforms state-of-the-art methods, reducing hallucination without
> compromising fluency or relevance. Our findings highlight the benefits of
> adaptive ensembling and point to a promising direction for improving LVLM
> robustness in high-stakes applications. The code is available at
> https://github.com/jinlin2021/ATED.

