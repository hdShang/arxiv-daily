---
layout: default
title: ProtoEFNet: Dynamic Prototype Learning for Inherently Interpretable Ejection Fraction Estimation in Echocardiography
---

# ProtoEFNet: Dynamic Prototype Learning for Inherently Interpretable Ejection Fraction Estimation in Echocardiography

**arXiv**: [2512.03339v1](https://arxiv.org/abs/2512.03339) | [PDF](https://arxiv.org/pdf/2512.03339.pdf)

**作者**: Yeganeh Ghamary, Victoria Wu, Hooman Vaseli, Christina Luong, Teresa Tsang, Siavash Bigdeli, Purang Abolmaesumi

---

## 💡 一句话要点

**提出ProtoEFNet，通过动态原型学习实现超声心动图射血分数估计的可解释性回归。**

**关键词**: `射血分数估计` `原型学习` `可解释人工智能` `超声心动图` `视频分析` `回归模型`

## 📋 核心要点

1. 核心问题：传统射血分数估计依赖人工且现有深度学习模型缺乏透明度，影响临床信任。
2. 方法要点：采用视频原型学习，学习动态时空原型以捕获心脏运动模式，并引入原型角度分离损失增强表示区分度。
3. 实验或效果：在EchonetDynamic数据集上，模型精度与非可解释模型相当，并提供临床相关洞察，损失函数提升F1分数约2%。

## 📄 摘要（原文）

> Ejection fraction (EF) is a crucial metric for assessing cardiac function and diagnosing conditions such as heart failure. Traditionally, EF estimation requires manual tracing and domain expertise, making the process time-consuming and subject to interobserver variability. Most current deep learning methods for EF prediction are black-box models with limited transparency, which reduces clinical trust. Some post-hoc explainability methods have been proposed to interpret the decision-making process after the prediction is made. However, these explanations do not guide the model's internal reasoning and therefore offer limited reliability in clinical applications. To address this, we introduce ProtoEFNet, a novel video-based prototype learning model for continuous EF regression. The model learns dynamic spatiotemporal prototypes that capture clinically meaningful cardiac motion patterns. Additionally, the proposed Prototype Angular Separation (PAS) loss enforces discriminative representations across the continuous EF spectrum. Our experiments on the EchonetDynamic dataset show that ProtoEFNet can achieve accuracy on par with its non-interpretable counterpart while providing clinically relevant insight. The ablation study shows that the proposed loss boosts performance with a 2% increase in F1 score from 77.67$\pm$2.68 to 79.64$\pm$2.10. Our source code is available at: https://github.com/DeepRCL/ProtoEF

