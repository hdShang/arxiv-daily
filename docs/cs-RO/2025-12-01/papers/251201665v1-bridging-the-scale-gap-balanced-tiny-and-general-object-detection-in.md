---
layout: default
title: Bridging the Scale Gap: Balanced Tiny and General Object Detection in Remote Sensing Imagery
---

# Bridging the Scale Gap: Balanced Tiny and General Object Detection in Remote Sensing Imagery

**arXiv**: [2512.01665v1](https://arxiv.org/abs/2512.01665) | [PDF](https://arxiv.org/pdf/2512.01665.pdf)

**作者**: Zhicheng Zhao, Yin Huang, Lingma Sun, Chenglong Li, Jin Tang

---

## 💡 一句话要点

**提出ScaleBridge-Det以解决遥感图像中密集微小与大型物体平衡检测的尺度差异问题**

**关键词**: `遥感图像检测` `微小物体检测` `多尺度融合` `专家路由` `查询分配` `跨域鲁棒性`

## 📋 核心要点

1. 核心问题：遥感图像中物体尺度差异大且密度分布不均，现有方法难以平衡微小与大型物体的检测性能
2. 方法要点：引入路由增强混合注意力模块动态融合多尺度专家特征，结合密度引导动态查询模块自适应分配检测资源
3. 实验或效果：在AI-TOD-V2和DTOD数据集上达到最先进性能，并在VisDrone上展示优越的跨域鲁棒性

## 📄 摘要（原文）

> Tiny object detection in remote sensing imagery has attracted significant research interest in recent years. Despite recent progress, achieving balanced detection performance across diverse object scales remains a formidable challenge, particularly in scenarios where dense tiny objects and large objects coexist. Although large foundation models have revolutionized general vision tasks, their application to tiny object detection remains unexplored due to the extreme scale variation and density distribution inherent to remote sensing imagery. To bridge this scale gap, we propose ScaleBridge-Det, to the best of our knowledge, the first large detection framework designed for tiny objects, which could achieve balanced performance across diverse scales through scale-adaptive expert routing and density-guided query allocation. Specifically, we introduce a Routing-Enhanced Mixture Attention (REM) module that dynamically selects and fuses scale-specific expert features via adaptive routing to address the tendency of standard MoE models to favor dominant scales. REM generates complementary and discriminative multi-scale representations suitable for both tiny and large objects. Furthermore, we present a Density-Guided Dynamic Query (DGQ) module that predicts object density to adaptively adjust query positions and numbers, enabling efficient resource allocation for objects of varying scales. The proposed framework allows ScaleBridge-Det to simultaneously optimize performance for both dense tiny and general objects without trade-offs. Extensive experiments on benchmark and cross-domain datasets demonstrate that ScaleBridge-Det achieves state-of-the-art performance on AI-TOD-V2 and DTOD, while exhibiting superior cross-domain robustness on VisDrone.

