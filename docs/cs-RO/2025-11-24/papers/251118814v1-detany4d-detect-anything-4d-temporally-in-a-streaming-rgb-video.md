---
layout: default
title: DetAny4D: Detect Anything 4D Temporally in a Streaming RGB Video
---

# DetAny4D: Detect Anything 4D Temporally in a Streaming RGB Video

**arXiv**: [2511.18814v1](https://arxiv.org/abs/2511.18814) | [PDF](https://arxiv.org/pdf/2511.18814.pdf)

**作者**: Jiawei Hou, Shenghao Zhang, Can Wang, Zheng Gu, Yonggen Ling, Taiping Zeng, Xiangyang Xue, Jingbo Zhang

---

## 💡 一句话要点

**提出DetAny4D端到端框架以解决流视频中4D物体检测的时序一致性问题**

**关键词**: `4D物体检测` `流视频分析` `时空建模` `多模态融合` `端到端学习` `时序一致性`

## 📋 核心要点

1. 核心问题：现有4D检测方法缺乏时序建模，且依赖多阶段流程易导致误差传播
2. 方法要点：融合多模态特征，设计几何感知时空解码器，采用多任务学习策略
3. 实验或效果：在DA4D数据集上验证，检测精度高且显著提升时序稳定性

## 📄 摘要（原文）

> Reliable 4D object detection, which refers to 3D object detection in streaming video, is crucial for perceiving and understanding the real world. Existing open-set 4D object detection methods typically make predictions on a frame-by-frame basis without modeling temporal consistency, or rely on complex multi-stage pipelines that are prone to error propagation across cascaded stages. Progress in this area has been hindered by the lack of large-scale datasets that capture continuous reliable 3D bounding box (b-box) annotations. To overcome these challenges, we first introduce DA4D, a large-scale 4D detection dataset containing over 280k sequences with high-quality b-box annotations collected under diverse conditions. Building on DA4D, we propose DetAny4D, an open-set end-to-end framework that predicts 3D b-boxes directly from sequential inputs. DetAny4D fuses multi-modal features from pre-trained foundational models and designs a geometry-aware spatiotemporal decoder to effectively capture both spatial and temporal dynamics. Furthermore, it adopts a multi-task learning architecture coupled with a dedicated training strategy to maintain global consistency across sequences of varying lengths. Extensive experiments show that DetAny4D achieves competitive detection accuracy and significantly improves temporal stability, effectively addressing long-standing issues of jitter and inconsistency in 4D object detection. Data and code will be released upon acceptance.

