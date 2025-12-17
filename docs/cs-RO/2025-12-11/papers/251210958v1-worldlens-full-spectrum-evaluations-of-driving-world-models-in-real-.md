---
layout: default
title: WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World
---

# WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World

**arXiv**: [2512.10958v1](https://arxiv.org/abs/2512.10958) | [PDF](https://arxiv.org/pdf/2512.10958.pdf)

**作者**: Ao Liang, Lingdong Kong, Tianyi Yan, Hongsi Liu, Wesley Yang, Ziqi Huang, Wei Yin, Jialong Zuo, Yixuan Hu, Dekai Zhu, Dongyue Lu, Youquan Liu, Guangfeng Jiang, Linfeng Li, Xiangtai Li, Long Zhuo, Lai Xing Ng, Benoit R. Cottereau, Changxin Gao, Liang Pan, Wei Tsang Ooi, Ziwei Liu

---

## 💡 一句话要点

**提出WorldLens基准以全面评估驾驶世界模型的真实性与功能性**

**关键词**: `世界模型评估` `驾驶场景生成` `几何一致性` `物理合理性` `人类偏好标注` `蒸馏评估模型`

## 📋 核心要点

1. 核心问题：生成世界模型缺乏统一评估标准，难以衡量几何、物理和行为可靠性
2. 方法要点：构建涵盖生成、重建、动作跟随、下游任务和人类偏好的五维度评估框架
3. 实验或效果：创建WorldLens-26K数据集和WorldLens-Agent模型，实现可扩展、可解释的评分

## 📄 摘要（原文）

> Generative world models are reshaping embodied AI, enabling agents to synthesize realistic 4D driving environments that look convincing but often fail physically or behaviorally. Despite rapid progress, the field still lacks a unified way to assess whether generated worlds preserve geometry, obey physics, or support reliable control. We introduce WorldLens, a full-spectrum benchmark evaluating how well a model builds, understands, and behaves within its generated world. It spans five aspects -- Generation, Reconstruction, Action-Following, Downstream Task, and Human Preference -- jointly covering visual realism, geometric consistency, physical plausibility, and functional reliability. Across these dimensions, no existing world model excels universally: those with strong textures often violate physics, while geometry-stable ones lack behavioral fidelity. To align objective metrics with human judgment, we further construct WorldLens-26K, a large-scale dataset of human-annotated videos with numerical scores and textual rationales, and develop WorldLens-Agent, an evaluation model distilled from these annotations to enable scalable, explainable scoring. Together, the benchmark, dataset, and agent form a unified ecosystem for measuring world fidelity -- standardizing how future models are judged not only by how real they look, but by how real they behave.

