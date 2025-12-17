---
layout: default
title: Semantic World Models
---

# Semantic World Models

**arXiv**: [2510.19818v1](https://arxiv.org/abs/2510.19818) | [PDF](https://arxiv.org/pdf/2510.19818.pdf)

**作者**: Jacob Berg, Chuning Zhu, Yanda Bao, Ishan Durugkar, Abhishek Gupta

---

## 💡 一句话要点

**提出语义世界模型以解决机器人控制中像素预测与规划目标不匹配问题**

**关键词**: `语义世界模型` `视觉问答` `机器人规划` `视觉语言模型` `泛化改进`

## 📋 核心要点

1. 核心问题：传统世界模型预测未来像素与规划决策目标不一致，导致性能不佳
2. 方法要点：将世界建模视为视觉问答问题，预测任务相关语义信息，利用视觉语言模型进行微调
3. 实验或效果：在开放机器人任务中实现策略改进，显著提升泛化能力

## 📄 摘要（原文）

> Planning with world models offers a powerful paradigm for robotic control.
> Conventional approaches train a model to predict future frames conditioned on
> current frames and actions, which can then be used for planning. However, the
> objective of predicting future pixels is often at odds with the actual planning
> objective; strong pixel reconstruction does not always correlate with good
> planning decisions. This paper posits that instead of reconstructing future
> frames as pixels, world models only need to predict task-relevant semantic
> information about the future. For such prediction the paper poses world
> modeling as a visual question answering problem about semantic information in
> future frames. This perspective allows world modeling to be approached with the
> same tools underlying vision language models. Thus vision language models can
> be trained as "semantic" world models through a supervised finetuning process
> on image-action-text data, enabling planning for decision-making while
> inheriting many of the generalization and robustness properties from the
> pretrained vision-language models. The paper demonstrates how such a semantic
> world model can be used for policy improvement on open-ended robotics tasks,
> leading to significant generalization improvements over typical paradigms of
> reconstruction-based action-conditional world modeling. Website available at
> https://weirdlabuw.github.io/swm.

