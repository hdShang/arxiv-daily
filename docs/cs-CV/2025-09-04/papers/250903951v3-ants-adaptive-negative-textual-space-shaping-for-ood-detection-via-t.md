---
layout: default
title: "ANTS: Adaptive Negative Textual Space Shaping for OOD Detection via Test-Time MLLM Understanding and Reasoning"
---

# ANTS: Adaptive Negative Textual Space Shaping for OOD Detection via Test-Time MLLM Understanding and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03951" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03951v3</a>
  <a href="https://arxiv.org/pdf/2509.03951.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03951v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03951v3', 'ANTS: Adaptive Negative Textual Space Shaping for OOD Detection via Test-Time MLLM Understanding and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenjie Zhu, Yabin Zhang, Xin Jin, Wenjun Zeng, Lei Zhang

**分类**: cs.CV

**发布日期**: 2025-09-04 (更新: 2025-11-19)

---

## 💡 一句话要点

**提出ANTS：利用MLLM理解和推理自适应地塑造负文本空间，提升OOD检测性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `OOD检测` `负文本空间` `多模态大语言模型` `MLLM` `零样本学习`

## 📋 核心要点

1. 现有OOD检测方法难以准确构建负空间，缺乏对OOD图像的理解，限制了检测性能。
2. ANTS利用MLLM的理解和推理能力，自适应地生成远OOD和近OOD的负文本空间。
3. 实验表明，ANTS在ImageNet上显著降低了FPR95，且具有免训练和零样本的优势。

## 📝 摘要（中文）

本文提出了一种自适应负文本空间塑造方法（ANTS），旨在提升OOD（Out-of-Distribution）检测性能。现有方法在构建精确的负空间时，缺乏对OOD图像的理解，并且缺乏与ID（In-Distribution）标签语义相似的负标签，限制了其在近OOD检测中的能力。ANTS利用多模态大语言模型（MLLM）的理解和推理能力来解决这些问题。具体而言，该方法缓存历史测试图像中可能为OOD的样本，并提示MLLM描述这些图像，生成表达性的负句子，精确地表征OOD分布，从而增强远OOD检测。对于近OOD场景，该方法缓存与历史测试图像视觉上相似的ID类别子集，并利用MLLM推理生成针对该子集的视觉上相似的负标签，有效减少假阴性，提高近OOD检测性能。为了平衡这两种类型的负文本空间，设计了一种自适应加权评分，使该方法能够处理不同的OOD任务设置（近OOD和远OOD），从而在开放环境中具有高度的适应性。在ImageNet基准测试中，ANTS显著降低了3.1%的FPR95，建立了新的state-of-the-art。此外，该方法是免训练和零样本的，具有很高的可扩展性。

## 🔬 方法详解

**问题定义**：现有的OOD检测方法，特别是基于负标签的方法，在构建负空间时存在局限性。它们通常缺乏对OOD数据的理解，难以生成准确描述OOD分布的负样本。此外，对于与ID数据相似的近OOD样本，现有方法难以生成语义相关的负标签，导致检测效果不佳。这些问题限制了OOD检测方法在实际开放环境中的应用。

**核心思路**：ANTS的核心思路是利用多模态大语言模型（MLLM）的强大理解和推理能力，自适应地构建负文本空间。通过MLLM对OOD图像的描述和推理，生成更具表达性和针对性的负样本，从而提高OOD检测的准确性和鲁棒性。该方法区分远OOD和近OOD场景，分别采用不同的策略生成负样本，并设计自适应权重平衡两种负空间。

**技术框架**：ANTS的整体框架包括以下几个主要阶段：1) 历史测试图像缓存：缓存历史测试中可能为OOD的样本以及与测试图像视觉相似的ID类别子集。2) MLLM提示与负样本生成：针对远OOD样本，提示MLLM描述图像，生成负句子；针对近OOD样本，利用MLLM推理生成视觉上相似的负标签。3) 自适应加权：设计自适应权重，平衡远OOD和近OOD负文本空间。4) OOD检测：利用构建的负文本空间进行OOD检测。

**关键创新**：ANTS最重要的创新点在于利用MLLM的理解和推理能力，自适应地生成负文本空间。与现有方法相比，ANTS能够更准确地描述OOD分布，并针对近OOD样本生成语义相关的负标签。此外，ANTS的自适应加权机制能够平衡不同类型的负空间，使其在不同的OOD任务设置中具有更好的适应性。该方法是免训练和零样本的，具有很高的可扩展性。

**关键设计**：ANTS的关键设计包括：1) MLLM提示工程：设计有效的提示语，引导MLLM生成高质量的负样本描述和推理结果。2) 相似度度量：选择合适的相似度度量方法，用于缓存与测试图像视觉相似的ID类别子集。3) 自适应权重计算：设计自适应权重计算公式，根据OOD任务的特点，动态调整远OOD和近OOD负空间的权重。4) OOD检测器：选择合适的OOD检测器，并利用构建的负文本空间进行训练或推理。

## 📊 实验亮点

ANTS在ImageNet基准测试中取得了显著的性能提升，FPR95降低了3.1%，达到了新的state-of-the-art。该方法无需训练，具有零样本的特性，使其易于部署和扩展。实验结果表明，ANTS能够有效地处理远OOD和近OOD样本，并在不同的OOD任务设置中表现出良好的适应性。

## 🎯 应用场景

ANTS具有广泛的应用前景，例如在自动驾驶中检测未知的交通状况，在医疗诊断中识别罕见疾病，在金融风控中识别欺诈交易等。该研究有助于提高AI系统在开放环境中的安全性和可靠性，并为未来的OOD检测研究提供新的思路。

## 📄 摘要（原文）

> The introduction of negative labels (NLs) has proven effective in enhancing Out-of-Distribution (OOD) detection. However, existing methods often lack an understanding of OOD images, making it difficult to construct an accurate negative space. Furthermore, the absence of negative labels semantically similar to ID labels constrains their capability in near-OOD detection. To address these issues, we propose shaping an Adaptive Negative Textual Space (ANTS) by leveraging the understanding and reasoning capabilities of multimodal large language models (MLLMs). Specifically, we cache images likely to be OOD samples from the historical test images and prompt the MLLM to describe these images, generating expressive negative sentences that precisely characterize the OOD distribution and enhance far-OOD detection. For the near-OOD setting, where OOD samples resemble the in-distribution (ID) subset, we cache the subset of ID classes that are visually similar to historical test images and then leverage MLLM reasoning to generate visually similar negative labels tailored to this subset, effectively reducing false negatives and improving near-OOD detection. To balance these two types of negative textual spaces, we design an adaptive weighted score that enables the method to handle different OOD task settings (near-OOD and far-OOD), making it highly adaptable in open environments. On the ImageNet benchmark, our ANTS significantly reduces the FPR95 by 3.1\%, establishing a new state-of-the-art. Furthermore, our method is training-free and zero-shot, enabling high scalability.

