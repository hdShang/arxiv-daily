---
layout: default
title: Unlocking Zero-Shot Plant Segmentation with Pl@ntNet Intelligence
---

# Unlocking Zero-Shot Plant Segmentation with Pl@ntNet Intelligence

**arXiv**: [2510.12579v1](https://arxiv.org/abs/2510.12579) | [PDF](https://arxiv.org/pdf/2510.12579.pdf)

**作者**: Simon Ravé, Jean-Christophe Lombardo, Pejman Rasti, Alexis Joly, David Rousseau

---

## 💡 一句话要点

**提出零样本植物分割方法，结合PlantNet与SAM解决农业图像分割问题**

**关键词**: `零样本分割` `植物图像分析` `农业计算机视觉` `基础模型融合` `掩码细化`

## 📋 核心要点

1. 核心问题：农业图像分割中标注数据稀缺，监督方法在复杂场景下性能受限
2. 方法要点：利用PlantNet模型生成粗分割掩码，再通过SAM进行精细化处理
3. 实验或效果：在多个数据集上评估，PlantNet微调DinoV2相比基础模型IoU提升

## 📄 摘要（原文）

> We present a zero-shot segmentation approach for agricultural imagery that
> leverages Plantnet, a large-scale plant classification model, in conjunction
> with its DinoV2 backbone and the Segment Anything Model (SAM). Rather than
> collecting and annotating new datasets, our method exploits Plantnet's
> specialized plant representations to identify plant regions and produce coarse
> segmentation masks. These masks are then refined by SAM to yield detailed
> segmentations. We evaluate on four publicly available datasets of various
> complexity in terms of contrast including some where the limited size of the
> training data and complex field conditions often hinder purely supervised
> methods. Our results show consistent performance gains when using
> Plantnet-fine-tuned DinoV2 over the base DinoV2 model, as measured by the
> Jaccard Index (IoU). These findings highlight the potential of combining
> foundation models with specialized plant-centric models to alleviate the
> annotation bottleneck and enable effective segmentation in diverse agricultural
> scenarios.

