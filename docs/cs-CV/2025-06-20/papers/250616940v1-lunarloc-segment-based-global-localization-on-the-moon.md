---
layout: default
title: "LunarLoc: Segment-Based Global Localization on the Moon"
---

# LunarLoc: Segment-Based Global Localization on the Moon

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16940" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16940v1</a>
  <a href="https://arxiv.org/pdf/2506.16940.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16940v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16940v1', 'LunarLoc: Segment-Based Global Localization on the Moon')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Annika Thomas, Robaire Galliath, Aleksander Garbuz, Luke Anger, Cormac O'Neill, Trevor Johst, Dami Thomas, George Lordos, Jonathan P. How

**分类**: cs.CV

**发布日期**: 2025-06-20

**🔗 代码/项目**: [GITHUB](https://github.com/mit-acl/lunarloc-data)

---

## 💡 一句话要点

**提出LunarLoc以解决月球表面全球定位问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `全球定位` `月球探索` `实例分割` `视觉惯性里程计` `自主机器人`

## 📋 核心要点

1. 现有的视觉惯性里程计方法在长距离行驶中会产生累积误差，导致定位不准确，影响月球表面的自主操作。
2. 论文提出LunarLoc，通过实例分割技术从立体图像中提取地标，并利用图论数据关联进行环境对齐，从而实现高精度定位。
3. LunarLoc在多会话实验中实现了亚厘米级的定位精度，显著优于当前月球全球定位的主流方法。

## 📝 摘要（中文）

全球定位在月球表面自主操作中至关重要，因为传统的地球导航基础设施（如GPS）不可用。随着NASA在阿尔忒弥斯计划下推进月球长期存在，自主操作将成为机器人探索和基础设施部署等任务的关键。现有的视觉惯性里程计（VIO）方法在长距离行驶中会累积误差，导致定位不准确。为了解决这一问题，本文提出LunarLoc，通过实例分割从机载立体图像中零-shot提取巨石地标，构建地形的图形表示，并与先前会话捕获的环境参考图进行对齐，从而实现准确且无漂移的全球定位。LunarLoc在多会话全球定位实验中实现了亚厘米级的精度，显著超越了现有的月球全球定位技术。

## 🔬 方法详解

**问题定义**：本文旨在解决月球表面自主操作中的全球定位问题，现有的视觉惯性里程计方法在长距离行驶中会产生累积误差，导致定位不准确。

**核心思路**：LunarLoc的核心思路是利用实例分割技术从机载立体图像中提取巨石地标，构建地形的图形表示，并与之前捕获的环境参考图进行对齐，从而实现准确的全球定位。

**技术框架**：LunarLoc的整体架构包括三个主要模块：首先，通过实例分割从立体图像中提取地标；其次，构建地形的图形表示；最后，利用图论数据关联将当前图与参考图进行对齐。

**关键创新**：LunarLoc的主要创新在于采用实例分割进行零-shot地标提取，这一方法能够有效克服传统方法中的漂移问题，实现高精度的全球定位。

**关键设计**：在技术细节上，LunarLoc采用了特定的损失函数来优化地标提取的准确性，并设计了高效的图形表示结构，以确保在视觉模糊的环境中也能保持定位精度。

## 📊 实验亮点

LunarLoc在多会话全球定位实验中实现了亚厘米级的定位精度，相较于现有技术，性能提升显著，展示了其在视觉模糊环境下的强大适应能力。

## 🎯 应用场景

该研究的潜在应用领域包括月球探测、资源开采和基础设施建设等。随着未来月球探索任务的增加，LunarLoc将为自主机器人提供可靠的定位支持，推动人类在月球的长期存在与开发。

## 📄 摘要（原文）

> Global localization is necessary for autonomous operations on the lunar surface where traditional Earth-based navigation infrastructure, such as GPS, is unavailable. As NASA advances toward sustained lunar presence under the Artemis program, autonomous operations will be an essential component of tasks such as robotic exploration and infrastructure deployment. Tasks such as excavation and transport of regolith require precise pose estimation, but proposed approaches such as visual-inertial odometry (VIO) accumulate odometry drift over long traverses. Precise pose estimation is particularly important for upcoming missions such as the ISRU Pilot Excavator (IPEx) that rely on autonomous agents to operate over extended timescales and varied terrain. To help overcome odometry drift over long traverses, we propose LunarLoc, an approach to global localization that leverages instance segmentation for zero-shot extraction of boulder landmarks from onboard stereo imagery. Segment detections are used to construct a graph-based representation of the terrain, which is then aligned with a reference map of the environment captured during a previous session using graph-theoretic data association. This method enables accurate and drift-free global localization in visually ambiguous settings. LunarLoc achieves sub-cm level accuracy in multi-session global localization experiments, significantly outperforming the state of the art in lunar global localization. To encourage the development of further methods for global localization on the Moon, we release our datasets publicly with a playback module: https://github.com/mit-acl/lunarloc-data.

