---
layout: default
title: NeuSpring: Neural Spring Fields for Reconstruction and Simulation of Deformable Objects from Videos
---

# NeuSpring: Neural Spring Fields for Reconstruction and Simulation of Deformable Objects from Videos

**arXiv**: [2511.08310v1](https://arxiv.org/abs/2511.08310) | [PDF](https://arxiv.org/pdf/2511.08310.pdf)

**作者**: Qingshan Xu, Jiao Liu, Shangshu Yu, Yuxuan Wang, Yuan Zhou, Junbao Zhou, Jiequan Cui, Yew-Soon Ong, Hanwang Zhang

---

## 💡 一句话要点

**提出NeuSpring神经弹簧场，从视频重建和模拟可变形物体，提升物理学习与预测性能。**

**关键词**: `可变形物体重建` `神经弹簧场` `弹簧质量模型` `物理模拟` `视频分析`

## 📋 核心要点

1. 现有方法忽略可变形物体内在物理属性，导致当前状态建模物理学习有限，泛化预测差。
2. NeuSpring结合弹簧质量模型，引入分段拓扑和神经弹簧场，建模多区域连接和弹簧物理属性。
3. 实验显示，在真实数据集上，当前状态和未来预测的Chamfer距离分别提升20%和25%。

## 📄 摘要（原文）

> In this paper, we aim to create physical digital twins of deformable objects under interaction. Existing methods focus more on the physical learning of current state modeling, but generalize worse to future prediction. This is because existing methods ignore the intrinsic physical properties of deformable objects, resulting in the limited physical learning in the current state modeling. To address this, we present NeuSpring, a neural spring field for the reconstruction and simulation of deformable objects from videos. Built upon spring-mass models for realistic physical simulation, our method consists of two major innovations: 1) a piecewise topology solution that efficiently models multi-region spring connection topologies using zero-order optimization, which considers the material heterogeneity of real-world objects. 2) a neural spring field that represents spring physical properties across different frames using a canonical coordinate-based neural network, which effectively leverages the spatial associativity of springs for physical learning. Experiments on real-world datasets demonstrate that our NeuSping achieves superior reconstruction and simulation performance for current state modeling and future prediction, with Chamfer distance improved by 20% and 25%, respectively.

