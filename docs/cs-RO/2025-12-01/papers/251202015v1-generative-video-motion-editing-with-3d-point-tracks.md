---
layout: default
title: Generative Video Motion Editing with 3D Point Tracks
---

# Generative Video Motion Editing with 3D Point Tracks

**arXiv**: [2512.02015v1](https://arxiv.org/abs/2512.02015) | [PDF](https://arxiv.org/pdf/2512.02015.pdf)

**作者**: Yao-Chih Lee, Zhoutong Zhang, Jiahui Huang, Jui-Hsien Wang, Joon-Young Lee, Jia-Bin Huang, Eli Shechtman, Zhengqi Li

---

## 💡 一句话要点

**提出基于3D点轨迹的视频生成框架，以联合编辑相机与物体运动**

**关键词**: `视频运动编辑` `3D点轨迹` `视频生成模型` `时空一致性` `深度线索`

## 📋 核心要点

1. 核心问题：现有视频运动编辑方法缺乏全场景上下文，难以精确控制细粒度物体运动
2. 方法要点：利用3D点轨迹作为条件，提供深度线索以处理遮挡和保持时空一致性
3. 实验或效果：在合成和真实数据上两阶段训练，支持相机/物体联合操纵、运动转移和非刚性变形

## 📄 摘要（原文）

> Camera and object motions are central to a video's narrative. However, precisely editing these captured motions remains a significant challenge, especially under complex object movements. Current motion-controlled image-to-video (I2V) approaches often lack full-scene context for consistent video editing, while video-to-video (V2V) methods provide viewpoint changes or basic object translation, but offer limited control over fine-grained object motion. We present a track-conditioned V2V framework that enables joint editing of camera and object motion. We achieve this by conditioning a video generation model on a source video and paired 3D point tracks representing source and target motions. These 3D tracks establish sparse correspondences that transfer rich context from the source video to new motions while preserving spatiotemporal coherence. Crucially, compared to 2D tracks, 3D tracks provide explicit depth cues, allowing the model to resolve depth order and handle occlusions for precise motion editing. Trained in two stages on synthetic and real data, our model supports diverse motion edits, including joint camera/object manipulation, motion transfer, and non-rigid deformation, unlocking new creative potential in video editing.

