---
layout: default
title: Forgetting by Pruning: Data Deletion in Join Cardinality Estimation
---

# Forgetting by Pruning: Data Deletion in Join Cardinality Estimation

**arXiv**: [2511.20293v1](https://arxiv.org/abs/2511.20293) | [PDF](https://arxiv.org/pdf/2511.20293.pdf)

**作者**: Chaowei He, Yuanjun Liu, Qingzhi Ma, Shenyuan Ren, Xizhao Luo, Lei Zhao, An Liu

---

## 💡 一句话要点

**提出CEP框架以解决多表学习基数估计中的数据删除挑战**

**关键词**: `基数估计` `机器去学习` `数据删除` `多表查询` `剪枝优化` `数据库系统`

## 📋 核心要点

1. 核心问题：多表关系数据中数据删除导致属性敏感、表间传播和域消失，引发严重高估
2. 方法要点：引入分布敏感剪枝和域剪枝，构建半连接删除结果并指导参数剪枝
3. 实验或效果：在IMDB和TPC-H数据集上CEP实现最低Q误差，计算开销仅0.3%-2.5%

## 📄 摘要（原文）

> Machine unlearning in learned cardinality estimation (CE) systems presents unique challenges due to the complex distributional dependencies in multi-table relational data. Specifically, data deletion, a core component of machine unlearning, faces three critical challenges in learned CE models: attribute-level sensitivity, inter-table propagation and domain disappearance leading to severe overestimation in multi-way joins. We propose Cardinality Estimation Pruning (CEP), the first unlearning framework specifically designed for multi-table learned CE systems. CEP introduces Distribution Sensitivity Pruning, which constructs semi-join deletion results and computes sensitivity scores to guide parameter pruning, and Domain Pruning, which removes support for value domains entirely eliminated by deletion. We evaluate CEP on state-of-the-art architectures NeuroCard and FACE across IMDB and TPC-H datasets. Results demonstrate CEP consistently achieves the lowest Q-error in multi-table scenarios, particularly under high deletion ratios, often outperforming full retraining. Furthermore, CEP significantly reduces convergence iterations, incurring negligible computational overhead of 0.3%-2.5% of fine-tuning time.

