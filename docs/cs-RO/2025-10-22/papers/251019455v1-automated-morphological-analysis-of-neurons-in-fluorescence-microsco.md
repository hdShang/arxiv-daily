---
layout: default
title: Automated Morphological Analysis of Neurons in Fluorescence Microscopy Using YOLOv8
---

# Automated Morphological Analysis of Neurons in Fluorescence Microscopy Using YOLOv8

**arXiv**: [2510.19455v1](https://arxiv.org/abs/2510.19455) | [PDF](https://arxiv.org/pdf/2510.19455.pdf)

**作者**: Banan Alnemri, Arwa Basbrain

---

## 💡 一句话要点

**提出基于YOLOv8的神经元形态自动分析管道，用于荧光显微镜图像。**

**关键词**: `神经元分割` `YOLOv8` `荧光显微镜` `形态分析` `实例分割`

## 📋 核心要点

1. 核心问题：荧光显微镜图像中神经元细胞分割与形态分析耗时且依赖人工。
2. 方法要点：使用YOLOv8模型在手动标注数据集上进行训练，实现实例分割。
3. 实验或效果：分割准确率超97%，形态测量准确率达75.32%。

## 📄 摘要（原文）

> Accurate segmentation and precise morphological analysis of neuronal cells in
> fluorescence microscopy images are crucial steps in neuroscience and biomedical
> imaging applications. However, this process is labor-intensive and
> time-consuming, requiring significant manual effort and expertise to ensure
> reliable outcomes. This work presents a pipeline for neuron instance
> segmentation and measurement based on a high-resolution dataset of
> stem-cell-derived neurons. The proposed method uses YOLOv8, trained on manually
> annotated microscopy images. The model achieved high segmentation accuracy,
> exceeding 97%. In addition, the pipeline utilized both ground truth and
> predicted masks to extract biologically significant features, including cell
> length, width, area, and grayscale intensity values. The overall accuracy of
> the extracted morphological measurements reached 75.32%, further supporting the
> effectiveness of the proposed approach. This integrated framework offers a
> valuable tool for automated analysis in cell imaging and neuroscience research,
> reducing the need for manual annotation and enabling scalable, precise
> quantification of neuron morphology.

