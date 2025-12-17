---
layout: default
title: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance
---

# Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance

**arXiv**: [2512.11173v1](https://arxiv.org/abs/2512.11173) | [PDF](https://arxiv.org/pdf/2512.11173.pdf)

**作者**: Tzu-Hsien Lee, Fidan Mahmudova, Karthik Desingh

**分类**: cs.RO

**发布日期**: 2025-12-11

**🔗 代码/项目**: [PROJECT_PAGE](https://rpm-lab-umn.github.io/category-level-last-meter-nav/)

---

## 💡 一句话要点

**提出基于单实例RGB图像模仿学习的类别级末端导航方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `末端导航` `模仿学习` `类别级泛化` `移动操作` `RGB图像` `机器人定位` `语言驱动分割`

## 📋 核心要点

1. 现有基于RGB的导航系统精度不足，难以满足移动操作中精确定位的需求，导致操作策略执行失败。
2. 提出一种基于物体中心的模仿学习框架，利用RGB图像、文本提示和空间得分矩阵解码器实现末端导航。
3. 实验表明，该方法在未见过的物体实例上实现了较高的边缘对齐和物体对齐成功率，无需深度信息或地图先验。

## 📝 摘要（中文）

本文提出了一种面向末端导航的、以物体为中心的模仿学习框架，旨在使四足移动机械臂仅使用板载摄像头的RGB图像观测，即可实现操作就绪的精确定位。该方法将导航策略建立在三个输入之上：目标图像、来自板载摄像头的多视角RGB观测以及指定目标物体的文本提示。然后，一个语言驱动的分割模块和一个空间得分矩阵解码器提供显式的物体定位和相对姿态推理。该系统使用来自类别中单个物体实例的真实世界数据，泛化到具有挑战性光照和背景条件的不同环境中未见过的物体实例。为了全面评估，引入了两个指标：使用真实方向的边缘对齐指标，以及评估机器人视觉上与目标对齐程度的物体对齐指标。结果表明，该策略在未见过的目标物体定位中，边缘对齐成功率为73.47%，物体对齐成功率为96.94%。

## 🔬 方法详解

**问题定义**：论文旨在解决移动机械臂末端导航的精确定位问题。现有基于RGB的导航系统通常只能提供米级精度，无法满足后续操作所需的精确位置，导致操作策略无法在训练数据的分布内执行，从而导致失败。

**核心思路**：论文的核心思路是利用模仿学习，让机器人学习如何仅通过RGB图像观测和文本提示，将自身定位到目标物体附近，达到操作就绪的状态。通过学习单个物体实例的数据，实现对整个物体类别的泛化。

**技术框架**：整体框架包含以下几个主要模块：1) 接收目标图像、多视角RGB观测和文本提示作为输入；2) 使用语言驱动的分割模块进行物体分割，提取目标物体；3) 使用空间得分矩阵解码器进行相对姿态推理，估计机器人与目标物体之间的相对位置关系；4) 根据估计的相对位置关系，控制机器人进行导航。

**关键创新**：该方法最重要的创新点在于实现了类别级别的末端导航，即仅使用单个物体实例的数据，就能泛化到同一类别下的其他未见过的物体实例。此外，该方法仅依赖RGB图像和文本提示，无需深度信息、激光雷达或地图先验，降低了系统的复杂性和成本。

**关键设计**：关键设计包括：1) 语言驱动的分割模块，用于从RGB图像中分割出目标物体；2) 空间得分矩阵解码器，用于估计机器人与目标物体之间的相对位置关系；3) 边缘对齐和物体对齐两个评估指标，用于评估导航策略的性能。损失函数未知。

## 📊 实验亮点

实验结果表明，该方法在未见过的目标物体定位中，边缘对齐成功率为73.47%，物体对齐成功率为96.94%。这些结果表明，该方法能够在类别级别上实现精确的末端导航，且无需深度信息、激光雷达或地图先验。该方法为统一的移动操作提供了一种可扩展的途径。

## 🎯 应用场景

该研究成果可应用于各种需要精确定位的移动操作任务，例如：在家庭环境中，机器人可以根据指令将自身定位到特定家具附近，以便进行清洁、维修等操作；在工业环境中，机器人可以精确定位到生产线上的特定部件附近，以便进行组装、检测等操作。该研究为实现通用移动操作机器人奠定了基础。

## 📄 摘要（原文）

> Achieving precise positioning of the mobile manipulator's base is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world data from a single object instance within a category, the system generalizes to unseen object instances across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 73.47% success in edge-alignment and 96.94% success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

