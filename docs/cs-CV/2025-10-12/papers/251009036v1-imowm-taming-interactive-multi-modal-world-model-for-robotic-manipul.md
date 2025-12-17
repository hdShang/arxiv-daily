---
layout: default
title: iMoWM: Taming Interactive Multi-Modal World Model for Robotic Manipulation
---

# iMoWM: Taming Interactive Multi-Modal World Model for Robotic Manipulation

**arXiv**: [2510.09036v1](https://arxiv.org/abs/2510.09036) | [PDF](https://arxiv.org/pdf/2510.09036.pdf)

**作者**: Chuanrui Zhang, Zhengxian Wu, Guanxing Lu, Yansong Tang, Ziwei Wang

---

## 💡 一句话要点

**提出iMoWM交互式多模态世界模型，以增强机器人操作中的物理推理能力。**

**关键词**: `机器人操作` `多模态世界模型` `自回归生成` `深度预测` `模型强化学习`

## 📋 核心要点

1. 核心问题：现有2D视频世界模型缺乏几何和空间推理，难以捕捉3D物理结构。
2. 方法要点：引入MMTokenizer统一多模态输入，实现自回归生成图像、深度图和机器人臂掩码。
3. 实验或效果：在模型强化学习和模仿学习中展示优越性，提升预测质量和仿真效率。

## 📄 摘要（原文）

> Learned world models hold significant potential for robotic manipulation, as
> they can serve as simulator for real-world interactions. While extensive
> progress has been made in 2D video-based world models, these approaches often
> lack geometric and spatial reasoning, which is essential for capturing the
> physical structure of the 3D world. To address this limitation, we introduce
> iMoWM, a novel interactive world model designed to generate color images, depth
> maps, and robot arm masks in an autoregressive manner conditioned on actions.
> To overcome the high computational cost associated with three-dimensional
> information, we propose MMTokenizer, which unifies multi-modal inputs into a
> compact token representation. This design enables iMoWM to leverage large-scale
> pretrained VideoGPT models while maintaining high efficiency and incorporating
> richer physical information. With its multi-modal representation, iMoWM not
> only improves the visual quality of future predictions but also serves as an
> effective simulator for model-based reinforcement learning (MBRL) and
> facilitates real-world imitation learning. Extensive experiments demonstrate
> the superiority of iMoWM across these tasks, showcasing the advantages of
> multi-modal world modeling for robotic manipulation. Homepage:
> https://xingyoujun.github.io/imowm/

