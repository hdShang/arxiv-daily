---
layout: default
title: SAM-DAQ: Segment Anything Model with Depth-guided Adaptive Queries for RGB-D Video Salient Object Detection
---

# SAM-DAQ: Segment Anything Model with Depth-guided Adaptive Queries for RGB-D Video Salient Object Detection

**arXiv**: [2511.09870v1](https://arxiv.org/abs/2511.09870) | [PDF](https://arxiv.org/pdf/2511.09870.pdf)

**作者**: Jia Lin, Xiaofei Zhou, Jiyuan Liu, Runmin Cong, Guodao Zhang, Zhi Liu, Jiyong Zhang

---

## 💡 一句话要点

**提出SAM-DAQ以解决RGB-D视频显著目标检测中的提示依赖与计算负担问题**

**关键词**: `RGB-D视频显著目标检测` `Segment Anything模型` `深度引导适配器` `查询驱动时序内存` `多模态特征融合`

## 📋 核心要点

1. 核心问题：SAM直接用于RGB-D视频显著目标检测时依赖手动提示、内存消耗高且计算负担重
2. 方法要点：使用深度引导并行适配器和查询驱动时序内存模块集成深度与时间线索
3. 实验或效果：在三个RGB-D VSOD数据集上实验，所有评估指标均优于现有方法

## 📄 摘要（原文）

> Recently segment anything model (SAM) has attracted widespread concerns, and it is often treated as a vision foundation model for universal segmentation. Some researchers have attempted to directly apply the foundation model to the RGB-D video salient object detection (RGB-D VSOD) task, which often encounters three challenges, including the dependence on manual prompts, the high memory consumption of sequential adapters, and the computational burden of memory attention. To address the limitations, we propose a novel method, namely Segment Anything Model with Depth-guided Adaptive Queries (SAM-DAQ), which adapts SAM2 to pop-out salient objects from videos by seamlessly integrating depth and temporal cues within a unified framework. Firstly, we deploy a parallel adapter-based multi-modal image encoder (PAMIE), which incorporates several depth-guided parallel adapters (DPAs) in a skip-connection way. Remarkably, we fine-tune the frozen SAM encoder under prompt-free conditions, where the DPA utilizes depth cues to facilitate the fusion of multi-modal features. Secondly, we deploy a query-driven temporal memory (QTM) module, which unifies the memory bank and prompt embeddings into a learnable pipeline. Concretely, by leveraging both frame-level queries and video-level queries simultaneously, the QTM module can not only selectively extract temporal consistency features but also iteratively update the temporal representations of the queries. Extensive experiments are conducted on three RGB-D VSOD datasets, and the results show that the proposed SAM-DAQ consistently outperforms state-of-the-art methods in terms of all evaluation metrics.

