---
layout: default
title: TwinOR: Photorealistic Digital Twins of Dynamic Operating Rooms for Embodied AI Research
---

# TwinOR: Photorealistic Digital Twins of Dynamic Operating Rooms for Embodied AI Research

**arXiv**: [2511.07412v1](https://arxiv.org/abs/2511.07412) | [PDF](https://arxiv.org/pdf/2511.07412.pdf)

**作者**: Han Zhang, Yiqing Shen, Roger D. Soberanis-Mukul, Ankita Ghosh, Hao Ding, Lalithkumar Seenivasan, Jose L. Porras, Zhekai Mao, Chenjia Li, Wenjie Xiao, Lonny Yarmus, Angela Christine Argento, Masaru Ishii, Mathias Unberath

---

## 💡 一句话要点

**提出TwinOR框架以构建手术室动态数字孪生，支持具身AI研究。**

**关键词**: `数字孪生` `手术室模拟` `具身AI` `3D重建` `多视角感知` `虚拟环境`

## 📋 核心要点

1. 核心问题：手术室安全限制阻碍具身AI在真实环境中感知与交互。
2. 方法要点：从视频重建静态几何，多视角感知动态运动，融合为沉浸式3D环境。
3. 实验或效果：合成数据使模型性能接近真实数据集，验证传感器级真实感。

## 📄 摘要（原文）

> Developing embodied AI for intelligent surgical systems requires safe,
> controllable environments for continual learning and evaluation. However,
> safety regulations and operational constraints in operating rooms (ORs) limit
> embodied agents from freely perceiving and interacting in realistic settings.
> Digital twins provide high-fidelity, risk-free environments for exploration and
> training. How we may create photorealistic and dynamic digital representations
> of ORs that capture relevant spatial, visual, and behavioral complexity remains
> unclear. We introduce TwinOR, a framework for constructing photorealistic,
> dynamic digital twins of ORs for embodied AI research. The system reconstructs
> static geometry from pre-scan videos and continuously models human and
> equipment motion through multi-view perception of OR activities. The static and
> dynamic components are fused into an immersive 3D environment that supports
> controllable simulation and embodied exploration. The proposed framework
> reconstructs complete OR geometry with centimeter level accuracy while
> preserving dynamic interaction across surgical workflows, enabling realistic
> renderings and a virtual playground for embodied AI systems. In our
> experiments, TwinOR simulates stereo and monocular sensor streams for geometry
> understanding and visual localization tasks. Models such as FoundationStereo
> and ORB-SLAM3 on TwinOR-synthesized data achieve performance within their
> reported accuracy on real indoor datasets, demonstrating that TwinOR provides
> sensor-level realism sufficient for perception and localization challenges. By
> establishing a real-to-sim pipeline for constructing dynamic, photorealistic
> digital twins of OR environments, TwinOR enables the safe, scalable, and
> data-efficient development and benchmarking of embodied AI, ultimately
> accelerating the deployment of embodied AI from sim-to-real.

