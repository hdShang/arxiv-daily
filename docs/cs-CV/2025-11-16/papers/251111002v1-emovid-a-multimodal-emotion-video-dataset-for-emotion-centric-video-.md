---
layout: default
title: EmoVid: A Multimodal Emotion Video Dataset for Emotion-Centric Video Understanding and Generation
---

# EmoVid: A Multimodal Emotion Video Dataset for Emotion-Centric Video Understanding and Generation

**arXiv**: [2511.11002v1](https://arxiv.org/abs/2511.11002) | [PDF](https://arxiv.org/pdf/2511.11002.pdf)

**作者**: Zongyang Qiu, Bingyuan Wang, Xingbei Chen, Yingqing He, Zeyu Wang

---

## 💡 一句话要点

**提出EmoVid数据集和情感条件视频生成方法以解决视频生成中情感维度缺失问题**

**关键词**: `情感视频数据集` `多模态标注` `情感条件生成` `视频生成技术` `视觉情感分析`

## 📋 核心要点

1. 核心问题：现有视频生成系统忽视情感维度，缺乏情感理解与生成任务的桥梁资源
2. 方法要点：构建多模态情感标注视频数据集，并基于Wan2.1模型开发情感条件视频生成技术
3. 实验或效果：在文本到视频和图像到视频任务中，定量指标和视觉质量显著提升

## 📄 摘要（原文）

> Emotion plays a pivotal role in video-based expression, but existing video generation systems predominantly focus on low-level visual metrics while neglecting affective dimensions. Although emotion analysis has made progress in the visual domain, the video community lacks dedicated resources to bridge emotion understanding with generative tasks, particularly for stylized and non-realistic contexts. To address this gap, we introduce EmoVid, the first multimodal, emotion-annotated video dataset specifically designed for creative media, which includes cartoon animations, movie clips, and animated stickers. Each video is annotated with emotion labels, visual attributes (brightness, colorfulness, hue), and text captions. Through systematic analysis, we uncover spatial and temporal patterns linking visual features to emotional perceptions across diverse video forms. Building on these insights, we develop an emotion-conditioned video generation technique by fine-tuning the Wan2.1 model. The results show a significant improvement in both quantitative metrics and the visual quality of generated videos for text-to-video and image-to-video tasks. EmoVid establishes a new benchmark for affective video computing. Our work not only offers valuable insights into visual emotion analysis in artistically styled videos, but also provides practical methods for enhancing emotional expression in video generation.

