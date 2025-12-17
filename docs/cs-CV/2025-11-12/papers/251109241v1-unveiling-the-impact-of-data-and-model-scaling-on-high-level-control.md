---
layout: default
title: Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots
---

# Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots

**arXiv**: [2511.09241v1](https://arxiv.org/abs/2511.09241) | [PDF](https://arxiv.org/pdf/2511.09241.pdf)

**作者**: Yuxi Wei, Zirui Wang, Kangning Yin, Yue Hu, Jingbo Wang, Siheng Chen

---

## 💡 一句话要点

**提出Humanoid-Union数据集和SCHUR框架以解决人形机器人高级控制中的数据扩展问题**

**关键词**: `人形机器人控制` `数据扩展` `运动生成` `模态对齐` `大规模数据集`

## 📋 核心要点

1. 核心问题：如何从丰富的人类视频中提取可学习表示并用于人形机器人高级控制
2. 方法要点：构建大规模人形机器人运动数据集，并开发可扩展学习框架SCHUR
3. 实验或效果：在MPJPE和FID指标上分别提升37%和25%，并在真实机器人中验证

## 📄 摘要（原文）

> Data scaling has long remained a critical bottleneck in robot learning. For humanoid robots, human videos and motion data are abundant and widely available, offering a free and large-scale data source. Besides, the semantics related to the motions enable modality alignment and high-level robot control learning. However, how to effectively mine raw video, extract robot-learnable representations, and leverage them for scalable learning remains an open problem. To address this, we introduce Humanoid-Union, a large-scale dataset generated through an autonomous pipeline, comprising over 260 hours of diverse, high-quality humanoid robot motion data with semantic annotations derived from human motion videos. The dataset can be further expanded via the same pipeline. Building on this data resource, we propose SCHUR, a scalable learning framework designed to explore the impact of large-scale data on high-level control in humanoid robots. Experimental results demonstrate that SCHUR achieves high robot motion generation quality and strong text-motion alignment under data and model scaling, with 37\% reconstruction improvement under MPJPE and 25\% alignment improvement under FID comparing with previous methods. Its effectiveness is further validated through deployment in real-world humanoid robot.

