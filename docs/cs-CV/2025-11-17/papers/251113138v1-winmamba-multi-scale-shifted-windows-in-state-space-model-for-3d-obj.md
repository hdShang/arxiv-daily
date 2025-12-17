---
layout: default
title: WinMamba: Multi-Scale Shifted Windows in State Space Model for 3D Object Detection
---

# WinMamba: Multi-Scale Shifted Windows in State Space Model for 3D Object Detection

**arXiv**: [2511.13138v1](https://arxiv.org/abs/2511.13138) | [PDF](https://arxiv.org/pdf/2511.13138.pdf)

**作者**: Longhui Zheng, Qiming Xia, Xiaolu Chen, Zhaoliang Liu, Chenglu Wen

---

## 💡 一句话要点

**提出WinMamba以解决3D目标检测中效率与长程依赖的平衡问题**

**关键词**: `3D目标检测` `状态空间模型` `多尺度特征` `窗口移位策略` `长程依赖` `自动驾驶`

## 📋 核心要点

1. 核心问题：3D目标检测需平衡计算效率与长程空间依赖，现有方法因固定窗口扫描丢失空间信息
2. 方法要点：引入WinMamba块，结合窗口尺度自适应模块和窗口移位策略，增强多尺度特征与上下文
3. 实验或效果：在KITTI和Waymo数据集上显著超越基线，验证WSF和AWF模块提升检测精度

## 📄 摘要（原文）

> 3D object detection is critical for autonomous driving, yet it remains fundamentally challenging to simultaneously maximize computational efficiency and capture long-range spatial dependencies. We observed that Mamba-based models, with their linear state-space design, capture long-range dependencies at lower cost, offering a promising balance between efficiency and accuracy. However, existing methods rely on axis-aligned scanning within a fixed window, inevitably discarding spatial information. To address this problem, we propose WinMamba, a novel Mamba-based 3D feature-encoding backbone composed of stacked WinMamba blocks. To enhance the backbone with robust multi-scale representation, the WinMamba block incorporates a window-scale-adaptive module that compensates voxel features across varying resolutions during sampling. Meanwhile, to obtain rich contextual cues within the linear state space, we equip the WinMamba layer with a learnable positional encoding and a window-shift strategy. Extensive experiments on the KITTI and Waymo datasets demonstrate that WinMamba significantly outperforms the baseline. Ablation studies further validate the individual contributions of the WSF and AWF modules in improving detection accuracy. The code will be made publicly available.

