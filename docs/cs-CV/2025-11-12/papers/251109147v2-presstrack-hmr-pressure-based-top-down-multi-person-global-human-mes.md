---
layout: default
title: PressTrack-HMR: Pressure-Based Top-Down Multi-Person Global Human Mesh Recovery
---

# PressTrack-HMR: Pressure-Based Top-Down Multi-Person Global Human Mesh Recovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09147" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09147v2</a>
  <a href="https://arxiv.org/pdf/2511.09147.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09147v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.09147v2', 'PressTrack-HMR: Pressure-Based Top-Down Multi-Person Global Human Mesh Recovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayue Yuan, Fangting Xie, Guangwen Ouyang, Changhai Ma, Ziyu Wu, Heyu Ding, Quan Wan, Yi Ke, Yuchen Wu, Xiaohui Cai

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-12 (更新: 2025-11-13)

**备注**: Accepted by AAAI-2026

**🔗 代码/项目**: [GITHUB](https://github.com/Jiayue-Yuan/PressTrack-HMR)

---

## 💡 一句话要点

**PressTrack-HMR：提出基于压力感知的多人全局人体网格重建方法**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `多人人体网格重建` `压力感知` `触觉传感器` `人体姿态估计` `运动分析` `隐私保护` `跟踪检测`

## 📋 核心要点

1. 传统视觉HMR易受遮挡、光照和隐私影响，而多人场景下压力信号分离是压力HMR的关键挑战。
2. PressTrack-HMR采用自顶向下策略，通过跟踪检测分割个体压力信号，再进行HMR。
3. 实验表明，该方法在多人压力HMR中表现出色，MPJPE达89.2mm，WA-MPJPE$_{100}$达112.6mm。

## 📝 摘要（中文）

多人全局人体网格重建（HMR）对于理解人群动态和交互至关重要。传统的基于视觉的HMR方法在现实场景中面临遮挡、光照不足和隐私问题等限制。人体与地面的触觉交互提供了一种无遮挡且保护隐私的替代方案来捕捉人体运动。现有研究表明，从触觉垫获取的压力信号可以有效地估计单人场景中的人体姿势。然而，当多个个体同时在垫子上随机行走时，如何区分不同人产生的混合压力信号，并随后获取个体的时间压力数据，仍然是将基于压力的HMR扩展到多人情况的挑战。本文提出了PressTrack-HMR，一种仅从压力信号中恢复多人全局人体网格的自顶向下流程。该流程利用跟踪检测策略，首先从原始压力数据中识别和分割每个个体的压力信号，然后对每个提取的个体信号执行HMR。此外，我们构建了一个多人交互压力数据集MIP，以促进进一步研究多人场景中基于压力的运动分析。实验结果表明，我们的方法在基于压力的多人HMR中表现出色，MPJPE为89.2 mm，WA-MPJPE$_{100}$为112.6 mm，展示了触觉垫在普及、保护隐私的多人动作识别方面的潜力。我们的数据集和代码可在https://github.com/Jiayue-Yuan/PressTrack-HMR获取。

## 🔬 方法详解

**问题定义**：论文旨在解决多人场景下，如何仅利用压力传感器数据进行全局人体网格重建的问题。现有基于视觉的方法在多人场景中容易受到遮挡、光照变化以及隐私泄露等问题的限制。虽然基于压力传感器的单人人体姿态估计已经取得了一些进展，但如何区分和分离多个个体产生的混合压力信号，是扩展到多人场景的关键痛点。

**核心思路**：论文的核心思路是采用一种“跟踪-检测”的自顶向下策略。首先，通过跟踪算法检测并分割出每个个体的压力信号，然后对每个分割出的个体压力信号进行独立的人体网格重建。这种方法避免了直接处理混合信号的复杂性，将多人问题分解为多个单人问题。

**技术框架**：PressTrack-HMR的整体框架包含以下几个主要阶段：1) 压力数据采集：通过触觉垫获取原始压力数据。2) 个体压力信号分割：利用跟踪算法（具体算法未知）从原始压力数据中识别和分割出每个个体的压力信号。3) 单人HMR：对每个分割出的个体压力信号，使用单人HMR算法（具体算法未知）进行人体网格重建。4) 全局人体网格重建：将每个个体的人体网格整合到全局坐标系中，得到最终的多人全局人体网格重建结果。

**关键创新**：该论文的关键创新在于提出了一个完整的、基于压力感知的多人全局人体网格重建流程。它将多人HMR问题分解为个体压力信号分割和单人HMR两个子问题，并利用跟踪-检测策略实现了个体压力信号的有效分离。与现有方法相比，该方法无需依赖视觉信息，能够有效应对遮挡、光照变化和隐私问题。

**关键设计**：论文中关于跟踪算法和单人HMR算法的具体细节未知。但是，可以推测，跟踪算法需要能够有效地处理压力信号的噪声和不确定性，并能够准确地跟踪每个个体的运动轨迹。单人HMR算法需要能够从压力信号中提取出足够的信息，以准确地估计人体姿势和形状。

## 📊 实验亮点

实验结果表明，PressTrack-HMR在多人压力HMR任务中取得了显著的性能。具体而言，该方法实现了89.2 mm的MPJPE（Mean Per Joint Position Error）和112.6 mm的WA-MPJPE$_{100}$（Weighted Average MPJPE within 100mm）。这些结果表明，该方法能够有效地从压力信号中恢复多人的人体网格，并具有较高的精度。与未提及的基线方法相比，该方法展示了压力传感器在多人人体运动分析方面的潜力。

## 🎯 应用场景

该研究成果可应用于智能家居、养老监护、运动分析、人机交互等领域。例如，在智能家居中，可以通过压力传感器感知家庭成员的活动状态，实现智能化的环境控制和安全监控。在养老监护中，可以监测老年人的步态和跌倒情况，及时提供帮助。在运动分析中，可以分析运动员的动作姿势，提高训练效果。此外，该技术在保护个人隐私方面具有优势，可用于需要匿名化人体行为分析的场景。

## 📄 摘要（原文）

> Multi-person global human mesh recovery (HMR) is crucial for understanding crowd dynamics and interactions. Traditional vision-based HMR methods sometimes face limitations in real-world scenarios due to mutual occlusions, insufficient lighting, and privacy concerns. Human-floor tactile interactions offer an occlusion-free and privacy-friendly alternative for capturing human motion. Existing research indicates that pressure signals acquired from tactile mats can effectively estimate human pose in single-person scenarios. However, when multiple individuals walk randomly on the mat simultaneously, how to distinguish intermingled pressure signals generated by different persons and subsequently acquire individual temporal pressure data remains a pending challenge for extending pressure-based HMR to the multi-person situation. In this paper, we present \textbf{PressTrack-HMR}, a top-down pipeline that recovers multi-person global human meshes solely from pressure signals. This pipeline leverages a tracking-by-detection strategy to first identify and segment each individual's pressure signal from the raw pressure data, and subsequently performs HMR for each extracted individual signal. Furthermore, we build a multi-person interaction pressure dataset \textbf{MIP}, which facilitates further research into pressure-based human motion analysis in multi-person scenarios. Experimental results demonstrate that our method excels in multi-person HMR using pressure data, with 89.2 $mm$ MPJPE and 112.6 $mm$ WA-MPJPE$_{100}$, and these showcase the potential of tactile mats for ubiquitous, privacy-preserving multi-person action recognition. Our dataset & code are available at https://github.com/Jiayue-Yuan/PressTrack-HMR.

