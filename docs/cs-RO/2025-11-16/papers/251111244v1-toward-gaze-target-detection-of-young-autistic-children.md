---
layout: default
title: Toward Gaze Target Detection of Young Autistic Children
---

# Toward Gaze Target Detection of Young Autistic Children

**arXiv**: [2511.11244v1](https://arxiv.org/abs/2511.11244) | [PDF](https://arxiv.org/pdf/2511.11244.pdf)

**作者**: Shijian Deng, Erin E. Kosloski, Siva Sai Nagender Vasireddy, Jia Li, Randi Sierra Sherwood, Feroz Mohamed Hatha, Siddhi Patel, Pamela R Rollins, Yapeng Tian

---

## 💡 一句话要点

**提出SACF框架以解决自闭症儿童注视目标检测中的类别不平衡问题**

**关键词**: `注视目标检测` `自闭症谱系障碍` `类别不平衡` `上下文感知` `双路径架构` `AGT数据集`

## 📋 核心要点

1. 核心问题：自闭症儿童注视目标检测中类别不平衡，因较少注视面部导致数据偏差。
2. 方法要点：采用双路径架构，结合社交与非社交专家模型，通过上下文感知门模块优化。
3. 实验或效果：在AGT数据集上实现SOTA性能，显著提升面部注视类别的检测准确率。

## 📄 摘要（原文）

> The automatic detection of gaze targets in autistic children through artificial intelligence can be impactful, especially for those who lack access to a sufficient number of professionals to improve their quality of life. This paper introduces a new, real-world AI application for gaze target detection in autistic children, which predicts a child's point of gaze from an activity image. This task is foundational for building automated systems that can measure joint attention-a core challenge in Autism Spectrum Disorder (ASD). To facilitate the study of this challenging application, we collected the first-ever Autism Gaze Target (AGT) dataset. We further propose a novel Socially Aware Coarse-to-Fine (SACF) gaze detection framework that explicitly leverages the social context of a scene to overcome the class imbalance common in autism datasets-a consequence of autistic children's tendency to show reduced gaze to faces. It utilizes a two-pathway architecture with expert models specialized in social and non-social gaze, guided by a context-awareness gate module. The results of our comprehensive experiments demonstrate that our framework achieves new state-of-the-art performance for gaze target detection in this population, significantly outperforming existing methods, especially on the critical minority class of face-directed gaze.

