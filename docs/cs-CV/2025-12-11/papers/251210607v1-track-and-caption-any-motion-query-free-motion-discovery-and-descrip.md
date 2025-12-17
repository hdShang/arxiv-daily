---
layout: default
title: Track and Caption Any Motion: Query-Free Motion Discovery and Description in Videos
---

# Track and Caption Any Motion: Query-Free Motion Discovery and Description in Videos

**arXiv**: [2512.10607v1](https://arxiv.org/abs/2512.10607) | [PDF](https://arxiv.org/pdf/2512.10607.pdf)

**作者**: Bishoy Galoaa, Sarah Ostadabbas

---

## 💡 一句话要点

**提出TCAM框架，通过无查询方式发现和描述视频中的运动模式，以解决遮挡、伪装或快速运动等挑战性条件下的视频理解问题。**

**关键词**: `视频理解` `运动模式发现` `无查询描述` `空间定位` `对比视觉-语言表示` `跨任务泛化`

## 📋 核心要点

1. 核心问题：在遮挡、伪装或快速运动等挑战性条件下，视频理解更依赖运动动态而非静态外观。
2. 方法要点：利用运动场注意力机制，结合对比视觉-语言表示，实现无查询的多运动活动发现和空间定位描述。
3. 实验或效果：在MeViS基准测试中，TCAM在视频到文本检索、空间定位精度和发现相关表达方面表现优异，展示强跨任务泛化能力。

## 📄 摘要（原文）

> We propose Track and Caption Any Motion (TCAM), a motion-centric framework for automatic video understanding that discovers and describes motion patterns without user queries. Understanding videos in challenging conditions like occlusion, camouflage, or rapid movement often depends more on motion dynamics than static appearance. TCAM autonomously observes a video, identifies multiple motion activities, and spatially grounds each natural language description to its corresponding trajectory through a motion-field attention mechanism. Our key insight is that motion patterns, when aligned with contrastive vision-language representations, provide powerful semantic signals for recognizing and describing actions. Through unified training that combines global video-text alignment with fine-grained spatial correspondence, TCAM enables query-free discovery of multiple motion expressions via multi-head cross-attention. On the MeViS benchmark, TCAM achieves 58.4% video-to-text retrieval, 64.9 JF for spatial grounding, and discovers 4.8 relevant expressions per video with 84.7% precision, demonstrating strong cross-task generalization.

