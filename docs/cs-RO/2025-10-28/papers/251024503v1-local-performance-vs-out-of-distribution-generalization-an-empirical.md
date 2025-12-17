---
layout: default
title: Local Performance vs. Out-of-Distribution Generalization: An Empirical Analysis of Personalized Federated Learning in Heterogeneous Data Environments
---

# Local Performance vs. Out-of-Distribution Generalization: An Empirical Analysis of Personalized Federated Learning in Heterogeneous Data Environments

**arXiv**: [2510.24503v1](https://arxiv.org/abs/2510.24503) | [PDF](https://arxiv.org/pdf/2510.24503.pdf)

**作者**: Mortesa Hussaini, Jan Theiß, Anthony Stein

---

## 💡 一句话要点

**提出FLIU方法以解决联邦学习中个性化与泛化性能的权衡问题**

**关键词**: `个性化联邦学习` `客户端漂移` `泛化性能` `异构数据` `FedAvg扩展` `自适应个性化`

## 📋 核心要点

1. 核心问题：异构数据下本地模型偏离全局最优，导致客户端漂移和泛化能力不足
2. 方法要点：扩展FedAvg，引入自适应个性化因子实现个体化更新
3. 实验或效果：在MNIST和CIFAR-10上评估，涵盖IID、非IID和Dirichlet分布

## 📄 摘要（原文）

> In the context of Federated Learning with heterogeneous data environments,
> local models tend to converge to their own local model optima during local
> training steps, deviating from the overall data distributions. Aggregation of
> these local updates, e.g., with FedAvg, often does not align with the global
> model optimum (client drift), resulting in an update that is suboptimal for
> most clients. Personalized Federated Learning approaches address this challenge
> by exclusively focusing on the average local performances of clients' models on
> their own data distribution. Generalization to out-of-distribution samples,
> which is a substantial benefit of FedAvg and represents a significant component
> of robustness, appears to be inadequately incorporated into the assessment and
> evaluation processes. This study involves a thorough evaluation of Federated
> Learning approaches, encompassing both their local performance and their
> generalization capabilities. Therefore, we examine different stages within a
> single communication round to enable a more nuanced understanding of the
> considered metrics. Furthermore, we propose and incorporate a modified approach
> of FedAvg, designated as Federated Learning with Individualized Updates (FLIU),
> extending the algorithm by a straightforward individualization step with an
> adaptive personalization factor. We evaluate and compare the approaches
> empirically using MNIST and CIFAR-10 under various distributional conditions,
> including benchmark IID and pathological non-IID, as well as additional novel
> test environments with Dirichlet distribution specifically developed to stress
> the algorithms on complex data heterogeneity.

