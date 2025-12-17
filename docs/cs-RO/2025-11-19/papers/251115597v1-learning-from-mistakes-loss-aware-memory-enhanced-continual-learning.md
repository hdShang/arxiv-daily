---
layout: default
title: Learning from Mistakes: Loss-Aware Memory Enhanced Continual Learning for LiDAR Place Recognition
---

# Learning from Mistakes: Loss-Aware Memory Enhanced Continual Learning for LiDAR Place Recognition

**arXiv**: [2511.15597v1](https://arxiv.org/abs/2511.15597) | [PDF](https://arxiv.org/pdf/2511.15597.pdf)

**作者**: Xufei Wang, Junqiao Zhao, Siyue Tao, Qiwen Gu, Wonbong Kim, Tiantian Feng

---

## 💡 一句话要点

**提出KDF+框架以解决LiDAR地点识别中的灾难性遗忘问题**

**关键词**: `LiDAR地点识别` `持续学习` `灾难性遗忘` `损失感知采样` `排练增强` `机器人导航`

## 📋 核心要点

1. 核心问题：LiDAR地点识别方法难以适应新环境且易遗忘旧知识
2. 方法要点：采用损失感知采样策略和排练增强机制提升样本选择与知识保留
3. 实验或效果：在多个基准测试中优于现有方法，实现稳定性能提升

## 📄 摘要（原文）

> LiDAR place recognition plays a crucial role in SLAM, robot navigation, and autonomous driving. However, existing LiDAR place recognition methods often struggle to adapt to new environments without forgetting previously learned knowledge, a challenge widely known as catastrophic forgetting. To address this issue, we propose KDF+, a novel continual learning framework for LiDAR place recognition that extends the KDF paradigm with a loss-aware sampling strategy and a rehearsal enhancement mechanism. The proposed sampling strategy estimates the learning difficulty of each sample via its loss value and selects samples for replay according to their estimated difficulty. Harder samples, which tend to encode more discriminative information, are sampled with higher probability while maintaining distributional coverage across the dataset. In addition, the rehearsal enhancement mechanism encourages memory samples to be further refined during new-task training by slightly reducing their loss relative to previous tasks, thereby reinforcing long-term knowledge retention. Extensive experiments across multiple benchmarks demonstrate that KDF+ consistently outperforms existing continual learning methods and can be seamlessly integrated into state-of-the-art continual learning for LiDAR place recognition frameworks to yield significant and stable performance gains. The code will be available at https://github.com/repo/KDF-plus.

