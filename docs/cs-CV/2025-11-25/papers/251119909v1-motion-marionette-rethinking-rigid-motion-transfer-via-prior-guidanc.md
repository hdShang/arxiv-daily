---
layout: default
title: Motion Marionette: Rethinking Rigid Motion Transfer via Prior Guidance
---

# Motion Marionette: Rethinking Rigid Motion Transfer via Prior Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.19909" class="toolbar-btn" target="_blank">📄 arXiv: 2511.19909v1</a>
  <a href="https://arxiv.org/pdf/2511.19909.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19909v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.19909v1', 'Motion Marionette: Rethinking Rigid Motion Transfer via Prior Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoxuan Wang, Jiachen Tao, Junyi Wu, Gaowen Liu, Ramana Rao Kompella, Yan Yan

**分类**: cs.CV

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**提出Motion Marionette以解决刚性运动转移问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `刚性运动转移` `时空先验` `视频生成` `可控生成` `视觉一致性`

## 📋 核心要点

1. 现有方法通常依赖外部几何或生成先验，导致在可泛化性与时间一致性之间存在权衡。
2. 本研究提出通过内部时空先验来指导运动转移，避免了外部约束的影响，提升了灵活性。
3. 实验结果显示，Motion Marionette在多种对象上表现出色，生成的视频在时间上保持一致，并能进行可控生成。

## 📝 摘要（中文）

我们提出了Motion Marionette，这是一个零-shot框架，旨在将单目源视频中的刚性运动转移到单视图目标图像中。以往的研究通常依赖几何、生成或仿真先验来指导转移过程，但这些外部先验引入了辅助约束，导致了可泛化性与时间一致性之间的权衡。为了解决这些局限性，我们提出通过内部先验来指导运动转移过程，该先验专门捕捉源视频与任何转移目标视频之间的时空变换。具体而言，我们首先将源视频和目标图像提升到统一的3D表示空间，从源视频中提取运动轨迹以构建独立于物体几何和语义的时空先验，编码相对的空间变化。该先验与目标对象结合，合成可控的速度场，并通过基于位置的动力学进行精细化，以减少伪影并增强视觉一致性。实验结果表明，Motion Marionette能够在不同对象间泛化，生成与源运动高度一致的时间一致性视频，并支持可控的视频生成。

## 🔬 方法详解

**问题定义**：本论文旨在解决刚性运动转移的问题，现有方法依赖外部先验，导致可泛化性与时间一致性之间的权衡。

**核心思路**：我们提出通过内部先验来指导运动转移，该先验捕捉源视频与目标视频之间的时空变换，避免了外部约束的影响。

**技术框架**：整体架构包括将源视频和目标图像提升到统一的3D表示空间，提取运动轨迹构建时空先验，并与目标对象结合生成速度场，最后通过基于位置的动力学进行精细化处理。

**关键创新**：最重要的创新在于引入内部时空先验，独立于物体几何和语义，能够有效编码相对空间变化，显著提升了运动转移的灵活性与一致性。

**关键设计**：在技术细节上，构建的时空先验通过运动轨迹提取，速度场的合成与精细化处理采用基于位置的动力学方法，确保生成视频的视觉一致性。

## 📊 实验亮点

实验结果表明，Motion Marionette在多种对象上均能有效泛化，生成的视频在时间一致性上与源运动高度对齐。与基线方法相比，生成视频的质量显著提升，具体性能数据尚未提供。

## 🎯 应用场景

该研究的潜在应用领域包括动画制作、虚拟现实和游戏开发等，能够为这些领域提供高效的运动转移解决方案，提升内容生成的灵活性和质量。未来，该方法可能会影响实时视频编辑和交互式媒体的生成方式。

## 📄 摘要（原文）

> We present Motion Marionette, a zero-shot framework for rigid motion transfer from monocular source videos to single-view target images. Previous works typically employ geometric, generative, or simulation priors to guide the transfer process, but these external priors introduce auxiliary constraints that lead to trade-offs between generalizability and temporal consistency. To address these limitations, we propose guiding the motion transfer process through an internal prior that exclusively captures the spatial-temporal transformations and is shared between the source video and any transferred target video. Specifically, we first lift both the source video and the target image into a unified 3D representation space. Motion trajectories are then extracted from the source video to construct a spatial-temporal (SpaT) prior that is independent of object geometry and semantics, encoding relative spatial variations over time. This prior is further integrated with the target object to synthesize a controllable velocity field, which is subsequently refined using Position-Based Dynamics to mitigate artifacts and enhance visual coherence. The resulting velocity field can be flexibly employed for efficient video production. Empirical results demonstrate that Motion Marionette generalizes across diverse objects, produces temporally consistent videos that align well with the source motion, and supports controllable video generation.

