---
layout: default
title: Uncovering Brain-Like Hierarchical Patterns in Vision-Language Models through fMRI-Based Neural Encoding
---

# Uncovering Brain-Like Hierarchical Patterns in Vision-Language Models through fMRI-Based Neural Encoding

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.16870" target="_blank" class="toolbar-btn">arXiv: 2510.16870v1</a>
    <a href="https://arxiv.org/pdf/2510.16870.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16870v1" 
            onclick="toggleFavorite(this, '2510.16870v1', 'Uncovering Brain-Like Hierarchical Patterns in Vision-Language Models through fMRI-Based Neural Encoding')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yudan Ren, Xinlong Wang, Kexin Wang, Tian Xia, Zihan Ma, Zhaowei Li, Xiangrong Bi, Xiao Li, Xiaowei He

**分类**: cs.CV

**发布日期**: 2025-10-19

**备注**: 14 pages, 7 figures

---

## 💡 一句话要点

**通过fMRI神经编码揭示视觉-语言模型中类脑分层模式**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `fMRI` `神经编码` `类脑智能` `多模态学习`

## 📋 核心要点

1. 现有研究未能充分理解人工神经网络与人脑多模态信息处理的内在联系，特别是忽略了神经元层面的分析。
2. 该论文提出了一种新颖的神经元级别分析框架，结合人工神经元分析与fMRI体素编码，研究VLM中的多模态信息处理。
3. 实验结果表明，VLM中的人工神经元能够预测生物神经元的活动，并展现出与人脑相似的功能冗余和极性模式。

## 📝 摘要（中文）

本研究旨在探索人工神经网络（ANN）与人脑处理之间的联系，现有研究的局限性在于：单模态ANN研究无法捕捉大脑固有的多模态处理能力，多模态ANN研究主要关注高层模型输出，忽略了单个神经元的关键作用。为了解决这些问题，我们提出了一种新的神经元级别分析框架，通过人脑活动研究视觉-语言模型（VLM）中的多模态信息处理机制。我们的方法将精细的人工神经元（AN）分析与基于fMRI的体素编码相结合，以检查两种架构不同的VLM：CLIP和METER。分析揭示了四个关键发现：（1）AN成功预测了跨多个功能网络（包括语言、视觉、注意力和默认模式）的生物神经元（BN）活动，证明了共享的表征机制；（2）AN和BN都通过重叠的神经表征表现出功能冗余，反映了大脑的容错和协作信息处理机制；（3）AN表现出与BN平行的极性模式，具有相反激活的BN在VLM层中显示出镜像激活趋势，反映了神经信息处理的复杂性和双向性；（4）CLIP和METER的架构驱动不同的BN：CLIP的独立分支显示出模态特定的专业化，而METER的跨模态设计产生统一的跨模态激活，突出了架构对ANN类脑属性的影响。这些结果为VLM在神经元级别上的类脑分层处理提供了有力的证据。

## 🔬 方法详解

**问题定义**：现有研究在理解视觉-语言模型（VLM）与人脑信息处理机制的对应关系时存在不足。一方面，单模态人工神经网络（ANN）的研究无法捕捉人脑固有的多模态信息处理能力。另一方面，现有的多模态ANN研究主要关注模型的高层输出，而忽略了单个神经元在信息处理中的关键作用。因此，如何从神经元层面深入理解VLM的类脑特性是一个亟待解决的问题。

**核心思路**：该论文的核心思路是将人工神经网络中的神经元活动与人脑的神经活动进行直接比较，从而揭示VLM中类脑信息处理的模式。具体而言，通过fMRI技术获取人脑在处理视觉和语言信息时的神经活动数据，然后利用神经编码模型，将VLM中人工神经元的活动与人脑神经元的活动进行关联。通过分析这种关联，可以深入了解VLM如何模拟人脑的多模态信息处理机制。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 选择两种具有代表性的VLM模型：CLIP和METER。CLIP采用独立分支处理视觉和语言信息，而METER则采用跨模态设计。2) 使用fMRI技术获取人脑在处理视觉和语言信息时的神经活动数据。3) 提取VLM中人工神经元的活动数据。4) 使用神经编码模型，将VLM中人工神经元的活动与人脑神经元的活动进行关联。5) 分析神经编码模型的结果，揭示VLM中类脑信息处理的模式。

**关键创新**：该论文的关键创新在于提出了一个神经元级别的分析框架，将人工神经网络中的神经元活动与人脑的神经活动进行直接比较。这种方法能够更深入地了解VLM如何模拟人脑的多模态信息处理机制。此外，该研究还首次揭示了VLM中人工神经元与人脑神经元之间存在功能冗余和极性模式等相似性。

**关键设计**：该研究的关键设计包括：1) 选择CLIP和METER两种架构不同的VLM模型，以便比较不同架构对VLM类脑特性的影响。2) 使用fMRI技术获取高质量的人脑神经活动数据。3) 采用合适的神经编码模型，建立人工神经元与人脑神经元之间的关联。4) 设计合理的实验方案，验证研究结果的可靠性。

## 📊 实验亮点

该研究发现，VLM中的人工神经元能够成功预测人脑多个功能网络（包括语言、视觉、注意力和默认模式）的生物神经元活动，证明了共享的表征机制。此外，研究还揭示了人工神经元和生物神经元都表现出功能冗余，以及人工神经元展现出与生物神经元平行的极性模式。CLIP和METER两种架构驱动不同的生物神经元活动，CLIP表现出模态特异性，而METER表现出跨模态统一激活。

## 🎯 应用场景

该研究成果可应用于开发更具生物合理性的人工智能系统，例如，设计更高效、更鲁棒的视觉-语言模型。此外，该研究还有助于深入理解人脑的信息处理机制，为神经科学研究提供新的视角和工具。未来，该研究或可用于开发新型脑机接口设备，实现更自然的人机交互。

## 📄 摘要（原文）

> While brain-inspired artificial intelligence(AI) has demonstrated promising results, current understanding of the parallels between artificial neural networks (ANNs) and human brain processing remains limited: (1) unimodal ANN studies fail to capture the brain's inherent multimodal processing capabilities, and (2) multimodal ANN research primarily focuses on high-level model outputs, neglecting the crucial role of individual neurons. To address these limitations, we propose a novel neuron-level analysis framework that investigates the multimodal information processing mechanisms in vision-language models (VLMs) through the lens of human brain activity. Our approach uniquely combines fine-grained artificial neuron (AN) analysis with fMRI-based voxel encoding to examine two architecturally distinct VLMs: CLIP and METER. Our analysis reveals four key findings: (1) ANs successfully predict biological neurons (BNs) activities across multiple functional networks (including language, vision, attention, and default mode), demonstrating shared representational mechanisms; (2) Both ANs and BNs demonstrate functional redundancy through overlapping neural representations, mirroring the brain's fault-tolerant and collaborative information processing mechanisms; (3) ANs exhibit polarity patterns that parallel the BNs, with oppositely activated BNs showing mirrored activation trends across VLM layers, reflecting the complexity and bidirectional nature of neural information processing; (4) The architectures of CLIP and METER drive distinct BNs: CLIP's independent branches show modality-specific specialization, whereas METER's cross-modal design yields unified cross-modal activation, highlighting the architecture's influence on ANN brain-like properties. These results provide compelling evidence for brain-like hierarchical processing in VLMs at the neuronal level.

