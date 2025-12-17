---
layout: default
title: Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding
---

# Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding

**arXiv**: [2512.05941v1](https://arxiv.org/abs/2512.05941) | [PDF](https://arxiv.org/pdf/2512.05941.pdf)

**作者**: Zhiyuan Jiang, Shenghao Xie, Wenyi Li, Wenqiang Zu, Peihang Li, Jiahao Qiu, Siqi Pei, Lei Ma, Tiejun Huang, Mengdi Wang, Shilong Liu

---

## 💡 一句话要点

**提出ZoomClick方法，利用缩放先验提升GUI grounding性能，无需训练。**

**关键词**: `GUI grounding` `缩放先验` `无训练方法` `动态空间聚焦` `自适应上下文切换` `基准测试`

## 📋 核心要点

1. 核心问题：现有GUI grounding方法依赖大规模边界框监督，面临跨平台泛化、复杂布局分析和细粒度定位挑战。
2. 方法要点：通过分析缩放的四个关键属性（预缩放、深度、收缩尺寸、最小裁剪尺寸），实现动态空间聚焦和自适应上下文切换。
3. 实验或效果：在多个主流基准测试中显著提升模型性能，例如UI-Venus-72B在ScreenSpot-Pro上达到73.1%成功率。

## 📄 摘要（原文）

> Grounding is a fundamental capability for building graphical user interface (GUI) agents. Although existing approaches rely on large-scale bounding box supervision, they still face various challenges, such as cross-platform generalization, complex layout analysis, and fine-grained element localization. In this paper, we investigate zoom as a strong yet underexplored prior for GUI grounding, and propose a training-free method, ZoomClick. By characterizing four key properties of zoom (i.e., pre-zoom, depth, shrink size, minimal crop size), we unlock its full capabilities for dynamic spatial focusing and adaptive context switching. Experiments demonstrate that our method significantly boosts the performance of both general vision-language and specialized GUI grounding models, achieving state-of-the-art results on several mainstream benchmarks; for example, UI-Venus-72B attains a 73.1% success rate on ScreenSpot-Pro. Furthermore, we present GUIZoom-Bench, a benchmark for evaluating model adaptability to zoom, aiming to inspire future research on improving zoom for further training and test-time scaling in GUI grounding tasks.

