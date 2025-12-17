---
layout: default
title: ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM
---

# ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

**arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032) | [PDF](https://arxiv.org/pdf/2512.14032.pdf)

**作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison

**分类**: cs.CV, cs.AI, eess.IV

**发布日期**: 2025-12-16

**备注**: Project Page: https://github.com/ialzugaray/ace-slam

**🔗 代码/项目**: [GITHUB](https://github.com/ialzugaray/ace-slam)

---

## 💡 一句话要点

**提出ACE-SLAM系统，基于场景坐标回归实现神经隐式实时RGB-D SLAM，解决现有方法实时性和内存效率不足的问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `神经隐式SLAM` `场景坐标回归` `实时RGB-D SLAM` `轻量级网络` `动态环境适应` `隐私保护` `地图表示` `重定位技术`

## 📋 核心要点

1. 现有神经隐式SLAM方法在实时性和内存效率方面存在不足，难以满足实际应用需求。
2. 论文提出基于场景坐标回归的轻量级网络，直接映射2D特征到3D坐标，实现高效隐式地图表示。
3. 实验表明，系统在合成和真实基准上达到严格实时性能，并在动态环境中表现可靠。

## 📝 摘要（中文）

我们提出了一种新颖的神经RGB-D同时定位与建图（SLAM）系统，能够实时学习场景的隐式地图。首次探索了在神经SLAM流程中使用场景坐标回归（SCR）作为核心隐式地图表示范式，该范式训练一个轻量级网络，直接将2D图像特征映射到3D全局坐标。SCR网络提供高效、低内存的3D地图表示，支持极快的重定位，并固有地保护隐私，使其特别适合神经隐式SLAM。我们的系统是首个通过依赖基于SCR的表示实现严格实时性的神经隐式RGB-D SLAM系统。我们引入了一种专门为此目的设计的新型SCR架构，并详细阐述了将SCR集成到实时SLAM流程中的关键设计选择。所得框架简单而灵活，无缝支持稀疏和稠密特征，并在动态环境中可靠运行，无需特殊适应。我们在已建立的合成和真实世界基准上评估了我们的方法，展示了与最先进技术相比的竞争性能。项目页面：https://github.com/ialzugaray/ace-slam

## 🔬 方法详解

ACE-SLAM的整体框架是一个神经RGB-D SLAM系统，核心采用场景坐标回归作为隐式地图表示。关键技术创新点包括：设计了一种新型SCR架构，专门针对实时SLAM优化，通过轻量级网络直接预测3D场景坐标；详细集成了SCR到实时SLAM流程中，支持稀疏和稠密特征的无缝处理。与现有方法的主要区别在于：首次将SCR范式应用于神经隐式SLAM，实现了严格实时性，而传统方法往往依赖更复杂的网络或存储密集型表示，导致计算和内存开销较大。

## 📊 实验亮点

在合成和真实世界基准测试中，ACE-SLAM实现了严格实时性能，重定位速度极快，内存占用低，并在动态环境中无需特殊适应即可可靠运行，性能与最先进方法竞争。

## 🎯 应用场景

该研究适用于增强现实、机器人导航和虚拟现实等领域，其高效实时SLAM能力可支持动态环境中的精准定位和地图构建，具有实际应用价值。

## 📄 摘要（原文）

> We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image features to 3D global coordinates. SCR networks provide efficient, low-memory 3D map representations, enable extremely fast relocalization, and inherently preserve privacy, making them particularly suitable for neural implicit SLAM.
>   Our system is the first one to achieve strict real-time in neural implicit RGB-D SLAM by relying on a SCR-based representation. We introduce a novel SCR architecture specifically tailored for this purpose and detail the critical design choices required to integrate SCR into a live SLAM pipeline. The resulting framework is simple yet flexible, seamlessly supporting both sparse and dense features, and operates reliably in dynamic environments without special adaptation. We evaluate our approach on established synthetic and real-world benchmarks, demonstrating competitive performance against the state of the art. Project Page: https://github.com/ialzugaray/ace-slam

