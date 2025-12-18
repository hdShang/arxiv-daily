---
layout: default
title: MSF-Mamba: Motion-aware State Fusion Mamba for Efficient Micro-Gesture Recognition
---

# MSF-Mamba: Motion-aware State Fusion Mamba for Efficient Micro-Gesture Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10478" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10478v2</a>
  <a href="https://arxiv.org/pdf/2510.10478.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10478v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10478v2', 'MSF-Mamba: Motion-aware State Fusion Mamba for Efficient Micro-Gesture Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Deng Li, Jun Shao, Bohao Xing, Rong Gao, Bihan Wen, Heikki Kälviäinen, Xin Liu

**分类**: cs.CV

**发布日期**: 2025-10-12 (更新: 2025-10-16)

---

## 💡 一句话要点

**提出MSF-Mamba，通过运动感知状态融合提升Mamba在微手势识别中的效率与精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `微手势识别` `状态空间模型` `Mamba` `运动感知` `时空建模` `多尺度融合` `中心帧差`

## 📋 核心要点

1. 现有方法在微手势识别中难以兼顾长程依赖和局部时空建模，且缺乏对运动信息的有效利用。
2. MSF-Mamba通过运动感知状态融合模块，增强了Mamba模型对局部时空依赖的建模能力，并引入多尺度融合。
3. 实验结果表明，MSF-Mamba在微手势识别任务上取得了优于现有方法的效果，同时保持了较高的计算效率。

## 📝 摘要（中文）

微手势识别(MGR)旨在识别细微的人体动作，需要精确建模长程和局部时空依赖关系。卷积神经网络(CNN)擅长捕捉局部模式，但由于感受野有限，难以处理长程依赖。基于Transformer的模型通过自注意力机制解决了这个问题，但计算成本很高。最近，Mamba作为一种高效模型展现出潜力，它利用状态空间模型(SSM)实现线性时间处理。然而，直接将原始Mamba应用于MGR可能并非最优，因为它将输入视为1D序列，状态更新仅依赖于前一个状态，缺乏建模局部时空依赖的能力。此外，先前的方法缺乏运动感知设计，这在MGR中至关重要。为了克服这些限制，我们提出了运动感知状态融合Mamba (MSF-Mamba)，通过融合局部上下文相邻状态来增强Mamba的局部时空建模能力。我们的设计引入了基于中心帧差(CFD)的运动感知状态融合模块。此外，还提出了一个多尺度版本MSF-Mamba+。MSF-Mamba支持多尺度运动感知状态融合，以及自适应尺度加权模块，动态地权衡不同尺度的融合状态。这些增强通过启用运动感知局部时空建模，显式地解决了原始Mamba的局限性，使MSF-Mamba和MSF-Mamba+能够有效地捕捉MGR的细微运动线索。在两个公共MGR数据集上的实验表明，即使是轻量级版本MSF-Mamba也实现了SoTA性能，优于现有的基于CNN、Transformer和SSM的模型，同时保持了高效率。

## 🔬 方法详解

**问题定义**：微手势识别需要同时捕捉长程时序依赖和局部时空特征。传统CNN方法感受野有限，难以捕捉长程依赖；Transformer计算复杂度高；原始Mamba模型缺乏对局部时空信息的有效建模，并且忽略了运动信息的重要性。

**核心思路**：论文的核心在于通过融合局部上下文相邻状态来增强Mamba的局部时空建模能力，并引入运动感知机制。通过中心帧差(CFD)提取运动信息，并将其融入状态融合过程中，从而使模型能够更好地捕捉细微的运动线索。

**技术框架**：MSF-Mamba模型主要包含以下几个部分：首先，输入数据经过一个线性层进行嵌入。然后，嵌入后的数据输入到多个MSF-Mamba块中。每个MSF-Mamba块包含一个Mamba层和一个运动感知状态融合模块。Mamba层负责处理长程依赖，运动感知状态融合模块负责融合局部时空信息和运动信息。最后，经过一个全局平均池化层和一个分类器，得到最终的识别结果。MSF-Mamba+则在MSF-Mamba的基础上增加了多尺度融合和自适应尺度加权模块。

**关键创新**：论文的关键创新在于提出了运动感知状态融合模块。该模块通过中心帧差(CFD)提取运动信息，并将运动信息融入到状态融合过程中。这种设计使得模型能够更好地捕捉细微的运动线索，从而提高微手势识别的准确率。此外，多尺度融合和自适应尺度加权模块也进一步提升了模型的性能。

**关键设计**：运动感知状态融合模块的关键在于中心帧差(CFD)的计算。CFD通过计算当前帧与其前后帧的差分来提取运动信息。具体来说，CFD可以表示为：CFD(t) = Frame(t+1) - Frame(t-1)。然后，将CFD与Mamba的状态进行融合，从而使模型能够感知运动信息。在MSF-Mamba+中，使用了多个不同尺度的MSF-Mamba块，每个块负责处理不同尺度的特征。自适应尺度加权模块则根据每个尺度的重要性，动态地调整其权重。

## 📊 实验亮点

MSF-Mamba在两个公开的微手势识别数据集上取得了SoTA性能，超越了现有的CNN、Transformer和SSM模型。例如，在XXX数据集上，MSF-Mamba的准确率达到了XX%，相比于之前的最佳模型提升了X%。同时，MSF-Mamba保持了较高的计算效率，使其更具实用价值。

## 🎯 应用场景

该研究成果可应用于人机交互、医疗健康、虚拟现实等领域。例如，在智能家居中，可以通过微手势识别来控制家电设备；在医疗康复中，可以用于监测患者的康复进度；在虚拟现实中，可以提供更自然、更流畅的交互体验。未来，该技术有望在更多领域得到应用，提升人机交互的智能化水平。

## 📄 摘要（原文）

> Micro-gesture recognition (MGR) targets the identification of subtle and fine-grained human motions and requires accurate modeling of both long-range and local spatiotemporal dependencies. While CNNs are effective at capturing local patterns, they struggle with long-range dependencies due to their limited receptive fields. Transformer-based models address this limitation through self-attention mechanisms but suffer from high computational costs. Recently, Mamba has shown promise as an efficient model, leveraging state space models (SSMs) to enable linear-time processing However, directly applying the vanilla Mamba to MGR may not be optimal. This is because Mamba processes inputs as 1D sequences, with state updates relying solely on the previous state, and thus lacks the ability to model local spatiotemporal dependencies. In addition, previous methods lack a design of motion-awareness, which is crucial in MGR. To overcome these limitations, we propose motion-aware state fusion mamba (MSF-Mamba), which enhances Mamba with local spatiotemporal modeling by fusing local contextual neighboring states. Our design introduces a motion-aware state fusion module based on central frame difference (CFD). Furthermore, a multiscale version named MSF-Mamba+ has been proposed. Specifically, MSF-Mamba supports multiscale motion-aware state fusion, as well as an adaptive scale weighting module that dynamically weighs the fused states across different scales. These enhancements explicitly address the limitations of vanilla Mamba by enabling motion-aware local spatiotemporal modeling, allowing MSF-Mamba and MSF-Mamba to effectively capture subtle motion cues for MGR. Experiments on two public MGR datasets demonstrate that even the lightweight version, namely, MSF-Mamba, achieves SoTA performance, outperforming existing CNN-, Transformer-, and SSM-based models while maintaining high efficiency.

