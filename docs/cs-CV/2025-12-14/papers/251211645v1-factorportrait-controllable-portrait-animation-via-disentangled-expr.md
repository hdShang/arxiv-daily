---
layout: default
title: FactorPortrait: Controllable Portrait Animation via Disentangled Expression, Pose, and Viewpoint
---

# FactorPortrait: Controllable Portrait Animation via Disentangled Expression, Pose, and Viewpoint

**arXiv**: [2512.11645v1](https://arxiv.org/abs/2512.11645) | [PDF](https://arxiv.org/pdf/2512.11645.pdf)

**作者**: Jiapeng Tang, Kai Li, Chengxiang Yin, Liuhao Ge, Fei Jiang, Jiu Xu, Matthias Nießner, Christian Häne, Timur Bagautdinov, Egor Zakharov, Peihong Guo

---

## 💡 一句话要点

**提出FactorPortrait，通过解耦控制实现单张肖像动画与视角合成**

**关键词**: `肖像动画` `视频扩散` `解耦控制` `视角合成` `表情迁移`

## 📋 核心要点

1. 核心问题：如何从单张肖像生成可控动画，同时解耦表情、姿态和视角
2. 方法要点：使用预训练编码器提取表情潜变量，结合Plücker射线图控制相机和姿态
3. 实验或效果：在合成数据集上训练，实验显示在真实感、控制精度和视角一致性上优于现有方法

## 📄 摘要（原文）

> We introduce FactorPortrait, a video diffusion method for controllable portrait animation that enables lifelike synthesis from disentangled control signals of facial expressions, head movement, and camera viewpoints. Given a single portrait image, a driving video, and camera trajectories, our method animates the portrait by transferring facial expressions and head movements from the driving video while simultaneously enabling novel view synthesis from arbitrary viewpoints. We utilize a pre-trained image encoder to extract facial expression latents from the driving video as control signals for animation generation. Such latents implicitly capture nuanced facial expression dynamics with identity and pose information disentangled, and they are efficiently injected into the video diffusion transformer through our proposed expression controller. For camera and head pose control, we employ Plücker ray maps and normal maps rendered from 3D body mesh tracking. To train our model, we curate a large-scale synthetic dataset containing diverse combinations of camera viewpoints, head poses, and facial expression dynamics. Extensive experiments demonstrate that our method outperforms existing approaches in realism, expressiveness, control accuracy, and view consistency.

