---
layout: default
title: Towards an Effective Action-Region Tracking Framework for Fine-grained Video Action Recognition
---

# Towards an Effective Action-Region Tracking Framework for Fine-grained Video Action Recognition

**arXiv**: [2511.21202v1](https://arxiv.org/abs/2511.21202) | [PDF](https://arxiv.org/pdf/2511.21202.pdf)

**作者**: Baoli Sun, Yihan Wang, Xinzhu Ma, Zhihui Wang, Kun Lu, Zhiyong Wang

---

## 💡 一句话要点

**提出动作区域跟踪框架以解决细粒度视频动作识别中局部细节动态追踪问题**

**关键词**: `细粒度动作识别` `动作区域跟踪` `查询-响应机制` `视觉语言模型` `轨迹对比约束` `视频理解`

## 📋 核心要点

1. 核心问题：现有方法难以捕捉细粒度动作类别间局部区域随时间演变的细微差异
2. 方法要点：使用查询-响应机制和文本约束语义来发现并跟踪动作相关区域，形成动作轨迹
3. 实验或效果：在广泛基准测试中优于先前最先进基线，验证了框架有效性

## 📄 摘要（原文）

> Fine-grained action recognition (FGAR) aims to identify subtle and distinctive differences among fine-grained action categories. However, current recognition methods often capture coarse-grained motion patterns but struggle to identify subtle details in local regions evolving over time. In this work, we introduce the Action-Region Tracking (ART) framework, a novel solution leveraging a query-response mechanism to discover and track the dynamics of distinctive local details, enabling effective distinction of similar actions. Specifically, we propose a region-specific semantic activation module that employs discriminative and text-constrained semantics as queries to capture the most action-related region responses in each video frame, facilitating interaction among spatial and temporal dimensions with corresponding video features. The captured region responses are organized into action tracklets, which characterize region-based action dynamics by linking related responses across video frames in a coherent sequence. The text-constrained queries encode nuanced semantic representations derived from textual descriptions of action labels extracted by language branches within Visual Language Models (VLMs). To optimize the action tracklets, we design a multi-level tracklet contrastive constraint among region responses at spatial and temporal levels, enabling effective discrimination within each frame and correlation between adjacent frames. Additionally, a task-specific fine-tuning mechanism refines textual semantics such that semantic representations encoded by VLMs are preserved while optimized for task preferences. Comprehensive experiments on widely used action recognition benchmarks demonstrate the superiority to previous state-of-the-art baselines.

