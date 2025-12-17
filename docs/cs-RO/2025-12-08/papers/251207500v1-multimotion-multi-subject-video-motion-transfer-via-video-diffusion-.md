---
layout: default
title: MultiMotion: Multi Subject Video Motion Transfer via Video Diffusion Transformer
---

# MultiMotion: Multi Subject Video Motion Transfer via Video Diffusion Transformer

**arXiv**: [2512.07500v1](https://arxiv.org/abs/2512.07500) | [PDF](https://arxiv.org/pdf/2512.07500.pdf)

**作者**: Penghui Liu, Jiangshan Wang, Yutong Shen, Shanhui Mo, Chenyang Qi, Yue Ma

---

## 💡 一句话要点

**提出MultiMotion框架，通过Maskaware Attention Motion Flow解决多对象视频运动转移中的运动纠缠问题。**

**关键词**: `视频运动转移` `扩散变换器` `多对象控制` `运动解缠` `基准数据集`

## 📋 核心要点

1. 核心问题：多对象视频运动转移在Diffusion Transformer中面临运动纠缠和对象级控制缺失的挑战。
2. 方法要点：引入Maskaware Attention Motion Flow，利用SAM2掩码在DiT流程中显式解缠和控制多对象运动特征。
3. 实验或效果：构建首个基于DiT的多对象运动转移基准数据集，实现精确、语义对齐且时间一致的运动转移。

## 📄 摘要（原文）

> Multi-object video motion transfer poses significant challenges for Diffusion Transformer (DiT) architectures due to inherent motion entanglement and lack of object-level control. We present MultiMotion, a novel unified framework that overcomes these limitations. Our core innovation is Maskaware Attention Motion Flow (AMF), which utilizes SAM2 masks to explicitly disentangle and control motion features for multiple objects within the DiT pipeline. Furthermore, we introduce RectPC, a high-order predictor-corrector solver for efficient and accurate sampling, particularly beneficial for multi-entity generation. To facilitate rigorous evaluation, we construct the first benchmark dataset specifically for DiT-based multi-object motion transfer. MultiMotion demonstrably achieves precise, semantically aligned, and temporally coherent motion transfer for multiple distinct objects, maintaining DiT's high quality and scalability. The code is in the supp.

