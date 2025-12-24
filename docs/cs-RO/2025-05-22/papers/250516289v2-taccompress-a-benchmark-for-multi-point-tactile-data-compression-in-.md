---
layout: default
title: TacCompress: A Benchmark for Multi-Point Tactile Data Compression in Dexterous Hand
---

# TacCompress: A Benchmark for Multi-Point Tactile Data Compression in Dexterous Hand

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.16289" class="toolbar-btn" target="_blank">📄 arXiv: 2505.16289v2</a>
  <a href="https://arxiv.org/pdf/2505.16289.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.16289v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.16289v2', 'TacCompress: A Benchmark for Multi-Point Tactile Data Compression in Dexterous Hand')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yan Zhao, Yang Li, Zhengxue Cheng, Hengdi Zhang, Li Song

**分类**: cs.RO

**发布日期**: 2025-05-22 (更新: 2025-08-28)

**备注**: 9 pages, 10 figures, 2 tables

---

## 💡 一句话要点

**提出TacCompress以解决多点触觉数据压缩问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `触觉数据压缩` `灵巧机器人` `多点触觉传感器` `数据集构建` `无损压缩` `有损压缩` `图像编码` `机器人操作`

## 📋 核心要点

1. 现有的灵巧机器人在操作过程中面临手内遮挡等挑战，导致对细粒度触觉感知的需求增加，进而增加了数据传输的带宽压力。
2. 本文提出了多点触觉数据集Dex-MPTD，并探讨了将触觉数据转换为图像后进行的无损和有损压缩方法，以提高数据传输效率。
3. 实验结果显示，触觉数据可无损压缩至0.0364比特每子样本，压缩比达到200倍，有损压缩器可实现约1000倍的数据减少，且保留了良好的数据质量。

## 📝 摘要（中文）

尽管机器人灵巧操作技术已取得显著进展，但在手内遮挡等挑战下，细粒度触觉感知仍然至关重要，导致更多触觉传感器的集成。然而，基于灵巧手物理结构的多点触觉信号的获取与压缩尚未得到充分研究。本文的贡献有二：首先，我们引入了多点触觉数据集（Dex-MPTD），该数据集捕获了多种物体和抓取姿态下的触觉信号，为灵巧机器人操作研究提供了全面的基准。其次，我们对Dex-MPTD进行了无损和有损压缩研究，通过将触觉数据转换为图像，并应用六种无损和五种有损图像编码器进行高效压缩。实验结果表明，触觉数据可以无损压缩至每个子样本0.0364比特，压缩比约为200倍。有损压缩器如HM和VTM可实现约1000倍的数据减少，同时保持可接受的数据保真度。

## 🔬 方法详解

**问题定义**：本文旨在解决灵巧手中多点触觉信号的获取与压缩问题，现有方法未能有效应对因传感器数量增加而导致的数据传输带宽压力。

**核心思路**：通过引入多点触觉数据集Dex-MPTD，并将触觉数据转换为图像，利用图像编码技术进行高效压缩，以降低数据传输负担。

**技术框架**：整体流程包括数据集的构建、触觉信号的采集、数据转换为图像、以及应用多种图像编码器进行压缩。主要模块包括数据采集模块、图像转换模块和压缩模块。

**关键创新**：最重要的创新在于提出了Dex-MPTD数据集，并探索了无损与有损压缩方法，尤其是发现针对屏幕内容的编码工具在压缩触觉数据方面优于通用编码器。

**关键设计**：在实验中采用了六种无损和五种有损图像编码器，关键参数设置包括压缩比、数据保真度等，确保在压缩过程中尽可能保留触觉信息的完整性。

## 📊 实验亮点

实验结果显示，触觉数据可无损压缩至每个子样本0.0364比特，实现约200倍的压缩比。有损压缩器如HM和VTM能够实现约1000倍的数据减少，同时保持可接受的数据保真度，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、智能制造和人机交互等场景。通过高效的触觉数据压缩，能够提升机器人在复杂环境中的操作能力，降低数据传输成本，推动灵巧机器人技术的进一步发展。

## 📄 摘要（原文）

> Though robotic dexterous manipulation has progressed substantially recently, challenges like in-hand occlusion still necessitate fine-grained tactile perception, leading to the integration of more tactile sensors into robotic hands. Consequently, the increased data volume imposes substantial bandwidth pressure on signal transmission from the hand's controller. However, the acquisition and compression of multi-point tactile signals based on the dexterous hands' physical structures have not been thoroughly explored. In this paper, our contributions are twofold. First, we introduce a Multi-Point Tactile Dataset for Dexterous Hand Grasping (Dex-MPTD). This dataset captures tactile signals from multiple contact sensors across various objects and grasping poses, offering a comprehensive benchmark for advancing dexterous robotic manipulation research. Second, we investigate both lossless and lossy compression on Dex-MPTD by converting tactile data into images and applying six lossless and five lossy image codecs for efficient compression. Experimental results demonstrate that tactile data can be losslessly compressed to as low as 0.0364 bits per sub-sample (bpss), achieving approximately 200$\times$ compression ratio compared to the raw tactile data. Efficient lossy compressors like HM and VTM can achieve about 1000$\times$ data reductions while preserving acceptable data fidelity. The exploration of lossy compression also reveals that screen-content-targeted coding tools outperform general-purpose codecs in compressing tactile data.

