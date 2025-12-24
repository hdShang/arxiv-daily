---
layout: default
title: "FedVLMBench: Benchmarking Federated Fine-Tuning of Vision-Language Models"
---

# FedVLMBench: Benchmarking Federated Fine-Tuning of Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09638" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09638v1</a>
  <a href="https://arxiv.org/pdf/2506.09638.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09638v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09638v1', 'FedVLMBench: Benchmarking Federated Fine-Tuning of Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiying Zheng, Ziyue Lin, Pengxin Guo, Yuyin Zhou, Feifei Wang, Liangqiong Qu

**分类**: cs.LG, cs.CV

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出FedVLMBench以解决联邦学习下视觉-语言模型微调评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `视觉-语言模型` `微调策略` `数据异质性` `多模态学习` `隐私保护` `基准评估`

## 📋 核心要点

1. 现有的视觉-语言模型微调方法大多依赖集中式训练，无法满足隐私要求高的领域，如医疗。
2. 本文提出FedVLMBench，作为第一个系统性基准，评估VLMs的联邦微调策略和模型架构。
3. 实验结果表明，2层MLP连接器在联邦学习中对编码器基础的VLMs表现最佳，且视觉任务对数据异质性更敏感。

## 📝 摘要（中文）

视觉-语言模型（VLMs）通过整合视觉和文本信息，在跨模态理解和生成方面展现了卓越能力。然而，现有的微调方法大多依赖集中式训练，难以满足医疗等领域的隐私需求。为此，本文提出了FedVLMBench，这是第一个系统性评估VLMs联邦微调的基准，整合了多种模型架构、微调策略和联邦学习算法。通过广泛实验，发现2层多层感知器（MLP）连接器在联邦学习中对编码器基础的VLMs表现最佳，同时当前的联邦学习方法对视觉任务的数据异质性敏感性显著高于文本任务。该基准为研究社区提供了重要工具和数据集，推动隐私保护的多模态基础模型的联邦训练。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言模型在联邦学习环境下微调评估缺乏系统性基准的问题。现有方法在隐私保护和数据异质性方面存在显著挑战。

**核心思路**：提出FedVLMBench基准，整合多种VLM架构、微调策略和联邦学习算法，以系统性评估联邦微调的效果和适用性。

**技术框架**：FedVLMBench包含两种主流VLM架构（基于编码器和无编码器）、四种微调策略、五种联邦学习算法，以及六个跨领域数据集，覆盖单任务和多任务场景。

**关键创新**：最重要的创新在于提供了一个全面的基准框架，能够评估不同微调策略和模型架构在联邦学习中的表现，填补了现有研究的空白。

**关键设计**：在实验中，采用了2层MLP连接器与并行连接器和大语言模型（LLM）调优的组合，发现其在编码器基础VLMs中的表现最佳。同时，针对数据异质性进行了深入分析，揭示了视觉任务和文本任务的敏感性差异。

## 📊 实验亮点

实验结果显示，采用2层MLP连接器的配置在编码器基础的VLMs中表现最佳，显著提升了模型在联邦学习中的性能。此外，视觉任务对数据异质性的敏感性明显高于文本任务，为未来的研究提供了重要的参考。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融等对隐私要求高的行业，能够在保护用户隐私的前提下，利用多模态数据进行模型训练。未来，FedVLMBench将为多模态基础模型的隐私保护训练提供标准化平台，推动相关领域的研究进展。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have demonstrated remarkable capabilities in cross-modal understanding and generation by integrating visual and textual information. While instruction tuning and parameter-efficient fine-tuning methods have substantially improved the generalization of VLMs, most existing approaches rely on centralized training, posing challenges for deployment in domains with strict privacy requirements like healthcare. Recent efforts have introduced Federated Learning (FL) into VLM fine-tuning to address these privacy concerns, yet comprehensive benchmarks for evaluating federated fine-tuning strategies, model architectures, and task generalization remain lacking. In this work, we present \textbf{FedVLMBench}, the first systematic benchmark for federated fine-tuning of VLMs. FedVLMBench integrates two mainstream VLM architectures (encoder-based and encoder-free), four fine-tuning strategies, five FL algorithms, six multimodal datasets spanning four cross-domain single-task scenarios and two cross-domain multitask settings, covering four distinct downstream task categories. Through extensive experiments, we uncover key insights into the interplay between VLM architectures, fine-tuning strategies, data heterogeneity, and multi-task federated optimization. Notably, we find that a 2-layer multilayer perceptron (MLP) connector with concurrent connector and LLM tuning emerges as the optimal configuration for encoder-based VLMs in FL. Furthermore, current FL methods exhibit significantly higher sensitivity to data heterogeneity in vision-centric tasks than text-centric ones, across both encoder-free and encoder-based VLM architectures. Our benchmark provides essential tools, datasets, and empirical guidance for the research community, offering a standardized platform to advance privacy-preserving, federated training of multimodal foundation models.

