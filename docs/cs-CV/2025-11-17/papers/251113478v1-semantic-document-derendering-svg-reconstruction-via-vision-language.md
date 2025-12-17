---
layout: default
title: Semantic Document Derendering: SVG Reconstruction via Vision-Language Modeling
---

# Semantic Document Derendering: SVG Reconstruction via Vision-Language Modeling

**arXiv**: [2511.13478v1](https://arxiv.org/abs/2511.13478) | [PDF](https://arxiv.org/pdf/2511.13478.pdf)

**作者**: Adam Hazimeh, Ke Wang, Mark Collier, Gilles Baechler, Efi Kokiopoulou, Pascal Frossard

---

## 💡 一句话要点

**提出SliDer框架，使用视觉语言模型将幻灯片图像转换为可编辑SVG格式。**

**关键词**: `语义文档去渲染` `视觉语言模型` `SVG重建` `幻灯片处理` `光栅矢量化`

## 📋 核心要点

1. 问题：现有几何光栅矢量化方法无法保留文档高层语义结构。
2. 方法：利用视觉语言模型检测元素属性，迭代生成SVG代码。
3. 效果：在Slide2SVG数据集上，LPIPS为0.069，人类评估偏好达82.9%。

## 📄 摘要（原文）

> Multimedia documents such as slide presentations and posters are designed to be interactive and easy to modify. Yet, they are often distributed in a static raster format, which limits editing and customization. Restoring their editability requires converting these raster images back into structured vector formats. However, existing geometric raster-vectorization methods, which rely on low-level primitives like curves and polygons, fall short at this task. Specifically, when applied to complex documents like slides, they fail to preserve the high-level structure, resulting in a flat collection of shapes where the semantic distinction between image and text elements is lost. To overcome this limitation, we address the problem of semantic document derendering by introducing SliDer, a novel framework that uses Vision-Language Models (VLMs) to derender slide images as compact and editable Scalable Vector Graphic (SVG) representations. SliDer detects and extracts attributes from individual image and text elements in a raster input and organizes them into a coherent SVG format. Crucially, the model iteratively refines its predictions during inference in a process analogous to human design, generating SVG code that more faithfully reconstructs the original raster upon rendering. Furthermore, we introduce Slide2SVG, a novel dataset comprising raster-SVG pairs of slide documents curated from real-world scientific presentations, to facilitate future research in this domain. Our results demonstrate that SliDer achieves a reconstruction LPIPS of 0.069 and is favored by human evaluators in 82.9% of cases compared to the strongest zero-shot VLM baseline.

