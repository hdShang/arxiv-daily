---
layout: default
title: PanoNav: Mapless Zero-Shot Object Navigation with Panoramic Scene Parsing and Dynamic Memory
---

# PanoNav: Mapless Zero-Shot Object Navigation with Panoramic Scene Parsing and Dynamic Memory

**arXiv**: [2511.06840v1](https://arxiv.org/abs/2511.06840) | [PDF](https://arxiv.org/pdf/2511.06840.pdf)

**作者**: Qunchao Jin, Yilin Wu, Changhao Chen

---

## 💡 一句话要点

**提出PanoNav框架以解决无地图零样本物体导航中的局部死锁问题**

**关键词**: `零样本物体导航` `全景场景解析` `动态内存机制` `无地图导航` `多模态大语言模型`

## 📋 核心要点

1. 核心问题：零样本物体导航在未知环境中易因缺乏历史上下文导致短视决策和局部死锁
2. 方法要点：集成全景场景解析模块和动态有界内存队列，增强空间解析与决策能力
3. 实验或效果：在公开导航基准上，SR和SPL指标显著优于代表性基线方法

## 📄 摘要（原文）

> Zero-shot object navigation (ZSON) in unseen environments remains a
> challenging problem for household robots, requiring strong perceptual
> understanding and decision-making capabilities. While recent methods leverage
> metric maps and Large Language Models (LLMs), they often depend on depth
> sensors or prebuilt maps, limiting the spatial reasoning ability of Multimodal
> Large Language Models (MLLMs). Mapless ZSON approaches have emerged to address
> this, but they typically make short-sighted decisions, leading to local
> deadlocks due to a lack of historical context. We propose PanoNav, a fully
> RGB-only, mapless ZSON framework that integrates a Panoramic Scene Parsing
> module to unlock the spatial parsing potential of MLLMs from panoramic RGB
> inputs, and a Memory-guided Decision-Making mechanism enhanced by a Dynamic
> Bounded Memory Queue to incorporate exploration history and avoid local
> deadlocks. Experiments on the public navigation benchmark show that PanoNav
> significantly outperforms representative baselines in both SR and SPL metrics.

