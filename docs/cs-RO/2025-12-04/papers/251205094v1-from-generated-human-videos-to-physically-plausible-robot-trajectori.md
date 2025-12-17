---
layout: default
title: From Generated Human Videos to Physically Plausible Robot Trajectories
---

# From Generated Human Videos to Physically Plausible Robot Trajectories

**arXiv**: [2512.05094v1](https://arxiv.org/abs/2512.05094) | [PDF](https://arxiv.org/pdf/2512.05094.pdf)

**作者**: James Ni, Zekai Wang, Wei Lin, Amir Bar, Yann LeCun, Trevor Darrell, Jitendra Malik, Roei Herzig

---

## 💡 一句话要点

**提出GenMimic以从生成视频中零模仿人类动作，实现机器人物理稳定控制**

**关键词**: `视频生成模型` `机器人控制` `强化学习` `人体动作模仿` `零样本泛化` `物理仿真`

## 📋 核心要点

1. 核心问题：如何从噪声生成视频中零样本执行人类动作，克服形态失真和物理约束
2. 方法要点：两阶段流程，先提取4D人体表示并重定向，后训练物理感知强化学习策略GenMimic
3. 实验或效果：在GenMimicBench基准上优于基线，Unitree G1机器人上实现稳定运动跟踪

## 📄 摘要（原文）

> Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic-a physics-aware reinforcement learning policy conditioned on 3D keypoints, and trained with symmetry regularization and keypoint-weighted tracking rewards. As a result, GenMimic can mimic human actions from noisy, generated videos. We curate GenMimicBench, a synthetic human-motion dataset generated using two video generation models across a spectrum of actions and contexts, establishing a benchmark for assessing zero-shot generalization and policy robustness. Extensive experiments demonstrate improvements over strong baselines in simulation and confirm coherent, physically stable motion tracking on a Unitree G1 humanoid robot without fine-tuning. This work offers a promising path to realizing the potential of video generation models as high-level policies for robot control.

