---
layout: default
title: Any4D: Unified Feed-Forward Metric 4D Reconstruction
---

# Any4D: Unified Feed-Forward Metric 4D Reconstruction

**arXiv**: [2512.10935v1](https://arxiv.org/abs/2512.10935) | [PDF](https://arxiv.org/pdf/2512.10935.pdf)

**作者**: Jay Karhade, Nikhil Keetha, Yuchen Zhang, Tanisha Gupta, Akash Sharma, Sebastian Scherer, Deva Ramanan

---

## 💡 一句话要点

**提出Any4D统一前馈度量4D重建方法，支持多模态输入与高效处理**

**关键词**: `4D重建` `多视图变换器` `度量尺度` `多模态融合` `前馈网络` `场景流`

## 📋 核心要点

1. 核心问题：现有方法多专注于2视图密集场景流或稀疏3D点跟踪，缺乏统一、可扩展的4D重建框架
2. 方法要点：采用模块化4D场景表示，结合以自我为中心和以世界为中心的因子，直接生成逐像素运动和几何预测
3. 实验或效果：在多样设置下实现更高精度（误差降低2-3倍）和计算效率（快15倍），支持下游应用

## 📄 摘要（原文）

> We present Any4D, a scalable multi-view transformer for metric-scale, dense feed-forward 4D reconstruction. Any4D directly generates per-pixel motion and geometry predictions for N frames, in contrast to prior work that typically focuses on either 2-view dense scene flow or sparse 3D point tracking. Moreover, unlike other recent methods for 4D reconstruction from monocular RGB videos, Any4D can process additional modalities and sensors such as RGB-D frames, IMU-based egomotion, and Radar Doppler measurements, when available. One of the key innovations that allows for such a flexible framework is a modular representation of a 4D scene; specifically, per-view 4D predictions are encoded using a variety of egocentric factors (depthmaps and camera intrinsics) represented in local camera coordinates, and allocentric factors (camera extrinsics and scene flow) represented in global world coordinates. We achieve superior performance across diverse setups - both in terms of accuracy (2-3X lower error) and compute efficiency (15X faster), opening avenues for multiple downstream applications.

