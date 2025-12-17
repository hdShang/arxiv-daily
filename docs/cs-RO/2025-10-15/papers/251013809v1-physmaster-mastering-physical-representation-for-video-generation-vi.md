---
layout: default
title: PhysMaster: Mastering Physical Representation for Video Generation via Reinforcement Learning
---

# PhysMaster: Mastering Physical Representation for Video Generation via Reinforcement Learning

**arXiv**: [2510.13809v1](https://arxiv.org/abs/2510.13809) | [PDF](https://arxiv.org/pdf/2510.13809.pdf)

**作者**: Sihui Ji, Xi Chen, Xin Tao, Pengfei Wan, Hengshuang Zhao

---

## 💡 一句话要点

**提出PhysMaster通过强化学习学习物理表示，以增强视频生成的物理合理性**

**关键词**: `视频生成` `物理表示学习` `强化学习` `人类反馈` `直接偏好优化` `图像到视频`

## 📋 核心要点

1. 当前视频生成模型视觉逼真但常违反物理定律，限制其作为世界模型的应用
2. 设计PhysEncoder从输入图像编码物理信息，并利用强化学习优化物理表示
3. 在代理任务中验证物理合理性，并展示对广泛物理场景的泛化能力

## 📄 摘要（原文）

> Video generation models nowadays are capable of generating visually realistic
> videos, but often fail to adhere to physical laws, limiting their ability to
> generate physically plausible videos and serve as ''world models''. To address
> this issue, we propose PhysMaster, which captures physical knowledge as a
> representation for guiding video generation models to enhance their
> physics-awareness. Specifically, PhysMaster is based on the image-to-video task
> where the model is expected to predict physically plausible dynamics from the
> input image. Since the input image provides physical priors like relative
> positions and potential interactions of objects in the scenario, we devise
> PhysEncoder to encode physical information from it as an extra condition to
> inject physical knowledge into the video generation process. The lack of proper
> supervision on the model's physical performance beyond mere appearance
> motivates PhysEncoder to apply reinforcement learning with human feedback to
> physical representation learning, which leverages feedback from generation
> models to optimize physical representations with Direct Preference Optimization
> (DPO) in an end-to-end manner. PhysMaster provides a feasible solution for
> improving physics-awareness of PhysEncoder and thus of video generation,
> proving its ability on a simple proxy task and generalizability to wide-ranging
> physical scenarios. This implies that our PhysMaster, which unifies solutions
> for various physical processes via representation learning in the reinforcement
> learning paradigm, can act as a generic and plug-in solution for physics-aware
> video generation and broader applications.

