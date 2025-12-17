---
layout: default
title: Enhancing Maritime Domain Awareness on Inland Waterways: A YOLO-Based Fusion of Satellite and AIS for Vessel Characterization
---

# Enhancing Maritime Domain Awareness on Inland Waterways: A YOLO-Based Fusion of Satellite and AIS for Vessel Characterization

**arXiv**: [2510.11449v1](https://arxiv.org/abs/2510.11449) | [PDF](https://arxiv.org/pdf/2510.11449.pdf)

**作者**: Geoffery Agorku, Sarah Hernandez, Hayley Hames, Cade Wagner

---

## 💡 一句话要点

**提出基于YOLO的卫星与AIS融合框架，以增强内河海事感知能力。**

**关键词**: `目标检测` `数据融合` `海事感知` `卫星图像` `AIS数据` `YOLO模型`

## 📋 核心要点

1. 核心问题：内河海事感知受限于合作系统漏洞，难以监测非合作船只。
2. 方法要点：融合高分辨率卫星图像与AIS轨迹数据，使用YOLO v11检测和表征船只。
3. 实验或效果：在测试集上，船只分类F1达95.8%，空间可转移性高达98%。

## 📄 摘要（原文）

> Maritime Domain Awareness (MDA) for inland waterways remains challenged by
> cooperative system vulnerabilities. This paper presents a novel framework that
> fuses high-resolution satellite imagery with vessel trajectory data from the
> Automatic Identification System (AIS). This work addresses the limitations of
> AIS-based monitoring by leveraging non-cooperative satellite imagery and
> implementing a fusion approach that links visual detections with AIS data to
> identify dark vessels, validate cooperative traffic, and support advanced MDA.
> The You Only Look Once (YOLO) v11 object detection model is used to detect and
> characterize vessels and barges by vessel type, barge cover, operational
> status, barge count, and direction of travel. An annotated data set of 4,550
> instances was developed from $5{,}973~\mathrm{mi}^2$ of Lower Mississippi River
> imagery. Evaluation on a held-out test set demonstrated vessel classification
> (tugboat, crane barge, bulk carrier, cargo ship, and hopper barge) with an F1
> score of 95.8\%; barge cover (covered or uncovered) detection yielded an F1
> score of 91.6\%; operational status (staged or in motion) classification
> reached an F1 score of 99.4\%. Directionality (upstream, downstream) yielded
> 93.8\% accuracy. The barge count estimation resulted in a mean absolute error
> (MAE) of 2.4 barges. Spatial transferability analysis across geographically
> disjoint river segments showed accuracy was maintained as high as 98\%. These
> results underscore the viability of integrating non-cooperative satellite
> sensing with AIS fusion. This approach enables near-real-time fleet
> inventories, supports anomaly detection, and generates high-quality data for
> inland waterway surveillance. Future work will expand annotated datasets,
> incorporate temporal tracking, and explore multi-modal deep learning to further
> enhance operational scalability.

