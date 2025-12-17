---
layout: default
title: Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling
---

# Video2Act: A Dual-System Video Diffusion Policy with Robotic Spatio-Motional Modeling

**arXiv**: [2512.03044v1](https://arxiv.org/abs/2512.03044) | [PDF](https://arxiv.org/pdf/2512.03044.pdf)

**作者**: Yueru Jia, Jiaming Liu, Shengbang Liu, Rui Zhou, Wanhe Yu, Yuyang Yan, Xiaowei Chi, Yandong Guo, Boxin Shi, Shanghang Zhang

---

## 💡 一句话要点

**提出Video2Act框架，通过视频扩散模型与扩散变换器的双系统设计，增强机器人动作学习的空间与运动感知能力。**

**关键词**: `视频扩散模型` `机器人策略学习` `运动感知表示` `扩散变换器` `双系统设计` `动作生成`

## 📋 核心要点

1. 现有方法忽视视频扩散模型中跨帧的连贯运动表示，导致机器人策略学习受限。
2. Video2Act提取前景边界和帧间运动变化，作为扩散变换器动作头的条件输入，实现异步双系统协作。
3. 在仿真和真实任务中，平均成功率分别提升7.7%和21.7%，展现强泛化能力。

## 📄 摘要（原文）

> Robust perception and dynamics modeling are fundamental to real-world robotic policy learning. Recent methods employ video diffusion models (VDMs) to enhance robotic policies, improving their understanding and modeling of the physical world. However, existing approaches overlook the coherent and physically consistent motion representations inherently encoded across frames in VDMs. To this end, we propose Video2Act, a framework that efficiently guides robotic action learning by explicitly integrating spatial and motion-aware representations. Building on the inherent representations of VDMs, we extract foreground boundaries and inter-frame motion variations while filtering out background noise and task-irrelevant biases. These refined representations are then used as additional conditioning inputs to a diffusion transformer (DiT) action head, enabling it to reason about what to manipulate and how to move. To mitigate inference inefficiency, we propose an asynchronous dual-system design, where the VDM functions as the slow System 2 and the DiT head as the fast System 1, working collaboratively to generate adaptive actions. By providing motion-aware conditions to System 1, Video2Act maintains stable manipulation even with low-frequency updates from the VDM. For evaluation, Video2Act surpasses previous state-of-the-art VLA methods by 7.7% in simulation and 21.7% in real-world tasks in terms of average success rate, further exhibiting strong generalization capabilities.

