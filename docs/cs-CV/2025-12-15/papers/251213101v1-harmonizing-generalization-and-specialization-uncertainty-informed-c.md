---
layout: default
title: Harmonizing Generalization and Specialization: Uncertainty-Informed Collaborative Learning for Semi-supervised Medical Image Segmentation
---

# Harmonizing Generalization and Specialization: Uncertainty-Informed Collaborative Learning for Semi-supervised Medical Image Segmentation

**arXiv**: [2512.13101v1](https://arxiv.org/abs/2512.13101) | [PDF](https://arxiv.org/pdf/2512.13101.pdf)

**作者**: Wenjing Lu, Yi Hong, Yang Yang

---

## 💡 一句话要点

**提出不确定性协同学习框架以解决半监督医学图像分割中泛化与特化不平衡问题**

**关键词**: `半监督学习` `医学图像分割` `不确定性估计` `知识蒸馏` `双教师框架` `伪标签学习`

## 📋 核心要点

1. 核心问题：视觉基础模型在有限标注或罕见病理变化下泛化不足，因通用先验与任务需求不匹配
2. 方法要点：采用双教师框架，结合冻结基础模型和自适应教师，通过不确定性调节伪标签学习
3. 实验或效果：在多种2D和3D分割基准上优于现有方法，显著减少标注需求接近全监督性能

## 📄 摘要（原文）

> Vision foundation models have demonstrated strong generalization in medical image segmentation by leveraging large-scale, heterogeneous pretraining. However, they often struggle to generalize to specialized clinical tasks under limited annotations or rare pathological variations, due to a mismatch between general priors and task-specific requirements. To address this, we propose Uncertainty-informed Collaborative Learning (UnCoL), a dual-teacher framework that harmonizes generalization and specialization in semi-supervised medical image segmentation. Specifically, UnCoL distills both visual and semantic representations from a frozen foundation model to transfer general knowledge, while concurrently maintaining a progressively adapting teacher to capture fine-grained and task-specific representations. To balance guidance from both teachers, pseudo-label learning in UnCoL is adaptively regulated by predictive uncertainty, which selectively suppresses unreliable supervision and stabilizes learning in ambiguous regions. Experiments on diverse 2D and 3D segmentation benchmarks show that UnCoL consistently outperforms state-of-the-art semi-supervised methods and foundation model baselines. Moreover, our model delivers near fully supervised performance with markedly reduced annotation requirements.

