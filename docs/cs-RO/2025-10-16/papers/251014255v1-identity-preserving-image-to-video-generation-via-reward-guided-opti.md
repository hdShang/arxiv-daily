---
layout: default
title: Identity-Preserving Image-to-Video Generation via Reward-Guided Optimization
---

# Identity-Preserving Image-to-Video Generation via Reward-Guided Optimization

**arXiv**: [2510.14255v1](https://arxiv.org/abs/2510.14255) | [PDF](https://arxiv.org/pdf/2510.14255.pdf)

**作者**: Liao Shen, Wentao Jiang, Yiran Zhu, Tiezheng Ge, Zhiguo Cao, Bo Zheng

---

## 💡 一句话要点

**提出身份保持奖励引导优化方法以解决图像到视频生成中身份一致性问题**

**关键词**: `图像到视频生成` `身份保持` `奖励引导优化` `扩散模型` `人脸身份评分`

## 📋 核心要点

1. 核心问题：现有图像到视频模型在人物表情和运动变化时难以保持输入图像与生成视频的身份一致性
2. 方法要点：基于强化学习优化扩散模型，使用人脸身份评分器和KL散度正则化提升身份保持
3. 实验或效果：在Wan 2.2和内部模型上验证方法有效性，增强身份保持和泛化能力

## 📄 摘要（原文）

> Recent advances in image-to-video (I2V) generation have achieved remarkable
> progress in synthesizing high-quality, temporally coherent videos from static
> images. Among all the applications of I2V, human-centric video generation
> includes a large portion. However, existing I2V models encounter difficulties
> in maintaining identity consistency between the input human image and the
> generated video, especially when the person in the video exhibits significant
> expression changes and movements. This issue becomes critical when the human
> face occupies merely a small fraction of the image. Since humans are highly
> sensitive to identity variations, this poses a critical yet under-explored
> challenge in I2V generation. In this paper, we propose Identity-Preserving
> Reward-guided Optimization (IPRO), a novel video diffusion framework based on
> reinforcement learning to enhance identity preservation. Instead of introducing
> auxiliary modules or altering model architectures, our approach introduces a
> direct and effective tuning algorithm that optimizes diffusion models using a
> face identity scorer. To improve performance and accelerate convergence, our
> method backpropagates the reward signal through the last steps of the sampling
> chain, enabling richer gradient feedback. We also propose a novel facial
> scoring mechanism that treats faces in ground-truth videos as facial feature
> pools, providing multi-angle facial information to enhance generalization. A
> KL-divergence regularization is further incorporated to stabilize training and
> prevent overfitting to the reward signal. Extensive experiments on Wan 2.2 I2V
> model and our in-house I2V model demonstrate the effectiveness of our method.
> Our project and code are available at
> \href{https://ipro-alimama.github.io/}{https://ipro-alimama.github.io/}.

