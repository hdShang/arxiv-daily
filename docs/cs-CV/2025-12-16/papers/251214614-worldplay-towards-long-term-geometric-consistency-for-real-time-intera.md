---
layout: default
title: WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling
---

# WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14614" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14614</a>
  <a href="https://arxiv.org/pdf/2512.14614.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14614" onclick="toggleFavorite(this, '2512.14614', 'WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenqiang Sun, Haiyu Zhang, Haoyuan Wang, Junta Wu, Zehan Wang, Zhenwei Wang, Yunhong Wang, Jun Zhang, Tengfei Wang, Chunchao Guo

**分类**: cs.CV, cs.GR

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**WorldPlay：面向实时交互世界建模的长时几何一致性视频扩散模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `视频扩散模型` `实时渲染` `交互式建模` `长时几何一致性` `上下文记忆` `知识蒸馏` `虚拟现实` `机器人`

## 📋 核心要点

1. 现有方法在实时交互世界建模中，难以兼顾速度和长期几何一致性，面临内存限制和误差累积的挑战。
2. WorldPlay通过双重动作表示、重构上下文记忆和上下文强制蒸馏，实现了快速、一致且可交互的世界建模。
3. 实验表明，WorldPlay能够以24 FPS生成720p长时程视频，并在几何一致性和泛化能力上优于现有技术。

## 📝 摘要（中文）

本文提出WorldPlay，一种流式视频扩散模型，能够实现具有长期几何一致性的实时交互世界建模，解决了现有方法在速度和内存之间的权衡问题。WorldPlay得益于三个关键创新：1) 使用双重动作表示，以响应用户的键盘和鼠标输入，实现鲁棒的动作控制；2) 为了保证长期一致性，我们的重构上下文记忆动态地从过去的帧中重建上下文，并使用时间重构来保持几何上重要但时间上久远的帧的可访问性，有效地缓解了记忆衰减；3) 我们还提出了一种新颖的上下文强制蒸馏方法，专为内存感知模型设计。对齐教师和学生模型之间的记忆上下文，保持学生模型使用长程信息的能力，从而在防止误差漂移的同时实现实时速度。综上所述，WorldPlay以24 FPS生成长时程流式720p视频，具有卓越的一致性，与现有技术相比表现出色，并在各种场景中表现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：现有实时交互世界建模方法需要在速度、内存占用和长期几何一致性之间进行权衡。一方面，为了保证实时性，模型往往无法利用足够长的历史信息，导致几何一致性较差。另一方面，如果简单地增加历史信息的长度，则会显著增加内存占用，并可能导致误差累积和漂移。因此，如何在有限的内存资源下，实现具有长期几何一致性的实时交互世界建模是一个关键问题。

**核心思路**：WorldPlay的核心思路是利用视频扩散模型，并结合双重动作表示、重构上下文记忆和上下文强制蒸馏等技术，在有限的内存资源下，实现具有长期几何一致性的实时交互世界建模。通过双重动作表示，模型可以更好地理解用户的交互意图；通过重构上下文记忆，模型可以有效地利用历史信息，保证长期几何一致性；通过上下文强制蒸馏，模型可以在保证速度的同时，防止误差漂移。

**技术框架**：WorldPlay的整体框架是一个流式视频扩散模型，包括以下几个主要模块：1) 双重动作表示模块，用于将用户的键盘和鼠标输入转换为动作表示；2) 重构上下文记忆模块，用于从过去的帧中重建上下文，并使用时间重构来保持几何上重要但时间上久远的帧的可访问性；3) 视频扩散模型，用于根据动作表示和上下文信息生成视频帧；4) 上下文强制蒸馏模块，用于训练内存感知模型，防止误差漂移。

**关键创新**：WorldPlay最重要的技术创新点在于重构上下文记忆和上下文强制蒸馏。重构上下文记忆能够有效地利用历史信息，保证长期几何一致性，缓解了记忆衰减问题。上下文强制蒸馏能够训练内存感知模型，在保证速度的同时，防止误差漂移。这两个创新点共同解决了现有方法在速度、内存占用和长期几何一致性之间的权衡问题。

**关键设计**：在重构上下文记忆模块中，论文使用了一种动态重建上下文的方法，根据帧的重要性选择性地保留和更新历史帧。在上下文强制蒸馏模块中，论文设计了一种新的损失函数，用于对齐教师和学生模型之间的记忆上下文，从而保持学生模型使用长程信息的能力。具体的网络结构和参数设置在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14614/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14614/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14614/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

WorldPlay在多个场景下进行了实验，结果表明，它能够以24 FPS生成720p长时程视频，具有卓越的几何一致性，并且在各种场景中表现出强大的泛化能力。与现有技术相比，WorldPlay在几何一致性指标上取得了显著的提升，并且能够生成更长时程的视频。

## 🎯 应用场景

WorldPlay在虚拟现实、游戏开发、机器人控制等领域具有广泛的应用前景。它可以用于创建具有高度真实感和交互性的虚拟环境，为用户提供沉浸式的体验。此外，WorldPlay还可以用于训练机器人，使其能够在复杂环境中进行导航和操作。

## 📄 摘要（原文）

> This paper presents WorldPlay, a streaming video diffusion model that enables real-time, interactive world modeling with long-term geometric consistency, resolving the trade-off between speed and memory that limits current methods. WorldPlay draws power from three key innovations. 1) We use a Dual Action Representation to enable robust action control in response to the user's keyboard and mouse inputs. 2) To enforce long-term consistency, our Reconstituted Context Memory dynamically rebuilds context from past frames and uses temporal reframing to keep geometrically important but long-past frames accessible, effectively alleviating memory attenuation. 3) We also propose Context Forcing, a novel distillation method designed for memory-aware model. Aligning memory context between the teacher and student preserves the student's capacity to use long-range information, enabling real-time speeds while preventing error drift. Taken together, WorldPlay generates long-horizon streaming 720p video at 24 FPS with superior consistency, comparing favorably with existing techniques and showing strong generalization across diverse scenes. Project page and online demo can be found:this https URLandthis https URL.

