---
layout: default
title: "UniFGVC: Universal Training-Free Few-Shot Fine-Grained Vision Classification via Attribute-Aware Multimodal Retrieval"
---

# UniFGVC: Universal Training-Free Few-Shot Fine-Grained Vision Classification via Attribute-Aware Multimodal Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04136" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04136v1</a>
  <a href="https://arxiv.org/pdf/2508.04136.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04136v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04136v1', 'UniFGVC: Universal Training-Free Few-Shot Fine-Grained Vision Classification via Attribute-Aware Multimodal Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyu Guo, Kuan Zhu, Xiangzhao Hao, Haiyun Guo, Ming Tang, Jinqiao Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出UniFGVC以解决少样本细粒度视觉分类问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `少样本学习` `细粒度分类` `多模态检索` `视觉语言模型` `开放世界知识`

## 📋 核心要点

1. 现有的少样本FGVC方法主要依赖于微调预训练模型，容易出现过拟合和泛化能力不足的问题。
2. 本文提出的UniFGVC框架通过多模态检索的方式，利用CDV-Captioner生成细粒度属性描述，从而增强模型的区分能力。
3. 在12个FGVC基准测试中，UniFGVC的表现持续优于传统的CLIP方法和一些完全监督的MLLM方法，显示出其有效性。

## 📝 摘要（中文）

少样本细粒度视觉分类（FGVC）旨在利用有限的数据使模型能够区分微妙的类别差异。现有方法主要通过微调预训练的视觉语言模型来提高性能，但面临过拟合和弱泛化的问题。为此，本文提出了UniFGVC，一个通用的无训练框架，将少样本FGVC重新构建为多模态检索。首先，提出了类别区分视觉描述生成器（CDV-Captioner），利用多模态大语言模型的开放世界知识生成结构化文本描述，捕捉细粒度属性特征。通过链式思维提示和视觉相似参考图像，CDV-Captioner减少了幻觉现象并增强了生成描述的区分性。使用该方法，我们将每个图像转换为图像-描述对，构建多模态类别模板以供后续检索。最后，利用现成的视觉和文本编码器嵌入查询和模板对，通过在联合空间中检索最近的模板来完成FGVC。UniFGVC确保与多种MLLM和编码器的广泛兼容性，在少样本FGVC场景中提供可靠的泛化和适应性。大量实验表明，其在12个FGVC基准上优于以往的少样本CLIP方法，甚至超过了若干完全监督的MLLM方法。

## 🔬 方法详解

**问题定义**：本文旨在解决少样本细粒度视觉分类中的过拟合和弱泛化问题。现有方法依赖于微调预训练模型，导致在有限样本下性能不佳。

**核心思路**：UniFGVC框架将FGVC问题重新构建为多模态检索，通过生成细粒度属性描述来增强模型的区分能力，避免了传统方法的训练过程。

**技术框架**：该框架主要包括两个模块：类别区分视觉描述生成器（CDV-Captioner）和检索模块。CDV-Captioner生成图像的结构化文本描述，而检索模块则通过嵌入查询和模板对来实现FGVC。

**关键创新**：CDV-Captioner的设计是本文的核心创新，通过链式思维提示和视觉相似参考图像，显著减少了生成描述的幻觉现象，提升了描述的准确性和区分性。

**关键设计**：在CDV-Captioner中，使用了多模态大语言模型的开放世界知识，结合视觉相似图像进行描述生成。检索模块则利用现成的视觉和文本编码器，确保了模型的广泛兼容性和适应性。

## 📊 实验亮点

在12个FGVC基准测试中，UniFGVC consistently outperform previous few-shot CLIP-based methods, achieving significant improvements in performance. 具体来说，UniFGVC在多个任务上均展现出优越的泛化能力，提升幅度达到XX%。

## 🎯 应用场景

该研究的潜在应用领域包括生物物种识别、产品分类以及任何需要细粒度分类的视觉任务。通过提供一种无训练的解决方案，UniFGVC能够在数据稀缺的情况下有效提升模型性能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Few-shot fine-grained visual classification (FGVC) aims to leverage limited data to enable models to discriminate subtly distinct categories. Recent works mostly finetuned the pre-trained visual language models to achieve performance gain, yet suffering from overfitting and weak generalization. To deal with this, we introduce UniFGVC, a universal training-free framework that reformulates few-shot FGVC as multimodal retrieval. First, we propose the Category-Discriminative Visual Captioner (CDV-Captioner) to exploit the open-world knowledge of multimodal large language models (MLLMs) to generate a structured text description that captures the fine-grained attribute features distinguishing closely related classes. CDV-Captioner uses chain-of-thought prompting and visually similar reference images to reduce hallucination and enhance discrimination of generated captions. Using it we can convert each image into an image-description pair, enabling more comprehensive feature representation, and construct the multimodal category templates using few-shot samples for the subsequent retrieval pipeline. Then, off-the-shelf vision and text encoders embed query and template pairs, and FGVC is accomplished by retrieving the nearest template in the joint space. UniFGVC ensures broad compatibility with diverse MLLMs and encoders, offering reliable generalization and adaptability across few-shot FGVC scenarios. Extensive experiments on 12 FGVC benchmarks demonstrate its consistent superiority over prior few-shot CLIP-based methods and even several fully-supervised MLLMs-based approaches.

