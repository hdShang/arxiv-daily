---
layout: default
title: CoDS: Enhancing Collaborative Perception in Heterogeneous Scenarios via Domain Separation
---

# CoDS: Enhancing Collaborative Perception in Heterogeneous Scenarios via Domain Separation

**arXiv**: [2510.13432v1](https://arxiv.org/abs/2510.13432) | [PDF](https://arxiv.org/pdf/2510.13432.pdf)

**作者**: Yushan Han, Hui Zhang, Honglei Zhang, Chuntao Ding, Yuanzhouhan Cao, Yidong Li

---

## 💡 一句话要点

**提出CoDS方法，通过域分离解决异构场景中的协作感知特征差异问题**

**关键词**: `协作感知` `域分离` `特征对齐` `异构场景` `推理效率` `自动驾驶`

## 📋 核心要点

1. 核心问题：异构场景中特征对齐易受噪声影响，且现有方法推理效率低
2. 方法要点：使用轻量级空间通道调整器和域分离模块进行特征对齐
3. 实验或效果：在异构场景中有效缓解特征差异，平衡检测精度与推理效率

## 📄 摘要（原文）

> Collaborative perception has been proven to improve individual perception in
> autonomous driving through multi-agent interaction. Nevertheless, most methods
> often assume identical encoders for all agents, which does not hold true when
> these models are deployed in real-world applications. To realize collaborative
> perception in actual heterogeneous scenarios, existing methods usually align
> neighbor features to those of the ego vehicle, which is vulnerable to noise
> from domain gaps and thus fails to address feature discrepancies effectively.
> Moreover, they adopt transformer-based modules for domain adaptation, which
> causes the model inference inefficiency on mobile devices. To tackle these
> issues, we propose CoDS, a Collaborative perception method that leverages
> Domain Separation to address feature discrepancies in heterogeneous scenarios.
> The CoDS employs two feature alignment modules, i.e., Lightweight
> Spatial-Channel Resizer (LSCR) and Distribution Alignment via Domain Separation
> (DADS). Besides, it utilizes the Domain Alignment Mutual Information (DAMI)
> loss to ensure effective feature alignment. Specifically, the LSCR aligns the
> neighbor feature across spatial and channel dimensions using a lightweight
> convolutional layer. Subsequently, the DADS mitigates feature distribution
> discrepancy with encoder-specific and encoder-agnostic domain separation
> modules. The former removes domain-dependent information and the latter
> captures task-related information. During training, the DAMI loss maximizes the
> mutual information between aligned heterogeneous features to enhance the domain
> separation process. The CoDS employs a fully convolutional architecture, which
> ensures high inference efficiency. Extensive experiments demonstrate that the
> CoDS effectively mitigates feature discrepancies in heterogeneous scenarios and
> achieves a trade-off between detection accuracy and inference efficiency.

