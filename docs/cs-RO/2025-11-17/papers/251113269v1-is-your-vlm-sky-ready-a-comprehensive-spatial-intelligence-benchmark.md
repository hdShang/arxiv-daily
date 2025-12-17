---
layout: default
title: Is your VLM Sky-Ready? A Comprehensive Spatial Intelligence Benchmark for UAV Navigation
---

# Is your VLM Sky-Ready? A Comprehensive Spatial Intelligence Benchmark for UAV Navigation

**arXiv**: [2511.13269v1](https://arxiv.org/abs/2511.13269) | [PDF](https://arxiv.org/pdf/2511.13269.pdf)

**作者**: Lingfeng Zhang, Yuchen Zhang, Hongsheng Li, Haoxiang Fu, Yingbo Tang, Hangjun Ye, Long Chen, Xiaojun Liang, Xiaoshuai Hao, Wenbo Ding

---

## 💡 一句话要点

**提出SpatialSky-Bench和Sky-VLM以提升无人机导航中视觉语言模型的空间智能**

**关键词**: `无人机导航` `空间智能基准` `视觉语言模型` `场景理解` `环境感知` `数据集构建`

## 📋 核心要点

1. 现有视觉语言模型在无人机导航中的空间智能能力未被充分探索，存在性能不足问题。
2. 开发SpatialSky-Bench基准和SpatialSky-Dataset数据集，用于评估和训练空间智能。
3. Sky-VLM在基准任务中实现最优性能，显著提升无人机场景的空间推理能力。

## 📄 摘要（原文）

> Vision-Language Models (VLMs), leveraging their powerful visual perception and reasoning capabilities, have been widely applied in Unmanned Aerial Vehicle (UAV) tasks. However, the spatial intelligence capabilities of existing VLMs in UAV scenarios remain largely unexplored, raising concerns about their effectiveness in navigating and interpreting dynamic environments. To bridge this gap, we introduce SpatialSky-Bench, a comprehensive benchmark specifically designed to evaluate the spatial intelligence capabilities of VLMs in UAV navigation. Our benchmark comprises two categories-Environmental Perception and Scene Understanding-divided into 13 subcategories, including bounding boxes, color, distance, height, and landing safety analysis, among others. Extensive evaluations of various mainstream open-source and closed-source VLMs reveal unsatisfactory performance in complex UAV navigation scenarios, highlighting significant gaps in their spatial capabilities. To address this challenge, we developed the SpatialSky-Dataset, a comprehensive dataset containing 1M samples with diverse annotations across various scenarios. Leveraging this dataset, we introduce Sky-VLM, a specialized VLM designed for UAV spatial reasoning across multiple granularities and contexts. Extensive experimental results demonstrate that Sky-VLM achieves state-of-the-art performance across all benchmark tasks, paving the way for the development of VLMs suitable for UAV scenarios. The source code is available at https://github.com/linglingxiansen/SpatialSKy.

