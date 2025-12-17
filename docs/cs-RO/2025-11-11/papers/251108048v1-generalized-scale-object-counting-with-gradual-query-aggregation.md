---
layout: default
title: Generalized-Scale Object Counting with Gradual Query Aggregation
---

# Generalized-Scale Object Counting with Gradual Query Aggregation

**arXiv**: [2511.08048v1](https://arxiv.org/abs/2511.08048) | [PDF](https://arxiv.org/pdf/2511.08048.pdf)

**作者**: Jer Pelhan, Alan Lukezic, Matej Kristan

---

## 💡 一句话要点

**提出GECO2方法以解决多尺度与密集小物体计数问题**

**关键词**: `少样本计数` `多尺度检测` `渐进查询聚合` `密集物体检测` `端到端学习`

## 📋 核心要点

1. 核心问题：现有计数器难以处理多尺度物体和密集小物体区域
2. 方法要点：使用渐进查询聚合跨尺度特征，生成高分辨率密集查询
3. 实验或效果：计数与检测精度提升10%，速度提高3倍，内存占用更小

## 📄 摘要（原文）

> Few-shot detection-based counters estimate the number of instances in the image specified only by a few test-time exemplars. A common approach to localize objects across multiple sizes is to merge backbone features of different resolutions. Furthermore, to enable small object detection in densely populated regions, the input image is commonly upsampled and tiling is applied to cope with the increased computational and memory requirements. Because of these ad-hoc solutions, existing counters struggle with images containing diverse-sized objects and densely populated regions of small objects. We propose GECO2, an end-to-end few-shot counting and detection method that explicitly addresses the object scale issues. A new dense query representation gradually aggregates exemplar-specific feature information across scales that leads to high-resolution dense queries that enable detection of large as well as small objects. GECO2 surpasses state-of-the-art few-shot counters in counting as well as detection accuracy by 10% while running 3x times faster at smaller GPU memory footprint.

