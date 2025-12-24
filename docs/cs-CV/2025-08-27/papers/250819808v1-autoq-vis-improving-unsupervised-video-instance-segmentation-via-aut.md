---
layout: default
title: "AutoQ-VIS: Improving Unsupervised Video Instance Segmentation via Automatic Quality Assessment"
---

# AutoQ-VIS: Improving Unsupervised Video Instance Segmentation via Automatic Quality Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19808" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19808v1</a>
  <a href="https://arxiv.org/pdf/2508.19808.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19808v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19808v1', 'AutoQ-VIS: Improving Unsupervised Video Instance Segmentation via Automatic Quality Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaixuan Lu, Mehmet Onurcan Kaya, Dim P. Papadopoulos

**分类**: cs.CV

**发布日期**: 2025-08-27

**备注**: Accepted to ICCV 2025 Workshop LIMIT

**🔗 代码/项目**: [GITHUB](https://github.com/wcbup/AutoQ-VIS)

---

## 💡 一句话要点

**提出AutoQ-VIS以解决无监督视频实例分割中的质量评估问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视频实例分割` `无监督学习` `质量评估` `自我训练` `合成数据` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有的无监督视频实例分割方法在处理像素级掩码和时间一致性标签时面临标注困难。
2. AutoQ-VIS通过质量引导的自我训练，建立伪标签生成与质量评估的闭环系统，逐步适应真实视频。
3. 在YouTubeVIS-2019验证集上，AutoQ-VIS的AP50达到了52.6，超越了VideoCutLER，显示出显著的性能提升。

## 📝 摘要（中文）

视频实例分割（VIS）面临显著的标注挑战，因为它需要像素级掩码和时间一致性标签。虽然最近的无监督方法如VideoCutLER通过合成数据消除了光流依赖，但仍受限于合成与真实域之间的差距。我们提出了AutoQ-VIS，这是一种新颖的无监督框架，通过质量引导的自我训练来弥合这一差距。我们的方法在伪标签生成和自动质量评估之间建立了闭环系统，使得从合成视频到真实视频的逐步适应成为可能。实验结果表明，在YouTubeVIS-2019验证集上，AutoQ-VIS达到了52.6的AP50，超越了之前的最先进方法VideoCutLER 4.4个百分点，同时无需人工标注。这证明了质量感知自我训练在无监督VIS中的可行性。

## 🔬 方法详解

**问题定义**：视频实例分割需要同时处理像素级掩码和时间一致性标签，现有无监督方法如VideoCutLER虽然消除了光流依赖，但仍面临合成与真实视频之间的域差距问题。

**核心思路**：AutoQ-VIS通过质量引导的自我训练方法，建立伪标签生成与自动质量评估之间的闭环，旨在有效地从合成视频适应到真实视频。

**技术框架**：该方法的整体架构包括伪标签生成模块和质量评估模块，二者相互作用，形成一个闭环系统。伪标签生成模块负责生成初步的实例分割结果，而质量评估模块则对这些结果进行评估并反馈，以改进伪标签的质量。

**关键创新**：AutoQ-VIS的主要创新在于引入了质量感知的自我训练机制，使得模型能够在无监督的情况下逐步提高对真实视频的适应能力，这与传统方法的静态训练方式有本质区别。

**关键设计**：在设计上，AutoQ-VIS采用了特定的损失函数来平衡伪标签的生成和质量评估，同时在网络结构上进行了优化，以提高模型对视频内容的理解能力。

## 📊 实验亮点

在实验中，AutoQ-VIS在YouTubeVIS-2019验证集上达到了52.6的AP50，超越了之前的最先进方法VideoCutLER 4.4个百分点，显示出其在无监督视频实例分割任务中的卓越性能，且无需任何人工标注。

## 🎯 应用场景

该研究的潜在应用场景包括自动视频编辑、监控视频分析和智能交通系统等领域。通过无监督的视频实例分割，能够降低人工标注成本，提高视频处理的效率和准确性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Video Instance Segmentation (VIS) faces significant annotation challenges due to its dual requirements of pixel-level masks and temporal consistency labels. While recent unsupervised methods like VideoCutLER eliminate optical flow dependencies through synthetic data, they remain constrained by the synthetic-to-real domain gap. We present AutoQ-VIS, a novel unsupervised framework that bridges this gap through quality-guided self-training. Our approach establishes a closed-loop system between pseudo-label generation and automatic quality assessment, enabling progressive adaptation from synthetic to real videos. Experiments demonstrate state-of-the-art performance with 52.6 $\text{AP}_{50}$ on YouTubeVIS-2019 val set, surpassing the previous state-of-the-art VideoCutLER by 4.4$\%$, while requiring no human annotations. This demonstrates the viability of quality-aware self-training for unsupervised VIS. The source code of our method is available at https://github.com/wcbup/AutoQ-VIS.

