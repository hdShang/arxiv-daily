---
layout: default
title: LiFMCR: Dataset and Benchmark for Light Field Multi-Camera Registration
---

# LiFMCR: Dataset and Benchmark for Light Field Multi-Camera Registration

**arXiv**: [2510.13729v1](https://arxiv.org/abs/2510.13729) | [PDF](https://arxiv.org/pdf/2510.13729.pdf)

**作者**: Aymeric Fleith, Julian Zirbel, Daniel Cremers, Niclas Zeller

---

## 💡 一句话要点

**提出LiFMCR数据集与基准以解决多相机光场注册问题**

**关键词**: `光场数据集` `多相机注册` `6自由度位姿` `RANSAC方法` `Plenoptic PnP算法` `运动捕捉系统`

## 📋 核心要点

1. 核心问题：现有光场数据集多限于单相机，缺乏外部高精度位姿真值。
2. 方法要点：提供同步图像序列与Vicon运动捕捉系统记录的6自由度位姿真值。
3. 实验或效果：基线方法显示与真值强对齐，支持可靠多视角光场处理。

## 📄 摘要（原文）

> We present LiFMCR, a novel dataset for the registration of multiple micro
> lens array (MLA)-based light field cameras. While existing light field datasets
> are limited to single-camera setups and typically lack external ground truth,
> LiFMCR provides synchronized image sequences from two high-resolution Raytrix
> R32 plenoptic cameras, together with high-precision 6-degrees of freedom (DoF)
> poses recorded by a Vicon motion capture system. This unique combination
> enables rigorous evaluation of multi-camera light field registration methods.
>   As a baseline, we provide two complementary registration approaches: a robust
> 3D transformation estimation via a RANSAC-based method using cross-view point
> clouds, and a plenoptic PnP algorithm estimating extrinsic 6-DoF poses from
> single light field images. Both explicitly integrate the plenoptic camera
> model, enabling accurate and scalable multi-camera registration. Experiments
> show strong alignment with the ground truth, supporting reliable multi-view
> light field processing.
>   Project page: https://lifmcr.github.io/

