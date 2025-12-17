---
layout: default
title: Motion Marionette: Rethinking Rigid Motion Transfer via Prior Guidance
---

# Motion Marionette: Rethinking Rigid Motion Transfer via Prior Guidance

**arXiv**: [2511.19909v1](https://arxiv.org/abs/2511.19909) | [PDF](https://arxiv.org/pdf/2511.19909.pdf)

**作者**: Haoxuan Wang, Jiachen Tao, Junyi Wu, Gaowen Liu, Ramana Rao Kompella, Yan Yan

---

## 💡 一句话要点

**提出Motion Marionette框架，通过内部先验实现单目视频到图像的零样本刚性运动迁移。**

**关键词**: `刚性运动迁移` `零样本学习` `空间-时间先验` `速度场合成` `视频生成`

## 📋 核心要点

1. 核心问题：现有方法依赖外部先验，导致泛化性与时间一致性间的权衡。
2. 方法要点：构建空间-时间先验，集成目标对象生成可控速度场，并优化视觉连贯性。
3. 实验或效果：框架泛化性强，生成视频时间一致，支持可控视频生成。

## 📄 摘要（原文）

> We present Motion Marionette, a zero-shot framework for rigid motion transfer from monocular source videos to single-view target images. Previous works typically employ geometric, generative, or simulation priors to guide the transfer process, but these external priors introduce auxiliary constraints that lead to trade-offs between generalizability and temporal consistency. To address these limitations, we propose guiding the motion transfer process through an internal prior that exclusively captures the spatial-temporal transformations and is shared between the source video and any transferred target video. Specifically, we first lift both the source video and the target image into a unified 3D representation space. Motion trajectories are then extracted from the source video to construct a spatial-temporal (SpaT) prior that is independent of object geometry and semantics, encoding relative spatial variations over time. This prior is further integrated with the target object to synthesize a controllable velocity field, which is subsequently refined using Position-Based Dynamics to mitigate artifacts and enhance visual coherence. The resulting velocity field can be flexibly employed for efficient video production. Empirical results demonstrate that Motion Marionette generalizes across diverse objects, produces temporally consistent videos that align well with the source motion, and supports controllable video generation.

