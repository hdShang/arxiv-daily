---
layout: default
title: MitUNet: Enhancing Floor Plan Recognition using a Hybrid Mix-Transformer and U-Net Architecture
---

# MitUNet: Enhancing Floor Plan Recognition using a Hybrid Mix-Transformer and U-Net Architecture

**arXiv**: [2512.02413v1](https://arxiv.org/abs/2512.02413) | [PDF](https://arxiv.org/pdf/2512.02413.pdf)

**作者**: Dmitriy Parashchuk, Alexey Kapshitskiy, Yuriy Karyakin

---

## 💡 一句话要点

**提出MitUNet混合架构以解决室内平面图墙分割中薄结构检测和边界精度不足的问题**

**关键词**: `墙分割` `混合神经网络` `注意力机制` `Tversky损失` `3D重建` `平面图识别`

## 📋 核心要点

1. 核心问题：现有方法在墙分割中难以检测薄结构且边界不规则，影响3D重建精度
2. 方法要点：结合Mix-Transformer编码器捕获全局上下文，U-Net解码器加scSE注意力块恢复精确边界，使用Tversky损失优化平衡精度与召回
3. 实验或效果：在CubiCasa5k和专有数据集上验证，生成结构正确且边界高精度的掩码，优于标准单任务模型

## 📄 摘要（原文）

> Automatic 3D reconstruction of indoor spaces from 2D floor plans requires high-precision semantic segmentation of structural elements, particularly walls. However, existing methods optimized for standard metrics often struggle to detect thin structural components and yield masks with irregular boundaries, lacking the geometric precision required for subsequent vectorization. To address this issue, we introduce MitUNet, a hybrid neural network architecture specifically designed for wall segmentation tasks in the context of 3D modeling. In MitUNet, we utilize a hierarchical Mix-Transformer encoder to capture global context and a U-Net decoder enhanced with scSE attention blocks for precise boundary recovery. Furthermore, we propose an optimization strategy based on the Tversky loss function to effectively balance precision and recall. By fine-tuning the hyperparameters of the loss function, we prioritize the suppression of false positive noise along wall boundaries while maintaining high sensitivity to thin structures. Our experiments on the public CubiCasa5k dataset and a proprietary regional dataset demonstrate that the proposed approach ensures the generation of structurally correct masks with high boundary accuracy, outperforming standard single-task models. MitUNet provides a robust tool for data preparation in automated 3D reconstruction pipelines.

