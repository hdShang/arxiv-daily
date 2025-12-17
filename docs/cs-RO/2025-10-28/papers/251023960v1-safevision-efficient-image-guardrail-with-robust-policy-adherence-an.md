---
layout: default
title: SafeVision: Efficient Image Guardrail with Robust Policy Adherence and Explainability
---

# SafeVision: Efficient Image Guardrail with Robust Policy Adherence and Explainability

**arXiv**: [2510.23960v1](https://arxiv.org/abs/2510.23960) | [PDF](https://arxiv.org/pdf/2510.23960.pdf)

**作者**: Peiyang Xu, Minzhou Pan, Zhaorun Chen, Shuang Yang, Chaowei Xiao, Bo Li

---

## 💡 一句话要点

**提出SafeVision图像护栏，通过类人推理解决不安全内容检测的适应性与透明度问题。**

**关键词**: `图像护栏` `语义推理` `动态适应` `策略遵循` `解释性AI` `数据集构建`

## 📋 核心要点

1. 传统图像护栏模型依赖预定义类别，缺乏语义推理，易误分类且难适应新威胁。
2. SafeVision集成数据生成、策略遵循训练和定制损失函数，实现动态策略对齐与解释性。
3. 在VisionHarm数据集上，SafeVision性能优于GPT-4o，速度快16倍以上，验证其高效性。

## 📄 摘要（原文）

> With the rapid proliferation of digital media, the need for efficient and
> transparent safeguards against unsafe content is more critical than ever.
> Traditional image guardrail models, constrained by predefined categories, often
> misclassify content due to their pure feature-based learning without semantic
> reasoning. Moreover, these models struggle to adapt to emerging threats,
> requiring costly retraining for new threats. To address these limitations, we
> introduce SafeVision, a novel image guardrail that integrates human-like
> reasoning to enhance adaptability and transparency. Our approach incorporates
> an effective data collection and generation framework, a policy-following
> training pipeline, and a customized loss function. We also propose a diverse QA
> generation and training strategy to enhance learning effectiveness. SafeVision
> dynamically aligns with evolving safety policies at inference time, eliminating
> the need for retraining while ensuring precise risk assessments and
> explanations. Recognizing the limitations of existing unsafe image benchmarks,
> which either lack granularity or cover limited risks, we introduce VisionHarm,
> a high-quality dataset comprising two subsets: VisionHarm Third-party
> (VisionHarm-T) and VisionHarm Comprehensive(VisionHarm-C), spanning diverse
> harmful categories. Through extensive experiments, we show that SafeVision
> achieves state-of-the-art performance on different benchmarks. SafeVision
> outperforms GPT-4o by 8.6% on VisionHarm-T and by 15.5% on VisionHarm-C, while
> being over 16x faster. SafeVision sets a comprehensive, policy-following, and
> explainable image guardrail with dynamic adaptation to emerging threats.

