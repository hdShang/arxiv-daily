---
layout: default
title: Neural B-frame Video Compression with Bi-directional Reference Harmonization
---

# Neural B-frame Video Compression with Bi-directional Reference Harmonization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08938" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08938v1</a>
  <a href="https://arxiv.org/pdf/2511.08938.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08938v1" onclick="toggleFavorite(this, '2511.08938v1', 'Neural B-frame Video Compression with Bi-directional Reference Harmonization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxi Liu, Dengchao Jin, Shuai Huo, Jiawen Gu, Chao Zhou, Huihui Bai, Ming Lu, Zhan Ma

**分类**: cs.CV

**发布日期**: 2025-11-12

**🔗 代码/项目**: [GITHUB](https://github.com/kwai/NVC)

---

## 💡 一句话要点

**提出BRHVC，通过双向参考帧协调优化神经B帧视频压缩性能**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `神经视频压缩` `B帧压缩` `双向参考帧` `运动补偿` `上下文融合`

## 📋 核心要点

1. 神经B帧视频压缩面临挑战，尤其是在分层编码中，双向参考帧的贡献可能不平衡，影响压缩效率。
2. BRHVC通过双向运动收敛（BMC）和双向上下文融合（BCF）来协调双向参考，优化参考信息的利用。
3. 实验结果表明，BRHVC超越了现有NVC方法，甚至在HEVC数据集上超过了传统编码VTM-RA。

## 📝 摘要（中文）

神经视频压缩（NVC）近年来取得了显著进展，但与P帧压缩相比，神经B帧视频压缩（NBVC）的研究仍不充分。NBVC可以采用双向参考帧以获得更好的压缩性能。然而，NBVC的分层编码可能会使连续时间预测复杂化，特别是在一些具有较大帧跨度的层级上，这可能导致两个参考帧的贡献不平衡。为了优化参考信息的利用，我们提出了一种新的NBVC方法，称为双向参考协调视频压缩（BRHVC），它具有提出的双向运动收敛（BMC）和双向上下文融合（BCF）。BMC在运动压缩中融合多个光流，从而实现更大规模上更精确的运动补偿。然后，BCF在运动补偿精度的指导下，显式地建模参考上下文的权重。凭借更有效的运动和上下文，BRHVC可以有效地协调双向参考。实验结果表明，我们的BRHVC优于以前最先进的NVC方法，甚至在HEVC数据集上超过了传统的编码VTM-RA（在随机访问配置下）。源代码已在https://github.com/kwai/NVC上发布。

## 🔬 方法详解

**问题定义**：神经B帧视频压缩(NBVC)旨在利用双向参考帧提高视频压缩效率。然而，NBVC的分层编码结构导致时间预测复杂化，尤其是在帧跨度较大的层级，两个参考帧的贡献可能不平衡，影响压缩性能。现有方法难以有效协调双向参考信息，导致压缩效率受限。

**核心思路**：BRHVC的核心思路是通过双向运动收敛(BMC)和双向上下文融合(BCF)来显式地建模和协调双向参考帧的信息。BMC旨在更精确地估计运动信息，而BCF则根据运动补偿的精度自适应地融合参考上下文，从而优化参考信息的利用。

**技术框架**：BRHVC的整体框架包括以下几个主要模块：1) 运动估计模块：用于估计双向光流；2) 双向运动收敛(BMC)模块：融合多个光流，提高运动补偿的准确性；3) 运动补偿模块：利用收敛后的运动信息进行运动补偿；4) 双向上下文融合(BCF)模块：根据运动补偿的精度，自适应地融合参考上下文；5) 残差编码模块：对运动补偿后的残差进行编码。

**关键创新**：BRHVC的关键创新在于提出了BMC和BCF两个模块。BMC通过融合多个光流来提高运动补偿的准确性，这与传统方法中仅使用单个光流不同。BCF则根据运动补偿的精度自适应地融合参考上下文，这使得模型能够更好地利用参考信息，从而提高压缩效率。

**关键设计**：BMC模块采用了一种加权平均的方法来融合多个光流，权重由光流的置信度决定。BCF模块使用了一个注意力机制来建模参考上下文的权重，注意力权重由运动补偿的精度决定。损失函数包括重建损失、率失真损失等，用于优化模型的性能。具体的网络结构细节和参数设置在论文中有详细描述。

## 📊 实验亮点

BRHVC在HEVC数据集上进行了实验，结果表明，BRHVC优于现有的神经视频压缩方法，甚至超过了传统的视频编码标准VTM-RA（在随机访问配置下）。这表明BRHVC在视频压缩性能方面具有显著的优势，能够有效地提高视频压缩效率。

## 🎯 应用场景

该研究成果可应用于各种视频压缩场景，例如视频会议、在线视频流媒体、视频监控等。通过提高视频压缩效率，可以降低带宽需求，提升用户体验，并降低存储成本。未来，该技术有望应用于更高分辨率、更高帧率的视频压缩，以及移动设备的实时视频压缩。

## 📄 摘要（原文）

> Neural video compression (NVC) has made significant progress in recent years, while neural B-frame video compression (NBVC) remains underexplored compared to P-frame compression. NBVC can adopt bi-directional reference frames for better compression performance. However, NBVC's hierarchical coding may complicate continuous temporal prediction, especially at some hierarchical levels with a large frame span, which could cause the contribution of the two reference frames to be unbalanced. To optimize reference information utilization, we propose a novel NBVC method, termed Bi-directional Reference Harmonization Video Compression (BRHVC), with the proposed Bi-directional Motion Converge (BMC) and Bi-directional Contextual Fusion (BCF). BMC converges multiple optical flows in motion compression, leading to more accurate motion compensation on a larger scale. Then BCF explicitly models the weights of reference contexts under the guidance of motion compensation accuracy. With more efficient motions and contexts, BRHVC can effectively harmonize bi-directional references. Experimental results indicate that our BRHVC outperforms previous state-of-the-art NVC methods, even surpassing the traditional coding, VTM-RA (under random access configuration), on the HEVC datasets. The source code is released at https://github.com/kwai/NVC.

