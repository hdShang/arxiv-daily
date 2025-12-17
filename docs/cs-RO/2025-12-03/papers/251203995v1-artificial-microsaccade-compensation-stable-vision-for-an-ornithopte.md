---
layout: default
title: Artificial Microsaccade Compensation: Stable Vision for an Ornithopter
---

# Artificial Microsaccade Compensation: Stable Vision for an Ornithopter

**arXiv**: [2512.03995v1](https://arxiv.org/abs/2512.03995) | [PDF](https://arxiv.org/pdf/2512.03995.pdf)

**作者**: Levi Burner, Guido de Croon, Yiannis Aloimonos

---

## 💡 一句话要点

**提出人工微扫视补偿方法，以稳定无尾扑翼机视频，实现实时无失真稳定。**

**关键词**: `视频稳定` `扑翼机视觉` `SO(3)优化` `实时处理` `微扫视补偿`

## 📋 核心要点

1. 核心问题：无尾扑翼机因12-20Hz抖动，难以使用相机传感，导致视频不稳定。
2. 方法要点：通过优化SO(3)表示的3D旋转，最小化图像强度变化，实现视频稳定。
3. 实验或效果：相比Adobe Premier Pro，本方法质量更高且实时运行，适合人眼观看。

## 📄 摘要（原文）

> Animals with foveated vision, including humans, experience microsaccades, small, rapid eye movements that they are not aware of. Inspired by this phenomenon, we develop a method for "Artificial Microsaccade Compensation". It can stabilize video captured by a tailless ornithopter that has resisted attempts to use camera-based sensing because it shakes at 12-20 Hz. Our approach minimizes changes in image intensity by optimizing over 3D rotation represented in SO(3). This results in a stabilized video, computed in real time, suitable for human viewing, and free from distortion. When adapted to hold a fixed viewing orientation, up to occasional saccades, it can dramatically reduce inter-frame motion while also benefiting from an efficient recursive update. When compared to Adobe Premier Pro's warp stabilizer, which is widely regarded as the best commercial video stabilization software available, our method achieves higher quality results while also running in real time.

