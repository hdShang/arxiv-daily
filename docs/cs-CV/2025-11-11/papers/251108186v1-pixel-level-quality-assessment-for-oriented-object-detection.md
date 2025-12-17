---
layout: default
title: Pixel-level Quality Assessment for Oriented Object Detection
---

# Pixel-level Quality Assessment for Oriented Object Detection

**arXiv**: [2511.08186v1](https://arxiv.org/abs/2511.08186) | [PDF](https://arxiv.org/pdf/2511.08186.pdf)

**作者**: Yunhui Zhu, Buliao Huang

---

## 💡 一句话要点

**提出像素级质量评估框架以解决定向目标检测中框级IoU预测的结构耦合问题**

**关键词**: `定向目标检测` `像素级质量评估` `空间一致性` `IoU预测` `检测器集成`

## 📋 核心要点

1. 定向目标检测中框级IoU预测存在结构耦合，导致定位质量被高估
2. PQA通过像素级空间一致性评估，避免直接比较预测框与估计真值框
3. 实验显示PQA可集成多种检测器，提升性能如Rotated RetinaNet AP增加5.96%

## 📄 摘要（原文）

> Modern oriented object detectors typically predict a set of bounding boxes and select the top-ranked ones based on estimated localization quality. Achieving high detection performance requires that the estimated quality closely aligns with the actual localization accuracy. To this end, existing approaches predict the Intersection over Union (IoU) between the predicted and ground-truth (GT) boxes as a proxy for localization quality. However, box-level IoU prediction suffers from a structural coupling issue: since the predicted box is derived from the detector's internal estimation of the GT box, the predicted IoU--based on their similarity--can be overestimated for poorly localized boxes. To overcome this limitation, we propose a novel Pixel-level Quality Assessment (PQA) framework, which replaces box-level IoU prediction with the integration of pixel-level spatial consistency. PQA measures the alignment between each pixel's relative position to the predicted box and its corresponding position to the GT box. By operating at the pixel level, PQA avoids directly comparing the predicted box with the estimated GT box, thereby eliminating the inherent similarity bias in box-level IoU prediction. Furthermore, we introduce a new integration metric that aggregates pixel-level spatial consistency into a unified quality score, yielding a more accurate approximation of the actual localization quality. Extensive experiments on HRSC2016 and DOTA demonstrate that PQA can be seamlessly integrated into various oriented object detectors, consistently improving performance (e.g., +5.96% AP$_{50:95}$ on Rotated RetinaNet and +2.32% on STD).

