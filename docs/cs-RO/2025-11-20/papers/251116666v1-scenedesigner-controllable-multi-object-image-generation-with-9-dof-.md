---
layout: default
title: SceneDesigner: Controllable Multi-Object Image Generation with 9-DoF Pose Manipulation
---

# SceneDesigner: Controllable Multi-Object Image Generation with 9-DoF Pose Manipulation

**arXiv**: [2511.16666v1](https://arxiv.org/abs/2511.16666) | [PDF](https://arxiv.org/pdf/2511.16666.pdf)

**作者**: Zhenyuan Qin, Xincheng Shuai, Henghui Ding

---

## 💡 一句话要点

**提出SceneDesigner以实现多对象9自由度姿态可控图像生成**

**关键词**: `可控图像生成` `多对象姿态控制` `9自由度姿态` `CNOCS图表示` `两阶段训练` `分离对象采样`

## 📋 核心要点

1. 核心问题：现有方法难以同时控制多对象的9D姿态，导致可控性差和质量下降
2. 方法要点：引入分支网络和CNOCS图表示，采用两阶段训练和分离对象采样技术
3. 实验或效果：在可控性和质量上显著优于现有方法，支持用户自定义姿态控制

## 📄 摘要（原文）

> Controllable image generation has attracted increasing attention in recent years, enabling users to manipulate visual content such as identity and style. However, achieving simultaneous control over the 9D poses (location, size, and orientation) of multiple objects remains an open challenge. Despite recent progress, existing methods often suffer from limited controllability and degraded quality, falling short of comprehensive multi-object 9D pose control. To address these limitations, we propose SceneDesigner, a method for accurate and flexible multi-object 9-DoF pose manipulation. SceneDesigner incorporates a branched network to the pre-trained base model and leverages a new representation, CNOCS map, which encodes 9D pose information from the camera view. This representation exhibits strong geometric interpretation properties, leading to more efficient and stable training. To support training, we construct a new dataset, ObjectPose9D, which aggregates images from diverse sources along with 9D pose annotations. To further address data imbalance issues, particularly performance degradation on low-frequency poses, we introduce a two-stage training strategy with reinforcement learning, where the second stage fine-tunes the model using a reward-based objective on rebalanced data. At inference time, we propose Disentangled Object Sampling, a technique that mitigates insufficient object generation and concept confusion in complex multi-object scenes. Moreover, by integrating user-specific personalization weights, SceneDesigner enables customized pose control for reference subjects. Extensive qualitative and quantitative experiments demonstrate that SceneDesigner significantly outperforms existing approaches in both controllability and quality. Code is publicly available at https://github.com/FudanCVL/SceneDesigner.

