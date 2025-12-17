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

**提出WorldPlay流式视频扩散模型，通过长期几何一致性实现实时交互式世界建模，解决速度与内存的权衡问题。**

**关键词**: `流式视频扩散模型` `实时交互式世界建模` `长期几何一致性` `重构上下文记忆` `上下文强制蒸馏` `双重动作表示` `内存感知模型` `长时视频生成`

## 📋 核心要点

1. 现有方法在实时交互式世界建模中面临速度与内存的权衡，难以同时保证长期几何一致性和实时性能。
2. WorldPlay采用双重动作表示、重构上下文记忆和上下文强制蒸馏，实现鲁棒控制、缓解记忆衰减并保持长程信息能力。
3. 模型能以24 FPS生成720p长时流式视频，在一致性和泛化性上优于现有技术，支持多样场景应用。

## 📝 摘要（中文）

本文介绍了WorldPlay，一种流式视频扩散模型，能够实现具有长期几何一致性的实时交互式世界建模，解决了当前方法在速度与内存之间的权衡限制。WorldPlay基于三个关键创新：1）采用双重动作表示，实现对用户键盘和鼠标输入的鲁棒动作控制；2）通过重构上下文记忆动态重建过去帧的上下文，并利用时间重帧保持几何重要但久远帧的可访问性，有效缓解记忆衰减；3）提出上下文强制，一种专为内存感知模型设计的新型蒸馏方法，通过对齐教师和学生模型的记忆上下文，保持学生模型使用长程信息的能力，实现实时速度同时防止误差漂移。综合来看，WorldPlay能以24 FPS生成具有卓越一致性的长时流式720p视频，优于现有技术，并在多样场景中展现出强大的泛化能力。项目页面和在线演示可在https://3d-models.hunyuan.tencent.com/world/和https://3d.hunyuan.tencent.com/sceneTo3D找到。

## 🔬 方法详解

WorldPlay是一个基于流式视频扩散模型的整体框架，旨在实现实时交互式世界建模。其关键技术创新包括：双重动作表示用于鲁棒响应用户输入；重构上下文记忆通过动态重建过去帧上下文和时间重帧来保持长期几何一致性，缓解记忆衰减；上下文强制蒸馏方法对齐教师和学生模型的记忆上下文，确保学生模型在实时推理中能有效利用长程信息。与现有方法的主要区别在于，它通过内存感知设计解决了速度与内存的权衡，避免了传统方法中因内存限制导致的误差漂移或性能下降。

## 📊 实验亮点

WorldPlay在实验中能以24 FPS实时生成720p长时流式视频，展现出卓越的几何一致性，优于现有技术，并在多样场景中验证了强大的泛化能力，有效解决了速度与内存的权衡问题。

## 🎯 应用场景

该研究在虚拟现实、游戏开发、自动驾驶模拟和机器人导航等领域具有潜在应用价值，能够支持实时交互式场景生成和长期一致性建模，提升用户体验和系统可靠性。

## 📄 摘要（原文）

> This paper presents WorldPlay, a streaming video diffusion model that enables real-time, interactive world modeling with long-term geometric consistency, resolving the trade-off between speed and memory that limits current methods. WorldPlay draws power from three key innovations. 1) We use a Dual Action Representation to enable robust action control in response to the user's keyboard and mouse inputs. 2) To enforce long-term consistency, our Reconstituted Context Memory dynamically rebuilds context from past frames and uses temporal reframing to keep geometrically important but long-past frames accessible, effectively alleviating memory attenuation. 3) We also propose Context Forcing, a novel distillation method designed for memory-aware model. Aligning memory context between the teacher and student preserves the student's capacity to use long-range information, enabling real-time speeds while preventing error drift. Taken together, WorldPlay generates long-horizon streaming 720p video at 24 FPS with superior consistency, comparing favorably with existing techniques and showing strong generalization across diverse scenes. Project page and online demo can be found: https://3d-models.hunyuan.tencent.com/world/ and https://3d.hunyuan.tencent.com/sceneTo3D.

