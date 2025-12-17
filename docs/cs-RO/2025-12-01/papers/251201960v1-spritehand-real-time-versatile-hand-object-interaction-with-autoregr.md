---
layout: default
title: SpriteHand: Real-Time Versatile Hand-Object Interaction with Autoregressive Video Generation
---

# SpriteHand: Real-Time Versatile Hand-Object Interaction with Autoregressive Video Generation

**arXiv**: [2512.01960v1](https://arxiv.org/abs/2512.01960) | [PDF](https://arxiv.org/pdf/2512.01960.pdf)

**作者**: Zisu Li, Hengye Lyu, Jiaxin Shi, Yufeng Zeng, Mingming Fan, Hanwang Zhang, Chen Liang

---

## 💡 一句话要点

**提出SpriteHand自回归视频生成框架，实现实时多样化手-物交互视频合成**

**关键词**: `自回归视频生成` `手-物交互` `实时合成` `因果推理` `混合后训练`

## 📋 核心要点

1. 核心问题：传统模拟方法难以处理非刚性或铰接物体的动态手-物交互
2. 方法要点：采用因果推理架构进行自回归生成，结合混合后训练提升视觉真实性和时序一致性
3. 实验或效果：模型支持实时流式生成，在视觉质量、物理合理性和交互保真度上优于基线

## 📄 摘要（原文）

> Modeling and synthesizing complex hand-object interactions remains a significant challenge, even for state-of-the-art physics engines. Conventional simulation-based approaches rely on explicitly defined rigid object models and pre-scripted hand gestures, making them inadequate for capturing dynamic interactions with non-rigid or articulated entities such as deformable fabrics, elastic materials, hinge-based structures, furry surfaces, or even living creatures. In this paper, we present SpriteHand, an autoregressive video generation framework for real-time synthesis of versatile hand-object interaction videos across a wide range of object types and motion patterns. SpriteHand takes as input a static object image and a video stream in which the hands are imagined to interact with the virtual object embedded in a real-world scene, and generates corresponding hand-object interaction effects in real time. Our model employs a causal inference architecture for autoregressive generation and leverages a hybrid post-training approach to enhance visual realism and temporal coherence. Our 1.3B model supports real-time streaming generation at around 18 FPS and 640x368 resolution, with an approximate 150 ms latency on a single NVIDIA RTX 5090 GPU, and more than a minute of continuous output. Experiments demonstrate superior visual quality, physical plausibility, and interaction fidelity compared to both generative and engine-based baselines.

