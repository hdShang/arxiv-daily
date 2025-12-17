---
layout: default
title: A Comparative Study on How Data Normalization Affects Zero-Shot Generalization in Time Series Foundation Models
---

# A Comparative Study on How Data Normalization Affects Zero-Shot Generalization in Time Series Foundation Models

**arXiv**: [2512.02833v1](https://arxiv.org/abs/2512.02833) | [PDF](https://arxiv.org/pdf/2512.02833.pdf)

**作者**: Ihab Ahmed, Denis Krompaß, Cheng Feng, Volker Tresp

---

## 💡 一句话要点

**比较数据归一化方法对时间序列基础模型零样本泛化的影响，确立REVIN为最优方法**

**关键词**: `时间序列基础模型` `数据归一化` `零样本泛化` `REVIN方法` `跨域尺度变化` `非平稳性`

## 📋 核心要点

1. 研究时间序列基础模型输入归一化方法，解决跨域尺度变化和非平稳性导致的泛化问题
2. 通过系统评估四种架构模型，实证REVIN在零样本MASE上相对未归一化基线降低89%，效率最高
3. 归一化效果受架构设计和优化目标影响，如训练损失尺度敏感性和模型类型

## 📄 摘要（原文）

> We investigate input normalization methods for Time-Series Foundation Models (TSFMs). While normalization is well-studied in dataset-specific time-series models, it remains overlooked in TSFMs where generalization is critical. Time-series data, unlike text or images, exhibits significant scale variation across domains and channels, coupled with non-stationarity, can undermine TSFM performance regardless of architectural complexity. Through systematic evaluation across four architecturally diverse TSFMs, we empirically establish REVIN as the most efficient approach, reducing zero-shot MASE by 89\% relative to an un-normalized baseline and by 44\% versus other normalization methods, while matching the best in-domain accuracy (0.84 MASE) without any dataset-level preprocessing -- yielding the highest accuracy-efficiency trade-off. Yet its effect utilization depends on architectural design choices and optimization objective, particularly with respect to training loss scale sensitivity and model type (probabilistic, point-forecast, or LLM-based models).

