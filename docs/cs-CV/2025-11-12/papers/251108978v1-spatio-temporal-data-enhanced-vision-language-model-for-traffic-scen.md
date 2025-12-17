---
layout: default
title: Spatio-Temporal Data Enhanced Vision-Language Model for Traffic Scene Understanding
---

# Spatio-Temporal Data Enhanced Vision-Language Model for Traffic Scene Understanding

**arXiv**: [2511.08978v1](https://arxiv.org/abs/2511.08978) | [PDF](https://arxiv.org/pdf/2511.08978.pdf)

**作者**: Jingtian Ma, Jingyuan Wang, Wayne Xin Zhao, Guoping Liu, Xiang Wen

---

## 💡 一句话要点

**提出ST-CLIP模型以解决交通场景理解中时空信息缺失问题**

**关键词**: `交通场景理解` `时空数据增强` `视觉语言模型` `提示学习` `少样本学习`

## 📋 核心要点

1. 核心问题：交通场景理解依赖时空和视觉文本数据，现有方法常忽略时空信息
2. 方法要点：基于CLIP设计SCAMP提示学习，集成时空上下文表示到词嵌入
3. 实验或效果：在真实数据集上，少样本学习策略下表现优越

## 📄 摘要（原文）

> Nowadays, navigation and ride-sharing apps have collected numerous images with spatio-temporal data. A core technology for analyzing such images, associated with spatiotemporal information, is Traffic Scene Understanding (TSU), which aims to provide a comprehensive description of the traffic scene. Unlike traditional spatio-temporal data analysis tasks, the dependence on both spatio-temporal and visual-textual data introduces distinct challenges to TSU task. However, recent research often treats TSU as a common image understanding task, ignoring the spatio-temporal information and overlooking the interrelations between different aspects of the traffic scene. To address these issues, we propose a novel SpatioTemporal Enhanced Model based on CILP (ST-CLIP) for TSU. Our model uses the classic vision-language model, CLIP, as the backbone, and designs a Spatio-temporal Context Aware Multiaspect Prompt (SCAMP) learning method to incorporate spatiotemporal information into TSU. The prompt learning method consists of two components: A dynamic spatio-temporal context representation module that extracts representation vectors of spatio-temporal data for each traffic scene image, and a bi-level ST-aware multi-aspect prompt learning module that integrates the ST-context representation vectors into word embeddings of prompts for the CLIP model. The second module also extracts low-level visual features and image-wise high-level semantic features to exploit interactive relations among different aspects of traffic scenes. To the best of our knowledge, this is the first attempt to integrate spatio-temporal information into visionlanguage models to facilitate TSU task. Experiments on two realworld datasets demonstrate superior performance in the complex scene understanding scenarios with a few-shot learning strategy.

