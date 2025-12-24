---
layout: default
title: "Extracting Multimodal Learngene in CLIP: Unveiling the Multimodal Generalizable Knowledge"
---

# Extracting Multimodal Learngene in CLIP: Unveiling the Multimodal Generalizable Knowledge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16673" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16673v1</a>
  <a href="https://arxiv.org/pdf/2506.16673.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16673v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16673v1', 'Extracting Multimodal Learngene in CLIP: Unveiling the Multimodal Generalizable Knowledge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruiming Chen, Junming Yang, Shiyu Xia, Xu Yang, Jing Wang, Xin Geng

**分类**: cs.CV

**发布日期**: 2025-06-20

---

## 💡 一句话要点

**提出MM-LG以高效提取CLIP中的多模态可泛化知识**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `可泛化知识` `CLIP` `模型初始化` `高效部署` `计算机视觉` `自然语言处理`

## 📋 核心要点

1. 现有的Learngene方法未能有效处理多模态场景中的可泛化知识，导致在不同规模的CLIP预训练中面临挑战。
2. 本文提出MM-LG框架，通过多模态和单模态模块加权提取可泛化知识，初始化不同规模和模态的后代模型。
3. 实验结果显示，MM-LG在Oxford-IIIT PET和Flickr30k数据集上分别提升了3.1%和4.13%的性能，同时减少了约25%的参数存储和2.8倍的预训练成本。

## 📝 摘要（中文）

CLIP（对比语言-图像预训练）因其多模态可泛化知识而受到广泛关注，这对下游任务至关重要。然而，大量参数和大规模预训练的计算开销使得预训练不同规模的CLIP面临挑战。Learngene从祖先模型中提取可泛化组件并初始化多样的后代模型，但现有的Learngene范式未能处理多模态场景中的可泛化知识。本文提出利用多模态模块提取多模态可泛化知识，进而提出MM-LG（多模态Learngene）框架，旨在从CLIP中提取和利用可泛化组件。实验表明，MM-LG在多个任务上表现优越，且显著降低了预训练成本，适合高效部署。

## 🔬 方法详解

**问题定义**：本文旨在解决现有Learngene方法在多模态场景中无法有效提取可泛化知识的问题，尤其是在不同规模的CLIP预训练中面临的计算开销挑战。

**核心思路**：提出MM-LG框架，通过建立多模态和单模态模块，采用加权求和的方式提取可泛化知识，从而为不同规模和模态的后代模型提供初始化。

**技术框架**：MM-LG框架包括两个主要模块：多模态模块和单模态模块，分别用于提取多模态和单模态的可泛化知识。通过加权求和的方式整合这些知识，形成对后代模型的有效初始化。

**关键创新**：MM-LG的创新在于引入多模态模块以提取多模态可泛化知识，解决了现有方法在多模态场景中的不足，显著提升了模型的适应性和性能。

**关键设计**：在参数设置上，MM-LG仅需约25%的参数存储，并通过优化的损失函数和网络结构设计，降低了预训练成本，提升了模型在多样化下游任务中的表现。

## 📊 实验亮点

实验结果显示，MM-LG在Oxford-IIIT PET和Flickr30k数据集上分别提升了3.1%和4.13%的性能，相较于传统的预训练和微调方法，MM-LG在性能上也有1.9%和3.65%的提升，同时显著降低了预训练成本，具有较高的实用价值。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理及其交叉领域，尤其是在需要高效模型部署的场景中，如图像识别、文本生成和多模态检索等。未来，MM-LG有望推动多模态学习技术的广泛应用，提升模型在实际任务中的表现。

## 📄 摘要（原文）

> CLIP (Contrastive Language-Image Pre-training) has attracted widespread attention for its multimodal generalizable knowledge, which is significant for downstream tasks. However, the computational overhead of a large number of parameters and large-scale pre-training poses challenges of pre-training a different scale of CLIP. Learngene extracts the generalizable components termed as learngene from an ancestry model and initializes diverse descendant models with it. Previous Learngene paradigms fail to handle the generalizable knowledge in multimodal scenarios. In this paper, we put forward the idea of utilizing a multimodal block to extract the multimodal generalizable knowledge, which inspires us to propose MM-LG (Multimodal Learngene), a novel framework designed to extract and leverage generalizable components from CLIP. Specifically, we first establish multimodal and unimodal blocks to extract the multimodal and unimodal generalizable knowledge in a weighted-sum manner. Subsequently, we employ these components to numerically initialize descendant models of varying scales and modalities. Extensive experiments demonstrate MM-LG's effectiveness, which achieves performance gains over existing learngene approaches (e.g.,+3.1% on Oxford-IIIT PET and +4.13% on Flickr30k) and comparable or superior results to the pre-training and fine-tuning paradigm (e.g.,+1.9% on Oxford-IIIT PET and +3.65% on Flickr30k). Notably, MM-LG requires only around 25% of the parameter storage while reducing around 2.8 times pre-training costs for diverse model scales compared to the pre-training and fine-tuning paradigm, making it particularly suitable for efficient deployment across diverse downstream tasks.

