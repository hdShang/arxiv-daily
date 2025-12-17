---
layout: default
title: Zero-Shot Video Translation and Editing with Frame Spatial-Temporal Correspondence
---

# Zero-Shot Video Translation and Editing with Frame Spatial-Temporal Correspondence

**arXiv**: [2512.03905v1](https://arxiv.org/abs/2512.03905) | [PDF](https://arxiv.org/pdf/2512.03905.pdf)

**作者**: Shuai Yang, Junxin Lin, Yifan Zhou, Ziwei Liu, Chen Change Loy

---

## 💡 一句话要点

**提出FRESCO框架，通过增强时空约束解决零样本视频翻译与编辑中的时序不一致问题。**

**关键词**: `零样本学习` `视频翻译` `视频编辑` `时空一致性` `扩散模型` `特征优化`

## 📋 核心要点

1. 核心问题：现有零样本方法依赖注意力机制的软约束，导致视频处理时出现时序不一致。
2. 方法要点：结合帧内与帧间对应关系，构建更鲁棒的时空约束，优化特征以提升一致性。
3. 实验或效果：在视频到视频翻译和文本引导视频编辑任务中验证，生成高质量、连贯的视频。

## 📄 摘要（原文）

> The remarkable success in text-to-image diffusion models has motivated extensive investigation of their potential for video applications. Zero-shot techniques aim to adapt image diffusion models for videos without requiring further model training. Recent methods largely emphasize integrating inter-frame correspondence into attention mechanisms. However, the soft constraint applied to identify the valid features to attend is insufficient, which could lead to temporal inconsistency. In this paper, we present FRESCO, which integrates intra-frame correspondence with inter-frame correspondence to formulate a more robust spatial-temporal constraint. This enhancement ensures a consistent transformation of semantically similar content between frames. Our method goes beyond attention guidance to explicitly optimize features, achieving high spatial-temporal consistency with the input video, significantly enhancing the visual coherence of manipulated videos. We verify FRESCO adaptations on two zero-shot tasks of video-to-video translation and text-guided video editing. Comprehensive experiments demonstrate the effectiveness of our framework in generating high-quality, coherent videos, highlighting a significant advance over current zero-shot methods.

