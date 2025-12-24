---
layout: default
title: "MEMFOF: High-Resolution Training for Memory-Efficient Multi-Frame Optical Flow Estimation"
---

# MEMFOF: High-Resolution Training for Memory-Efficient Multi-Frame Optical Flow Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23151" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23151v1</a>
  <a href="https://arxiv.org/pdf/2506.23151.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23151v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23151v1', 'MEMFOF: High-Resolution Training for Memory-Efficient Multi-Frame Optical Flow Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vladislav Bargatin, Egor Chistov, Alexander Yakovenko, Dmitriy Vatolin

**分类**: cs.CV, cs.AI, cs.MM

**发布日期**: 2025-06-29

**备注**: Accepted at ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/msu-video-group/memfof)

---

## 💡 一句话要点

**提出MEMFOF以解决高分辨率光流估计中的内存效率问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `光流估计` `高分辨率训练` `内存效率` `多帧估计` `深度学习`

## 📋 核心要点

1. 现有光流估计方法在高分辨率输入下，GPU内存消耗过大，影响了实际应用。
2. MEMFOF通过优化多帧估计与内存使用的平衡，实现了高效的光流估计，支持1080p原生训练。
3. 实验结果显示，MEMFOF在多个基准测试中表现优异，准确率和运行效率均优于资源消耗更大的替代方案。

## 📝 摘要（中文）

近年来，光流估计的进展虽然提高了准确性，但在高分辨率（FullHD）输入下，GPU内存消耗显著增加。本文提出MEMFOF，一种内存高效的多帧光流方法，能够在多帧估计与GPU内存使用之间找到良好的平衡。MEMFOF在1080p输入下运行时仅需2.09 GB的GPU内存，训练时为28.5 GB，允许在原生1080p下进行训练，无需裁剪或下采样。通过系统性地回顾RAFT类架构的设计选择，结合减少的相关体积和高分辨率训练协议，MEMFOF在多个基准测试中实现了最先进的性能，同时显著降低了内存开销。

## 🔬 方法详解

**问题定义**：本文旨在解决高分辨率光流估计中GPU内存消耗过大的问题。现有方法在处理1080p输入时，往往需要大量内存，限制了其应用场景。

**核心思路**：MEMFOF通过引入内存高效的多帧光流估计方法，优化了多帧估计过程与GPU内存使用之间的权衡，允许在不裁剪或下采样的情况下进行高分辨率训练。

**技术框架**：MEMFOF的整体架构包括多个模块，首先是输入图像的预处理，然后是多帧光流的估计，最后通过高分辨率训练协议进行优化。该方法结合了减少的相关体积，提升了计算效率。

**关键创新**：MEMFOF的主要创新在于其内存效率，能够在仅需2.09 GB的运行内存和28.5 GB的训练内存下实现高分辨率光流估计，显著优于传统方法。

**关键设计**：在设计上，MEMFOF采用了优化的损失函数和网络结构，减少了相关体积的计算，同时保持了高分辨率输入的处理能力。

## 📊 实验亮点

在实验中，MEMFOF在Spring基准测试中以3.289的1像素异常率排名第一，在Sintel（干净）数据集上以0.963的端点误差（EPE）领先，并在KITTI-2015上实现了2.94%的最佳Fl-all误差，展示了其在准确性和运行效率上的显著优势。

## 🎯 应用场景

MEMFOF在视频分析、自动驾驶、运动捕捉等领域具有广泛的应用潜力。其高效的内存使用和准确的光流估计能力，使其能够在资源受限的环境中实现实时处理，推动了相关技术的发展。

## 📄 摘要（原文）

> Recent advances in optical flow estimation have prioritized accuracy at the cost of growing GPU memory consumption, particularly for high-resolution (FullHD) inputs. We introduce MEMFOF, a memory-efficient multi-frame optical flow method that identifies a favorable trade-off between multi-frame estimation and GPU memory usage. Notably, MEMFOF requires only 2.09 GB of GPU memory at runtime for 1080p inputs, and 28.5 GB during training, which uniquely positions our method to be trained at native 1080p without the need for cropping or downsampling. We systematically revisit design choices from RAFT-like architectures, integrating reduced correlation volumes and high-resolution training protocols alongside multi-frame estimation, to achieve state-of-the-art performance across multiple benchmarks while substantially reducing memory overhead. Our method outperforms more resource-intensive alternatives in both accuracy and runtime efficiency, validating its robustness for flow estimation at high resolutions. At the time of submission, our method ranks first on the Spring benchmark with a 1-pixel (1px) outlier rate of 3.289, leads Sintel (clean) with an endpoint error (EPE) of 0.963, and achieves the best Fl-all error on KITTI-2015 at 2.94%. The code is available at https://github.com/msu-video-group/memfof.

