---
layout: default
title: GOPLA: Generalizable Object Placement Learning via Synthetic Augmentation of Human Arrangement
---

# GOPLA: Generalizable Object Placement Learning via Synthetic Augmentation of Human Arrangement

**arXiv**: [2510.14627v1](https://arxiv.org/abs/2510.14627) | [PDF](https://arxiv.org/pdf/2510.14627.pdf)

**作者**: Yao Zhong, Hanzhi Chen, Simon Schaefer, Anran Zhang, Stefan Leutenegger

---

## 💡 一句话要点

**提出GOPLA框架，通过合成增强人类演示学习通用物体放置，以解决机器人家庭组织任务。**

**关键词**: `物体放置学习` `合成数据增强` `多模态大语言模型` `扩散规划器` `机器人辅助` `几何可行性`

## 📋 核心要点

1. 核心问题：机器人物体放置需兼顾语义偏好和几何可行性，面临数据稀缺挑战。
2. 方法要点：使用多模态大语言模型生成结构化计划，结合扩散规划器生成放置位姿。
3. 实验效果：在真实场景中，放置成功率比次优方法提高30.04个百分点，泛化性强。

## 📄 摘要（原文）

> Robots are expected to serve as intelligent assistants, helping humans with
> everyday household organization. A central challenge in this setting is the
> task of object placement, which requires reasoning about both semantic
> preferences (e.g., common-sense object relations) and geometric feasibility
> (e.g., collision avoidance). We present GOPLA, a hierarchical framework that
> learns generalizable object placement from augmented human demonstrations. A
> multi-modal large language model translates human instructions and visual
> inputs into structured plans that specify pairwise object relationships. These
> plans are then converted into 3D affordance maps with geometric common sense by
> a spatial mapper, while a diffusion-based planner generates placement poses
> guided by test-time costs, considering multi-plan distributions and collision
> avoidance. To overcome data scarcity, we introduce a scalable pipeline that
> expands human placement demonstrations into diverse synthetic training data.
> Extensive experiments show that our approach improves placement success rates
> by 30.04 percentage points over the runner-up, evaluated on positioning
> accuracy and physical plausibility, demonstrating strong generalization across
> a wide range of real-world robotic placement scenarios.

