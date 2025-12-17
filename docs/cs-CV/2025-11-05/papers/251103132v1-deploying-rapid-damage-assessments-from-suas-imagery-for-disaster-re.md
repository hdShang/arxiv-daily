---
layout: default
title: Deploying Rapid Damage Assessments from sUAS Imagery for Disaster Response
---

# Deploying Rapid Damage Assessments from sUAS Imagery for Disaster Response

**arXiv**: [2511.03132v1](https://arxiv.org/abs/2511.03132) | [PDF](https://arxiv.org/pdf/2511.03132.pdf)

**作者**: Thomas Manzini, Priyankari Perali, Robin R. Murphy

---

## 💡 一句话要点

**提出首个AI/ML系统，用于无人机图像自动评估建筑损伤，部署于飓风灾害响应。**

**关键词**: `无人机图像分析` `建筑损伤评估` `灾害响应系统` `机器学习部署` `计算机视觉应用`

## 📋 核心要点

1. 核心问题：无人机图像数据量过大，传输与人工评估延迟灾害响应。
2. 方法要点：基于最大无人机图像数据集训练模型，实现建筑损伤自动评估。
3. 实验或效果：部署于飓风响应，18分钟内评估415座建筑，提升效率。

## 📄 摘要（原文）

> This paper presents the first AI/ML system for automating building damage
> assessment in uncrewed aerial systems (sUAS) imagery to be deployed
> operationally during federally declared disasters (Hurricanes Debby and
> Helene). In response to major disasters, sUAS teams are dispatched to collect
> imagery of the affected areas to assess damage; however, at recent disasters,
> teams collectively delivered between 47GB and 369GB of imagery per day,
> representing more imagery than can reasonably be transmitted or interpreted by
> subject matter experts in the disaster scene, thus delaying response efforts.
> To alleviate this data avalanche encountered in practice, computer vision and
> machine learning techniques are necessary. While prior work has been deployed
> to automatically assess damage in satellite imagery, there is no current state
> of practice for sUAS-based damage assessment systems, as all known work has
> been confined to academic settings. This work establishes the state of practice
> via the development and deployment of models for building damage assessment
> with sUAS imagery. The model development involved training on the largest known
> dataset of post-disaster sUAS aerial imagery, containing 21,716 building damage
> labels, and the operational training of 91 disaster practitioners. The best
> performing model was deployed during the responses to Hurricanes Debby and
> Helene, where it assessed a combined 415 buildings in approximately 18 minutes.
> This work contributes documentation of the actual use of AI/ML for damage
> assessment during a disaster and lessons learned to the benefit of the AI/ML
> research and user communities.

