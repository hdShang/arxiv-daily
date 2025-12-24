---
layout: default
title: Quaff: Quantized Parameter-Efficient Fine-Tuning under Outlier Spatial Stability Hypothesis
---

# Quaff: Quantized Parameter-Efficient Fine-Tuning under Outlier Spatial Stability Hypothesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14742" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14742v2</a>
  <a href="https://arxiv.org/pdf/2505.14742.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14742v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14742v2', 'Quaff: Quantized Parameter-Efficient Fine-Tuning under Outlier Spatial Stability Hypothesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hong Huang, Dapeng Wu

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-05-29)

**备注**: Accepted by ACL 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Little0o0/Quaff.git)

---

## 💡 一句话要点

**提出Quaff以解决资源受限设备上LLM微调效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化微调` `异常空间稳定假设` `大型语言模型` `参数高效` `资源受限设备` `动量缩放` `计算效率` `内存优化`

## 📋 核心要点

1. 现有的量化微调方法在资源受限设备上难以实现高效性能，尤其是在处理激活异常时面临重大挑战。
2. 本文提出了异常空间稳定假设（OSSH），并基于此开发了Quaff框架，通过动量缩放优化低精度激活表示。
3. 在GPQA推理基准上，Quaff实现了1.73倍的延迟减少和30%的内存节省，同时在Phi-3模型上提高了0.6%的准确率。

## 📝 摘要（中文）

大型语言模型（LLMs）在多个领域取得了显著成就，但在资源受限的个人设备上部署时，任务特定微调的计算和内存需求仍然阻碍其应用。尽管量化提供了提高效率的途径，但现有方法在性能与开销之间难以平衡，往往导致高计算/内存成本或未能有效处理激活异常，这是量化微调中的关键瓶颈。为了解决这些挑战，本文提出了异常空间稳定假设（OSSH），并基于此提出了Quaff，一个量化的参数高效微调框架，通过有针对性的动量缩放优化低精度激活表示。Quaff通过轻量级操作动态抑制不变通道中的异常，消除了全精度权重存储和全局重缩放，同时减少了量化误差。大量实验验证了OSSH，并展示了Quaff的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在资源受限设备上进行任务特定微调时的计算和内存需求过高的问题。现有的量化方法往往无法有效处理激活异常，导致性能下降。

**核心思路**：论文提出的异常空间稳定假设（OSSH）认为，在微调过程中，某些激活异常通道在训练迭代中保持稳定的空间位置。基于这一假设，Quaff框架通过动量缩放优化低精度激活表示，专注于抑制不变通道中的异常。

**技术框架**：Quaff的整体架构包括激活表示的量化、动量缩放的应用以及异常通道的动态抑制。该框架通过轻量级操作实现高效的微调，避免了全精度权重存储和全局重缩放。

**关键创新**：Quaff的核心创新在于引入了OSSH，并通过动态抑制不变通道中的异常来优化量化过程。这种方法与传统的量化微调方法相比，显著降低了计算和内存开销，同时保持了模型性能。

**关键设计**：在Quaff中，动量缩放的参数设置经过精心设计，以确保在抑制异常的同时，尽量减少量化误差。此外，损失函数的设计也考虑了激活通道的稳定性，以提高微调效果。

## 📊 实验亮点

在GPQA推理基准上，Quaff实现了1.73倍的延迟减少和30%的内存节省，同时在Phi-3模型上提高了0.6%的准确率。这些实验结果表明，Quaff在效率、性能和可部署性之间达成了良好的平衡。

## 🎯 应用场景

Quaff框架的潜在应用场景包括个人设备上的大型语言模型微调，如智能手机、平板电脑等。通过降低计算和内存需求，Quaff使得个性化的LLM部署变得更加可行，具有广泛的实际价值。未来，随着技术的进一步发展，Quaff可能会推动更多智能设备的智能化应用。

## 📄 摘要（原文）

> Large language models (LLMs) have made exciting achievements across various domains, yet their deployment on resource-constrained personal devices remains hindered by the prohibitive computational and memory demands of task-specific fine-tuning. While quantization offers a pathway to efficiency, existing methods struggle to balance performance and overhead, either incurring high computational/memory costs or failing to address activation outliers, a critical bottleneck in quantized fine-tuning. To address these challenges, we propose the Outlier Spatial Stability Hypothesis (OSSH): During fine-tuning, certain activation outlier channels retain stable spatial positions across training iterations. Building on OSSH, we propose Quaff, a Quantized parameter-efficient fine-tuning framework for LLMs, optimizing low-precision activation representations through targeted momentum scaling. Quaff dynamically suppresses outliers exclusively in invariant channels using lightweight operations, eliminating full-precision weight storage and global rescaling while reducing quantization errors. Extensive experiments across ten benchmarks validate OSSH and demonstrate Quaff's efficacy. Specifically, on the GPQA reasoning benchmark, Quaff achieves a 1.73x latency reduction and 30% memory savings over full-precision fine-tuning while improving accuracy by 0.6% on the Phi-3 model, reconciling the triple trade-off between efficiency, performance, and deployability. By enabling consumer-grade GPU fine-tuning (e.g., RTX 2080 Super) without sacrificing model utility, Quaff democratizes personalized LLM deployment. The code is available at https://github.com/Little0o0/Quaff.git.

