---
layout: default
title: End-to-End Multi-Person Pose Estimation with Pose-Aware Video Transformer
---

# End-to-End Multi-Person Pose Estimation with Pose-Aware Video Transformer

**arXiv**: [2511.13208v1](https://arxiv.org/abs/2511.13208) | [PDF](https://arxiv.org/pdf/2511.13208.pdf)

**作者**: Yonghui Yu, Jiahang Cai, Xun Wang, Wenwu Yang

---

## 💡 一句话要点

**提出PAVE-Net端到端视频多人姿态估计方法，消除启发式操作。**

**关键词**: `端到端姿态估计` `视频姿态估计` `时空注意力` `多人姿态估计` `姿态感知网络`

## 📋 核心要点

1. 现有方法依赖检测和NMS等启发式操作，限制精度和效率。
2. 引入PAVE-Net，结合空间编码器和时空姿态解码器，实现跨帧关联。
3. 在PoseTrack2017上mAP提升6.0，精度与先进方法相当，效率显著提高。

## 📄 摘要（原文）

> Existing multi-person video pose estimation methods typically adopt a two-stage pipeline: detecting individuals in each frame, followed by temporal modeling for single-person pose estimation. This design relies on heuristic operations such as detection, RoI cropping, and non-maximum suppression (NMS), limiting both accuracy and efficiency. In this paper, we present a fully end-to-end framework for multi-person 2D pose estimation in videos, effectively eliminating heuristic operations. A key challenge is to associate individuals across frames under complex and overlapping temporal trajectories. To address this, we introduce a novel Pose-Aware Video transformEr Network (PAVE-Net), which features a spatial encoder to model intra-frame relations and a spatiotemporal pose decoder to capture global dependencies across frames. To achieve accurate temporal association, we propose a pose-aware attention mechanism that enables each pose query to selectively aggregate features corresponding to the same individual across consecutive frames.Additionally, we explicitly model spatiotemporal dependencies among pose keypoints to improve accuracy. Notably, our approach is the first end-to-end method for multi-frame 2D human pose estimation.Extensive experiments show that PAVE-Net substantially outperforms prior image-based end-to-end methods, achieving a \textbf{6.0} mAP improvement on PoseTrack2017, and delivers accuracy competitive with state-of-the-art two-stage video-based approaches, while offering significant gains in efficiency.Project page: https://github.com/zgspose/PAVENet

