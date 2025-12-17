---
layout: default
title: The Image as Its Own Reward: Reinforcement Learning with Adversarial Reward for Image Generation
---

# The Image as Its Own Reward: Reinforcement Learning with Adversarial Reward for Image Generation

**arXiv**: [2511.20256v1](https://arxiv.org/abs/2511.20256) | [PDF](https://arxiv.org/pdf/2511.20256.pdf)

**作者**: Weijia Mao, Hao Chen, Zhenheng Yang, Mike Zheng Shou

---

## 💡 一句话要点

**提出Adv-GRPO框架，以对抗奖励解决图像生成中奖励函数不可靠问题。**

**关键词**: `强化学习` `图像生成` `对抗奖励` `视觉基础模型` `奖励黑客攻击`

## 📋 核心要点

1. 核心问题：现有奖励函数易被黑客攻击，无法准确反映人类感知。
2. 方法要点：使用图像自身作为奖励，结合参考图像和视觉基础模型提供密集视觉信号。
3. 实验或效果：在人类评估中，图像质量和美学胜率分别达70.0%和72.4%。

## 📄 摘要（原文）

> A reliable reward function is essential for reinforcement learning (RL) in image generation. Most current RL approaches depend on pre-trained preference models that output scalar rewards to approximate human preferences. However, these rewards often fail to capture human perception and are vulnerable to reward hacking, where higher scores do not correspond to better images. To address this, we introduce Adv-GRPO, an RL framework with an adversarial reward that iteratively updates both the reward model and the generator. The reward model is supervised using reference images as positive samples and can largely avoid being hacked. Unlike KL regularization that constrains parameter updates, our learned reward directly guides the generator through its visual outputs, leading to higher-quality images. Moreover, while optimizing existing reward functions can alleviate reward hacking, their inherent biases remain. For instance, PickScore may degrade image quality, whereas OCR-based rewards often reduce aesthetic fidelity. To address this, we take the image itself as a reward, using reference images and vision foundation models (e.g., DINO) to provide rich visual rewards. These dense visual signals, instead of a single scalar, lead to consistent gains across image quality, aesthetics, and task-specific metrics. Finally, we show that combining reference samples with foundation-model rewards enables distribution transfer and flexible style customization. In human evaluation, our method outperforms Flow-GRPO and SD3, achieving 70.0% and 72.4% win rates in image quality and aesthetics, respectively. Code and models have been released.

