---
layout: default
title: "MITS: A Large-Scale Multimodal Benchmark Dataset for Intelligent Traffic Surveillance"
---

# MITS: A Large-Scale Multimodal Benchmark Dataset for Intelligent Traffic Surveillance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09730" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09730v1</a>
  <a href="https://arxiv.org/pdf/2509.09730.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09730v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09730v1', 'MITS: A Large-Scale Multimodal Benchmark Dataset for Intelligent Traffic Surveillance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaikai Zhao, Zhaoxiang Liu, Peng Wang, Xin Wang, Zhicheng Ma, Yajun Xu, Wenjing Zhang, Yibing Nan, Kai Wang, Shiguo Lian

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-10

**备注**: accepted by Image and Vision Computing

---

## 💡 一句话要点

**提出大规模多模态智能交通监控数据集MITS，提升LMM在ITS领域的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `智能交通监控` `多模态学习` `大型数据集` `视觉问答` `图像描述` `交通事件识别` `目标检测`

## 📋 核心要点

1. 通用多模态模型在智能交通监控领域表现受限，缺乏专用数据集是主要瓶颈。
2. 构建大规模多模态数据集MITS，包含真实ITS图像、图像描述和视觉问答对，覆盖多种ITS任务。
3. 在MITS上微调LMM，显著提升了模型在ITS应用中的性能，并开源数据集及代码。

## 📝 摘要（中文）

通用领域的大型多模态模型(LMM)在各种图像-文本任务中取得了显著进展。然而，由于缺乏专门的多模态数据集，它们在智能交通监控(ITS)领域的性能仍然有限。为了解决这个问题，我们推出了MITS（多模态智能交通监控），这是第一个专门为ITS设计的大规模多模态基准数据集。MITS包括170,400张独立收集的真实世界ITS图像，这些图像来自交通监控摄像头，并标注了八个主要类别和24个子类别的ITS特定对象和事件，涵盖了各种环境条件。此外，通过系统的数据生成流程，我们生成了高质量的图像描述和500万个指令跟随式视觉问答对，解决了五个关键的ITS任务：对象和事件识别、对象计数、对象定位、背景分析和事件推理。为了证明MITS的有效性，我们在该数据集上微调了主流的LMM，从而能够开发ITS特定的应用程序。实验结果表明，MITS显著提高了LMM在ITS应用中的性能，例如LLaVA-1.5的性能从0.494提高到0.905（+83.2%）。我们以开源形式发布数据集、代码和模型，为推进ITS和LMM研究提供高价值资源。

## 🔬 方法详解

**问题定义**：现有通用领域的多模态模型在智能交通监控（ITS）领域的应用效果不佳，主要原因是缺乏针对该领域的大规模、高质量的多模态数据集。现有数据集无法满足ITS任务的特定需求，例如细粒度的对象和事件识别、复杂的场景理解和推理等。这限制了LMM在ITS领域的应用潜力。

**核心思路**：论文的核心思路是构建一个大规模、高质量的ITS领域多模态数据集MITS，通过提供丰富的图像数据、详细的标注信息和多样化的视觉问答对，来弥补现有数据集的不足。该数据集旨在促进LMM在ITS领域的应用，并提升其性能。

**技术框架**：MITS数据集的构建主要包含两个阶段：数据收集和数据生成。数据收集阶段，从交通监控摄像头收集了170,400张真实世界的ITS图像，并标注了八个主要类别和24个子类别的ITS特定对象和事件。数据生成阶段，通过系统的流程生成了高质量的图像描述和500万个指令跟随式视觉问答对，涵盖了对象和事件识别、对象计数、对象定位、背景分析和事件推理等五个关键的ITS任务。

**关键创新**：MITS是第一个专门为智能交通监控（ITS）领域设计的大规模多模态基准数据集。其创新之处在于：1) 数据规模大，包含170,400张真实ITS图像和500万个视觉问答对；2) 数据质量高，图像标注细致，视觉问答对设计合理；3) 任务覆盖全面，涵盖了ITS领域多个关键任务。

**关键设计**：数据生成流程是MITS的关键设计之一。该流程采用系统化的方法，确保生成高质量的图像描述和视觉问答对。具体来说，图像描述的生成采用了基于模板的方法，并结合人工校对，以保证描述的准确性和流畅性。视觉问答对的生成则采用了多种策略，包括基于规则的方法、基于模型的方法和人工生成的方法，以保证问答对的多样性和挑战性。

## 📊 实验亮点

实验结果表明，在MITS数据集上微调LMM可以显著提升其在ITS应用中的性能。例如，LLaVA-1.5的性能从0.494提高到0.905（+83.2%），LLaVA-1.6的性能从0.678提高到0.921（+35.8%），Qwen2-VL的性能从0.584提高到0.926（+58.6%），Qwen2.5-VL的性能从0.732提高到0.930（+27.0%）。这些结果表明MITS数据集对于提升LMM在ITS领域的性能具有重要价值。

## 🎯 应用场景

该研究成果可广泛应用于智能交通监控领域，例如智能交通管理、自动驾驶、安全监控等。MITS数据集的发布将促进LMM在ITS领域的应用，提升交通监控系统的智能化水平，例如实现更准确的交通事件检测、更智能的交通流量控制和更高效的交通安全管理。未来，基于MITS数据集训练的模型可以部署在实际的交通监控系统中，为城市交通管理提供更强大的技术支持。

## 📄 摘要（原文）

> General-domain large multimodal models (LMMs) have achieved significant advances in various image-text tasks. However, their performance in the Intelligent Traffic Surveillance (ITS) domain remains limited due to the absence of dedicated multimodal datasets. To address this gap, we introduce MITS (Multimodal Intelligent Traffic Surveillance), the first large-scale multimodal benchmark dataset specifically designed for ITS. MITS includes 170,400 independently collected real-world ITS images sourced from traffic surveillance cameras, annotated with eight main categories and 24 subcategories of ITS-specific objects and events under diverse environmental conditions. Additionally, through a systematic data generation pipeline, we generate high-quality image captions and 5 million instruction-following visual question-answer pairs, addressing five critical ITS tasks: object and event recognition, object counting, object localization, background analysis, and event reasoning. To demonstrate MITS's effectiveness, we fine-tune mainstream LMMs on this dataset, enabling the development of ITS-specific applications. Experimental results show that MITS significantly improves LMM performance in ITS applications, increasing LLaVA-1.5's performance from 0.494 to 0.905 (+83.2%), LLaVA-1.6's from 0.678 to 0.921 (+35.8%), Qwen2-VL's from 0.584 to 0.926 (+58.6%), and Qwen2.5-VL's from 0.732 to 0.930 (+27.0%). We release the dataset, code, and models as open-source, providing high-value resources to advance both ITS and LMM research.

