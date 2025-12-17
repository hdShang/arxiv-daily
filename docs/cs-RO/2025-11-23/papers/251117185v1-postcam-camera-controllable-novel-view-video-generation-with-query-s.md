---
layout: default
title: PostCam: Camera-Controllable Novel-View Video Generation with Query-Shared Cross-Attention
---

# PostCam: Camera-Controllable Novel-View Video Generation with Query-Shared Cross-Attention

**arXiv**: [2511.17185v1](https://arxiv.org/abs/2511.17185) | [PDF](https://arxiv.org/pdf/2511.17185.pdf)

**作者**: Yipeng Chen, Zhichao Ye, Zhenzhou Fang, Xinyu Chen, Xiaoyu Zhang, Jialing Liu, Nan Wang, Haomin Liu, Guofeng Zhang

---

## 💡 一句话要点

**提出PostCam框架，通过查询共享交叉注意力实现动态场景中相机轨迹的编辑。**

**关键词**: `新视角视频生成` `相机控制` `交叉注意力` `动态场景编辑` `两阶段训练`

## 📋 核心要点

1. 现有视频重捕获方法相机运动注入策略不佳，影响控制精度和视觉细节保留。
2. 引入查询共享交叉注意力模块，融合6-DoF相机位姿和2D渲染帧以提升控制精度。
3. 实验显示相机控制精度和视图一致性提升超20%，生成质量优于现有方法。

## 📄 摘要（原文）

> We propose PostCam, a framework for novel-view video generation that enables post-capture editing of camera trajectories in dynamic scenes. We find that existing video recapture methods suffer from suboptimal camera motion injection strategies; such suboptimal designs not only limit camera control precision but also result in generated videos that fail to preserve fine visual details from the source video. To achieve more accurate and flexible motion manipulation, PostCam introduces a query-shared cross-attention module. It integrates two distinct forms of control signals: the 6-DoF camera poses and the 2D rendered video frames. By fusing them into a unified representation within a shared feature space, our model can extract underlying motion cues, which enhances both control precision and generation quality. Furthermore, we adopt a two-stage training strategy: the model first learns coarse camera control from pose inputs, and then incorporates visual information to refine motion accuracy and enhance visual fidelity. Experiments on both real-world and synthetic datasets demonstrate that PostCam outperforms state-of-the-art methods by over 20% in camera control precision and view consistency, while achieving the highest video generation quality. Our project webpage is publicly available at: https://cccqaq.github.io/PostCam.github.io/

