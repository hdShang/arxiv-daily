---
layout: default
title: Soft pneumatic grippers: Topology optimization, 3D-printing and experimental validation
---

# Soft pneumatic grippers: Topology optimization, 3D-printing and experimental validation

**arXiv**: [2511.19211v1](https://arxiv.org/abs/2511.19211) | [PDF](https://arxiv.org/pdf/2511.19211.pdf)

**作者**: Prabhat Kumar, Chandra Prakash, Josh Pinskier, David Howard, Matthijs Langelaar

---

## 💡 一句话要点

**提出拓扑优化框架以设计软气动抓取器，提升抓取性能。**

**关键词**: `拓扑优化` `软气动抓取器` `3D打印` `有限元分析` `稳健设计`

## 📋 核心要点

1. 核心问题：软气动抓取器设计中需处理依赖设计的驱动负载。
2. 方法要点：采用稳健拓扑优化，结合Darcy定律和应变能约束。
3. 实验或效果：优化单元优于传统设计，3D打印抓取器验证多对象抓取。

## 📄 摘要（原文）

> This paper presents a systematic topology optimization framework for designing a soft pneumatic gripper (SPG), explicitly considering the design-dependent nature of the actuating load. The load is modeled using Darcy's law with an added drainage term. A 2D soft arm unit is optimized by formulating it as a compliant mechanism design problem using the robust formulation. The problem is posed as a min-max optimization, where the output deformations of blueprint and eroded designs are considered. A volume constraint is imposed on the blueprint part, while a strain-energy constraint is enforced on the eroded part. The MMA is employed to solve the optimization problem and obtain the optimized soft unit. Finite element analysis with the Ogden material model confirms that the optimized 2D unit outperforms a conventional rectangular design under pneumatic loading. The optimized 2D unit is extruded to obtain a 3D module, and ten such units are assembled to create a soft arm. Deformation profiles of the optimized arm are analysed under different pressure loads. Four arms are 3D-printed and integrated with a supporting structure to realize the proposed SPG. The gripping performance of the SPG is demonstrated on objects with different weights, sizes, stiffness, and shapes.

