---
layout: default
title: "S$^2$Q-VDiT: Accurate Quantized Video Diffusion Transformer with Salient Data and Sparse Token Distillation"
---

# S$^2$Q-VDiT: Accurate Quantized Video Diffusion Transformer with Salient Data and Sparse Token Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04016" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04016v3</a>
  <a href="https://arxiv.org/pdf/2508.04016.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04016v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04016v3', 'S$^2$Q-VDiT: Accurate Quantized Video Diffusion Transformer with Salient Data and Sparse Token Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weilun Feng, Haotong Qin, Chuanguang Yang, Xiangqi Li, Han Yang, Yuqi Li, Zhulin An, Libo Huang, Michele Magno, Yongjun Xu

**分类**: cs.CV

**发布日期**: 2025-08-06 (更新: 2025-10-27)

**🔗 代码/项目**: [GITHUB](https://github.com/wlfeng0509/s2q-vdit)

---

## 💡 一句话要点

**提出S$^2$Q-VDiT以解决视频扩散模型的量化与学习挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频生成` `扩散变换器` `量化技术` `稀疏注意力` `模型压缩` `深度学习`

## 📋 核心要点

1. 现有的视频扩散模型在参数量上达到数十亿，导致计算成本高昂，推理效率低下。
2. 提出S$^2$Q-VDiT，通过Hessian-aware显著数据选择和注意力引导的稀疏token蒸馏，优化量化过程和学习效率。
3. 在W4A6量化下，S$^2$Q-VDiT实现了3.9倍的模型压缩和1.3倍的推理加速，表现出色。

## 📝 摘要（中文）

扩散变换器已成为视频生成模型的主流范式，但其数十亿参数导致显著的计算成本。量化技术通过减少内存使用和加速推理提供了有效解决方案。然而，视频扩散模型中空间与时间信息的联合建模导致极长的token序列，增加了校准方差和学习难度。为此，本文提出了S$^2$Q-VDiT，一个后训练量化框架，利用显著数据和稀疏token蒸馏。在校准阶段，量化性能对校准数据的选择高度敏感。为此，我们引入了Hessian-aware显著数据选择，构建高质量的校准数据集。同时，针对学习挑战，我们分析了V-DMs中固有的稀疏注意力模式，提出了基于注意力的稀疏token蒸馏。S$^2$Q-VDiT在W4A6量化下实现了无损性能，同时提供了3.9倍的模型压缩和1.3倍的推理加速。

## 🔬 方法详解

**问题定义**：本文旨在解决视频扩散模型在量化过程中面临的高计算成本和学习挑战。现有方法在处理长token序列时，容易引入高校准方差，影响模型性能。

**核心思路**：S$^2$Q-VDiT通过引入Hessian-aware显著数据选择和注意力引导的稀疏token蒸馏，优化了校准数据的质量和学习过程，旨在提高量化性能和模型效率。

**技术框架**：整体架构包括两个主要模块：Hessian-aware显著数据选择用于构建高质量的校准数据集，注意力引导的稀疏token蒸馏则用于优化模型的学习过程。

**关键创新**：最重要的创新在于结合了显著数据选择和稀疏token蒸馏，针对视频扩散模型的特性进行优化，显著提高了量化性能与学习效率。

**关键设计**：在参数设置上，采用W4A6量化策略，设计了特定的损失函数以适应稀疏注意力模式，并通过token-wise注意力分布来强调对模型输出影响较大的token。

## 📊 实验亮点

S$^2$Q-VDiT在W4A6量化下实现了无损性能，模型压缩率达到3.9倍，推理速度提升1.3倍，相较于现有基线表现出显著的性能提升，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括视频生成、实时视频处理和智能监控等。通过提高视频扩散模型的效率，S$^2$Q-VDiT能够在资源受限的环境中实现高质量的视频生成，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Diffusion transformers have emerged as the mainstream paradigm for video generation models. However, the use of up to billions of parameters incurs significant computational costs. Quantization offers a promising solution by reducing memory usage and accelerating inference. Nonetheless, we observe that the joint modeling of spatial and temporal information in video diffusion models (V-DMs) leads to extremely long token sequences, which introduces high calibration variance and learning challenges. To address these issues, we propose S$^2$Q-VDiT, a post-training quantization framework for V-DMs that leverages Salient data and Sparse token distillation. During the calibration phase, we identify that quantization performance is highly sensitive to the choice of calibration data. To mitigate this, we introduce \textit{Hessian-aware Salient Data Selection}, which constructs high-quality calibration datasets by considering both diffusion and quantization characteristics unique to V-DMs. To tackle the learning challenges, we further analyze the sparse attention patterns inherent in V-DMs. Based on this observation, we propose \textit{Attention-guided Sparse Token Distillation}, which exploits token-wise attention distributions to emphasize tokens that are more influential to the model's output. Under W4A6 quantization, S$^2$Q-VDiT achieves lossless performance while delivering $3.9\times$ model compression and $1.3\times$ inference acceleration. Code will be available at https://github.com/wlfeng0509/s2q-vdit.

