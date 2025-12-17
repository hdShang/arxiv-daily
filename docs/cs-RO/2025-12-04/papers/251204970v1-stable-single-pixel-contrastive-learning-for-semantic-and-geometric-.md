---
layout: default
title: Stable Single-Pixel Contrastive Learning for Semantic and Geometric Tasks
---

# Stable Single-Pixel Contrastive Learning for Semantic and Geometric Tasks

**arXiv**: [2512.04970v1](https://arxiv.org/abs/2512.04970) | [PDF](https://arxiv.org/pdf/2512.04970.pdf)

**作者**: Leonid Pogorelyuk, Niels Bracher, Aaron Verkleeren, Lars Kühmichel, Stefan T. Radev

---

## 💡 一句话要点

**提出稳定单像素对比损失，用于学习同时捕获语义和几何信息的像素级表示。**

**关键词**: `像素级表示学习` `对比学习` `语义几何联合学习` `过完备描述符` `视图不变性` `合成环境实验`

## 📋 核心要点

1. 核心问题：如何学习像素级表示以联合捕获语义和几何信息，无需基于动量的师生训练。
2. 方法要点：使用稳定对比损失，将图像像素映射到过完备描述符，实现视图不变性和语义意义。
3. 实验或效果：在合成2D和3D环境中进行实验，验证损失特性和过完备表示的有效性。

## 📄 摘要（原文）

> We pilot a family of stable contrastive losses for learning pixel-level representations that jointly capture semantic and geometric information. Our approach maps each pixel of an image to an overcomplete descriptor that is both view-invariant and semantically meaningful. It enables precise point-correspondence across images without requiring momentum-based teacher-student training. Two experiments in synthetic 2D and 3D environments demonstrate the properties of our loss and the resulting overcomplete representations.

