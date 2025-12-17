---
layout: default
title: View-Consistent Diffusion Representations for 3D-Consistent Video Generation
---

# View-Consistent Diffusion Representations for 3D-Consistent Video Generation

**arXiv**: [2511.18991v1](https://arxiv.org/abs/2511.18991) | [PDF](https://arxiv.org/pdf/2511.18991.pdf)

**作者**: Duolikun Danier, Ge Gao, Steven McDonagh, Changjian Li, Hakan Bilen, Oisin Mac Aodha

---

## 💡 一句话要点

**提出ViCoDR方法以解决视频生成中的3D不一致性问题**

**关键词**: `视频生成` `3D一致性` `扩散模型` `多视角表示` `视图一致性`

## 📋 核心要点

1. 核心问题：视频生成模型存在3D不一致性，导致物体和结构在相机姿态变化时变形
2. 方法要点：通过改进视频扩散模型的多视角一致性表示，学习视图一致的扩散表示
3. 实验或效果：在相机控制图像到视频、文本到视频和多视角生成模型中，显著提升3D一致性

## 📄 摘要（原文）

> Video generation models have made significant progress in generating realistic content, enabling applications in simulation, gaming, and film making. However, current generated videos still contain visual artifacts arising from 3D inconsistencies, e.g., objects and structures deforming under changes in camera pose, which can undermine user experience and simulation fidelity. Motivated by recent findings on representation alignment for diffusion models, we hypothesize that improving the multi-view consistency of video diffusion representations will yield more 3D-consistent video generation. Through detailed analysis on multiple recent camera-controlled video diffusion models we reveal strong correlations between 3D-consistent representations and videos. We also propose ViCoDR, a new approach for improving the 3D consistency of video models by learning multi-view consistent diffusion representations. We evaluate ViCoDR on camera controlled image-to-video, text-to-video, and multi-view generation models, demonstrating significant improvements in the 3D consistency of the generated videos. Project page: https://danier97.github.io/ViCoDR.

