---
layout: default
title: ViPRA: Video Prediction for Robot Actions
---

# ViPRA: Video Prediction for Robot Actions

**arXiv**: [2511.07732v1](https://arxiv.org/abs/2511.07732) | [PDF](https://arxiv.org/pdf/2511.07732.pdf)

**作者**: Sandeep Routray, Hengkai Pan, Unnat Jain, Shikhar Bahl, Deepak Pathak

---

## 💡 一句话要点

**提出ViPRA框架，从无动作视频学习机器人连续控制，提升泛化能力。**

**关键词**: `视频预测` `机器人控制` `潜在动作学习` `光流一致性` `连续动作解码`

## 📋 核心要点

1. 问题：无标签动作视频难以直接用于机器人学习，限制物理交互利用。
2. 方法：训练视频-语言模型预测未来观测和运动中心潜在动作，使用感知损失和光流一致性。
3. 效果：在SIMPLER基准提升16%，真实世界任务提升13%，支持22Hz高频控制。

## 📄 摘要（原文）

> Can we turn a video prediction model into a robot policy? Videos, including those of humans or teleoperated robots, capture rich physical interactions. However, most of them lack labeled actions, which limits their use in robot learning. We present Video Prediction for Robot Actions (ViPRA), a simple pretraining-finetuning framework that learns continuous robot control from these actionless videos. Instead of directly predicting actions, we train a video-language model to predict both future visual observations and motion-centric latent actions, which serve as intermediate representations of scene dynamics. We train these latent actions using perceptual losses and optical flow consistency to ensure they reflect physically grounded behavior. For downstream control, we introduce a chunked flow matching decoder that maps latent actions to robot-specific continuous action sequences, using only 100 to 200 teleoperated demonstrations. This approach avoids expensive action annotation, supports generalization across embodiments, and enables smooth, high-frequency continuous control upto 22 Hz via chunked action decoding. Unlike prior latent action works that treat pretraining as autoregressive policy learning, explicitly models both what changes and how. Our method outperforms strong baselines, with a 16% gain on the SIMPLER benchmark and a 13% improvement across real world manipulation tasks. We will release models and code at https://vipra-project.github.io

