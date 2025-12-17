---
layout: default
title: UniGeoSeg: Towards Unified Open-World Segmentation for Geospatial Scenes
---

# UniGeoSeg: Towards Unified Open-World Segmentation for Geospatial Scenes

**arXiv**: [2511.23332v1](https://arxiv.org/abs/2511.23332) | [PDF](https://arxiv.org/pdf/2511.23332.pdf)

**作者**: Shuo Ni, Di Wang, He Chen, Haonan Guo, Ning Zhang, Jing Zhang

---

## 💡 一句话要点

**提出UniGeoSeg统一框架，解决遥感指令驱动分割任务碎片化和数据不足问题。**

**关键词**: `遥感图像分割` `指令驱动学习` `多任务学习` `零样本泛化` `大规模数据集`

## 📋 核心要点

1. 核心问题：现有遥感指令驱动分割方法任务碎片化且数据有限，阻碍理解和泛化。
2. 方法要点：构建GeoSeg-1M百万级数据集，并设计UniGeoSeg框架，集成任务感知文本增强和渐进训练。
3. 实验或效果：在GeoSeg-Bench和公共基准上实现先进性能，展示强零样本泛化能力。

## 📄 摘要（原文）

> Instruction-driven segmentation in remote sensing generates masks from guidance, offering great potential for accessible and generalizable applications. However, existing methods suffer from fragmented task formulations and limited instruction data, hindering effective understanding and generalization. To address these issues, we introduce GeoSeg-1M, the first million-scale dataset for remote sensing instruction-driven segmentation, constructed via an automatic mask filtering and instruction generation pipeline that synthesizes referring, interactive, and reasoning segmentation instructions from multiple public datasets. GeoSeg-1M contains 590K images, 117 categories, and 1.1M image-mask-instruction triplets. Building upon this foundation, we further curate GeoSeg-Bench, a challenging benchmark designed to evaluate contextual understanding and reasoning capabilities across diverse instruction-driven tasks and complex geospatial scenes. Furthermore, we present UniGeoSeg, a unified framework that serves as a strong baseline, incorporating task-aware text enhancement, latent knowledge memory, and a progressive training strategy to facilitate multi-task learning. Extensive experiments demonstrate the state-of-the-art performance of UniGeoSeg across GeoSeg-Bench and diverse public benchmarks, while exhibiting strong zero-shot generalization. Datasets and source code were released at https://github.com/MiliLab/UniGeoSeg.

