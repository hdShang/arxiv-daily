---
layout: default
title: "RMT-KD: Random Matrix Theoretic Causal Knowledge Distillation"
---

# RMT-KD: Random Matrix Theoretic Causal Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15724" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15724v3</a>
  <a href="https://arxiv.org/pdf/2509.15724.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15724v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15724v3', 'RMT-KD: Random Matrix Theoretic Causal Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Davide Ettori, Nastaran Darabi, Sureshkumar Senthilkumar, Amit Ranjan Trivedi

**分类**: cs.LG

**发布日期**: 2025-09-19 (更新: 2025-09-29)

**备注**: 5 pages, submitted to ICASSP 2026, September 2025

---

## 💡 一句话要点

**提出RMT-KD以解决深度学习模型压缩问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `知识蒸馏` `随机矩阵理论` `模型压缩` `深度学习` `边缘计算` `自蒸馏` `性能优化`

## 📋 核心要点

1. 现有的大型深度学习模型在边缘设备上部署面临高计算和存储成本的挑战。
2. RMT-KD通过随机矩阵理论进行知识蒸馏，逐层保留有用的信息方向，从而有效压缩模型。
3. 在多个基准数据集上，RMT-KD实现了显著的参数减少和推理速度提升，同时保持了较高的准确率。

## 📝 摘要（中文）

大型深度学习模型如BERT和ResNet在性能上处于领先地位，但由于其体积和计算需求，难以在边缘设备上部署。本文提出了一种名为RMT-KD的压缩方法，利用随机矩阵理论（RMT）进行知识蒸馏，逐步减少网络规模。RMT-KD通过保留隐藏表示的谱特性识别的有信息方向，避免了剪枝或启发式秩选择。该方法逐层应用RMT因果降维，并结合自蒸馏以保持稳定性和准确性。在GLUE、AG News和CIFAR-10数据集上，RMT-KD实现了高达80%的参数减少，仅损失2%的准确率，推理速度提高了2.8倍，功耗几乎减半。这些结果确立了RMT-KD作为一种数学基础的网络蒸馏方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大型深度学习模型在边缘设备上部署时的高计算和存储成本问题。现有方法如剪枝和启发式秩选择存在信息损失和不稳定性等痛点。

**核心思路**：RMT-KD的核心思想是利用随机矩阵理论，通过分析隐藏表示的谱特性，保留有信息的方向，从而实现有效的知识蒸馏和模型压缩。

**技术框架**：RMT-KD的整体架构包括逐层应用RMT因果降维和自蒸馏过程。首先，通过RMT分析隐藏层的特征，然后选择保留的方向，最后进行自蒸馏以确保模型的稳定性和准确性。

**关键创新**：RMT-KD的主要创新在于引入随机矩阵理论作为知识蒸馏的基础，区别于传统的剪枝方法，能够更好地保留模型的有效信息。

**关键设计**：在参数设置上，RMT-KD通过谱特性选择保留的方向，损失函数设计为平衡压缩率与准确率，网络结构上则采用层级自蒸馏策略以增强模型的稳定性。

## 📊 实验亮点

RMT-KD在GLUE、AG News和CIFAR-10数据集上表现出色，最高实现80%的参数减少，准确率仅损失2%。此外，推理速度提升了2.8倍，功耗几乎减半，显示出其在模型压缩和加速方面的显著优势。

## 🎯 应用场景

RMT-KD的研究成果在边缘计算、移动设备和物联网等领域具有广泛的应用潜力。通过有效压缩深度学习模型，RMT-KD能够在保持高性能的同时，降低计算资源的需求，推动智能设备的普及和应用。未来，该方法有望在实时推理和低功耗计算场景中发挥重要作用。

## 📄 摘要（原文）

> Large deep learning models such as BERT and ResNet achieve state-of-the-art performance but are costly to deploy at the edge due to their size and compute demands. We present RMT-KD, a compression method that leverages Random Matrix Theory (RMT) for knowledge distillation to iteratively reduce network size. Instead of pruning or heuristic rank selection, RMT-KD preserves only informative directions identified via the spectral properties of hidden representations. RMT-based causal reduction is applied layer by layer with self-distillation to maintain stability and accuracy. On GLUE, AG News, and CIFAR-10, RMT-KD achieves up to 80% parameter reduction with only 2% accuracy loss, delivering 2.8x faster inference and nearly halved power consumption. These results establish RMT-KD as a mathematically grounded approach to network distillation.

