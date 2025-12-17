---
layout: default
title: WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling
---

# WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling

**arXiv**: [2512.14614v1](https://arxiv.org/abs/2512.14614) | [PDF](https://arxiv.org/pdf/2512.14614.pdf)

**作者**: Wenqiang Sun, Haiyu Zhang, Haoyuan Wang, Junta Wu, Zehan Wang, Zhenwei Wang, Yunhong Wang, Jun Zhang, Tengfei Wang, Chunchao Guo

**分类**: cs.CV, cs.GR

**发布日期**: 2025-12-16

**备注**: project page: https://3d-models.hunyuan.tencent.com/world/, demo: https://3d.hunyuan.tencent.com/sceneTo3D

---

## 💡 一句话要点

**提出WorldPlay流式视频扩散模型，实现实时交互式世界建模并保持长期几何一致性**

🎯 **匹配领域**: **视觉里程计** **世界模型** **强化学习**

**关键词**: `流式视频扩散模型` `实时交互式世界建模` `长期几何一致性` `重构上下文记忆` `上下文强制蒸馏` `双动作表示` `内存感知模型` `时间重帧技术`

## 📋 核心要点

1. 现有方法在实时交互式世界建模中面临速度与内存的权衡，难以保持长期几何一致性，导致误差漂移和记忆衰减问题。
2. 论文提出WorldPlay模型，核心创新包括双动作表示、重构上下文记忆和上下文强制蒸馏，旨在增强动作控制、动态管理记忆并保持长程信息一致性。
3. 实验结果显示，WorldPlay能以24 FPS实时生成720p长时视频，在几何一致性和泛化能力上优于现有技术，有效解决了速度与内存的冲突。

## 📝 摘要（中文）

本文介绍了WorldPlay，一种流式视频扩散模型，能够实现实时、交互式的世界建模，并保持长期几何一致性，解决了当前方法在速度与内存之间的权衡限制。WorldPlay基于三个关键创新：1）采用双动作表示，实现对用户键盘和鼠标输入的鲁棒动作控制；2）通过重构上下文记忆动态重建过去帧的上下文，并使用时间重帧技术保持几何重要但久远帧的可访问性，有效缓解记忆衰减；3）提出上下文强制，一种专为内存感知模型设计的新蒸馏方法，通过对齐教师和学生模型的记忆上下文，保留学生模型使用长程信息的能力，实现实时速度同时防止误差漂移。综合来看，WorldPlay能以24 FPS生成720p长时流式视频，具有优越的一致性，优于现有技术，并在多样场景中展现出强泛化能力。项目页面和在线演示可在https://3d-models.hunyuan.tencent.com/world/和https://3d.hunyuan.tencent.com/sceneTo3D找到。

## 🔬 方法详解

WorldPlay是一个基于流式视频扩散模型的整体框架，用于实时交互式世界建模。其关键技术创新包括：1）双动作表示，通过编码用户输入实现鲁棒动作控制；2）重构上下文记忆，动态重建过去帧上下文并使用时间重帧技术保持几何重要帧的可访问性，以缓解记忆衰减；3）上下文强制蒸馏，一种新蒸馏方法，通过对齐教师和学生模型的记忆上下文，确保学生模型能有效利用长程信息，防止误差漂移。与现有方法的主要区别在于，WorldPlay通过内存感知设计解决了速度与内存的权衡，实现了长期几何一致性，而传统方法往往在实时性上牺牲一致性或依赖大量内存。

## 📊 实验亮点

最重要的实验结果是WorldPlay能以24 FPS实时生成720p长时流式视频，在几何一致性上显著优于现有技术，并在多样场景中展现出强泛化能力，有效解决了速度与内存的冲突。

## 🎯 应用场景

该研究在虚拟现实、游戏开发、自动驾驶模拟和机器人导航等领域具有潜在应用价值，能够支持实时交互式场景生成和动态世界建模，提升用户体验和系统效率。

## 📄 摘要（原文）

> This paper presents WorldPlay, a streaming video diffusion model that enables real-time, interactive world modeling with long-term geometric consistency, resolving the trade-off between speed and memory that limits current methods. WorldPlay draws power from three key innovations. 1) We use a Dual Action Representation to enable robust action control in response to the user's keyboard and mouse inputs. 2) To enforce long-term consistency, our Reconstituted Context Memory dynamically rebuilds context from past frames and uses temporal reframing to keep geometrically important but long-past frames accessible, effectively alleviating memory attenuation. 3) We also propose Context Forcing, a novel distillation method designed for memory-aware model. Aligning memory context between the teacher and student preserves the student's capacity to use long-range information, enabling real-time speeds while preventing error drift. Taken together, WorldPlay generates long-horizon streaming 720p video at 24 FPS with superior consistency, comparing favorably with existing techniques and showing strong generalization across diverse scenes. Project page and online demo can be found: https://3d-models.hunyuan.tencent.com/world/ and https://3d.hunyuan.tencent.com/sceneTo3D.

