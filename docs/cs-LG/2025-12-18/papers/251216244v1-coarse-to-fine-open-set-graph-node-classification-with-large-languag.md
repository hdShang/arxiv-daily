---
layout: default
title: Coarse-to-Fine Open-Set Graph Node Classification with Large Language Models
---

# Coarse-to-Fine Open-Set Graph Node Classification with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16244" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16244v1</a>
  <a href="https://arxiv.org/pdf/2512.16244.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16244v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16244v1', 'Coarse-to-Fine Open-Set Graph Node Classification with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xueqi Ma, Xingjun Ma, Sarah Monazam Erfani, Danilo Mandic, James Bailey

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

**备注**: Accepted to AAAI 2026

---

## 💡 一句话要点

**提出CFC框架，利用大语言模型实现图节点开放集分类与细粒度OOD识别。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `开放集分类` `图神经网络` `大语言模型` `OOD检测` `OOD分类` `图节点分类` `粗到细学习`

## 📋 核心要点

1. 现有开放集图节点分类方法难以提供OOD样本的细粒度信息，限制了其在高风险场景的应用。
2. CFC框架利用大语言模型进行粗粒度OOD检测和标签生成，再用GNN进行细粒度分类，实现OOD分类。
3. 实验表明，CFC在OOD检测和分类任务上均优于现有方法，尤其在OOD分类准确率方面提升显著。

## 📝 摘要（中文）

开发能够在识别分布内(ID)数据的同时检测分布外(OOD)样本的开放集分类方法，对于在开放世界场景中部署图神经网络(GNN)至关重要。现有方法通常将所有OOD样本视为单个类别，然而现实应用，尤其是在欺诈检测和医疗诊断等高风险场景中，需要对OOD样本进行更深入的了解，包括其可能的标签。这提出了一个关键问题：能否在没有真实标签信息的情况下将OOD检测扩展到OOD分类？为了解决这个问题，我们提出了一个粗到细的开放集分类(CFC)框架，该框架利用大型语言模型(LLM)处理图数据集。CFC由三个关键组件组成：一个粗分类器，它使用LLM提示进行OOD检测和异常值标签生成；一个基于GNN的细分类器，该分类器使用粗分类器识别的OOD样本进行训练，以增强OOD检测和ID分类；以及通过LLM提示和后处理OOD标签实现的精细化OOD分类。与依赖合成或辅助OOD样本的方法不同，CFC采用基于其内在含义的语义OOD实例，这些实例是真正分布外的，从而提高了可解释性和实用性。实验结果表明，CFC在图和文本领域将OOD检测提高了10%，并在图数据集上实现了高达70%的OOD分类准确率。

## 🔬 方法详解

**问题定义**：现有图神经网络的开放集分类方法主要关注区分ID样本和OOD样本，但通常将所有OOD样本视为一个类别，无法提供关于OOD样本的更细粒度信息。在实际应用中，例如欺诈检测或医疗诊断，了解OOD样本的潜在类别至关重要。因此，论文旨在解决如何在没有OOD样本真实标签的情况下，对OOD样本进行分类的问题。

**核心思路**：论文的核心思路是利用大语言模型(LLM)的语义理解能力，对OOD样本进行粗粒度的分类，生成伪标签，然后利用这些伪标签训练图神经网络(GNN)，从而实现细粒度的OOD分类。这种“粗到细”的方法能够有效地利用LLM的先验知识，同时结合GNN在图结构数据上的优势。

**技术框架**：CFC框架包含三个主要阶段：1) **粗分类器**：使用LLM对图节点进行分类，并识别OOD样本，同时生成OOD样本的伪标签。LLM通过特定的prompt进行引导，以生成具有语义意义的标签。2) **细分类器**：使用GNN，并利用粗分类器识别的OOD样本及其伪标签进行训练，从而提高GNN在OOD检测和ID分类方面的性能。3) **OOD分类优化**：使用LLM对GNN的OOD分类结果进行优化，通过prompt工程和后处理，进一步提升OOD分类的准确性。

**关键创新**：CFC框架的关键创新在于将大语言模型(LLM)引入到图神经网络的开放集分类任务中，并利用LLM的语义理解能力生成OOD样本的伪标签。与现有方法依赖合成或辅助OOD样本不同，CFC直接利用LLM对真实OOD样本进行分类，从而提高了OOD分类的可解释性和实用性。

**关键设计**：在粗分类器阶段，关键在于设计合适的LLM prompt，以引导LLM生成高质量的OOD伪标签。在细分类器阶段，使用标准的GNN模型，并采用交叉熵损失函数进行训练。在OOD分类优化阶段，通过prompt工程和后处理，对LLM的输出进行修正，以提高OOD分类的准确性。具体的参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16244v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16244v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16244v1/ood-prompt.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CFC框架在图和文本领域将OOD检测的性能提升了10%，并在图数据集上实现了高达70%的OOD分类准确率。这些结果表明，CFC框架能够有效地利用大语言模型的语义理解能力，提高图神经网络在开放集分类任务中的性能。

## 🎯 应用场景

该研究成果可应用于欺诈检测、医疗诊断、金融风控等领域。通过识别和分类异常节点，可以帮助发现潜在的欺诈行为、疾病风险或金融风险。未来，该方法可以扩展到其他类型的图数据和开放世界场景，为智能决策提供更可靠的支持。

## 📄 摘要（原文）

> Developing open-set classification methods capable of classifying in-distribution (ID) data while detecting out-of-distribution (OOD) samples is essential for deploying graph neural networks (GNNs) in open-world scenarios. Existing methods typically treat all OOD samples as a single class, despite real-world applications, especially high-stake settings such as fraud detection and medical diagnosis, demanding deeper insights into OOD samples, including their probable labels. This raises a critical question: can OOD detection be extended to OOD classification without true label information? To address this question, we propose a Coarse-to-Fine open-set Classification (CFC) framework that leverages large language models (LLMs) for graph datasets. CFC consists of three key components: a coarse classifier that uses LLM prompts for OOD detection and outlier label generation, a GNN-based fine classifier trained with OOD samples identified by the coarse classifier for enhanced OOD detection and ID classification, and refined OOD classification achieved through LLM prompts and post-processed OOD labels. Unlike methods that rely on synthetic or auxiliary OOD samples, CFC employs semantic OOD instances that are genuinely out-of-distribution based on their inherent meaning, improving interpretability and practical utility. Experimental results show that CFC improves OOD detection by ten percent over state-of-the-art methods on graph and text domains and achieves up to seventy percent accuracy in OOD classification on graph datasets.

