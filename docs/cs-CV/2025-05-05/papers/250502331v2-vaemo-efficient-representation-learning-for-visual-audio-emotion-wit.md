---
layout: default
title: VAEmo: Efficient Representation Learning for Visual-Audio Emotion with Knowledge Injection
---

# VAEmo: Efficient Representation Learning for Visual-Audio Emotion with Knowledge Injection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02331" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02331v2</a>
  <a href="https://arxiv.org/pdf/2505.02331.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02331v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02331v2', 'VAEmo: Efficient Representation Learning for Visual-Audio Emotion with Knowledge Injection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Cheng, Zhiwei Zhao, Yichao He, Zhenzhen Hu, Jia Li, Meng Wang, Richang Hong

**分类**: cs.CV, cs.SD

**发布日期**: 2025-05-05 (更新: 2025-08-02)

**备注**: Source code and pre-trained models will be available at https://github.com/MSA-LMC/VAEmo

**DOI**: [10.1145/3746027.3754924](https://doi.org/10.1145/3746027.3754924)

---

## 💡 一句话要点

**提出VAEmo以解决多模态情感识别中的数据稀缺与表达差异问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态情感识别` `视觉-音频融合` `知识注入` `自监督学习` `情感语义建模` `对比学习` `大语言模型`

## 📋 核心要点

1. 现有的多模态情感识别方法主要依赖模态特定编码器和粗略的内容级对齐，限制了情感语义的细粒度建模。
2. VAEmo通过两阶段框架，首先在大规模VA语料库上进行预训练，然后利用多模态大语言模型生成情感描述，注入外部知识以提升表示能力。
3. 在多个下游任务中，VAEmo展现出优越的性能，证明了其紧凑设计和跨模态编码的有效性，显著提升了情感识别的准确性。

## 📝 摘要（中文）

多模态情感识别（AVER）旨在通过非语言的视觉-音频（VA）线索推断人类情感，具有互补的模态优势和语言无关性。然而，由于情感表达的固有模糊性、跨模态表达差异以及可靠标注数据的稀缺，AVER仍然面临挑战。为了解决这些问题，本文提出VAEmo，一个高效的两阶段框架，通过外部知识注入实现情感中心的VA联合表示学习。第一阶段在大规模说话者中心的VA语料库上进行预训练，第二阶段通过多模态大语言模型生成详细的情感描述，并通过双路径对比学习将其与VA表示对齐。实验表明，VAEmo在多个下游AVER基准上实现了最先进的性能，突出了统一跨模态编码和情感感知语义指导的优势。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态情感识别中的数据稀缺、情感表达模糊及跨模态表达差异等问题。现有方法在情感语义建模上存在局限性，难以实现细粒度的情感理解。

**核心思路**：VAEmo的核心思路是通过两阶段框架进行情感中心的VA联合表示学习。第一阶段通过无情感标签的预训练学习表达性和互补的表示，第二阶段通过生成的情感描述进一步增强表示的情感语义。

**技术框架**：VAEmo的整体架构分为两个主要阶段：第一阶段是一个统一且轻量的表示网络，在大规模VA语料库上进行掩码重建和对比目标的预训练；第二阶段利用多模态大语言模型生成情感描述，并通过双路径对比学习将文本语义与VA表示对齐。

**关键创新**：VAEmo的主要创新在于引入外部知识注入机制，通过对齐文本和VA表示，弥补了情感表达的模态差异。这一方法与传统依赖模态特定编码器的方式有本质区别。

**关键设计**：在设计中，采用了掩码重建和对比学习的损失函数，确保了表示的丰富性和准确性。同时，网络结构经过优化，以实现高效的情感表示学习。具体参数设置和网络层次结构的细节在实验部分进行了详细说明。

## 📊 实验亮点

在多个下游AVER基准测试中，VAEmo实现了最先进的性能，相较于现有方法，情感识别准确率提升了显著的X%（具体数据未知），展示了其在统一跨模态编码和情感感知语义指导方面的优势。

## 🎯 应用场景

VAEmo的研究成果在情感计算、智能人机交互、心理健康监测等领域具有广泛的应用潜力。通过提高情感识别的准确性，该技术能够为情感驱动的应用提供更为精准的支持，推动相关技术的发展与普及。

## 📄 摘要（原文）

> Audiovisual emotion recognition (AVER) aims to infer human emotions from nonverbal visual-audio (VA) cues, offering modality-complementary and language-agnostic advantages. However, AVER remains challenging due to the inherent ambiguity of emotional expressions, cross-modal expressive disparities, and the scarcity of reliably annotated data. Recent self-supervised AVER approaches have introduced strong multimodal representations, yet they predominantly rely on modality-specific encoders and coarse content-level alignment, limiting fine-grained emotional semantic modeling. To address these issues, we propose VAEmo, an efficient two-stage framework for emotion-centric joint VA representation learning with external knowledge injection. In Stage~1, a unified and lightweight representation network is pre-trained on large-scale speaker-centric VA corpora via masked reconstruction and contrastive objectives, mitigating the modality gap and learning expressive, complementary representations without emotion labels. In Stage~2, multimodal large language models automatically generate detailed affective descriptions according to our well-designed chain-of-thought prompting for only a small subset of VA samples; these rich textual semantics are then injected by aligning their corresponding embeddings with VA representations through dual-path contrastive learning, further bridging the emotion gap. Extensive experiments on multiple downstream AVER benchmarks show that VAEmo achieves state-of-the-art performance with a compact design, highlighting the benefit of unified cross-modal encoding and emotion-aware semantic guidance for efficient, generalizable VA emotion representations.

