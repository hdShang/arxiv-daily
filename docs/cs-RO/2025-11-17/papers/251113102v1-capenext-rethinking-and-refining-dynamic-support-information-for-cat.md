---
layout: default
title: CapeNext: Rethinking and refining dynamic support information for category-agnostic pose estimation
---

# CapeNext: Rethinking and refining dynamic support information for category-agnostic pose estimation

**arXiv**: [2511.13102v1](https://arxiv.org/abs/2511.13102) | [PDF](https://arxiv.org/pdf/2511.13102.pdf)

**作者**: Yu Zhu, Dan Zeng, Shuiwang Li, Qijun Zhao, Qiaomu Shen, Bo Tang

---

## 💡 一句话要点

**提出CapeNext框架，通过动态支持信息解决类别无关姿态估计中的语义歧义和细粒度差异问题。**

**关键词**: `类别无关姿态估计` `跨模态交互` `特征精炼` `语义嵌入` `姿态匹配`

## 📋 核心要点

1. 核心问题：静态关节嵌入存在跨类别语义歧义和细粒度变化区分不足。
2. 方法要点：集成层次跨模态交互与双流特征精炼，增强关节嵌入。
3. 实验效果：在MP-100数据集上大幅超越现有方法，不依赖网络骨干。

## 📄 摘要（原文）

> Recent research in Category-Agnostic Pose Estimation (CAPE) has adopted fixed textual keypoint description as semantic prior for two-stage pose matching frameworks. While this paradigm enhances robustness and flexibility by disentangling the dependency of support images, our critical analysis reveals two inherent limitations of static joint embedding: (1) polysemy-induced cross-category ambiguity during the matching process(e.g., the concept "leg" exhibiting divergent visual manifestations across humans and furniture), and (2) insufficient discriminability for fine-grained intra-category variations (e.g., posture and fur discrepancies between a sleeping white cat and a standing black cat). To overcome these challenges, we propose a new framework that innovatively integrates hierarchical cross-modal interaction with dual-stream feature refinement, enhancing the joint embedding with both class-level and instance-specific cues from textual description and specific images. Experiments on the MP-100 dataset demonstrate that, regardless of the network backbone, CapeNext consistently outperforms state-of-the-art CAPE methods by a large margin.

