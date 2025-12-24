---
layout: default
title: "EMLoC: Emulator-based Memory-efficient Fine-tuning with LoRA Correction"
---

# EMLoC: Emulator-based Memory-efficient Fine-tuning with LoRA Correction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12015" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12015v1</a>
  <a href="https://arxiv.org/pdf/2506.12015.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12015v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12015v1', 'EMLoC: Emulator-based Memory-efficient Fine-tuning with LoRA Correction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hsi-Che Lin, Yu-Chu Yu, Kai-Po Chang, Yu-Chiang Frank Wang

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-06-13

**备注**: Under review. Project page: https://hsi-che-lin.github.io/EMLoC/

---

## 💡 一句话要点

**提出EMLoC框架以解决大模型微调的内存开销问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型微调` `内存效率` `LoRA` `仿真器` `奇异值分解` `深度学习` `自然语言处理` `计算机视觉`

## 📋 核心要点

1. 现有方法在大规模基础模型微调中面临显著的内存开销，限制了其在领域特定任务中的应用。
2. EMLoC框架通过构建轻量级仿真器和LoRA修正，实现了在推理内存预算内的高效微调。
3. 实验结果显示，EMLoC在多个数据集上优于基线方法，能够在单个GPU上高效微调大模型。

## 📝 摘要（中文）

开源基础模型的快速发展使其在多个领域具备强大的通用能力。然而，对于大规模基础模型进行领域特定或个性化任务的微调，因其显著的内存开销而变得极为昂贵。本文提出了EMLoC，一个基于仿真器的内存高效微调框架，结合LoRA修正，能够在与推理相同的内存预算内进行模型微调。EMLoC通过对小型下游校准集进行激活感知的奇异值分解（SVD）构建任务特定的轻量级仿真器，随后在该仿真器上通过LoRA进行微调。为了解决原始模型与压缩仿真器之间的错位问题，本文提出了一种新颖的补偿算法，以修正微调后的LoRA模块，从而可以合并到原始模型中进行推理。EMLoC支持灵活的压缩比和标准训练流程，适应广泛的应用场景。大量实验表明，EMLoC在多个数据集和模态上超越了其他基线，且在不进行量化的情况下，能够在单个24GB消费级GPU上微调38B模型，为个体用户带来了高效且实用的模型适应能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模基础模型在领域特定任务微调时的内存开销问题。现有方法通常需要大量内存，限制了其在实际应用中的可行性。

**核心思路**：EMLoC通过构建轻量级仿真器，结合LoRA技术，在内存预算内实现高效微调。该设计使得微调过程不再依赖于原始模型的全部参数，从而降低内存需求。

**技术框架**：EMLoC的整体架构包括三个主要模块：首先，使用激活感知的奇异值分解（SVD）构建轻量级仿真器；其次，在该仿真器上进行LoRA微调；最后，应用补偿算法修正微调后的LoRA模块，以便将其合并到原始模型中进行推理。

**关键创新**：EMLoC的主要创新在于提出了一种新的补偿算法，解决了原始模型与压缩仿真器之间的错位问题。这一创新使得微调后的模型能够有效地与原始模型兼容。

**关键设计**：在设计中，EMLoC允许灵活的压缩比，并采用标准的训练流程。此外，激活感知的SVD和LoRA的结合是其核心技术细节之一，确保了微调过程的高效性和准确性。

## 📊 实验亮点

EMLoC在多个数据集上表现优异，超越了现有基线方法，尤其是在不进行量化的情况下，能够在单个24GB的消费级GPU上成功微调38B参数的模型，展示了其在内存效率和性能上的显著提升。

## 🎯 应用场景

EMLoC框架具有广泛的应用潜力，尤其适用于需要快速适应大规模基础模型的领域，如自然语言处理、计算机视觉和个性化推荐系统。其高效的微调能力使得中小型企业和个人开发者能够在有限的资源下，利用大模型进行特定任务的优化，推动了AI技术的普及与应用。

## 📄 摘要（原文）

> Open-source foundation models have seen rapid adoption and development, enabling powerful general-purpose capabilities across diverse domains. However, fine-tuning large foundation models for domain-specific or personalized tasks remains prohibitively expensive for most users due to the significant memory overhead beyond that of inference. We introduce EMLoC, an Emulator-based Memory-efficient fine-tuning framework with LoRA Correction, which enables model fine-tuning within the same memory budget required for inference. EMLoC constructs a task-specific light-weight emulator using activation-aware singular value decomposition (SVD) on a small downstream calibration set. Fine-tuning then is performed on this lightweight emulator via LoRA. To tackle the misalignment between the original model and the compressed emulator, we propose a novel compensation algorithm to correct the fine-tuned LoRA module, which thus can be merged into the original model for inference. EMLoC supports flexible compression ratios and standard training pipelines, making it adaptable to a wide range of applications. Extensive experiments demonstrate that EMLoC outperforms other baselines across multiple datasets and modalities. Moreover, without quantization, EMLoC enables fine-tuning of a 38B model on a single 24GB consumer GPU-bringing efficient and practical model adaptation to individual users.

