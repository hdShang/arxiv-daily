---
layout: default
title: RxnCaption: Reformulating Reaction Diagram Parsing as Visual Prompt Guided Captioning
---

# RxnCaption: Reformulating Reaction Diagram Parsing as Visual Prompt Guided Captioning

**arXiv**: [2511.02384v1](https://arxiv.org/abs/2511.02384) | [PDF](https://arxiv.org/pdf/2511.02384.pdf)

**作者**: Jiahe Song, Chuang Wang, Bowen Jiang, Yinfan Wang, Hao Zheng, Xingjian Wei, Chengjin Liu, Junyuan Gao, Yubin Wang, Lijun Wu, Jiang Wu, Qian Yu, Conghui He

---

## 💡 一句话要点

**提出RxnCaption框架，将化学反应图解析转化为视觉提示引导的图说生成问题**

**关键词**: `化学反应图解析` `视觉语言模型` `视觉提示` `分子检测` `数据集构建` `信息提取`

## 📋 核心要点

1. 化学文献中的反应图以图像形式存在，难以被机器读取用于AI训练
2. 使用BIVP策略，通过MolYOLO检测分子并添加视觉提示，简化解析为自然语言描述
3. 构建RxnCaption-11k数据集，实验显示在多个指标上达到最优性能

## 📄 摘要（原文）

> Large-scale chemical reaction datasets are crucial for AI research in
> chemistry. However, existing chemical reaction data often exist as images
> within papers, making them not machine-readable and unusable for training
> machine learning models. In response to this challenge, we propose the
> RxnCaption framework for the task of chemical Reaction Diagram Parsing (RxnDP).
> Our framework reformulates the traditional coordinate prediction driven parsing
> process into an image captioning problem, which Large Vision-Language Models
> (LVLMs) handle naturally. We introduce a strategy termed "BBox and Index as
> Visual Prompt" (BIVP), which uses our state-of-the-art molecular detector,
> MolYOLO, to pre-draw molecular bounding boxes and indices directly onto the
> input image. This turns the downstream parsing into a natural-language
> description problem. Extensive experiments show that the BIVP strategy
> significantly improves structural extraction quality while simplifying model
> design. We further construct the RxnCaption-11k dataset, an order of magnitude
> larger than prior real-world literature benchmarks, with a balanced test subset
> across four layout archetypes. Experiments demonstrate that RxnCaption-VL
> achieves state-of-the-art performance on multiple metrics. We believe our
> method, dataset, and models will advance structured information extraction from
> chemical literature and catalyze broader AI applications in chemistry. We will
> release data, models, and code on GitHub.

