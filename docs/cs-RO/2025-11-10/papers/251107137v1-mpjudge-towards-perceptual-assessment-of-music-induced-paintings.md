---
layout: default
title: MPJudge: Towards Perceptual Assessment of Music-Induced Paintings
---

# MPJudge: Towards Perceptual Assessment of Music-Induced Paintings

**arXiv**: [2511.07137v1](https://arxiv.org/abs/2511.07137) | [PDF](https://arxiv.org/pdf/2511.07137.pdf)

**作者**: Shiqi Jiang, Tianyi Liang, Changbo Wang, Chenhui Li

---

## 💡 一句话要点

**提出MPJudge框架以解决音乐诱导绘画的感知评估问题**

**关键词**: `音乐诱导绘画` `感知评估` `多模态融合` `直接偏好优化` `数据集构建`

## 📋 核心要点

1. 核心问题：评估绘画是否忠实反映音乐，现有方法依赖情感识别引入噪声且忽略更广感知线索
2. 方法要点：构建MPD数据集，采用调制融合机制整合音乐特征到视觉编码器，并使用直接偏好优化训练
3. 实验或效果：实验显示方法优于现有方法，定性结果更准确识别绘画中音乐相关区域

## 📄 摘要（原文）

> Music induced painting is a unique artistic practice, where visual artworks
> are created under the influence of music. Evaluating whether a painting
> faithfully reflects the music that inspired it poses a challenging perceptual
> assessment task. Existing methods primarily rely on emotion recognition models
> to assess the similarity between music and painting, but such models introduce
> considerable noise and overlook broader perceptual cues beyond emotion. To
> address these limitations, we propose a novel framework for music induced
> painting assessment that directly models perceptual coherence between music and
> visual art. We introduce MPD, the first large scale dataset of music painting
> pairs annotated by domain experts based on perceptual coherence. To better
> handle ambiguous cases, we further collect pairwise preference annotations.
> Building on this dataset, we present MPJudge, a model that integrates music
> features into a visual encoder via a modulation based fusion mechanism. To
> effectively learn from ambiguous cases, we adopt Direct Preference Optimization
> for training. Extensive experiments demonstrate that our method outperforms
> existing approaches. Qualitative results further show that our model more
> accurately identifies music relevant regions in paintings.

