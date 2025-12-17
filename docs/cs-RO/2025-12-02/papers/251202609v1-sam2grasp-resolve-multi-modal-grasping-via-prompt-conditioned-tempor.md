---
layout: default
title: SAM2Grasp: Resolve Multi-modal Grasping via Prompt-conditioned Temporal Action Prediction
---

# SAM2Grasp: Resolve Multi-modal Grasping via Prompt-conditioned Temporal Action Prediction

**arXiv**: [2512.02609v1](https://arxiv.org/abs/2512.02609) | [PDF](https://arxiv.org/pdf/2512.02609.pdf)

**作者**: Shengkai Wu, Jinrong Yang, Wenqiu Luo, Linfeng Gao, Chaohui Shang, Meiyu Zhi, Mingshan Sun, Fangping Yang, Liangliang Ren, Yong Zhao

---

## 💡 一句话要点

**提出SAM2Grasp框架，通过提示条件化时序动作预测解决多模态抓取问题**

**关键词**: `机器人抓取` `模仿学习` `多模态问题` `时序动作预测` `提示条件化` `视觉跟踪`

## 📋 核心要点

1. 核心问题：模仿学习在多目标场景中因训练信号冲突导致动作平均化失效
2. 方法要点：利用冻结SAM2模型进行时序跟踪，结合轻量动作头实现提示条件化抓取轨迹预测
3. 实验或效果：在杂乱多对象抓取任务中达到先进性能，有效消除策略模糊性

## 📄 摘要（原文）

> Imitation learning for robotic grasping is often plagued by the multimodal problem: when a scene contains multiple valid targets, demonstrations of grasping different objects create conflicting training signals. Standard imitation learning policies fail by averaging these distinct actions into a single, invalid action. In this paper, we introduce SAM2Grasp, a novel framework that resolves this issue by reformulating the task as a uni-modal, prompt-conditioned prediction problem. Our method leverages the frozen SAM2 model to use its powerful visual temporal tracking capability and introduces a lightweight, trainable action head that operates in parallel with its native segmentation head. This design allows for training only the small action head on pre-computed temporal-visual features from SAM2. During inference, an initial prompt, such as a bounding box provided by an upstream object detection model, designates the specific object to be grasped. This prompt conditions the action head to predict a unique, unambiguous grasp trajectory for that object alone. In all subsequent video frames, SAM2's built-in temporal tracking capability automatically maintains stable tracking of the selected object, enabling our model to continuously predict the grasp trajectory from the video stream without further external guidance. This temporal-prompted approach effectively eliminates ambiguity from the visuomotor policy. We demonstrate through extensive experiments that SAM2Grasp achieves state-of-the-art performance in cluttered, multi-object grasping tasks.

