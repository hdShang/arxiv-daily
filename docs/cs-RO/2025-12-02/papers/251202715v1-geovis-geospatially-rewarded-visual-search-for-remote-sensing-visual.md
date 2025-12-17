---
layout: default
title: GeoViS: Geospatially Rewarded Visual Search for Remote Sensing Visual Grounding
---

# GeoViS: Geospatially Rewarded Visual Search for Remote Sensing Visual Grounding

**arXiv**: [2512.02715v1](https://arxiv.org/abs/2512.02715) | [PDF](https://arxiv.org/pdf/2512.02715.pdf)

**作者**: Peirong Zhang, Yidan Zhang, Luxiao Xu, Jinliang Lin, Zonghao Guo, Fengxiang Wang, Xue Yang, Kaiwen Wei, Lei Wang

---

## 💡 一句话要点

**提出GeoViS框架，通过渐进式搜索解决遥感图像中微小目标的视觉定位问题。**

**关键词**: `遥感视觉定位` `渐进式搜索` `多模态大语言模型` `地理空间推理` `奖励引导探索`

## 📋 核心要点

1. 核心问题：遥感图像中目标极小且查询涉及复杂地理空间关系，导致视觉定位困难。
2. 方法要点：采用树状结构渐进搜索，结合多模态感知和奖励引导探索，迭代优化地理空间假设。
3. 实验或效果：在五个基准测试中超越现有方法，展现精确地理空间理解和强泛化能力。

## 📄 摘要（原文）

> Recent advances in multimodal large language models(MLLMs) have led to remarkable progress in visual grounding, enabling fine-grained cross-modal alignment between textual queries and image regions. However, transferring such capabilities to remote sensing imagery remains challenging, as targets are often extremely small within kilometer-scale scenes, and queries typically involve intricate geospatial relations such as relative positions, spatial hierarchies, or contextual dependencies across distant objects. To address these challenges, we propose GeoViS, a Geospatially Rewarded Visual Search framework that reformulates remote sensing visual grounding as a progressive search-and-reasoning process. Rather than directly predicting the target location in a single step, GeoViS actively explores the global image through a tree-structured sequence of visual cues, integrating multimodal perception, spatial reasoning, and reward-guided exploration to refine geospatial hypotheses iteratively. This design enables the model to detect subtle small-scale targets while maintaining holistic scene awareness. Extensive experiments on five remote sensing grounding benchmarks demonstrate that GeoViS achieves precise geospatial understanding and consistently surpasses existing methods across key visual grounding metrics, highlighting its strong cross-domain generalization and interpretability.

