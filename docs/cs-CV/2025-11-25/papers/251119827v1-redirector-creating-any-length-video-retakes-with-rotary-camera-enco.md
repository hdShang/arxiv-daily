---
layout: default
title: ReDirector: Creating Any-Length Video Retakes with Rotary Camera Encoding
---

# ReDirector: Creating Any-Length Video Retakes with Rotary Camera Encoding

**arXiv**: [2511.19827v1](https://arxiv.org/abs/2511.19827) | [PDF](https://arxiv.org/pdf/2511.19827.pdf)

**作者**: Byeongjun Park, Byung-Hoon Kim, Hyungjin Chung, Jong Chul Ye

---

## 💡 一句话要点

**提出ReDirector方法，通过旋转相机编码生成任意长度视频重拍，提升相机控制与几何一致性。**

**关键词**: `视频重拍生成` `旋转位置编码` `相机控制` `几何一致性` `多视图关系`

## 📋 核心要点

1. 核心问题：现有方法误用RoPE，导致输入与目标视频的时空位置未对齐。
2. 方法要点：引入RoCE，将相机条件融入RoPE相位偏移，捕获多视图关系。
3. 实验或效果：在分布外相机轨迹和视频长度上，改善动态对象定位和背景保留。

## 📄 摘要（原文）

> We present ReDirector, a novel camera-controlled video retake generation method for dynamically captured variable-length videos. In particular, we rectify a common misuse of RoPE in previous works by aligning the spatiotemporal positions of the input video and the target retake. Moreover, we introduce Rotary Camera Encoding (RoCE), a camera-conditioned RoPE phase shift that captures and integrates multi-view relationships within and across the input and target videos. By integrating camera conditions into RoPE, our method generalizes to out-of-distribution camera trajectories and video lengths, yielding improved dynamic object localization and static background preservation. Extensive experiments further demonstrate significant improvements in camera controllability, geometric consistency, and video quality across various trajectories and lengths.

