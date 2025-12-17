---
layout: default
title: RodEpil: A Video Dataset of Laboratory Rodents for Seizure Detection and Benchmark Evaluation
---

# RodEpil: A Video Dataset of Laboratory Rodents for Seizure Detection and Benchmark Evaluation

**arXiv**: [2511.10431v1](https://arxiv.org/abs/2511.10431) | [PDF](https://arxiv.org/pdf/2511.10431.pdf)

**作者**: Daniele Perlo, Vladimir Despotovic, Selma Boudissa, Sang-Yoon Kim, Petr Nazarov, Yanrong Zhang, Max Wintermark, Olivier Keunen

---

## 💡 一句话要点

**提出RodEpil视频数据集以支持实验室啮齿动物癫痫发作自动检测**

**关键词**: `视频数据集` `癫痫发作检测` `实验室啮齿动物` `TimeSformer` `非侵入监测`

## 📋 核心要点

1. 核心问题：自动检测实验室啮齿动物的癫痫发作事件，用于临床前癫痫研究。
2. 方法要点：使用基于Transformer的视频分类器TimeSformer，处理顶部和侧视视频片段。
3. 实验或效果：五折交叉验证显示平均F1分数达97%，数据集和代码已公开。

## 📄 摘要（原文）

> We introduce a curated video dataset of laboratory rodents for automatic detection of convulsive events. The dataset contains short (10~s) top-down and side-view video clips of individual rodents, labeled at clip level as normal activity or seizure. It includes 10,101 negative samples and 2,952 positive samples collected from 19 subjects. We describe the data curation, annotation protocol and preprocessing pipeline, and report baseline experiments using a transformer-based video classifier (TimeSformer). Experiments employ five-fold cross-validation with strict subject-wise partitioning to prevent data leakage (no subject appears in more than one fold). Results show that the TimeSformer architecture enables discrimination between seizure and normal activity with an average F1-score of 97%. The dataset and baseline code are publicly released to support reproducible research on non-invasive, video-based monitoring in preclinical epilepsy research. RodEpil Dataset access - DOI: 10.5281/zenodo.17601357

