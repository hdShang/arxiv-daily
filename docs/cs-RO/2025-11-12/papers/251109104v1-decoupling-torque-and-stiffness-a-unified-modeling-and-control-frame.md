---
layout: default
title: Decoupling Torque and Stiffness: A Unified Modeling and Control Framework for Antagonistic Artificial Muscles
---

# Decoupling Torque and Stiffness: A Unified Modeling and Control Framework for Antagonistic Artificial Muscles

**arXiv**: [2511.09104v1](https://arxiv.org/abs/2511.09104) | [PDF](https://arxiv.org/pdf/2511.09104.pdf)

**作者**: Amirhossein Kazemipour, Robert K. Katzschmann

---

## 💡 一句话要点

**提出统一框架实现拮抗人工肌肉的实时扭矩与刚度独立控制**

**关键词**: `拮抗人工肌肉` `扭矩刚度解耦` `统一建模` `级联控制` `阻抗控制` `人机交互`

## 📋 核心要点

1. 核心问题：现有软肌肉控制器难以在动态接触中维持扭矩与刚度的独立控制
2. 方法要点：使用统一力模型和级联控制器，通过偏置和共收缩坐标实现解耦
3. 实验或效果：仿真验证显示接触中保持独立性，软表面稳定快200倍，刚性表面力减少81%

## 📄 摘要（原文）

> Antagonistic soft actuators built from artificial muscles (PAMs, HASELs, DEAs) promise plant-level torque-stiffness decoupling, yet existing controllers for soft muscles struggle to maintain independent control through dynamic contact transients. We present a unified framework enabling independent torque and stiffness commands in real-time for diverse soft actuator types. Our unified force law captures diverse soft muscle physics in a single model with sub-ms computation, while our cascaded controller with analytical inverse dynamics maintains decoupling despite model errors and disturbances. Using co-contraction/bias coordinates, the controller independently modulates torque via bias and stiffness via co-contraction-replicating biological impedance strategies. Simulation-based validation through contact experiments demonstrates maintained independence: 200x faster settling on soft surfaces, 81% force reduction on rigid surfaces, and stable interaction vs 22-54% stability for fixed policies. This framework provides a foundation for enabling musculoskeletal antagonistic systems to execute adaptive impedance control for safe human-robot interaction.

