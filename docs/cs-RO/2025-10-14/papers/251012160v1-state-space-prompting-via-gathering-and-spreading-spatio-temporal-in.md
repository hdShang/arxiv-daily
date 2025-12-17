---
layout: default
title: State Space Prompting via Gathering and Spreading Spatio-Temporal Information for Video Understanding
---

# State Space Prompting via Gathering and Spreading Spatio-Temporal Information for Video Understanding

**arXiv**: [2510.12160v1](https://arxiv.org/abs/2510.12160) | [PDF](https://arxiv.org/pdf/2510.12160.pdf)

**作者**: Jiahuan Zhou, Kai Zhu, Zhenyu Cui, Zichen Liu, Xu Zou, Gang Hua

---

## 💡 一句话要点

**提出状态空间提示方法以解决视频理解中时空信息传播不足的问题**

**关键词**: `视频理解` `状态空间模型` `提示学习` `时空信息传播` `参数高效微调`

## 📋 核心要点

1. 问题：预训练状态空间模型压缩视觉提示时，难以捕获视频的时空上下文信息。
2. 方法：设计帧内聚集和帧间扩散模块，自适应平衡和压缩关键时空信息。
3. 效果：在四个基准数据集上平均提升2.76%，同时减少微调参数开销。

## 📄 摘要（原文）

> Recently, pre-trained state space models have shown great potential for video
> classification, which sequentially compresses visual tokens in videos with
> linear complexity, thereby improving the processing efficiency of video data
> while maintaining high performance. To apply powerful pre-trained models to
> downstream tasks, prompt learning is proposed to achieve efficient downstream
> task adaptation with only a small number of fine-tuned parameters. However, the
> sequentially compressed visual prompt tokens fail to capture the spatial and
> temporal contextual information in the video, thus limiting the effective
> propagation of spatial information within a video frame and temporal
> information between frames in the state compression model and the extraction of
> discriminative information. To tackle the above issue, we proposed a State
> Space Prompting (SSP) method for video understanding, which combines
> intra-frame and inter-frame prompts to aggregate and propagate key
> spatiotemporal information in the video. Specifically, an Intra-Frame Gathering
> (IFG) module is designed to aggregate spatial key information within each
> frame. Besides, an Inter-Frame Spreading (IFS) module is designed to spread
> discriminative spatio-temporal information across different frames. By
> adaptively balancing and compressing key spatio-temporal information within and
> between frames, our SSP effectively propagates discriminative information in
> videos in a complementary manner. Extensive experiments on four video benchmark
> datasets verify that our SSP significantly outperforms existing SOTA methods by
> 2.76% on average while reducing the overhead of fine-tuning parameters.

