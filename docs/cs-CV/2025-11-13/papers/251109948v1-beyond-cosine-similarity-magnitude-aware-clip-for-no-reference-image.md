---
layout: default
title: Beyond Cosine Similarity Magnitude-Aware CLIP for No-Reference Image Quality Assessment
---

# Beyond Cosine Similarity Magnitude-Aware CLIP for No-Reference Image Quality Assessment

**arXiv**: [2511.09948v1](https://arxiv.org/abs/2511.09948) | [PDF](https://arxiv.org/pdf/2511.09948.pdf)

**作者**: Zhicheng Liao, Dongxu Wu, Zhenshan Shi, Sijie Mai, Hanwei Zhu, Lingyu Zhu, Yuncheng Jiang, Baoliang Chen

---

## 💡 一句话要点

**提出自适应融合框架，结合余弦相似度与特征幅度，提升无参考图像质量评估性能。**

**关键词**: `无参考图像质量评估` `CLIP模型` `特征幅度` `自适应融合` `Box-Cox变换` `余弦相似度`

## 📋 核心要点

1. 核心问题：CLIP模型用于NR-IQA时，仅依赖语义相似度，忽略图像特征幅度与感知质量的相关性。
2. 方法要点：提取CLIP图像特征绝对幅度，应用Box-Cox变换归一化，并与余弦相似度自适应融合。
3. 实验或效果：在多个IQA基准数据集上，无需任务特定训练，性能优于现有方法。

## 📄 摘要（原文）

> Recent efforts have repurposed the Contrastive Language-Image Pre-training (CLIP) model for No-Reference Image Quality Assessment (NR-IQA) by measuring the cosine similarity between the image embedding and textual prompts such as "a good photo" or "a bad photo." However, this semantic similarity overlooks a critical yet underexplored cue: the magnitude of the CLIP image features, which we empirically find to exhibit a strong correlation with perceptual quality. In this work, we introduce a novel adaptive fusion framework that complements cosine similarity with a magnitude-aware quality cue. Specifically, we first extract the absolute CLIP image features and apply a Box-Cox transformation to statistically normalize the feature distribution and mitigate semantic sensitivity. The resulting scalar summary serves as a semantically-normalized auxiliary cue that complements cosine-based prompt matching. To integrate both cues effectively, we further design a confidence-guided fusion scheme that adaptively weighs each term according to its relative strength. Extensive experiments on multiple benchmark IQA datasets demonstrate that our method consistently outperforms standard CLIP-based IQA and state-of-the-art baselines, without any task-specific training.

