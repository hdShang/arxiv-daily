---
layout: default
title: Towards Efficient and Effective Multi-Camera Encoding for End-to-End Driving
---

# Towards Efficient and Effective Multi-Camera Encoding for End-to-End Driving

**arXiv**: [2512.10947v1](https://arxiv.org/abs/2512.10947) | [PDF](https://arxiv.org/pdf/2512.10947.pdf)

**作者**: Jiawei Yang, Ziyu Chen, Yurong You, Yan Wang, Yiming Li, Yuxiao Chen, Boyi Li, Boris Ivanovic, Marco Pavone, Yue Wang

---

## 💡 一句话要点

**提出Flex场景编码器，以高效处理端到端自动驾驶中的多摄像头数据瓶颈。**

**关键词**: `多摄像头编码` `端到端自动驾驶` `场景表示学习` `高效推理` `数据驱动方法`

## 📋 核心要点

1. 核心问题：多摄像头数据量大，处理效率低，是端到端自动驾驶的计算瓶颈。
2. 方法要点：使用可学习场景令牌联合编码多摄像头和时序图像信息，无需依赖3D先验。
3. 实验或效果：在2万小时数据集上，推理吞吐量提升2.2倍，驾驶性能大幅超越现有方法。

## 📄 摘要（原文）

> We present Flex, an efficient and effective scene encoder that addresses the computational bottleneck of processing high-volume multi-camera data in end-to-end autonomous driving. Flex employs a small set of learnable scene tokens to jointly encode information from all image tokens across different cameras and timesteps. By design, our approach is geometry-agnostic, learning a compact scene representation directly from data without relying on the explicit 3D inductive biases, such as Bird-Eye-View (BEV), occupancy or tri-plane representations, which are common in prior work. This holistic encoding strategy aggressively compresses the visual input for the downstream Large Language Model (LLM) based policy model. Evaluated on a large-scale proprietary dataset of 20,000 driving hours, our Flex achieves 2.2x greater inference throughput while improving driving performance by a large margin compared to state-of-the-art methods. Furthermore, we show that these compact scene tokens develop an emergent capability for scene decomposition without any explicit supervision. Our findings challenge the prevailing assumption that 3D priors are necessary, demonstrating that a data-driven, joint encoding strategy offers a more scalable, efficient and effective path for future autonomous driving systems.

