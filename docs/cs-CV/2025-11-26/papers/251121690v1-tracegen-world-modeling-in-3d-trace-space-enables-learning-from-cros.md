---
layout: default
title: TraceGen: World Modeling in 3D Trace Space Enables Learning from Cross-Embodiment Videos
---

# TraceGen: World Modeling in 3D Trace Space Enables Learning from Cross-Embodiment Videos

**arXiv**: [2511.21690v1](https://arxiv.org/abs/2511.21690) | [PDF](https://arxiv.org/pdf/2511.21690.pdf)

**作者**: Seungjae Lee, Yoonkyo Jung, Inkook Chun, Yao-Chih Lee, Zikui Cai, Hongjia Huang, Aayush Talreja, Tan Dat Dao, Yongyuan Liang, Jia-Bin Huang, Furong Huang

---

## 💡 一句话要点

**提出TraceGen在3D轨迹空间建模世界，以从跨具身视频中学习机器人任务**

**关键词**: `3D轨迹空间` `跨具身学习` `世界建模` `机器人任务学习` `视频数据转换` `高效推理`

## 📋 核心要点

1. 核心问题：从少量演示学习新机器人任务时，跨具身、环境和任务的视频差异阻碍直接利用
2. 方法要点：引入3D轨迹空间作为符号表示，抽象外观保留几何结构，预测未来运动
3. 实验或效果：仅用五个目标视频，在真实机器人上达到80%成功率，推理速度提升50-600倍

## 📄 摘要（原文）

> Learning new robot tasks on new platforms and in new scenes from only a handful of demonstrations remains challenging. While videos of other embodiments - humans and different robots - are abundant, differences in embodiment, camera, and environment hinder their direct use. We address the small-data problem by introducing a unifying, symbolic representation - a compact 3D "trace-space" of scene-level trajectories - that enables learning from cross-embodiment, cross-environment, and cross-task videos. We present TraceGen, a world model that predicts future motion in trace-space rather than pixel space, abstracting away appearance while retaining the geometric structure needed for manipulation. To train TraceGen at scale, we develop TraceForge, a data pipeline that transforms heterogeneous human and robot videos into consistent 3D traces, yielding a corpus of 123K videos and 1.8M observation-trace-language triplets. Pretraining on this corpus produces a transferable 3D motion prior that adapts efficiently: with just five target robot videos, TraceGen attains 80% success across four tasks while offering 50-600x faster inference than state-of-the-art video-based world models. In the more challenging case where only five uncalibrated human demonstration videos captured on a handheld phone are available, it still reaches 67.5% success on a real robot, highlighting TraceGen's ability to adapt across embodiments without relying on object detectors or heavy pixel-space generation.

