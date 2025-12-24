---
layout: default
title: "Towards Unified Multimodal Misinformation Detection in Social Media: A Benchmark Dataset and Baseline"
---

# Towards Unified Multimodal Misinformation Detection in Social Media: A Benchmark Dataset and Baseline

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25991" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25991v2</a>
  <a href="https://arxiv.org/pdf/2509.25991.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25991v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25991v2', 'Towards Unified Multimodal Misinformation Detection in Social Media: A Benchmark Dataset and Baseline')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haiyang Li, Yaxiong Wang, Shengeng Tang, Lianwei Wu, Lechao Cheng, Zhun Zhong

**分类**: cs.AI, cs.CV

**发布日期**: 2025-09-30 (更新: 2025-10-15)

---

## 💡 一句话要点

**提出OmniFake数据集与UMFDet框架，统一解决社交媒体中人工与AI生成的多模态虚假信息检测问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态虚假信息检测` `统一框架` `视觉-语言模型` `混合专家网络` `归因链式思考`

## 📋 核心要点

1. 现有方法通常针对人工或AI生成的多模态虚假信息进行独立研究，缺乏统一处理两种类型欺骗的能力。
2. 论文提出UMFDet框架，利用VLM骨干网络、类别感知MoE适配器和归因链式思考机制，实现对两种类型虚假信息的统一检测。
3. 实验结果表明，UMFDet在OmniFake数据集上表现出色，优于专门的基线模型，证明了其在实际场景中的有效性。

## 📝 摘要（中文）

近年来，社交媒体上多模态虚假内容的检测日益受到关注。主要存在两种欺骗形式：人为制造的虚假信息（如谣言和误导性帖子）和由图像合成模型或视觉-语言模型（VLMs）生成的AI内容。尽管两者都具有欺骗意图，但通常是孤立地进行研究。自然语言处理研究侧重于人为撰写的虚假信息，而计算机视觉领域则针对AI生成的伪造内容。因此，现有模型通常只专用于一种类型的虚假内容。然而，在实际场景中，多模态帖子的类型通常是未知的，这限制了此类专用系统的有效性。为了弥合这一差距，我们构建了多模态新闻欺骗综合数据集（OmniFake），这是一个包含12.7万个样本的综合基准，它将来自现有资源的人工虚假信息与新合成的AI生成示例相结合。基于此数据集，我们提出了统一多模态虚假内容检测（UMFDet）框架，旨在处理这两种欺骗形式。UMFDet利用VLM骨干网络，并辅以类别感知的混合专家（MoE）适配器来捕获类别特定的线索，以及归因链式思考机制，为定位显著的欺骗信号提供隐式推理指导。广泛的实验表明，UMFDet在两种虚假信息类型上都实现了稳健且一致的性能，优于专门的基线模型，并为实际的多模态欺骗检测提供了一种实用的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决社交媒体中多模态虚假信息检测问题，特别是如何统一处理人工制造和AI生成两种类型的欺骗内容。现有方法通常针对其中一种类型进行优化，无法有效应对实际场景中类型未知的多模态帖子，泛化能力较差。

**核心思路**：论文的核心思路是构建一个统一的框架，使其能够同时学习和区分人工和AI生成的多模态虚假信息。通过利用视觉-语言模型（VLM）的强大表示能力，并引入类别感知的混合专家（MoE）适配器和归因链式思考机制，来增强模型对不同类型欺骗信号的识别能力。

**技术框架**：UMFDet框架主要包含以下几个模块：1) VLM骨干网络：用于提取多模态特征；2) 类别感知MoE适配器：根据输入样本的类别（人工或AI生成）选择不同的专家网络，以捕获类别特定的线索；3) 归因链式思考机制：通过生成一系列中间推理步骤，引导模型关注与欺骗相关的关键区域，提供隐式推理指导。整个框架通过端到端的方式进行训练。

**关键创新**：论文的关键创新在于提出了一个统一的多模态虚假信息检测框架，能够同时处理人工和AI生成的欺骗内容。类别感知MoE适配器和归因链式思考机制是两个重要的技术创新点，前者能够有效区分不同类型的欺骗信号，后者能够提供隐式推理指导，帮助模型定位关键的欺骗区域。

**关键设计**：类别感知MoE适配器由多个专家网络组成，每个专家网络负责处理特定类别的样本。在训练过程中，根据输入样本的类别，选择相应的专家网络进行激活。归因链式思考机制通过生成一系列中间推理步骤，例如“图像中是否存在不自然的阴影？”、“文本描述是否与图像内容一致？”等，引导模型关注与欺骗相关的关键区域。损失函数包括分类损失和归因损失，用于优化模型的分类性能和归因能力。

## 📊 实验亮点

UMFDet在OmniFake数据集上取得了显著的性能提升，在人工虚假信息和AI生成虚假信息两种类型上均优于专门的基线模型。实验结果表明，UMFDet能够有效利用类别感知的MoE适配器和归因链式思考机制，提高模型对不同类型欺骗信号的识别能力，实现更鲁棒和一致的性能。

## 🎯 应用场景

该研究成果可应用于社交媒体平台的内容审核、新闻真实性验证等领域，有助于识别和过滤虚假信息，维护网络空间的健康生态。未来，该技术还可扩展到其他多模态欺骗检测场景，例如深度伪造视频检测、恶意软件识别等。

## 📄 摘要（原文）

> In recent years, detecting fake multimodal content on social media has drawn increasing attention. Two major forms of deception dominate: human-crafted misinformation (e.g., rumors and misleading posts) and AI-generated content produced by image synthesis models or vision-language models (VLMs). Although both share deceptive intent, they are typically studied in isolation. NLP research focuses on human-written misinformation, while the CV community targets AI-generated artifacts. As a result, existing models are often specialized for only one type of fake content. In real-world scenarios, however, the type of a multimodal post is usually unknown, limiting the effectiveness of such specialized systems. To bridge this gap, we construct the Omnibus Dataset for Multimodal News Deception (OmniFake), a comprehensive benchmark of 127K samples that integrates human-curated misinformation from existing resources with newly synthesized AI-generated examples. Based on this dataset, we propose Unified Multimodal Fake Content Detection (UMFDet), a framework designed to handle both forms of deception. UMFDet leverages a VLM backbone augmented with a Category-aware Mixture-of-Experts (MoE) Adapter to capture category-specific cues, and an attribution chain-of-thought mechanism that provides implicit reasoning guidance for locating salient deceptive signals. Extensive experiments demonstrate that UMFDet achieves robust and consistent performance across both misinformation types, outperforming specialized baselines and offering a practical solution for real-world multimodal deception detection.

