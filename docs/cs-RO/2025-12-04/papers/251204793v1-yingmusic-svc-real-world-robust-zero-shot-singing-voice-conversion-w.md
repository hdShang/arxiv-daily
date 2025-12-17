---
layout: default
title: YingMusic-SVC: Real-World Robust Zero-Shot Singing Voice Conversion with Flow-GRPO and Singing-Specific Inductive Biases
---

# YingMusic-SVC: Real-World Robust Zero-Shot Singing Voice Conversion with Flow-GRPO and Singing-Specific Inductive Biases

**arXiv**: [2512.04793v1](https://arxiv.org/abs/2512.04793) | [PDF](https://arxiv.org/pdf/2512.04793.pdf)

**作者**: Gongyu Chen, Xiaoyu Zhang, Zhenqiang Weng, Junjie Zheng, Da Shen, Chaofan Ding, Wei-Qiang Zhang, Zihao Chen

---

## 💡 一句话要点

**提出YingMusic-SVC以解决真实歌曲中零样本歌声转换的鲁棒性问题**

**关键词**: `歌声转换` `零样本学习` `鲁棒性增强` `流匹配` `强化学习` `归纳偏置`

## 📋 核心要点

1. 核心问题：现有零样本歌声转换系统在真实歌曲中因和声干扰、音高错误和缺乏歌唱归纳偏置而脆弱
2. 方法要点：结合连续预训练、鲁棒监督微调和Flow-GRPO强化学习，引入歌唱训练的音色移位器和音高感知适配器
3. 实验或效果：在多轨基准测试中，在音色相似度、可懂度和感知自然度上优于基线，尤其在伴奏和和声污染条件下

## 📄 摘要（原文）

> Singing voice conversion (SVC) aims to render the target singer's timbre while preserving melody and lyrics. However, existing zero-shot SVC systems remain fragile in real songs due to harmony interference, F0 errors, and the lack of inductive biases for singing. We propose YingMusic-SVC, a robust zero-shot framework that unifies continuous pre-training, robust supervised fine-tuning, and Flow-GRPO reinforcement learning. Our model introduces a singing-trained RVC timbre shifter for timbre-content disentanglement, an F0-aware timbre adaptor for dynamic vocal expression, and an energy-balanced rectified flow matching loss to enhance high-frequency fidelity. Experiments on a graded multi-track benchmark show that YingMusic-SVC achieves consistent improvements over strong open-source baselines in timbre similarity, intelligibility, and perceptual naturalness, especially under accompanied and harmony-contaminated conditions, demonstrating its effectiveness for real-world SVC deployment.

