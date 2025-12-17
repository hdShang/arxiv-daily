---
layout: default
title: Automated Tennis Player and Ball Tracking with Court Keypoints Detection (Hawk Eye System)
---

# Automated Tennis Player and Ball Tracking with Court Keypoints Detection (Hawk Eye System)

**arXiv**: [2511.04126v1](https://arxiv.org/abs/2511.04126) | [PDF](https://arxiv.org/pdf/2511.04126.pdf)

**作者**: Venkata Manikanta Desu, Syed Fawaz Ali

---

## 💡 一句话要点

**提出自动化网球分析框架，集成多模型检测追踪球员、球和球场关键点。**

**关键词**: `球员检测` `球追踪` `球场关键点检测` `实时分析` `深度学习模型` `性能指标`

## 📋 核心要点

1. 核心问题：自动化网球比赛分析，实时检测追踪球员、球和球场空间参考。
2. 方法要点：使用YOLOv8检测球员，YOLOv5追踪球，ResNet50检测球场关键点。
3. 实验或效果：在多变球场条件下表现稳健，输出注释视频和详细性能指标。

## 📄 摘要（原文）

> This study presents a complete pipeline for automated tennis match analysis.
> Our framework integrates multiple deep learning models to detect and track
> players and the tennis ball in real time, while also identifying court
> keypoints for spatial reference. Using YOLOv8 for player detection, a
> custom-trained YOLOv5 model for ball tracking, and a ResNet50-based
> architecture for court keypoint detection, our system provides detailed
> analytics including player movement patterns, ball speed, shot accuracy, and
> player reaction times. The experimental results demonstrate robust performance
> in varying court conditions and match scenarios. The model outputs an annotated
> video along with detailed performance metrics, enabling coaches, broadcasters,
> and players to gain actionable insights into the dynamics of the game.

