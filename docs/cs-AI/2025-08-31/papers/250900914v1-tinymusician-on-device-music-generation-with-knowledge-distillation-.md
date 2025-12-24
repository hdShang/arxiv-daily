---
layout: default
title: "TinyMusician: On-Device Music Generation with Knowledge Distillation and Mixed Precision Quantization"
---

# TinyMusician: On-Device Music Generation with Knowledge Distillation and Mixed Precision Quantization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00914" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00914v1</a>
  <a href="https://arxiv.org/pdf/2509.00914.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00914v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00914v1', 'TinyMusician: On-Device Music Generation with Knowledge Distillation and Mixed Precision Quantization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hainan Wang, Mehdi Hosseinzadeh, Reza Rawassizadeh

**分类**: cs.SD, cs.AI, eess.AS

**发布日期**: 2025-08-31

**备注**: 12 pages for main context, 5 figures

---

## 💡 一句话要点

**提出TinyMusician以解决边缘设备音乐生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `音乐生成` `知识蒸馏` `混合精度量化` `边缘计算` `Transformer模型` `模型压缩` `音频处理`

## 📋 核心要点

1. 现有的基于Transformer的音乐生成模型对计算资源和推理时间的需求过高，难以在边缘设备上部署。
2. TinyMusician通过蒸馏技术和混合精度量化，显著降低了模型大小，同时保持了音乐生成的高质量。
3. 实验结果显示，TinyMusician在减少55%模型大小的同时，仍能保留93%的原始模型性能，具有较高的实用价值。

## 📝 摘要（中文）

生成模型的成功在音乐生成领域引起了前所未有的关注。基于Transformer的架构虽然在模型性能上设立了新的基准，但由于其庞大的参数量，导致对计算资源和推理时间的需求极高，从而限制了其在智能手机和可穿戴设备等边缘设备上的实际应用。本文提出了TinyMusician，这是一个从最先进的音乐生成模型MusicGen蒸馏而来的轻量级音乐生成模型。TinyMusician结合了两项创新：阶段混合双向和偏斜KL散度以及自适应混合精度量化。实验结果表明，TinyMusician在模型大小减少55%的情况下，仍保留了93%的MusicGen-Small性能。TinyMusician是首个可在移动设备上部署的音乐生成模型，消除了对云的依赖，同时保持高音频保真度和高效的资源使用。

## 🔬 方法详解

**问题定义**：本文旨在解决现有音乐生成模型在边缘设备上部署的难题，主要痛点在于其对计算资源和推理时间的高需求。

**核心思路**：TinyMusician通过知识蒸馏和混合精度量化技术，降低模型复杂度，提升在资源受限环境下的运行效率。

**技术框架**：TinyMusician的整体架构包括两个主要模块：知识蒸馏模块用于提取MusicGen的知识，混合精度量化模块用于优化模型的计算性能。

**关键创新**：本文的关键创新在于引入阶段混合双向和偏斜KL散度，以及自适应混合精度量化，这些技术显著提升了模型的压缩率和推理速度。

**关键设计**：在模型设计中，采用了特定的损失函数来平衡音质与模型大小，同时优化了网络结构以适应边缘设备的计算能力。通过这些设计，TinyMusician实现了高效的资源使用和音频保真度。

## 📊 实验亮点

实验结果表明，TinyMusician在模型大小减少55%的情况下，仍能保留93%的MusicGen-Small性能。这一成果展示了其在边缘设备上高效运行的能力，标志着音乐生成技术的一个重要进步。

## 🎯 应用场景

TinyMusician的潜在应用场景包括移动音乐创作、实时音乐生成和个性化音乐推荐等。其轻量级特性使得音乐生成能够在智能手机和其他边缘设备上实现，具有广泛的市场价值和应用前景。未来，TinyMusician可能会推动音乐创作的民主化，使更多用户能够轻松生成高质量的音乐作品。

## 📄 摘要（原文）

> The success of the generative model has gained unprecedented attention in the music generation area. Transformer-based architectures have set new benchmarks for model performance. However, their practical adoption is hindered by some critical challenges: the demand for massive computational resources and inference time, due to their large number of parameters. These obstacles make them infeasible to deploy on edge devices, such as smartphones and wearables, with limited computational resources. In this work, we present TinyMusician, a lightweight music generation model distilled from MusicGen (a State-of-the-art music generation model). TinyMusician integrates two innovations: (i) Stage-mixed Bidirectional and Skewed KL-Divergence and (ii) Adaptive Mixed-Precision Quantization. The experimental results demonstrate that TinyMusician retains 93% of the MusicGen-Small performance with 55% less model size. TinyMusician is the first mobile-deployable music generation model that eliminates cloud dependency while maintaining high audio fidelity and efficient resource usage

