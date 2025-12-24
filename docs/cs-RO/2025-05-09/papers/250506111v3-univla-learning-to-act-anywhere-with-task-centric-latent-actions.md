---
layout: default
title: "UniVLA: Learning to Act Anywhere with Task-centric Latent Actions"
---

# UniVLA: Learning to Act Anywhere with Task-centric Latent Actions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06111" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06111v3</a>
  <a href="https://arxiv.org/pdf/2505.06111.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06111v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06111v3', 'UniVLA: Learning to Act Anywhere with Task-centric Latent Actions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingwen Bu, Yanting Yang, Jisong Cai, Shenyuan Gao, Guanghui Ren, Maoqing Yao, Ping Luo, Hongyang Li

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-09 (更新: 2025-11-03)

**备注**: Accepted to RSS 2025. Code is available at https://github.com/OpenDriveLab/UniVLA

---

## 💡 一句话要点

**提出UniVLA以解决机器人跨环境学习能力不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨体现学习` `视觉-语言-动作` `潜在动作模型` `机器人政策学习` `多模态融合` `任务中心表示` `数据高效利用`

## 📋 核心要点

1. 现有方法依赖于大量动作标注数据，导致机器人在不同环境和体现中学习能力受限。
2. UniVLA通过潜在动作模型从视频中提取任务中心的动作表示，增强了跨环境的学习能力。
3. 在多个基准测试中，UniVLA的性能超过OpenVLA，且预训练计算量和下游数据需求显著降低。

## 📝 摘要（中文）

一般化机器人应在多种环境中有效执行任务。然而，现有方法往往依赖于扩展带有动作标注的数据，导致其能力受限于单一物理规格，难以在不同的体现和环境中学习可转移的知识。为了解决这些局限性，本文提出了UniVLA，一个用于学习跨体现视觉-语言-动作（VLA）策略的新框架。其核心创新在于通过潜在动作模型从视频中推导任务中心的动作表示，从而利用广泛的跨体现和视角的数据。通过引入语言指令并在DINO特征空间内建立潜在动作模型，UniVLA在多个操作和导航基准测试中取得了最先进的结果，并在真实机器人部署中表现出色。

## 🔬 方法详解

**问题定义**：本文旨在解决现有机器人学习方法在不同环境和体现中知识迁移能力不足的问题。现有方法通常依赖于大量的动作标注数据，导致其在多样化环境中的适应性差。

**核心思路**：UniVLA的核心思路是通过潜在动作模型从视频中提取任务中心的动作表示，结合语言指令来减轻任务无关动态的影响，从而实现跨体现的学习。

**技术框架**：UniVLA的整体架构包括数据收集、潜在动作模型的训练、特征提取和策略学习等模块。通过在DINO特征空间内建立潜在动作模型，系统能够高效解码动作并应用于不同机器人。

**关键创新**：UniVLA的主要创新在于其任务中心的动作表示提取方法，能够有效利用互联网规模的视频数据，并在不同机器人间实现策略的迁移。这一方法与现有的依赖单一物理规格的策略学习方法本质上不同。

**关键设计**：在设计中，UniVLA采用了特定的损失函数以优化动作表示的学习，并在网络结构上结合了DINO特征提取技术，以增强模型的泛化能力。

## 📊 实验亮点

在多个操作和导航基准测试中，UniVLA的性能超过了OpenVLA，预训练计算量减少至不足1/20，下游数据需求降低至1/10。随着异构数据的持续引入，模型的性能持续提升，显示出其在机器人政策学习中的巨大潜力。

## 🎯 应用场景

UniVLA的研究成果在多种机器人应用场景中具有广泛的潜在价值，包括家庭服务机器人、工业自动化和探索性机器人等。其高效的策略学习能力将推动机器人在复杂环境中的自主决策和操作能力，未来可能在智能制造和人机协作等领域产生深远影响。

## 📄 摘要（原文）

> A generalist robot should perform effectively across various environments. However, most existing approaches heavily rely on scaling action-annotated data to enhance their capabilities. Consequently, they are often limited to single physical specification and struggle to learn transferable knowledge across different embodiments and environments. To confront these limitations, we propose UniVLA, a new framework for learning cross-embodiment vision-language-action (VLA) policies. Our key innovation is to derive task-centric action representations from videos with a latent action model. This enables us to exploit extensive data across a wide spectrum of embodiments and perspectives. To mitigate the effect of task-irrelevant dynamics, we incorporate language instructions and establish a latent action model within the DINO feature space. Learned from internet-scale videos, the generalist policy can be deployed to various robots through efficient latent action decoding. We obtain state-of-the-art results across multiple manipulation and navigation benchmarks, as well as real-robot deployments. UniVLA achieves superior performance over OpenVLA with less than 1/20 of pretraining compute and 1/10 of downstream data. Continuous performance improvements are observed as heterogeneous data, even including human videos, are incorporated into the training pipeline. The results underscore UniVLA's potential to facilitate scalable and efficient robot policy learning.

