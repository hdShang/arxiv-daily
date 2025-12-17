---
layout: default
title: Generative Early Stage Ranking
---

# Generative Early Stage Ranking

**arXiv**: [2511.21095v1](https://arxiv.org/abs/2511.21095) | [PDF](https://arxiv.org/pdf/2511.21095.pdf)

**作者**: Juhee Hong, Meng Liu, Shengzhi Wang, Xiaoheng Mao, Huihui Cheng, Leon Gao, Christopher Leung, Jin Zhou, Chandra Mouli Sekar, Zhao Zhu, Ruochen Liu, Tuan Trieu, Dawei Sun, Jeet Kanjani, Rui Li, Jing Qian, Xuan Cao, Minjie Fan, Mingze Gao

---

## 💡 一句话要点

**提出生成式早期排序范式以解决用户-物品解耦方法在效果上的限制**

**关键词**: `推荐系统` `早期排序` `注意力机制` `用户-物品交互` `多阶段排序` `效率优化`

## 📋 核心要点

1. 早期排序系统采用用户-物品解耦方法，难以捕捉细粒度亲和性与跨信号交互
2. 引入混合注意力模块，包括硬匹配、目标感知自注意力和交叉注意力，增强用户-物品交互
3. 通过离线与在线实验验证，在关键指标、参与度和消费任务上取得显著提升

## 📄 摘要（原文）

> Large-scale recommendations commonly adopt a multi-stage cascading ranking system paradigm to balance effectiveness and efficiency. Early Stage Ranking (ESR) systems utilize the "user-item decoupling" approach, where independently learned user and item representations are only combined at the final layer. While efficient, this design is limited in effectiveness, as it struggles to capture fine-grained user-item affinities and cross-signals. To address these, we propose the Generative Early Stage Ranking (GESR) paradigm, introducing the Mixture of Attention (MoA) module which leverages diverse attention mechanisms to bridge the effectiveness gap: the Hard Matching Attention (HMA) module encodes explicit cross-signals by computing raw match counts between user and item features; the Target-Aware Self Attention module generates target-aware user representations conditioned on the item, enabling more personalized learning; and the Cross Attention modules facilitate early and more enriched interactions between user-item features. MoA's specialized attention encodings are further refined in the final layer through a Multi-Logit Parameterized Gating (MLPG) module, which integrates the newly learned embeddings via gating and produces secondary logits that are fused with the primary logit. To address the efficiency and latency challenges, we have introduced a comprehensive suite of optimization techniques. These span from custom kernels that maximize the capabilities of the latest hardware to efficient serving solutions powered by caching mechanisms. The proposed GESR paradigm has shown substantial improvements in topline metrics, engagement, and consumption tasks, as validated by both offline and online experiments. To the best of our knowledge, this marks the first successful deployment of full target-aware attention sequence modeling within an ESR stage at such a scale.

