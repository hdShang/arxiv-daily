---
layout: default
title: AutoScape: Geometry-Consistent Long-Horizon Scene Generation
---

# AutoScape: Geometry-Consistent Long-Horizon Scene Generation

**arXiv**: [2510.20726v1](https://arxiv.org/abs/2510.20726) | [PDF](https://arxiv.org/pdf/2510.20726.pdf)

**作者**: Jiacheng Chen, Ziyu Jiang, Mingfu Liang, Bingbing Zhuang, Jong-Chyi Su, Sparsh Garg, Ying Wu, Manmohan Chandraker

---

## 💡 一句话要点

**提出AutoScape框架，通过几何一致关键帧生成长时驾驶场景视频**

**关键词**: `长时场景生成` `RGB-D扩散模型` `几何一致性` `视频插值` `驾驶场景`

## 📋 核心要点

1. 核心问题：长时驾驶场景生成中几何一致性与视频连贯性难以保持
2. 方法要点：使用RGB-D扩散模型迭代生成几何一致关键帧，并基于点云条件引导采样
3. 实验或效果：生成20秒以上视频，FID和FVD分数分别提升48.6%和43.0%

## 📄 摘要（原文）

> This paper proposes AutoScape, a long-horizon driving scene generation
> framework. At its core is a novel RGB-D diffusion model that iteratively
> generates sparse, geometrically consistent keyframes, serving as reliable
> anchors for the scene's appearance and geometry. To maintain long-range
> geometric consistency, the model 1) jointly handles image and depth in a shared
> latent space, 2) explicitly conditions on the existing scene geometry (i.e.,
> rendered point clouds) from previously generated keyframes, and 3) steers the
> sampling process with a warp-consistent guidance. Given high-quality RGB-D
> keyframes, a video diffusion model then interpolates between them to produce
> dense and coherent video frames. AutoScape generates realistic and
> geometrically consistent driving videos of over 20 seconds, improving the
> long-horizon FID and FVD scores over the prior state-of-the-art by 48.6\% and
> 43.0\%, respectively.

