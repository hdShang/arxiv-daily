---
layout: default
title: MatAnyone 2: Scaling Video Matting via a Learned Quality Evaluator
---

# MatAnyone 2: Scaling Video Matting via a Learned Quality Evaluator

**arXiv**: [2512.11782v1](https://arxiv.org/abs/2512.11782) | [PDF](https://arxiv.org/pdf/2512.11782.pdf)

**作者**: Peiqing Yang, Shangchen Zhou, Kai Hao, Qingyi Tao

---

## 💡 一句话要点

**提出学习型抠图质量评估器以扩展视频抠图，通过质量反馈和数据集构建提升性能。**

**关键词**: `视频抠图` `质量评估` `数据集构建` `参考帧训练` `语义稳定性` `边界监督`

## 📋 核心要点

1. 视频抠图受限于数据集规模和真实性，缺乏有效边界监督导致细节缺失。
2. 引入学习型抠图质量评估器，无需真值评估语义和边界质量，提供像素级评估图。
3. 构建大规模真实视频抠图数据集VMReal，结合参考帧训练策略，在基准测试中达到最优性能。

## 📄 摘要（原文）

> Video matting remains limited by the scale and realism of existing datasets. While leveraging segmentation data can enhance semantic stability, the lack of effective boundary supervision often leads to segmentation-like mattes lacking fine details. To this end, we introduce a learned Matting Quality Evaluator (MQE) that assesses semantic and boundary quality of alpha mattes without ground truth. It produces a pixel-wise evaluation map that identifies reliable and erroneous regions, enabling fine-grained quality assessment. The MQE scales up video matting in two ways: (1) as an online matting-quality feedback during training to suppress erroneous regions, providing comprehensive supervision, and (2) as an offline selection module for data curation, improving annotation quality by combining the strengths of leading video and image matting models. This process allows us to build a large-scale real-world video matting dataset, VMReal, containing 28K clips and 2.4M frames. To handle large appearance variations in long videos, we introduce a reference-frame training strategy that incorporates long-range frames beyond the local window for effective training. Our MatAnyone 2 achieves state-of-the-art performance on both synthetic and real-world benchmarks, surpassing prior methods across all metrics.

