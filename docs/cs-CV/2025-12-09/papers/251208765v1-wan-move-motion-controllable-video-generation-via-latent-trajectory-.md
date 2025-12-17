---
layout: default
title: Wan-Move: Motion-controllable Video Generation via Latent Trajectory Guidance
---

# Wan-Move: Motion-controllable Video Generation via Latent Trajectory Guidance

**arXiv**: [2512.08765v1](https://arxiv.org/abs/2512.08765) | [PDF](https://arxiv.org/pdf/2512.08765.pdf)

**作者**: Ruihang Chu, Yefei He, Zhekai Chen, Shiwei Zhang, Xiaogang Xu, Bin Xia, Dingdong Wang, Hongwei Yi, Xihui Liu, Hengshuang Zhao, Yu Liu, Yingya Zhang, Yujiu Yang

---

## 💡 一句话要点

**提出Wan-Move框架，通过潜在轨迹引导实现视频生成中的精确运动控制。**

**关键词**: `视频生成` `运动控制` `潜在轨迹` `时空特征` `基准评估` `可扩展框架`

## 📋 核心要点

1. 现有方法运动控制粒度粗且可扩展性有限，难以满足实际应用需求。
2. 核心方法是将密集点轨迹投影到潜在空间，传播首帧特征以生成对齐的时空特征图作为运动指导。
3. 实验表明，Wan-Move在MoveBench基准上生成5秒480p视频，运动可控性媲美商业工具，并公开代码与数据。

## 📄 摘要（原文）

> We present Wan-Move, a simple and scalable framework that brings motion control to video generative models. Existing motion-controllable methods typically suffer from coarse control granularity and limited scalability, leaving their outputs insufficient for practical use. We narrow this gap by achieving precise and high-quality motion control. Our core idea is to directly make the original condition features motion-aware for guiding video synthesis. To this end, we first represent object motions with dense point trajectories, allowing fine-grained control over the scene. We then project these trajectories into latent space and propagate the first frame's features along each trajectory, producing an aligned spatiotemporal feature map that tells how each scene element should move. This feature map serves as the updated latent condition, which is naturally integrated into the off-the-shelf image-to-video model, e.g., Wan-I2V-14B, as motion guidance without any architecture change. It removes the need for auxiliary motion encoders and makes fine-tuning base models easily scalable. Through scaled training, Wan-Move generates 5-second, 480p videos whose motion controllability rivals Kling 1.5 Pro's commercial Motion Brush, as indicated by user studies. To support comprehensive evaluation, we further design MoveBench, a rigorously curated benchmark featuring diverse content categories and hybrid-verified annotations. It is distinguished by larger data volume, longer video durations, and high-quality motion annotations. Extensive experiments on MoveBench and the public dataset consistently show Wan-Move's superior motion quality. Code, models, and benchmark data are made publicly available.

