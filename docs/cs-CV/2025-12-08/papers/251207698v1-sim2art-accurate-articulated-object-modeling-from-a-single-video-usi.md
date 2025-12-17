---
layout: default
title: sim2art: Accurate Articulated Object Modeling from a Single Video using Synthetic Training Data Only
---

# sim2art: Accurate Articulated Object Modeling from a Single Video using Synthetic Training Data Only

**arXiv**: [2512.07698v1](https://arxiv.org/abs/2512.07698) | [PDF](https://arxiv.org/pdf/2512.07698.pdf)

**作者**: Arslan Artykov, Corentin Sautier, Vincent Lepetit

---

## 💡 一句话要点

**提出sim2art方法，仅用合成数据训练，从单目视频中准确建模关节物体**

**关键词**: `关节物体建模` `单目视频理解` `合成数据训练` `部件分割` `关节参数估计` `数据驱动方法`

## 📋 核心要点

1. 核心问题：从自由移动相机拍摄的单目视频中恢复关节物体的部件分割和关节参数，解决机器人学和数字孪生中的建模挑战
2. 方法要点：首个数据驱动方法，联合预测部件分割和关节参数，仅依赖合成数据进行训练，实现强泛化到真实物体
3. 实验或效果：在真实世界物体上展示良好泛化能力，适用于动态环境中的实时应用，提供可扩展的实用解决方案

## 📄 摘要（原文）

> Understanding articulated objects is a fundamental challenge in robotics and digital twin creation. To effectively model such objects, it is essential to recover both part segmentation and the underlying joint parameters. Despite the importance of this task, previous work has largely focused on setups like multi-view systems, object scanning, or static cameras. In this paper, we present the first data-driven approach that jointly predicts part segmentation and joint parameters from monocular video captured with a freely moving camera. Trained solely on synthetic data, our method demonstrates strong generalization to real-world objects, offering a scalable and practical solution for articulated object understanding. Our approach operates directly on casually recorded video, making it suitable for real-time applications in dynamic environments. Project webpage: https://aartykov.github.io/sim2art/

