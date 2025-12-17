---
layout: default
title: EReLiFM: Evidential Reliability-Aware Residual Flow Meta-Learning for Open-Set Domain Generalization under Noisy Labels
---

# EReLiFM: Evidential Reliability-Aware Residual Flow Meta-Learning for Open-Set Domain Generalization under Noisy Labels

**arXiv**: [2510.12687v1](https://arxiv.org/abs/2510.12687) | [PDF](https://arxiv.org/pdf/2510.12687.pdf)

**作者**: Kunyu Peng, Di Wen, Kailun Yang, Jia Fu, Yufan Chen, Ruiping Liu, Jiamin Wu, Junwei Zheng, M. Saquib Sarfraz, Luc Van Gool, Danda Pani Paudel, Rainer Stiefelhagen

---

## 💡 一句话要点

**提出EReLiFM方法以解决带噪声标签的开放集域泛化问题**

**关键词**: `开放集域泛化` `噪声标签处理` `元学习` `证据学习` `残差流匹配`

## 📋 核心要点

1. 开放集域泛化在噪声标签下难以识别已知类和拒绝未知类
2. 使用证据损失聚类和残差流匹配机制增强域间迁移能力
3. 实验显示在OSDG-NL任务中性能优于现有方法

## 📄 摘要（原文）

> Open-Set Domain Generalization (OSDG) aims to enable deep learning models to
> recognize unseen categories in new domains, which is crucial for real-world
> applications. Label noise hinders open-set domain generalization by corrupting
> source-domain knowledge, making it harder to recognize known classes and reject
> unseen ones. While existing methods address OSDG under Noisy Labels (OSDG-NL)
> using hyperbolic prototype-guided meta-learning, they struggle to bridge domain
> gaps, especially with limited clean labeled data. In this paper, we propose
> Evidential Reliability-Aware Residual Flow Meta-Learning (EReLiFM). We first
> introduce an unsupervised two-stage evidential loss clustering method to
> promote label reliability awareness. Then, we propose a residual flow matching
> mechanism that models structured domain- and category-conditioned residuals,
> enabling diverse and uncertainty-aware transfer paths beyond
> interpolation-based augmentation. During this meta-learning process, the model
> is optimized such that the update direction on the clean set maximizes the loss
> decrease on the noisy set, using pseudo labels derived from the most confident
> predicted class for supervision. Experimental results show that EReLiFM
> outperforms existing methods on OSDG-NL, achieving state-of-the-art
> performance. The source code is available at
> https://github.com/KPeng9510/ERELIFM.

