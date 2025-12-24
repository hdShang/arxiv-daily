---
layout: default
title: "WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling"
---

# WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14614" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14614v1</a>
  <a href="https://arxiv.org/pdf/2512.14614.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14614v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14614v1', 'WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenqiang Sun, Haiyu Zhang, Haoyuan Wang, Junta Wu, Zehan Wang, Zhenwei Wang, Yunhong Wang, Jun Zhang, Tengfei Wang, Chunchao Guo

**分类**: cs.CV, cs.GR

**发布日期**: 2025-12-16

**备注**: project page: https://3d-models.hunyuan.tencent.com/world/, demo: https://3d.hunyuan.tencent.com/sceneTo3D

---

## 💡 一句话要点

**WorldPlay：提出一种具有长期几何一致性的实时交互式世界建模方法。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `实时渲染` `世界建模` `视频扩散模型` `长期一致性` `几何约束`

## 📋 核心要点

1. 现有世界建模方法在速度和长期几何一致性之间存在权衡，难以实现实时交互。
2. WorldPlay通过双重动作表示、重构上下文记忆和上下文强制蒸馏，实现长期几何一致性的实时交互式世界建模。
3. 实验表明，WorldPlay能够以24 FPS生成720p视频，具有卓越的一致性，并在各种场景中表现出强大的泛化能力。

## 📝 摘要（中文）

本文提出了一种名为WorldPlay的流式视频扩散模型，该模型能够实现具有长期几何一致性的实时交互式世界建模，从而解决了现有方法在速度和内存之间的权衡问题。WorldPlay的核心在于三项创新：1) 使用双重动作表示，以响应用户的键盘和鼠标输入，实现鲁棒的动作控制；2) 为了保证长期一致性，重构上下文记忆动态地从过去的帧中重建上下文，并使用时间重构来保持几何上重要的但时间上较远的帧的可访问性，从而有效地缓解了记忆衰减；3) 提出了一种新颖的上下文强制蒸馏方法，专为内存感知模型设计。通过对齐教师和学生模型之间的内存上下文，保持学生模型使用长程信息的能力，从而在实现实时速度的同时防止误差漂移。综上所述，WorldPlay能够以24 FPS的速度生成长时程的720p流式视频，具有卓越的一致性，与现有技术相比具有优势，并在各种场景中表现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：现有实时世界建模方法难以在速度和长期几何一致性之间取得平衡。为了保证长期一致性，需要存储大量的历史帧信息，导致内存占用过高，影响实时性。反之，为了保证实时性，只能使用有限的历史帧信息，导致长期几何一致性较差。

**核心思路**：WorldPlay的核心思路是利用视频扩散模型，并结合双重动作表示、重构上下文记忆和上下文强制蒸馏，在保证实时性的前提下，实现长期几何一致性。通过重构上下文记忆，可以动态地从过去的帧中重建上下文，并使用时间重构来保持几何上重要的但时间上较远的帧的可访问性，从而有效地缓解了记忆衰减。

**技术框架**：WorldPlay的整体框架是一个流式视频扩散模型，主要包含以下几个模块：1) 双重动作表示模块，用于接收用户的键盘和鼠标输入，并将其转换为动作表示；2) 重构上下文记忆模块，用于从过去的帧中重建上下文，并使用时间重构来保持几何上重要的帧的可访问性；3) 视频扩散模型，用于根据动作表示和上下文信息生成新的视频帧；4) 上下文强制蒸馏模块，用于训练内存感知模型，使其能够有效地利用长程信息。

**关键创新**：WorldPlay的关键创新在于以下三个方面：1) 提出了双重动作表示，能够更鲁棒地响应用户的输入；2) 提出了重构上下文记忆，能够有效地缓解记忆衰减，保证长期几何一致性；3) 提出了上下文强制蒸馏，能够训练内存感知模型，使其能够有效地利用长程信息。

**关键设计**：在双重动作表示中，论文具体如何编码键盘和鼠标输入？重构上下文记忆模块中，时间重构的具体实现方式是什么？上下文强制蒸馏模块中，教师模型和学生模型的具体结构是什么？损失函数如何设计以保证学生模型能够学习到教师模型的长程信息利用能力？这些细节在论文中应该有更详细的描述，但摘要中未提及。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14614v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14614v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14614v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

WorldPlay能够以24 FPS的速度生成720p流式视频，具有卓越的一致性，与现有技术相比具有优势，并在各种场景中表现出强大的泛化能力。具体性能指标和对比基线需要在论文中查找。

## 🎯 应用场景

WorldPlay具有广泛的应用前景，例如虚拟现实、增强现实、游戏开发、机器人导航等领域。它可以用于创建具有长期几何一致性的交互式虚拟环境，为用户提供更加沉浸式的体验。此外，它还可以用于训练机器人，使其能够在复杂的环境中进行导航和操作。

## 📄 摘要（原文）

> This paper presents WorldPlay, a streaming video diffusion model that enables real-time, interactive world modeling with long-term geometric consistency, resolving the trade-off between speed and memory that limits current methods. WorldPlay draws power from three key innovations. 1) We use a Dual Action Representation to enable robust action control in response to the user's keyboard and mouse inputs. 2) To enforce long-term consistency, our Reconstituted Context Memory dynamically rebuilds context from past frames and uses temporal reframing to keep geometrically important but long-past frames accessible, effectively alleviating memory attenuation. 3) We also propose Context Forcing, a novel distillation method designed for memory-aware model. Aligning memory context between the teacher and student preserves the student's capacity to use long-range information, enabling real-time speeds while preventing error drift. Taken together, WorldPlay generates long-horizon streaming 720p video at 24 FPS with superior consistency, comparing favorably with existing techniques and showing strong generalization across diverse scenes. Project page and online demo can be found: https://3d-models.hunyuan.tencent.com/world/ and https://3d.hunyuan.tencent.com/sceneTo3D.

