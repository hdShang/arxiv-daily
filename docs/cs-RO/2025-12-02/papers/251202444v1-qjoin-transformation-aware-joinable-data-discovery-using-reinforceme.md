---
layout: default
title: QJoin: Transformation-aware Joinable Data Discovery Using Reinforcement Learning
---

# QJoin: Transformation-aware Joinable Data Discovery Using Reinforcement Learning

**arXiv**: [2512.02444v1](https://arxiv.org/abs/2512.02444) | [PDF](https://arxiv.org/pdf/2512.02444.pdf)

**作者**: Ning Wang, Sainyam Galhotra

---

## 💡 一句话要点

**提出QJoin强化学习框架，以解决异构数据中基于转换的可连接表发现问题。**

**关键词**: `数据集成` `连接发现` `强化学习` `转换学习` `数据重用` `异构数据`

## 📋 核心要点

1. 核心问题：传统连接发现方法仅支持等值连接，无法处理标识符格式不一致或系统转换的场景。
2. 方法要点：使用强化学习训练代理，在唯一性感知奖励下探索高价值转换链，并引入代理转移和转换重用机制加速新任务。
3. 实验或效果：在AutoJoin基准上平均F1-score达91.0%，在开放数据集中通过重用减少运行时间达7.4%。

## 📄 摘要（原文）

> Discovering which tables in large, heterogeneous repositories can be joined and by what transformations is a central challenge in data integration and data discovery. Traditional join discovery methods are largely designed for equi-joins, which assume that join keys match exactly or nearly so. These techniques, while efficient in clean, well-normalized databases, fail in open or federated settings where identifiers are inconsistently formatted, embedded, or split across multiple columns. Approximate or fuzzy joins alleviate minor string variations but cannot capture systematic transformations. We introduce QJoin, a reinforcement-learning framework that learns and reuses transformation strategies across join tasks. QJoin trains an agent under a uniqueness-aware reward that balances similarity with key distinctiveness, enabling it to explore concise, high-value transformation chains. To accelerate new joins, we introduce two reuse mechanisms: (i) agent transfer, which initializes new policies from pretrained agents, and (ii) transformation reuse, which caches successful operator sequences for similar column clusters. On the AutoJoin Web benchmark (31 table pairs), QJoin achieves an average F1-score of 91.0%. For 19,990 join tasks in NYC+Chicago open datasets, Qjoin reduces runtime by up to 7.4% (13,747 s) by using reusing. These results demonstrate that transformation learning and reuse can make join discovery both more accurate and more efficient.

