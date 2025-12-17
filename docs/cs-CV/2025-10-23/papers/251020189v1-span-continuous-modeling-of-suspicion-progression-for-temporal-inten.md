---
layout: default
title: SPAN: Continuous Modeling of Suspicion Progression for Temporal Intention Localization
---

# SPAN: Continuous Modeling of Suspicion Progression for Temporal Intention Localization

**arXiv**: [2510.20189v1](https://arxiv.org/abs/2510.20189) | [PDF](https://arxiv.org/pdf/2510.20189.pdf)

**作者**: Xinyi Hu, Yuran Wang, Yue Li, Wenxuan Liu, Zheng Wang

---

## 💡 一句话要点

**提出SPAN网络以连续建模可疑意图，提升视频监控的早期检测能力**

**关键词**: `时序意图定位` `连续回归建模` `可疑行为分析` `视频监控` `时序点过程`

## 📋 核心要点

1. 现有离散分类方法无法捕捉可疑意图的连续变化，限制早期干预和可解释性
2. SPAN采用连续回归方法，结合时序点过程理论建模长期依赖和累积效应
3. 在HAI数据集上，SPAN显著降低MSE 19.8%，提升mAP 1.78%，尤其在低频案例中表现优异

## 📄 摘要（原文）

> Temporal Intention Localization (TIL) is crucial for video surveillance,
> focusing on identifying varying levels of suspicious intentions to improve
> security monitoring. However, existing discrete classification methods fail to
> capture the continuous nature of suspicious intentions, limiting early
> intervention and explainability. In this paper, we propose the Suspicion
> Progression Analysis Network (SPAN), which shifts from discrete classification
> to continuous regression, enabling the capture of fluctuating and evolving
> suspicious intentions. We reveal that suspicion exhibits long-term dependencies
> and cumulative effects, similar to Temporal Point Process (TPP) theory. Based
> on these insights, we define a suspicion score formula that models continuous
> changes while accounting for temporal characteristics. We also introduce
> Suspicion Coefficient Modulation, which adjusts suspicion coefficients using
> multimodal information to reflect the varying impacts of suspicious actions.
> Additionally, the Concept-Anchored Mapping method is proposed to link
> suspicious actions to predefined intention concepts, offering insights into
> both the actions and their potential underlying intentions. Extensive
> experiments on the HAI dataset show that SPAN significantly outperforms
> existing methods, reducing MSE by 19.8% and improving average mAP by 1.78%.
> Notably, SPAN achieves a 2.74% mAP gain in low-frequency cases, demonstrating
> its superior ability to capture subtle behavioral changes. Compared to discrete
> classification systems, our continuous suspicion modeling approach enables
> earlier detection and proactive intervention, greatly enhancing system
> explainability and practical utility in security applications.

