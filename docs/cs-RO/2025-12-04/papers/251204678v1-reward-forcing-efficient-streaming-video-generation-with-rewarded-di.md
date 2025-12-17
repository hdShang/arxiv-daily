---
layout: default
title: Reward Forcing: Efficient Streaming Video Generation with Rewarded Distribution Matching Distillation
---

# Reward Forcing: Efficient Streaming Video Generation with Rewarded Distribution Matching Distillation

**arXiv**: [2512.04678v1](https://arxiv.org/abs/2512.04678) | [PDF](https://arxiv.org/pdf/2512.04678.pdf)

**作者**: Yunhong Lu, Yanhong Zeng, Haobo Li, Hao Ouyang, Qiuyu Wang, Ka Leong Cheng, Jiapeng Zhu, Hengyuan Cao, Zhipeng Zhang, Xing Zhu, Yujun Shen, Min Zhang

---

## 💡 一句话要点

**提出Reward Forcing框架，通过EMA-Sink和Re-DMD解决流式视频生成中初始帧复制和动态质量不足的问题。**

**关键词**: `流式视频生成` `注意力机制` `蒸馏训练` `动态质量优化` `高效推理`

## 📋 核心要点

1. 核心问题：现有方法依赖静态初始帧作为注意力令牌，导致视频帧复制初始帧，动态运动减弱。
2. 方法要点：引入EMA-Sink令牌，通过指数移动平均融合退出窗口的令牌，捕获长期上下文和近期动态；提出Re-DMD蒸馏，基于视觉语言模型奖励优先动态样本，提升运动质量。
3. 实验或效果：在标准基准上达到先进性能，单H100 GPU上实现23.1 FPS的高质量流式视频生成。

## 📄 摘要（原文）

> Efficient streaming video generation is critical for simulating interactive and dynamic worlds. Existing methods distill few-step video diffusion models with sliding window attention, using initial frames as sink tokens to maintain attention performance and reduce error accumulation. However, video frames become overly dependent on these static tokens, resulting in copied initial frames and diminished motion dynamics. To address this, we introduce Reward Forcing, a novel framework with two key designs. First, we propose EMA-Sink, which maintains fixed-size tokens initialized from initial frames and continuously updated by fusing evicted tokens via exponential moving average as they exit the sliding window. Without additional computation cost, EMA-Sink tokens capture both long-term context and recent dynamics, preventing initial frame copying while maintaining long-horizon consistency. Second, to better distill motion dynamics from teacher models, we propose a novel Rewarded Distribution Matching Distillation (Re-DMD). Vanilla distribution matching treats every training sample equally, limiting the model's ability to prioritize dynamic content. Instead, Re-DMD biases the model's output distribution toward high-reward regions by prioritizing samples with greater dynamics rated by a vision-language model. Re-DMD significantly enhances motion quality while preserving data fidelity. We include both quantitative and qualitative experiments to show that Reward Forcing achieves state-of-the-art performance on standard benchmarks while enabling high-quality streaming video generation at 23.1 FPS on a single H100 GPU.

