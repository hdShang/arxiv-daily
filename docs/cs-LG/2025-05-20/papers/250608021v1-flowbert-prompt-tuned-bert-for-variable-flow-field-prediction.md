---
layout: default
title: FlowBERT: Prompt-tuned BERT for variable flow field prediction
---

# FlowBERT: Prompt-tuned BERT for variable flow field prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08021" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08021v1</a>
  <a href="https://arxiv.org/pdf/2506.08021.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08021v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08021v1', 'FlowBERT: Prompt-tuned BERT for variable flow field prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weihao Zou, Weibing Feng, Pin Wu

**分类**: cs.LG, physics.flu-dyn

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出FlowBERT以解决传统CFD方法计算成本高的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `流场预测` `知识转移` `计算流体动力学` `深度学习` `适当正交分解` `微调模型` `流体动力学`

## 📋 核心要点

1. 现有的计算流体动力学方法计算成本高，且深度学习模型在不同条件下的迁移能力有限。
2. 本研究提出FlowBERT框架，通过知识转移和POD降维，结合流体动力学文本模板，提升流场预测能力。
3. 实验结果显示，FlowBERT在少样本学习中优于传统模型，预测时间从数小时缩短至数秒，且准确率超过90%。

## 📝 摘要（中文）

本研究提出了一种基于知识转移的通用流场预测框架FlowBERT，旨在解决传统计算流体动力学（CFD）方法的高计算成本及现有深度学习模型的有限跨条件迁移能力。该框架创新性地将适当正交分解（POD）降维与预训练大语言模型（LLM）的微调策略相结合，POD用于压缩流场特征的表示，而微调模型则学习在状态空间中编码系统动态。为了增强模型对流场数据的适应性，我们特别设计了面向流体动力学的文本模板，通过丰富的上下文语义信息提高预测性能。实验结果表明，该框架在少样本学习场景中优于传统Transformer模型，并在不同的流入条件和翼型几何形状下表现出卓越的泛化能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决传统计算流体动力学（CFD）方法在计算成本和效率上的不足，尤其是在面对不同流入条件和几何形状时，现有深度学习模型的迁移能力有限。

**核心思路**：论文提出的FlowBERT框架通过结合适当正交分解（POD）和预训练大语言模型（LLM）的微调策略，旨在实现高效的流场预测。POD用于提取和压缩流场特征，而微调的LLM则能够更好地学习流体系统的动态特性。

**技术框架**：FlowBERT的整体架构包括两个主要模块：首先是POD模块，用于流场特征的降维和压缩；其次是微调的LLM模块，负责在状态空间中学习系统动态。通过流体动力学导向的文本模板，增强模型对流场数据的适应性。

**关键创新**：FlowBERT的主要创新在于将POD与LLM微调相结合，形成了一种新的知识转移范式。这种方法不仅提高了流场特征的表示能力，还增强了模型在不同条件下的泛化能力，显著优于传统的CFD方法和深度学习模型。

**关键设计**：在模型设计中，POD的参数设置和文本模板的设计是关键因素。损失函数采用了适应性策略，以确保模型在训练过程中能够有效学习流场的动态特性。网络结构上，FlowBERT在Transformer基础上进行了优化，以适应流体动力学的特定需求。

## 📊 实验亮点

实验结果显示，FlowBERT在少样本学习场景中表现优异，相较于传统的Navier-Stokes方程求解器，预测时间从数小时缩短至数秒，同时保持超过90%的准确率，展现了显著的性能提升。

## 🎯 应用场景

该研究的FlowBERT框架具有广泛的潜在应用，尤其是在航空航天、汽车工程和其他工程领域的流体动力学预测中。通过快速准确的流场预测，能够为气动优化、流动控制等工程问题提供有效的解决方案，推动相关技术的发展。

## 📄 摘要（原文）

> This study proposes a universal flow field prediction framework based on knowledge transfer
>   from large language model (LLM), addressing the high computational costs of traditional
>   computational fluid dynamics (CFD) methods and the limited cross-condition transfer capability
>   of existing deep learning models. The framework innovatively integrates Proper Orthogonal
>   Decomposition (POD) dimensionality reduction with fine-tuning strategies for pretrained LLM,
>   where POD facilitates compressed representation of flow field features while the fine-tuned model
>   learns to encode system dynamics in state space. To enhance the model's adaptability to flow field
>   data, we specifically designed fluid dynamics-oriented text templates that improve predictive
>   performance through enriched contextual semantic information. Experimental results demonstrate
>   that our framework outperforms conventional Transformer models in few-shot learning scenarios while
>   exhibiting exceptional generalization across various inflow conditions and airfoil geometries.
>   Ablation studies reveal the contributions of key components in the FlowBERT architecture. Compared
>   to traditional Navier-Stokes equation solvers requiring hours of computation, our approach reduces
>   prediction time to seconds while maintaining over 90% accuracy. The developed knowledge transfer
>   paradigm establishes a new direction for rapid fluid dynamics prediction, with potential
>   applications extending to aerodynamic optimization, flow control, and other engineering domains.

