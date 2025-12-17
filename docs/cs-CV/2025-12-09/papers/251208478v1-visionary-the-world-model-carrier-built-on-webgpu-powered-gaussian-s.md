---
layout: default
title: Visionary: The World Model Carrier Built on WebGPU-Powered Gaussian Splatting Platform
---

# Visionary: The World Model Carrier Built on WebGPU-Powered Gaussian Splatting Platform

**arXiv**: [2512.08478v1](https://arxiv.org/abs/2512.08478) | [PDF](https://arxiv.org/pdf/2512.08478.pdf)

**作者**: Yuning Gong, Yifei Liu, Yifan Zhan, Muyao Niu, Xueying Li, Yuanjun Liao, Jiaming Chen, Yuanyuan Gao, Jiaqi Chen, Minming Chen, Li Zhou, Yuning Zhang, Wei Wang, Xiaoqing Hou, Huaxi Huang, Shixiang Tang, Le Ma, Dingwen Zhang, Xue Yang, Junchi Yan, Yanchi Zhang, Yinqiang Zheng, Xiao Sun, Zhihang Zhong

---

## 💡 一句话要点

**提出Visionary平台，基于WebGPU和ONNX推理实现浏览器内实时动态高斯溅射渲染，降低世界模型部署门槛。**

**关键词**: `高斯溅射渲染` `WebGPU平台` `动态神经处理` `浏览器内推理` `世界模型载体` `实时渲染`

## 📋 核心要点

1. 现有高斯溅射渲染方案碎片化、笨重，部署困难且动态内容支持有限。
2. Visionary采用WebGPU渲染器和每帧ONNX推理，支持标准3DGS及插件式算法生成动态高斯。
3. 实验显示，在相同资产下，Visionary通过GPU基元排序实现更高渲染效率，支持多种变体如4DGS和神经化身。

## 📄 摘要（原文）

> Neural rendering, particularly 3D Gaussian Splatting (3DGS), has evolved rapidly and become a key component for building world models. However, existing viewer solutions remain fragmented, heavy, or constrained by legacy pipelines, resulting in high deployment friction and limited support for dynamic content and generative models. In this work, we present Visionary, an open, web-native platform for real-time various Gaussian Splatting and meshes rendering. Built on an efficient WebGPU renderer with per-frame ONNX inference, Visionary enables dynamic neural processing while maintaining a lightweight, "click-to-run" browser experience. It introduces a standardized Gaussian Generator contract, which not only supports standard 3DGS rendering but also allows plug-and-play algorithms to generate or update Gaussians each frame. Such inference also enables us to apply feedforward generative post-processing. The platform further offers a plug in three.js library with a concise TypeScript API for seamless integration into existing web applications. Experiments show that, under identical 3DGS assets, Visionary achieves superior rendering efficiency compared to current Web viewers due to GPU-based primitive sorting. It already supports multiple variants, including MLP-based 3DGS, 4DGS, neural avatars, and style transformation or enhancement networks. By unifying inference and rendering directly in the browser, Visionary significantly lowers the barrier to reproduction, comparison, and deployment of 3DGS-family methods, serving as a unified World Model Carrier for both reconstructive and generative paradigms.

