---
layout: default
title: FlowSteer: Guiding Few-Step Image Synthesis with Authentic Trajectories
---

# FlowSteer: Guiding Few-Step Image Synthesis with Authentic Trajectories

**arXiv**: [2511.18834v1](https://arxiv.org/abs/2511.18834) | [PDF](https://arxiv.org/pdf/2511.18834.pdf)

**作者**: Lei Ke, Hubery Yin, Gongye Liu, Zhengyao Lv, Jingcai Guo, Chen Li, Wenhan Luo, Yujiu Yang, Jing Lyu

---

## 💡 一句话要点

**提出FlowSteer方法，通过真实轨迹引导提升少步图像合成效率**

**关键词**: `流匹配` `图像合成` `蒸馏训练` `轨迹对齐` `少步推理`

## 📋 核心要点

1. 核心问题：ReFlow方法在流匹配中采样效率低，实际性能不如一致性蒸馏和分数蒸馏
2. 方法要点：引入在线轨迹对齐和对抗蒸馏目标，优化学生模型沿教师轨迹生成
3. 实验或效果：在SD3上验证方法有效性，修复FlowMatchEulerDiscreteScheduler缺陷

## 📄 摘要（原文）

> With the success of flow matching in visual generation, sampling efficiency remains a critical bottleneck for its practical application. Among flow models' accelerating methods, ReFlow has been somehow overlooked although it has theoretical consistency with flow matching. This is primarily due to its suboptimal performance in practical scenarios compared to consistency distillation and score distillation. In this work, we investigate this issue within the ReFlow framework and propose FlowSteer, a method unlocks the potential of ReFlow-based distillation by guiding the student along teacher's authentic generation trajectories. We first identify that Piecewised ReFlow's performance is hampered by a critical distribution mismatch during the training and propose Online Trajectory Alignment(OTA) to resolve it. Then, we introduce a adversarial distillation objective applied directly on the ODE trajectory, improving the student's adherence to the teacher's generation trajectory. Furthermore, we find and fix a previously undiscovered flaw in the widely-used FlowMatchEulerDiscreteScheduler that largely degrades few-step inference quality. Our experiment result on SD3 demonstrates our method's efficacy.

