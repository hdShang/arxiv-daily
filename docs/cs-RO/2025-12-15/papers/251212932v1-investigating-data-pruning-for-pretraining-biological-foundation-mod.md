---
layout: default
title: Investigating Data Pruning for Pretraining Biological Foundation Models at Scale
---

# Investigating Data Pruning for Pretraining Biological Foundation Models at Scale

**arXiv**: [2512.12932v1](https://arxiv.org/abs/2512.12932) | [PDF](https://arxiv.org/pdf/2512.12932.pdf)

**作者**: Yifan Wu, Jiyue Jiang, Xichen Ye, Yiqi Wang, Chang Zhou, Yitao Xu, Jiayang Chen, He Hu, Weizhong Zhang, Cheng Jin, Jiao Yuan, Yu Li

---

## 💡 一句话要点

**提出影响引导的数据剪枝框架以降低生物基础模型预训练的计算成本**

**关键词**: `生物基础模型` `数据剪枝` `影响估计` `预训练优化` `计算效率`

## 📋 核心要点

1. 生物基础模型预训练依赖海量数据，计算成本高且可复现性差
2. 引入基于子集的自影响公式，高效估计样本重要性，设计Top-k和覆盖中心影响选择策略
3. 在RNA-FM和ESM-C上验证，极端剪枝率超99%时优于随机基线，核心集性能优于十倍大随机子集

## 📄 摘要（原文）

> Biological foundation models (BioFMs), pretrained on large-scale biological sequences, have recently shown strong potential in providing meaningful representations for diverse downstream bioinformatics tasks. However, such models often rely on millions to billions of training sequences and billions of parameters, resulting in prohibitive computational costs and significant barriers to reproducibility and accessibility, particularly for academic labs. To address these challenges, we investigate the feasibility of data pruning for BioFM pretraining and propose a post-hoc influence-guided data pruning framework tailored to biological domains. Our approach introduces a subset-based self-influence formulation that enables efficient estimation of sample importance at low computational cost, and builds upon it two simple yet effective selection strategies, namely Top-k Influence (Top I) and Coverage-Centric Influence (CCI). We empirically validate our method on two representative BioFMs, RNA-FM and ESM-C. For RNA, our framework consistently outperforms random selection baselines under an extreme pruning rate of over 99 percent, demonstrating its effectiveness. Furthermore, we show the generalizability of our framework on protein-related tasks using ESM-C. In particular, our coreset even outperforms random subsets that are ten times larger in both RNA and protein settings, revealing substantial redundancy in biological sequence datasets. These findings underscore the potential of influence-guided data pruning to substantially reduce the computational cost of BioFM pretraining, paving the way for more efficient, accessible, and sustainable biological AI research.

