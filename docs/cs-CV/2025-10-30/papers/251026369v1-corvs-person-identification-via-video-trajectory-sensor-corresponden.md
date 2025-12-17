---
layout: default
title: CorVS: Person Identification via Video Trajectory-Sensor Correspondence in a Real-World Warehouse
---

# CorVS: Person Identification via Video Trajectory-Sensor Correspondence in a Real-World Warehouse

**arXiv**: [2510.26369v1](https://arxiv.org/abs/2510.26369) | [PDF](https://arxiv.org/pdf/2510.26369.pdf)

**作者**: Kazuma Kano, Yuki Mori, Shin Katayama, Kenta Urano, Takuro Yonezawa, Nobuo Kawaguchi

---

## 💡 一句话要点

**提出CorVS方法，通过视频轨迹与传感器对应关系解决真实仓库中人员识别问题**

**关键词**: `人员识别` `视频轨迹` `传感器测量` `深度学习` `仓库监控` `数据对应`

## 📋 核心要点

1. 核心问题：仅凭视觉数据在真实仓库中识别个体不实用，现有方法在现实条件下易失效
2. 方法要点：使用深度学习预测轨迹与传感器测量的对应概率和可靠性，并随时间匹配
3. 实验或效果：基于实际仓库操作数据集验证，证明方法在真实应用中的有效性

## 📄 摘要（原文）

> Worker location data is key to higher productivity in industrial sites.
> Cameras are a promising tool for localization in logistics warehouses since
> they also offer valuable environmental contexts such as package status.
> However, identifying individuals with only visual data is often impractical.
> Accordingly, several prior studies identified people in videos by comparing
> their trajectories and wearable sensor measurements. While this approach has
> advantages such as independence from appearance, the existing methods may break
> down under real-world conditions. To overcome this challenge, we propose CorVS,
> a novel data-driven person identification method based on correspondence
> between visual tracking trajectories and sensor measurements. Firstly, our deep
> learning model predicts correspondence probabilities and reliabilities for
> every pair of a trajectory and sensor measurements. Secondly, our algorithm
> matches the trajectories and sensor measurements over time using the predicted
> probabilities and reliabilities. We developed a dataset with actual warehouse
> operations and demonstrated the method's effectiveness for real-world
> applications.

