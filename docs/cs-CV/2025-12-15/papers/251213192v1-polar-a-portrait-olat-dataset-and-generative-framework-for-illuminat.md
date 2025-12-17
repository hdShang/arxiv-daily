---
layout: default
title: POLAR: A Portrait OLAT Dataset and Generative Framework for Illumination-Aware Face Modeling
---

# POLAR: A Portrait OLAT Dataset and Generative Framework for Illumination-Aware Face Modeling

**arXiv**: [2512.13192v1](https://arxiv.org/abs/2512.13192) | [PDF](https://arxiv.org/pdf/2512.13192.pdf)

**作者**: Zhuo Chen, Chengqun Yang, Zhuo Su, Zheng Lv, Jingnan Gao, Xiaoyuan Zhang, Xiaokang Yang, Yichao Yan

---

## 💡 一句话要点

**提出POLAR数据集与POLARNet模型以解决人脸重光照中大规模物理一致数据不足的问题**

**关键词**: `人脸重光照` `OLAT数据集` `流式生成模型` `物理一致光照` `肖像建模` `光照学习框架`

## 📋 核心要点

1. 核心问题：人脸重光照受限于大规模、物理一致的光照数据可用性
2. 方法要点：基于POLAR数据集开发流式生成模型POLARNet，从单张肖像预测每光OLAT响应
3. 实验或效果：模型能捕捉细粒度方向感知光照效果，保持身份，实现可扩展可控重光照

## 📄 摘要（原文）

> Face relighting aims to synthesize realistic portraits under novel illumination while preserving identity and geometry. However, progress remains constrained by the limited availability of large-scale, physically consistent illumination data. To address this, we introduce POLAR, a large-scale and physically calibrated One-Light-at-a-Time (OLAT) dataset containing over 200 subjects captured under 156 lighting directions, multiple views, and diverse expressions. Building upon POLAR, we develop a flow-based generative model POLARNet that predicts per-light OLAT responses from a single portrait, capturing fine-grained and direction-aware illumination effects while preserving facial identity. Unlike diffusion or background-conditioned methods that rely on statistical or contextual cues, our formulation models illumination as a continuous, physically interpretable transformation between lighting states, enabling scalable and controllable relighting. Together, POLAR and POLARNet form a unified illumination learning framework that links real data, generative synthesis, and physically grounded relighting, establishing a self-sustaining "chicken-and-egg" cycle for scalable and reproducible portrait illumination.

