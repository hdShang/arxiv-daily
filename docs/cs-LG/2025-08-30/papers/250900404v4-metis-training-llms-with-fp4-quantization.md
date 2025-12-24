---
layout: default
title: "Metis: Training LLMs with FP4 Quantization"
---

# Metis: Training LLMs with FP4 Quantization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00404" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00404v4</a>
  <a href="https://arxiv.org/pdf/2509.00404.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00404v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00404v4', 'Metis: Training LLMs with FP4 Quantization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hengjie Cao, Mengyi Chen, Yifeng Yang, Ruijun Huang, Fang Dong, Jixian Zhou, Anrui Chen, Mingzhi Dong, Yujiang Wang, Jinlong Hou, Yuan Cheng, Fan Wu, Fan Yang, Tun Lu, Ning Gu, Li Shang

**分类**: cs.LG

**发布日期**: 2025-08-30 (更新: 2025-09-30)

---

## 💡 一句话要点

**提出Metis框架以解决大语言模型低位训练中的量化偏差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化训练` `大语言模型` `谱域量化` `低位训练` `机器学习`

## 📋 核心要点

1. 现有方法在低位训练大语言模型时面临量化偏差和谱失真的挑战，影响训练性能。
2. Metis框架通过将各向异性谱划分为更窄的子分布进行独立量化，减少误差并保持谱结构。
3. 在LLaMA-3 8B模型上，Metis实现了仅0.4%的训练损失差距和0.1%的准确度下降，显著优于BF16和Nvidia的FP4方案。

## 📝 摘要（中文）

本研究识别出参数、激活和梯度的奇异值谱中的各向异性，认为这是大语言模型（LLMs）低位训练的根本障碍。这些谱由少量大奇异值主导，导致数值范围宽广，从而引发量化偏差和严重的谱失真，最终降低训练性能。为此，本文提出了Metis，一个谱域量化框架，通过将各向异性谱划分为更窄的子分布进行独立量化，从而减少误差并保持谱结构。Metis在LLaMA-3 8B模型上进行训练，使用100B个token，能够实现W4A4G4的稳健训练，FP4量化的权重、激活和梯度仅导致0.4%的训练损失差距和0.1%的下游准确度下降，相较于BF16，Metis不仅匹配了BF16的精度，还超越了Nvidia最近发布的FP4方案，实现了更低的损失和更高的下游准确度，同时显著降低了计算开销。

## 🔬 方法详解

**问题定义**：本论文旨在解决大语言模型低位训练中的量化偏差和谱失真问题。现有方法由于奇异值谱的各向异性，导致数值范围过宽，影响训练效果。

**核心思路**：提出Metis框架，通过将奇异值谱划分为更窄的子分布进行独立量化，从而减少量化误差并保持谱的结构特征。该设计旨在解决现有方法的局限性，提升训练性能。

**技术框架**：Metis的整体架构包括两个主要模块：1) 稀疏随机采样以保持主谱子空间，2) 随机投影以降低分解成本。通过这两个模块，Metis能够有效地进行谱域量化。

**关键创新**：Metis的核心创新在于其谱域量化方法，能够将各向异性谱划分为独立的子分布，这一方法与传统的量化技术有本质区别，显著降低了量化引起的误差。

**关键设计**：在参数设置上，Metis采用FP4量化方案，损失函数设计上注重减少量化误差，网络结构上则保持了主谱子空间的稀疏性和随机性，以确保高效的计算性能。

## 📊 实验亮点

在LLaMA-3 8B模型的实验中，Metis实现了仅0.4%的训练损失差距和0.1%的准确度下降，相较于BF16，Metis不仅匹配了其精度，还在性能上超越了Nvidia的FP4方案，表现出更低的损失和更高的下游准确度，同时显著降低了计算开销。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等大语言模型的训练。通过提高低位训练的效率和准确性，Metis能够在资源受限的环境中实现更高效的模型训练，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> This work identifies anisotropy in the singular value spectra of parameters, activations, and gradients as the fundamental barrier to low-bit training of large language models (LLMs). These spectra are dominated by a small fraction of large singular values, inducing wide numerical ranges that cause quantization bias and severe spectral distortion, ultimately degrading training performance. This work presents Metis, a spectral-domain quantization framework that partitions anisotropic spectra into narrower sub-distributions for independent quantization, thereby reducing errors and preserving spectral structure. To minimize overhead, Metis leverages two key properties of the dominant spectral subspace: preservation via sparsely random sampling and preservation via random projection, reducing decomposition cost to a negligible level. On LLaMA-3 8B trained with 100B tokens, Metis enables robust W4A4G4 training with FP4 quantization of weights, activations, and gradients, yielding only a 0.4% training loss gap and a 0.1% degradation in downstream accuracy relative to BF16. Beyond matching BF16 fidelity, Metis also surpasses our implementation of Nvidia's recently announced (yet to be publicly released) FP4 recipe, consistently achieving lower loss and higher downstream accuracy while incurring significantly lower computational overhead. The code implementation for Metis is available at: https://anonymous.4open.science/r/Metis-quantization-644B.

