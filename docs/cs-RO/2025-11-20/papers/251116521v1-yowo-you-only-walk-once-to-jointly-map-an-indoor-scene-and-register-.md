---
layout: default
title: YOWO: You Only Walk Once to Jointly Map An Indoor Scene and Register Ceiling-mounted Cameras
---

# YOWO: You Only Walk Once to Jointly Map An Indoor Scene and Register Ceiling-mounted Cameras

**arXiv**: [2511.16521v1](https://arxiv.org/abs/2511.16521) | [PDF](https://arxiv.org/pdf/2511.16521.pdf)

**作者**: Fan Yang, Sosuke Yamao, Ikuo Kusajima, Atsunori Moteki, Shoichi Masui, Shan Jiang

---

## 💡 一句话要点

**提出YOWO方法以联合映射室内场景并注册天花板摄像头**

**关键词**: `室内场景映射` `摄像头注册` `因子图优化` `RGB-D视觉` `轨迹关联` `联合优化`

## 📋 核心要点

1. 核心问题：天花板摄像头注册到室内场景布局困难，手动或自动方法效率低或精度差。
2. 方法要点：使用移动代理头戴RGB-D相机遍历场景，同步摄像头视频，通过轨迹关联和因子图优化实现联合映射与注册。
3. 实验或效果：在新建数据集上验证，方法统一框架下有效完成两任务并提升性能。

## 📄 摘要（原文）

> Using ceiling-mounted cameras (CMCs) for indoor visual capturing opens up a wide range of applications. However, registering CMCs to the target scene layout presents a challenging task. While manual registration with specialized tools is inefficient and costly, automatic registration with visual localization may yield poor results when visual ambiguity exists. To alleviate these issues, we propose a novel solution for jointly mapping an indoor scene and registering CMCs to the scene layout. Our approach involves equipping a mobile agent with a head-mounted RGB-D camera to traverse the entire scene once and synchronize CMCs to capture this mobile agent. The egocentric videos generate world-coordinate agent trajectories and the scene layout, while the videos of CMCs provide pseudo-scale agent trajectories and CMC relative poses. By correlating all the trajectories with their corresponding timestamps, the CMC relative poses can be aligned to the world-coordinate scene layout. Based on this initialization, a factor graph is customized to enable the joint optimization of ego-camera poses, scene layout, and CMC poses. We also develop a new dataset, setting the first benchmark for collaborative scene mapping and CMC registration (https://sites.google.com/view/yowo/home). Experimental results indicate that our method not only effectively accomplishes two tasks within a unified framework, but also jointly enhances their performance. We thus provide a reliable tool to facilitate downstream position-aware applications.

