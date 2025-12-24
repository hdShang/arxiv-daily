---
layout: default
title: Unified Multimodal Brain Decoding via Cross-Subject Soft-ROI Fusion
---

# Unified Multimodal Brain Decoding via Cross-Subject Soft-ROI Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20249" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20249v1</a>
  <a href="https://arxiv.org/pdf/2512.20249.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20249v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20249v1', 'Unified Multimodal Brain Decoding via Cross-Subject Soft-ROI Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuanyu Hu

**分类**: cs.LG, cs.CV, eess.IV

**发布日期**: 2025-12-23

**备注**: 15 pages, 2 figures, 4 tables. Submitted to ICPR 2026

---

## 💡 一句话要点

**提出BrainROI模型，通过跨被试软ROI融合实现统一的多模态脑解码，提升脑活动到自然语言描述的泛化性和可解释性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态脑解码` `跨被试泛化` `软ROI融合` `可解释性` `脑机接口`

## 📋 核心要点

1. 现有脑解码方法在跨被试泛化能力和模型可解释性方面存在不足，难以适应个体差异。
2. 论文提出BrainROI模型，利用软ROI融合和可解释的提示优化，提升跨被试脑解码的性能和透明度。
3. 实验表明，BrainROI模型在NSD数据集上显著提升了BLEU-4和CIDEr等指标，优于现有方法。

## 📝 摘要（中文）

多模态脑解码旨在从fMRI等脑活动信号中重建与视觉刺激一致的语义信息，并生成可读的自然语言描述。然而，多模态脑解码在跨被试泛化和可解释性方面仍面临关键挑战。我们提出了BrainROI模型，并在NSD数据集上的脑-字幕评估中取得了领先水平的结果。在跨被试设置下，与最新的state-of-the-art方法和代表性基线相比，BLEU-4和CIDEr等指标显示出明显的改进。首先，为了解决不同被试间功能脑拓扑的异质性，我们设计了一种新的fMRI编码器，使用多图谱软功能分割（soft-ROI）作为共享空间，并将MINDLLM中的离散ROI连接策略扩展到体素级门控融合机制（Voxel-gate）。我们还通过全局标签对齐来确保一致的ROI映射，从而增强跨被试的可迁移性。其次，为了克服手动和黑盒提示方法在稳定性和透明度方面的局限性，我们引入了一个可解释的提示优化过程。在一个小样本闭环中，我们使用本地部署的Qwen模型来迭代生成和选择人类可读的提示，从而提高了提示设计的稳定性，并保留了可审计的优化轨迹。最后，我们在推理过程中施加参数化的解码约束，以进一步提高生成描述的稳定性和质量。

## 🔬 方法详解

**问题定义**：多模态脑解码旨在从脑活动信号（如fMRI）重建语义信息并生成自然语言描述。现有方法在跨被试泛化能力和可解释性方面存在挑战。不同被试的脑功能拓扑结构存在异质性，导致模型难以在不同个体间有效迁移。此外，手动或黑盒提示方法缺乏稳定性和透明度，影响生成描述的质量和可控性。

**核心思路**：论文的核心思路是通过跨被试软ROI融合和可解释的提示优化来解决上述问题。利用软ROI作为共享空间，缓解个体间脑功能拓扑的差异。设计体素级门控融合机制（Voxel-gate）和全局标签对齐，增强跨被试的可迁移性。引入可解释的提示优化过程，提高提示设计的稳定性和透明度。

**技术框架**：BrainROI模型包含fMRI编码器、提示优化模块和解码器三个主要模块。fMRI编码器负责将fMRI信号映射到共享的软ROI空间。提示优化模块利用本地部署的Qwen模型迭代生成和选择人类可读的提示。解码器基于编码后的fMRI特征和优化后的提示生成自然语言描述。在推理阶段，施加参数化的解码约束，进一步提高生成描述的质量。

**关键创新**：论文的关键创新在于以下几点：1) 提出基于软ROI融合的fMRI编码器，有效缓解了不同被试间脑功能拓扑的异质性。2) 设计了体素级门控融合机制（Voxel-gate），增强了ROI特征的表达能力。3) 引入了可解释的提示优化过程，提高了提示设计的稳定性和透明度。与现有方法相比，BrainROI模型在跨被试泛化能力和可解释性方面具有显著优势。

**关键设计**：fMRI编码器使用多图谱软功能分割（soft-ROI）作为共享空间，通过Voxel-gate机制融合不同ROI的特征。全局标签对齐确保一致的ROI映射。提示优化模块使用本地部署的Qwen模型，通过小样本闭环迭代生成和选择提示。解码器采用参数化的解码约束，例如长度约束和关键词约束，以提高生成描述的质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20249v1/frame.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20249v1/combination.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20249v1/IPO.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

BrainROI模型在NSD数据集上的跨被试脑-字幕评估中取得了领先水平的结果。与state-of-the-art方法和代表性基线相比，BLEU-4和CIDEr等指标显示出明显的改进，验证了该模型在跨被试泛化能力和生成描述质量方面的优势。可解释的提示优化过程也提高了提示设计的稳定性和透明度。

## 🎯 应用场景

该研究成果可应用于神经科学、认知科学和人工智能等领域。潜在应用包括：开发更精准的脑机接口、辅助诊断神经系统疾病、提升人机交互的自然性和智能化水平。通过理解大脑活动与语义信息之间的关联，有望为人工智能的认知建模和自然语言处理提供新的思路。

## 📄 摘要（原文）

> Multimodal brain decoding aims to reconstruct semantic information that is consistent with visual stimuli from brain activity signals such as fMRI, and then generate readable natural language descriptions. However, multimodal brain decoding still faces key challenges in cross-subject generalization and interpretability. We propose a BrainROI model and achieve leading-level results in brain-captioning evaluation on the NSD dataset. Under the cross-subject setting, compared with recent state-of-the-art methods and representative baselines, metrics such as BLEU-4 and CIDEr show clear improvements. Firstly, to address the heterogeneity of functional brain topology across subjects, we design a new fMRI encoder. We use multi-atlas soft functional parcellations (soft-ROI) as a shared space. We extend the discrete ROI Concatenation strategy in MINDLLM to a voxel-wise gated fusion mechanism (Voxel-gate). We also ensure consistent ROI mapping through global label alignment, which enhances cross-subject transferability. Secondly, to overcome the limitations of manual and black-box prompting methods in stability and transparency, we introduce an interpretable prompt optimization process. In a small-sample closed loop, we use a locally deployed Qwen model to iteratively generate and select human-readable prompts. This process improves the stability of prompt design and preserves an auditable optimization trajectory. Finally, we impose parameterized decoding constraints during inference to further improve the stability and quality of the generated descriptions.

