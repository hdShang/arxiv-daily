---
layout: default
title: CoPRS: Learning Positional Prior from Chain-of-Thought for Reasoning Segmentation
---

# CoPRS: Learning Positional Prior from Chain-of-Thought for Reasoning Segmentation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11173" target="_blank" class="toolbar-btn">arXiv: 2510.11173v2</a>
    <a href="https://arxiv.org/pdf/2510.11173.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11173v2" 
            onclick="toggleFavorite(this, '2510.11173v2', 'CoPRS: Learning Positional Prior from Chain-of-Thought for Reasoning Segmentation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhenyu Lu, Liupeng Li, Jinpeng Wang, Yan Feng, Bin Chen, Ke Chen, Yaowei Wang

**分类**: cs.CV, cs.MM

**发布日期**: 2025-10-13 (更新: 2025-12-10)

**备注**: 20 pages, 8 figures, 7 tables

**🔗 代码/项目**: [GITHUB](https://github.com/ZhenyuLU-Heliodore/CoPRS.git)

---

## 💡 一句话要点

**CoPRS：提出基于思维链的位置先验学习方法，用于提升推理分割任务的性能与可解释性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理分割` `思维链` `位置先验` `多模态学习` `可解释性` `图像分割` `视觉推理`

## 📋 核心要点

1. 现有推理分割方法直接连接语言模型的隐藏特征到掩码解码器，或仅表示文本中的位置，限制了解释性和语义细节。
2. CoPRS通过多模态思维链（MCoT）生成可学习的位置先验热图，连接语言推理和分割，增强了模型的可解释性。
3. 实验结果表明，CoPRS在RefCOCO系列和ReasonSeg数据集上达到了或超过了当前最佳性能，并验证了推理过程与分割结果的对齐。

## 📝 摘要（中文）

本文提出了一种基于多模态思维链（MCoT）的位置感知模型CoPRS，旨在通过可微且可解释的位置先验（以热图形式呈现）来桥接语言推理和分割任务。通过MCoT使推理过程清晰化，并将其表达为密集的、可微的热图，该接口增强了解释性和诊断分析，并产生更集中的目标证据。一个可学习的注意力token聚合图像和推理文本的特征，以生成该位置先验，并通过轻量级解码器将其解码为精确的掩码，从而在推理和分割之间建立直接联系。在RefCOCO系列和ReasonSeg数据集上，CoPRS在可比协议下匹配或超过了每个标准分割上报告的最佳指标，在验证和测试集上的性能均达到或超过了先前的最先进水平。大量实验表明，CoT轨迹、生成的热图和解码的掩码之间存在很强的正相关性，支持推理输出和下游掩码生成之间的可解释对齐。这些发现共同支持了该范式在桥接推理和分割方面的效用，并显示了推理驱动的集中和更精确的掩码预测方面的优势。

## 🔬 方法详解

**问题定义**：现有推理分割方法在连接语言推理和图像分割时，存在可解释性差和语义细节不足的问题。直接将语言模型的隐藏特征连接到掩码解码器，或者简单地表示文本中的位置信息，无法充分利用推理过程中的信息，导致分割结果不够精确，且难以理解模型做出决策的原因。

**核心思路**：CoPRS的核心思路是通过引入一个可学习的位置先验热图，将语言推理过程显式地表达出来，并将其作为图像分割的指导信息。该热图能够突出显示图像中与推理相关的区域，从而引导分割过程更加关注目标对象，提高分割的准确性和可解释性。

**技术框架**：CoPRS的整体框架包括以下几个主要模块：1) 多模态思维链（MCoT）模块，用于生成语言推理过程；2) 注意力Token模块，用于聚合图像和推理文本的特征；3) 位置先验生成模块，用于生成可学习的位置先验热图；4) 轻量级解码器，用于将位置先验热图解码为精确的掩码。整个流程首先通过MCoT进行推理，然后利用注意力Token融合多模态信息，生成位置先验，最后通过解码器得到分割结果。

**关键创新**：CoPRS的关键创新在于引入了可学习的位置先验热图，它将语言推理过程显式地表达出来，并将其作为图像分割的指导信息。与现有方法相比，CoPRS能够更好地利用推理过程中的信息，提高分割的准确性和可解释性。此外，CoPRS还采用了注意力Token机制，能够有效地融合图像和推理文本的特征，从而生成更精确的位置先验。

**关键设计**：CoPRS的关键设计包括：1) MCoT模块的具体实现方式，例如使用的语言模型和推理策略；2) 注意力Token模块的结构和参数设置；3) 位置先验热图的生成方式，例如使用的损失函数和网络结构；4) 轻量级解码器的结构和参数设置。这些设计细节共同决定了CoPRS的性能和可解释性。

## 📊 实验亮点

CoPRS在RefCOCO系列和ReasonSeg数据集上取得了显著的性能提升。在RefCOCO系列数据集上，CoPRS在多个分割上匹配或超过了当前最佳性能。在ReasonSeg数据集上，CoPRS的性能也达到了或超过了先前的最先进水平。实验结果表明，CoPRS能够有效地利用语言推理信息，提高图像分割的准确性和可解释性。

## 🎯 应用场景

CoPRS在视觉推理和图像分割领域具有广泛的应用前景，例如智能图像编辑、机器人导航、医学图像分析等。通过将语言推理和图像分割相结合，CoPRS可以实现更加智能和精确的图像处理，为相关应用提供更强大的支持。未来，CoPRS还可以应用于更复杂的场景，例如视频理解和三维重建等。

## 📄 摘要（原文）

> Existing works on reasoning segmentation either connect hidden features from a language model directly to a mask decoder or represent positions in text, which limits interpretability and semantic detail. To solve this, we present CoPRS, a Multi-modal Chain-of-Thought (MCoT)-based positional perception model that bridges language reasoning to segmentation through a differentiable and interpretable positional prior instantiated as a heatmap. By making the reasoning process clear via MCoT and expressing it as a dense, differentiable heatmap, this interface enhances interpretability and diagnostic analysis and yields more concentrated evidence on the target. A learnable concentration token aggregates features of the image and reasoning text to generate this positional prior, which is decoded to precise masks through a lightweight decoder, providing a direct connection between reasoning and segmentation. Across the RefCOCO series and ReasonSeg, CoPRS matches or surpasses the best reported metrics on each standard split under comparable protocols, with performance at or above the prior state of the art across both validation and test partitions. Extensive experiments demonstrate a strong positive correlation among the CoT trajectory, the generated heatmap, and the decoded mask, supporting an interpretable alignment between the reasoning output and downstream mask generation. Collectively, these findings support the utility of this paradigm in bridging reasoning and segmentation and show advantages in concentration driven by reasoning and in more precise mask prediction. Code, checkpoints and logs are released at https://github.com/ZhenyuLU-Heliodore/CoPRS.git.

