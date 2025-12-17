---
layout: default
title: FedHUG: Federated Heterogeneous Unsupervised Generalization for Remote Physiological Measurements
---

# FedHUG: Federated Heterogeneous Unsupervised Generalization for Remote Physiological Measurements

**arXiv**: [2510.12132v1](https://arxiv.org/abs/2510.12132) | [PDF](https://arxiv.org/pdf/2510.12132.pdf)

**作者**: Xiao Yang, Jiyao Wang

---

## 💡 一句话要点

**提出FedHUG框架以解决联邦学习中无监督远程生理测量的异构泛化问题**

**关键词**: `联邦学习` `无监督学习` `远程生理测量` `异构数据` `域泛化` `长尾问题`

## 📋 核心要点

1. 核心问题：远程生理测量依赖隐私数据，现有方法需标注数据，难以在无标签用户数据上更新模型
2. 方法要点：引入最小偏差聚合和全局分布感知学习控制器，处理异构特征和标签分布偏斜
3. 实验或效果：在RGB视频和毫米波雷达估计中优于现有技术，代码将开源

## 📄 摘要（原文）

> Remote physiological measurement gained wide attention, while it requires
> collecting users' privacy-sensitive information, and existing contactless
> measurements still rely on labeled client data. This presents challenges when
> we want to further update real-world deployed models with numerous user data
> lacking labels. To resolve these challenges, we instantiate a new protocol
> called Federated Unsupervised Domain Generalization (FUDG) in this work.
> Subsequently, the \textbf{Fed}erated \textbf{H}eterogeneous
> \textbf{U}nsupervised \textbf{G}eneralization (\textbf{FedHUG}) framework is
> proposed and consists of: (1) Minimal Bias Aggregation module dynamically
> adjusts aggregation weights based on prior-driven bias evaluation to cope with
> heterogeneous non-IID features from multiple domains. (2) The Global
> Distribution-aware Learning Controller parameterizes the label distribution and
> dynamically manipulates client-specific training strategies, thereby mitigating
> the server-client label distribution skew and long-tail issue. The proposal
> shows superior performance across state-of-the-art techniques in estimation
> with either RGB video or mmWave radar. The code will be released.

