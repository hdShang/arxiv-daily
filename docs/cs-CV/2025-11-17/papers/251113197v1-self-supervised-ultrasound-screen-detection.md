---
layout: default
title: Self-Supervised Ultrasound Screen Detection
---

# Self-Supervised Ultrasound Screen Detection

**arXiv**: [2511.13197v1](https://arxiv.org/abs/2511.13197) | [PDF](https://arxiv.org/pdf/2511.13197.pdf)

**作者**: Alberto Gomez, Jorge Oliveira, Ramon Casero, Agis Chartsias

---

## 💡 一句话要点

**提出自监督超声屏幕检测方法，从显示器照片提取图像以绕过DICOM瓶颈。**

**关键词**: `超声图像处理` `自监督学习` `屏幕检测` `图像校正` `医学影像分析`

## 📋 核心要点

1. 核心问题：超声图像依赖DICOM传输，存在效率瓶颈，影响算法测试与原型开发。
2. 方法要点：设计自监督流程，从显示器照片中提取并校正超声图像，无需人工标注。
3. 实验或效果：校正图像视觉保真度高，心脏视图分类平衡准确率达0.79，接近原生DICOM。

## 📄 摘要（原文）

> Ultrasound (US) machines display images on a built-in monitor, but routine transfer to hospital systems relies on DICOM. We propose a self-supervised pipeline to extract the US image from a photograph of the monitor. This removes the DICOM bottleneck and enables rapid testing and prototyping of new algorithms. In a proof-of-concept study, the rectified images retained enough visual fidelity to classify cardiac views with a balanced accuracy of 0.79 with respect to the native DICOMs.

