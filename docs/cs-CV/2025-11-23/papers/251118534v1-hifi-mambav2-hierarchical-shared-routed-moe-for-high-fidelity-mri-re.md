---
layout: default
title: HiFi-MambaV2: Hierarchical Shared-Routed MoE for High-Fidelity MRI Reconstruction
---

# HiFi-MambaV2: Hierarchical Shared-Routed MoE for High-Fidelity MRI Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18534" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18534v1</a>
  <a href="https://arxiv.org/pdf/2511.18534.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18534v1" onclick="toggleFavorite(this, '2511.18534v1', 'HiFi-MambaV2: Hierarchical Shared-Routed MoE for High-Fidelity MRI Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengcheng Fang, Hongli Chen, Guangzhen Yao, Jian Shi, Fangfang Tang, Xiaohao Cai, Shanshan Shan, Feng Liu

**分类**: cs.CV

**发布日期**: 2025-11-23

---

## 💡 一句话要点

**HiFi-MambaV2：用于高保真MRI重建的分层共享路由MoE Mamba架构**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `MRI重建` `混合专家模型` `Mamba架构` `频率分解` `医学影像` `深度学习` `数据一致性`

## 📋 核心要点

1. 现有MRI重建方法难以在恢复高频细节的同时保持解剖结构的连贯性，导致图像质量受限。
2. HiFi-MambaV2通过结合频率分解和内容自适应计算，利用分层共享路由MoE Mamba架构实现高保真重建。
3. 实验结果表明，HiFi-MambaV2在多个数据集上显著优于CNN、Transformer和现有Mamba方法，提升了图像质量。

## 📝 摘要（中文）

本文提出HiFi-MambaV2，一种分层共享路由的混合专家(MoE) Mamba架构，用于从欠采样的k空间数据中重建高保真MR图像。该模型将频率分解与内容自适应计算相结合。它包含两个核心组件：(i) 可分离的频率一致拉普拉斯金字塔(SF-Lap)，提供抗混叠、稳定的低频和高频流；(ii) 分层共享路由MoE，执行逐像素的top-1稀疏调度到共享专家和本地路由器，实现有效的专业化和稳定的跨深度行为。一个轻量级的全局上下文路径被融合到一个展开的、数据一致性正则化的骨干网络中，以加强长程推理并保持解剖学连贯性。在fastMRI、CC359、ACDC、M4Raw和Prostate158上的评估表明，HiFi-MambaV2在单线圈和多线圈设置以及多个加速因子下，在PSNR、SSIM和NMSE方面始终优于基于CNN、Transformer和先前的基于Mamba的基线，并在高频细节和整体结构保真度方面持续改进。这些结果表明HiFi-MambaV2能够实现可靠且鲁棒的MRI重建。

## 🔬 方法详解

**问题定义**：论文旨在解决从欠采样k空间数据重建高保真MRI图像的问题。现有方法，包括基于CNN和Transformer的方法，难以同时恢复高频细节并保持解剖结构的连贯性，导致重建图像模糊或失真。

**核心思路**：论文的核心思路是将频率分解与内容自适应计算相结合。通过将图像分解为低频和高频分量，并使用MoE结构进行内容自适应处理，模型能够更好地捕捉图像的细节和结构信息。Mamba架构的使用则有助于捕捉序列依赖关系。

**技术框架**：HiFi-MambaV2的整体架构包含以下几个主要模块：(1) 可分离的频率一致拉普拉斯金字塔(SF-Lap)：用于将输入图像分解为低频和高频分量。(2) 分层共享路由MoE：用于对不同频率分量进行内容自适应处理，其中包含共享专家和本地路由器。(3) 轻量级全局上下文路径：用于捕捉图像的全局信息，并保持解剖结构的连贯性。(4) 数据一致性正则化的骨干网络：用于保证重建图像与原始k空间数据的一致性。

**关键创新**：该论文的关键创新在于：(1) 提出了可分离的频率一致拉普拉斯金字塔(SF-Lap)，能够有效地分离低频和高频分量，并减少混叠伪影。(2) 提出了分层共享路由MoE，能够根据输入内容自适应地选择不同的专家进行处理，提高模型的表达能力。(3) 将全局上下文路径融入到骨干网络中，能够更好地捕捉图像的全局信息，并保持解剖结构的连贯性。

**关键设计**：SF-Lap采用可分离的卷积操作，降低了计算复杂度。MoE结构采用top-1稀疏调度，保证了计算效率。全局上下文路径采用轻量级的设计，避免了引入过多的计算开销。数据一致性正则化采用标准的k空间一致性损失函数。具体的网络结构参数（如卷积核大小、通道数等）和损失函数权重等细节在论文中有详细描述。

## 📊 实验亮点

HiFi-MambaV2在fastMRI、CC359、ACDC、M4Raw和Prostate158等多个数据集上进行了评估，结果表明其在PSNR、SSIM和NMSE等指标上均优于现有的CNN、Transformer和Mamba方法。例如，在fastMRI数据集上，HiFi-MambaV2在加速因子为4的情况下，PSNR提升了超过1dB，SSIM提升了0.01，表明其在高频细节和整体结构保真度方面具有显著优势。

## 🎯 应用场景

HiFi-MambaV2在医学影像领域具有广泛的应用前景，可以用于提高MRI图像的重建质量，从而辅助医生进行更准确的诊断。该技术可以应用于各种MRI扫描，包括脑部、心脏、腹部等，并可以与其他医学影像技术相结合，例如CT和PET，以提供更全面的诊断信息。此外，该技术还可以应用于低剂量MRI扫描，以减少患者的辐射暴露。

## 📄 摘要（原文）

> Reconstructing high-fidelity MR images from undersampled k-space data requires recovering high-frequency details while maintaining anatomical coherence. We present HiFi-MambaV2, a hierarchical shared-routed Mixture-of-Experts (MoE) Mamba architecture that couples frequency decomposition with content-adaptive computation. The model comprises two core components: (i) a separable frequency-consistent Laplacian pyramid (SF-Lap) that delivers alias-resistant, stable low- and high-frequency streams; and (ii) a hierarchical shared-routed MoE that performs per-pixel top-1 sparse dispatch to shared experts and local routers, enabling effective specialization with stable cross-depth behavior. A lightweight global context path is fused into an unrolled, data-consistency-regularized backbone to reinforce long-range reasoning and preserve anatomical coherence. Evaluated on fastMRI, CC359, ACDC, M4Raw, and Prostate158, HiFi-MambaV2 consistently outperforms CNN-, Transformer-, and prior Mamba-based baselines in PSNR, SSIM, and NMSE across single- and multi-coil settings and multiple acceleration factors, consistently surpassing consistent improvements in high-frequency detail and overall structural fidelity. These results demonstrate that HiFi-MambaV2 enables reliable and robust MRI reconstruction.

