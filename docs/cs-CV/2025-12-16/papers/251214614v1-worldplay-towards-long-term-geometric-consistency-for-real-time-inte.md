---
layout: default
title: WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling
---

# WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14614" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14614v1</a>
  <a href="https://arxiv.org/pdf/2512.14614.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14614v1" onclick="toggleFavorite(this, '2512.14614v1', 'WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenqiang Sun, Haiyu Zhang, Haoyuan Wang, Junta Wu, Zehan Wang, Zhenwei Wang, Yunhong Wang, Jun Zhang, Tengfei Wang, Chunchao Guo

**分类**: cs.CV, cs.GR

**发布日期**: 2025-12-16

**备注**: project page: https://3d-models.hunyuan.tencent.com/world/, demo: https://3d.hunyuan.tencent.com/sceneTo3D

---

## 💡 一句话要点

**WorldPlay：提出一种具有长期几何一致性的实时交互式世界建模方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `实时渲染` `交互式建模` `视频扩散模型` `长期一致性` `上下文记忆` `知识蒸馏` `几何约束` `虚拟现实`

## 📋 核心要点

1. 现有方法在实时交互式世界建模中，难以兼顾速度和长期几何一致性，存在内存限制和误差累积问题。
2. WorldPlay通过双重动作表示、重构上下文记忆和上下文强制蒸馏，实现长期几何一致性和实时渲染。
3. 实验结果表明，WorldPlay能够以24FPS生成720p视频，并在长期一致性和泛化性方面优于现有技术。

## 📝 摘要（中文）

本文提出WorldPlay，一种流式视频扩散模型，能够实现具有长期几何一致性的实时交互式世界建模，解决了当前方法在速度和内存之间的权衡问题。WorldPlay得益于三个关键创新：1) 我们使用双重动作表示，以实现对用户键盘和鼠标输入的鲁棒动作控制。2) 为了保证长期一致性，我们的重构上下文记忆动态地从过去的帧中重建上下文，并使用时间重构来保持几何上重要但时间上久远的帧的可访问性，有效地缓解了记忆衰减。3) 我们还提出了一种专为内存感知模型设计的新型蒸馏方法，即上下文强制。对齐教师和学生模型之间的记忆上下文，保持学生模型使用长程信息的能力，从而在防止误差漂移的同时实现实时速度。综上所述，WorldPlay以24 FPS生成长时程流式720p视频，具有卓越的一致性，与现有技术相比具有优势，并在各种场景中表现出强大的泛化能力。项目页面和在线演示可在以下网址找到：https://3d-models.hunyuan.tencent.com/world/ 和 https://3d.hunyuan.tencent.com/sceneTo3D。

## 🔬 方法详解

**问题定义**：现有实时交互式世界建模方法面临着速度和长期几何一致性之间的矛盾。为了保证实时性，通常需要限制模型的复杂度和输入序列的长度，导致模型难以捕捉长期依赖关系，从而产生几何不一致的现象。此外，随着时间推移，误差会逐渐累积，进一步降低建模质量。因此，如何在有限的计算资源和内存条件下，实现具有长期几何一致性的实时交互式世界建模是一个关键挑战。

**核心思路**：WorldPlay的核心思路是利用视频扩散模型，并结合双重动作表示、重构上下文记忆和上下文强制蒸馏等技术，来解决长期几何一致性问题。通过双重动作表示，模型能够更好地理解用户的交互意图；通过重构上下文记忆，模型能够有效地利用历史信息，缓解记忆衰减；通过上下文强制蒸馏，模型能够在保证实时性的前提下，保持对长期信息的感知能力。

**技术框架**：WorldPlay的整体框架包含以下几个主要模块：1) 双重动作表示模块，用于将用户的键盘和鼠标输入转换为模型可理解的动作表示。2) 重构上下文记忆模块，用于从过去的帧中重建上下文，并使用时间重构来保持几何上重要但时间上久远的帧的可访问性。3) 视频扩散模型，用于生成新的视频帧。4) 上下文强制蒸馏模块，用于训练内存感知模型，使其能够在保证实时性的前提下，保持对长期信息的感知能力。

**关键创新**：WorldPlay最重要的技术创新点在于重构上下文记忆和上下文强制蒸馏。重构上下文记忆能够有效地利用历史信息，缓解记忆衰减，从而保证长期几何一致性。上下文强制蒸馏能够训练内存感知模型，使其能够在保证实时性的前提下，保持对长期信息的感知能力。这与传统的蒸馏方法不同，传统方法通常只关注输出结果的相似性，而忽略了模型内部的记忆状态。

**关键设计**：在重构上下文记忆模块中，论文采用了一种动态重建上下文的方法，即根据当前帧的几何信息，选择性地从过去的帧中提取上下文信息。在上下文强制蒸馏模块中，论文设计了一种新的损失函数，该损失函数不仅考虑了输出结果的相似性，还考虑了教师和学生模型之间的记忆状态的相似性。具体来说，该损失函数包括两部分：一部分是传统的L1或L2损失，用于衡量输出结果的相似性；另一部分是KL散度损失，用于衡量教师和学生模型之间的记忆状态的相似性。

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

WorldPlay在多个场景下进行了实验，结果表明其能够以24FPS生成720p视频，并在长期几何一致性和泛化性方面优于现有技术。与现有方法相比，WorldPlay能够生成更稳定、更逼真的虚拟环境，并能够更好地响应用户的交互。

## 🎯 应用场景

WorldPlay在游戏开发、虚拟现实、机器人导航等领域具有广泛的应用前景。它可以用于创建逼真的虚拟环境，并允许用户与环境进行实时交互。此外，WorldPlay还可以用于训练机器人，使其能够在复杂环境中进行导航和操作。该研究的实际价值在于提高了实时交互式世界建模的质量和效率，并为未来的研究提供了新的思路。

## 📄 摘要（原文）

> This paper presents WorldPlay, a streaming video diffusion model that enables real-time, interactive world modeling with long-term geometric consistency, resolving the trade-off between speed and memory that limits current methods. WorldPlay draws power from three key innovations. 1) We use a Dual Action Representation to enable robust action control in response to the user's keyboard and mouse inputs. 2) To enforce long-term consistency, our Reconstituted Context Memory dynamically rebuilds context from past frames and uses temporal reframing to keep geometrically important but long-past frames accessible, effectively alleviating memory attenuation. 3) We also propose Context Forcing, a novel distillation method designed for memory-aware model. Aligning memory context between the teacher and student preserves the student's capacity to use long-range information, enabling real-time speeds while preventing error drift. Taken together, WorldPlay generates long-horizon streaming 720p video at 24 FPS with superior consistency, comparing favorably with existing techniques and showing strong generalization across diverse scenes. Project page and online demo can be found: https://3d-models.hunyuan.tencent.com/world/ and https://3d.hunyuan.tencent.com/sceneTo3D.

