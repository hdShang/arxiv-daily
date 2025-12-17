---
layout: default
title: Hoecken-D Hand: A Novel Robotic Hand for Linear Parallel Pinching and Self-Adaptive Grasping
---

# Hoecken-D Hand: A Novel Robotic Hand for Linear Parallel Pinching and Self-Adaptive Grasping

**arXiv**: [2510.13553v1](https://arxiv.org/abs/2510.13553) | [PDF](https://arxiv.org/pdf/2510.13553.pdf)

**作者**: Wentao Guo, Wenzeng Zhang

---

## 💡 一句话要点

**提出Hoecken-D手爪，结合改进Hoecken连杆与差动弹簧机制，实现线性平行夹持和自适应抓取。**

**关键词**: `机器人手爪` `欠驱动抓取` `Hoecken连杆` `差动机制` `自适应抓取` `线性夹持`

## 📋 核心要点

1. 核心问题：机器人抓取需兼顾精确夹持与自适应不规则物体，传统方法依赖多执行器增加复杂度。
2. 方法要点：改进Hoecken连杆，引入差动链接和弹簧机制，单执行器驱动，实现接触触发重构。
3. 实验或效果：原型测试显示，在多种几何物体上可靠抓取，线性夹持跨度约200毫米，成本低。

## 📄 摘要（原文）

> This paper presents the Hoecken-D Hand, an underactuated robotic gripper that
> combines a modified Hoecken linkage with a differential spring mechanism to
> achieve both linear parallel pinching and a mid-stroke transition to adaptive
> envelope. The original Hoecken linkage is reconfigured by replacing one member
> with differential links, preserving straight-line guidance while enabling
> contact-triggered reconfiguration without additional actuators. A
> double-parallelogram arrangement maintains fingertip parallelism during
> conventional pinching, whereas the differential mechanism allows one finger to
> wrap inward upon encountering an obstacle, improving stability on irregular or
> thin objects. The mechanism can be driven by a single linear actuator,
> minimizing complexity and cost; in our prototype, each finger is driven by its
> own linear actuator for simplicity. We perform kinematic modeling and force
> analysis to characterize grasp performance, including simulated grasping forces
> and spring-opening behavior under varying geometric parameters. The design was
> prototyped using PLA-based 3D printing, achieving a linear pinching span of
> approximately 200 mm. Preliminary tests demonstrate reliable grasping in both
> modes across a wide range of object geometries, highlighting the Hoecken-D Hand
> as a compact, adaptable, and cost-effective solution for manipulation in
> unstructured environments.

