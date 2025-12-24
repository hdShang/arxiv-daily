---
layout: default
title: "MambaVSR: Content-Aware Scanning State Space Model for Video Super-Resolution"
---

# MambaVSR: Content-Aware Scanning State Space Model for Video Super-Resolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11768" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11768v1</a>
  <a href="https://arxiv.org/pdf/2506.11768.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11768v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11768v1', 'MambaVSR: Content-Aware Scanning State Space Model for Video Super-Resolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linfeng He, Meiqin Liu, Qi Tang, Chao Yao, Yao Zhao

**分类**: cs.CV

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出MambaVSR以解决视频超分辨率中的非局部依赖建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `视频超分辨率` `内容感知` `状态空间模型` `共享指南构建` `动态时空交互` `高频细节恢复` `稀疏注意力` `非局部依赖`

## 📋 核心要点

1. 现有视频超分辨率方法在处理错位帧的非局部依赖性时效率低下，尤其在大运动和长序列中表现不佳。
2. MambaVSR引入了内容感知扫描机制，通过共享指南构建和内容感知序列化实现动态时空交互，提升了模型性能。
3. 实验结果显示，MambaVSR在REDS数据集上比现有变换器方法提高了0.58 dB PSNR，且参数量减少了55%。

## 📝 摘要（中文）

视频超分辨率（VSR）在有效建模错位帧之间的非局部依赖性以及保持计算效率方面面临重大挑战。现有方法通常依赖光流策略或变换器架构，但在大运动位移和长视频序列中表现不佳。为此，本文提出了MambaVSR，这是第一个将创新的内容感知扫描机制纳入VSR的状态空间模型框架。MambaVSR通过共享指南构建（SCC）和内容感知序列化（CAS）模块，实现了动态时空交互，显著提升了视频超分辨率的性能。实验结果表明，MambaVSR在REDS数据集上比基于变换器的方法提高了0.58 dB PSNR，同时参数量减少了55%。

## 🔬 方法详解

**问题定义**：本文旨在解决视频超分辨率中的非局部依赖建模问题，现有方法在处理错位帧时效率低下，尤其在大运动和长视频序列中表现不佳。

**核心思路**：MambaVSR通过引入内容感知扫描机制，结合共享指南构建（SCC）和内容感知序列化（CAS），实现动态时空交互，从而有效对齐和聚合多帧中的相似内容。

**技术框架**：MambaVSR的整体架构包括SCC模块和CAS模块。SCC模块通过稀疏注意力构建帧内语义连接图，并利用谱聚类生成自适应空间扫描序列；CAS模块则通过交错时间特征来对齐和聚合多帧内容。

**关键创新**：MambaVSR的核心创新在于其内容感知扫描机制，能够动态处理时空交互，区别于传统的刚性1D序列处理方式，显著提升了视频超分辨率的效果。

**关键设计**：在设计中，SCC模块采用稀疏注意力机制以提高计算效率，CAS模块则通过学习的空间顺序交错时间特征来实现非局部内容的聚合，确保了全局依赖与局部细节的有效结合。

## 📊 实验亮点

MambaVSR在REDS数据集上的实验结果显示，其PSNR比基于变换器的方法提高了0.58 dB，同时参数量减少了55%。这一显著的性能提升证明了其在视频超分辨率任务中的有效性和优势。

## 🎯 应用场景

MambaVSR在视频超分辨率领域具有广泛的应用潜力，尤其适用于需要高质量视频重建的场景，如视频监控、影视制作和虚拟现实等。其高效的模型设计和优越的性能将推动相关技术的进一步发展和应用。

## 📄 摘要（原文）

> Video super-resolution (VSR) faces critical challenges in effectively modeling non-local dependencies across misaligned frames while preserving computational efficiency. Existing VSR methods typically rely on optical flow strategies or transformer architectures, which struggle with large motion displacements and long video sequences. To address this, we propose MambaVSR, the first state-space model framework for VSR that incorporates an innovative content-aware scanning mechanism. Unlike rigid 1D sequential processing in conventional vision Mamba methods, our MambaVSR enables dynamic spatiotemporal interactions through the Shared Compass Construction (SCC) and the Content-Aware Sequentialization (CAS). Specifically, the SCC module constructs intra-frame semantic connectivity graphs via efficient sparse attention and generates adaptive spatial scanning sequences through spectral clustering. Building upon SCC, the CAS module effectively aligns and aggregates non-local similar content across multiple frames by interleaving temporal features along the learned spatial order. To bridge global dependencies with local details, the Global-Local State Space Block (GLSSB) synergistically integrates window self-attention operations with SSM-based feature propagation, enabling high-frequency detail recovery under global dependency guidance. Extensive experiments validate MambaVSR's superiority, outperforming the Transformer-based method by 0.58 dB PSNR on the REDS dataset with 55% fewer parameters.

