---
layout: default
title: Dreamcrafter: Immersive Editing of 3D Radiance Fields Through Flexible, Generative Inputs and Outputs
---

# Dreamcrafter: Immersive Editing of 3D Radiance Fields Through Flexible, Generative Inputs and Outputs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20129" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20129v1</a>
  <a href="https://arxiv.org/pdf/2512.20129.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20129v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20129v1', 'Dreamcrafter: Immersive Editing of 3D Radiance Fields Through Flexible, Generative Inputs and Outputs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cyrus Vachha, Yixiao Kang, Zach Dive, Ashwat Chidambaram, Anik Gupta, Eunice Jun, Bjoern Hartmann

**分类**: cs.HC, cs.CV

**发布日期**: 2025-12-23

**备注**: CHI 2025, Project page: https://dream-crafter.github.io/

---

## 💡 一句话要点

**Dreamcrafter：通过灵活的生成式输入输出实现沉浸式3D辐射场编辑**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D辐射场编辑` `生成式AI` `虚拟现实` `沉浸式交互` `场景创作`

## 📋 核心要点

1. 现有3D场景编辑方法在高抽象层次修改时存在高延迟，而直接操作则缺乏AI的生成能力。
2. Dreamcrafter通过VR界面结合生成式AI，提供自然语言和直接操作等多种控制方式，实现实时沉浸式编辑。
3. 该系统采用模块化架构，集成了生成式AI算法，并引入代理表示来支持高延迟操作期间的交互。

## 📝 摘要（中文）

3D场景创作是空间计算应用的核心任务。降低现有门槛的竞争愿景包括：（1）专注于3D内容的沉浸式直接操作；（2）利用AI技术捕获真实场景（如NeRFs、3D高斯溅射等3D辐射场），并在更高的抽象层次上修改它们，但代价是高延迟。我们统一了这些方法的互补优势，并研究如何将生成式AI的进步集成到实时、沉浸式3D辐射场编辑中。我们介绍了Dreamcrafter，一个基于VR的3D场景编辑系统，它：（1）提供了一个模块化架构来集成生成式AI算法；（2）结合了不同级别的控制来创建对象，包括自然语言和直接操作；（3）引入了代理表示，以支持高延迟操作期间的交互。我们贡献了关于控制偏好的经验性发现，并讨论了文本输入之外的生成式AI界面如何增强场景编辑和世界构建中的创造力。

## 🔬 方法详解

**问题定义**：论文旨在解决3D辐射场编辑中，现有方法要么依赖高延迟的生成式AI，要么依赖缺乏AI辅助的直接操作的问题。现有方法难以兼顾实时性和创造性，限制了3D场景编辑的效率和用户体验。

**核心思路**：Dreamcrafter的核心思路是将生成式AI的强大生成能力与VR环境下的实时交互相结合。通过模块化的架构，系统可以灵活地集成不同的生成式AI算法，并提供多种控制方式，包括自然语言和直接操作，从而实现低延迟、高创造性的3D场景编辑。

**技术框架**：Dreamcrafter系统主要包含以下几个模块：VR交互界面、生成式AI模块、代理表示模块和辐射场渲染模块。用户在VR界面中通过自然语言或直接操作输入指令，生成式AI模块根据指令生成或修改3D内容，代理表示模块用于在生成式AI处理期间提供低延迟的交互反馈，最后辐射场渲染模块将最终结果渲染到VR界面中。

**关键创新**：Dreamcrafter的关键创新在于其模块化的架构和代理表示的设计。模块化架构使得系统可以灵活地集成不同的生成式AI算法，适应不同的编辑需求。代理表示则通过使用低分辨率或简化的3D模型，在生成式AI处理期间提供实时的交互反馈，从而缓解了高延迟带来的问题。

**关键设计**：Dreamcrafter的关键设计包括：(1) VR交互界面的设计，需要考虑用户在VR环境下的操作习惯和舒适度；(2) 生成式AI模块的选择和集成，需要根据具体的编辑任务选择合适的算法，并进行优化；(3) 代理表示的生成和更新策略，需要在保证实时性的前提下，尽可能地保留原始3D内容的细节；(4) 辐射场渲染模块的优化，需要在保证渲染质量的前提下，尽可能地提高渲染速度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20129v1/images/chi_paper_dreamcrafter_teaser_figure_v3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20129v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20129v1/images/move_obj.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过用户研究验证了Dreamcrafter的有效性。研究结果表明，用户更倾向于结合自然语言和直接操作进行3D场景编辑。此外，代理表示的引入显著提升了用户在高延迟操作期间的交互体验。这些结果表明，Dreamcrafter在提升3D场景编辑的效率和创造性方面具有显著优势。

## 🎯 应用场景

Dreamcrafter可应用于游戏开发、虚拟现实内容创作、建筑设计、工业设计等领域。它能够降低3D场景创作的门槛，提高创作效率，并为用户提供更具创造性和沉浸感的体验。未来，该技术有望推动空间计算应用的发展，并改变人们与3D世界的交互方式。

## 📄 摘要（原文）

> Authoring 3D scenes is a central task for spatial computing applications. Competing visions for lowering existing barriers are (1) focus on immersive, direct manipulation of 3D content or (2) leverage AI techniques that capture real scenes (3D Radiance Fields such as, NeRFs, 3D Gaussian Splatting) and modify them at a higher level of abstraction, at the cost of high latency. We unify the complementary strengths of these approaches and investigate how to integrate generative AI advances into real-time, immersive 3D Radiance Field editing. We introduce Dreamcrafter, a VR-based 3D scene editing system that: (1) provides a modular architecture to integrate generative AI algorithms; (2) combines different levels of control for creating objects, including natural language and direct manipulation; and (3) introduces proxy representations that support interaction during high-latency operations. We contribute empirical findings on control preferences and discuss how generative AI interfaces beyond text input enhance creativity in scene editing and world building.

