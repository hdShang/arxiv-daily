---
layout: default
title: 3-Tracer: A Tri-level Temporal-Aware Framework for Audio Forgery Detection and Localization
---

# 3-Tracer: A Tri-level Temporal-Aware Framework for Audio Forgery Detection and Localization

**arXiv**: [2511.21237v1](https://arxiv.org/abs/2511.21237) | [PDF](https://arxiv.org/pdf/2511.21237.pdf)

**作者**: Shuhan Xia, Xuannan Liu, Xing Cui, Peipei Li

---

## 💡 一句话要点

**提出T3-Tracer框架以解决部分音频伪造检测与定位问题**

**关键词**: `音频伪造检测` `多级时间分析` `帧级特征聚合` `段级异常检测` `伪造定位`

## 📋 核心要点

1. 核心问题：部分音频伪造难以检测，因攻击者仅修改关键帧而保持整体感知真实
2. 方法要点：联合分析帧、段和音频级，使用FA-FAM和SMDAM模块捕获多级异常
3. 实验或效果：在三个数据集上实现先进性能，验证框架有效性

## 📄 摘要（原文）

> Recently, partial audio forgery has emerged as a new form of audio manipulation. Attackers selectively modify partial but semantically critical frames while preserving the overall perceptual authenticity, making such forgeries particularly difficult to detect. Existing methods focus on independently detecting whether a single frame is forged, lacking the hierarchical structure to capture both transient and sustained anomalies across different temporal levels. To address these limitations, We identify three key levels relevant to partial audio forgery detection and present T3-Tracer, the first framework that jointly analyzes audio at the frame, segment, and audio levels to comprehensively detect forgery traces. T3-Tracer consists of two complementary core modules: the Frame-Audio Feature Aggregation Module (FA-FAM) and the Segment-level Multi-Scale Discrepancy-Aware Module (SMDAM). FA-FAM is designed to detect the authenticity of each audio frame. It combines both frame-level and audio-level temporal information to detect intra-frame forgery cues and global semantic inconsistencies. To further refine and correct frame detection, we introduce SMDAM to detect forgery boundaries at the segment level. It adopts a dual-branch architecture that jointly models frame features and inter-frame differences across multi-scale temporal windows, effectively identifying abrupt anomalies that appeared on the forged boundaries. Extensive experiments conducted on three challenging datasets demonstrate that our approach achieves state-of-the-art performance.

