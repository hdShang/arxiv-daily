---
layout: default
title: OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction
---

# OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16842" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16842v1</a>
  <a href="https://arxiv.org/pdf/2512.16842.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16842v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16842v1', 'OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxin Ray Song, Jinzhou Li, Rao Fu, Devin Murphy, Kaichen Zhou, Rishi Shiv, Yaqi Li, Haoyu Xiong, Crystal Elaine Owens, Yilun Du, Yiyue Luo, Xianyi Cheng, Antonio Torralba, Wojciech Matusik, Paul Pu Liang

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-12-18

**备注**: https://opentouch-tactile.github.io/

---

## 💡 一句话要点

**OpenTouch：构建真实场景下完整手部触觉交互数据集与基准**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `触觉感知` `具身智能` `机器人操作` `多模态学习` `自我中心视觉` `数据集` `基准测试`

## 📋 核心要点

1. 现有方法缺乏在真实场景下同步第一人称视频与完整手部触觉的数据集，阻碍了视觉感知与物理交互的融合。
2. OpenTouch构建了首个真实场景下的自我中心完整手部触觉数据集，包含同步视频、触觉和姿态数据，并提供详细文本注释。
3. 通过OpenTouch，论文提出了检索和分类基准，验证了触觉信号在抓取理解和跨模态对齐方面的有效性。

## 📝 摘要（中文）

人手是与物理世界交互的主要界面，但自我中心感知很少知道何时、何地或以多大力度进行接触。目前缺乏稳健的可穿戴触觉传感器，并且没有现有的真实场景数据集将第一人称视频与完整手部触觉对齐。为了弥合视觉感知和物理交互之间的差距，我们提出了OpenTouch，这是第一个真实场景下的自我中心完整手部触觉数据集，包含5.1小时的同步视频-触觉-姿态数据和2,900个带有详细文本注释的精选片段。使用OpenTouch，我们引入了检索和分类基准，以探究触觉如何支撑感知和行动。我们表明，触觉信号为抓取理解提供了一个紧凑而强大的线索，加强了跨模态对齐，并且可以从真实场景视频查询中可靠地检索。通过发布这个带注释的视觉-触觉-姿态数据集和基准，我们的目标是推进多模态自我中心感知、具身学习和富接触机器人操作。

## 🔬 方法详解

**问题定义**：现有方法缺乏在真实场景下同步第一人称视角视频与完整手部触觉信息的数据集。这使得研究人员难以开发能够理解和利用触觉信息的视觉感知系统，从而限制了具身智能和机器人操作的发展。现有的触觉传感器和数据集往往集中在实验室环境或特定任务上，难以泛化到复杂的真实世界场景。

**核心思路**：OpenTouch的核心思路是构建一个大规模、高质量的真实场景数据集，包含同步的第一人称视角视频、完整手部触觉数据和手部姿态信息。通过提供这样的数据集，研究人员可以训练和评估模型，以学习触觉与视觉之间的关系，从而提高对物理交互的理解能力。此外，论文还提出了基于该数据集的检索和分类基准，以促进相关研究的进展。

**技术框架**：OpenTouch数据集的构建流程包括数据采集、数据同步、数据标注和数据发布。数据采集使用可穿戴触觉传感器记录手部触觉信息，同时使用第一人称相机记录视频。数据同步将触觉数据、视频数据和手部姿态数据对齐。数据标注包括文本描述和关键帧标注。数据发布将数据集公开，并提供相应的API和工具。

**关键创新**：OpenTouch的关键创新在于它是第一个在真实场景下采集的自我中心完整手部触觉数据集。与现有的数据集相比，OpenTouch具有更大的规模、更高的质量和更强的泛化能力。此外，论文还提出了基于该数据集的检索和分类基准，为相关研究提供了一个统一的评估平台。

**关键设计**：OpenTouch数据集包含5.1小时的同步视频-触觉-姿态数据和2,900个带有详细文本注释的精选片段。触觉传感器采用了高分辨率的触觉感应技术，能够捕捉到细微的触觉变化。视频采用了高帧率的相机，能够捕捉到快速的手部动作。手部姿态数据采用了先进的姿态估计算法，能够准确地估计手部关节的位置和方向。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16842v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16842v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16842v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，触觉信号能够显著提高抓取理解的准确性，并加强跨模态对齐的效果。通过OpenTouch数据集，研究人员能够从真实场景视频查询中可靠地检索到相关的触觉信息。这些结果验证了触觉在感知和行动中的重要作用。

## 🎯 应用场景

OpenTouch数据集和基准测试为多模态自我中心感知、具身学习和富接触机器人操作等领域提供了重要资源。该研究成果可应用于开发更智能的机器人，使其能够更好地理解和操纵物理世界，例如在家庭服务、工业自动化和医疗保健等领域。

## 📄 摘要（原文）

> The human hand is our primary interface to the physical world, yet egocentric perception rarely knows when, where, or how forcefully it makes contact. Robust wearable tactile sensors are scarce, and no existing in-the-wild datasets align first-person video with full-hand touch. To bridge the gap between visual perception and physical interaction, we present OpenTouch, the first in-the-wild egocentric full-hand tactile dataset, containing 5.1 hours of synchronized video-touch-pose data and 2,900 curated clips with detailed text annotations. Using OpenTouch, we introduce retrieval and classification benchmarks that probe how touch grounds perception and action. We show that tactile signals provide a compact yet powerful cue for grasp understanding, strengthen cross-modal alignment, and can be reliably retrieved from in-the-wild video queries. By releasing this annotated vision-touch-pose dataset and benchmark, we aim to advance multimodal egocentric perception, embodied learning, and contact-rich robotic manipulation.

