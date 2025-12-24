---
layout: default
title: "Think Before You Segment: An Object-aware Reasoning Agent for Referring Audio-Visual Segmentation"
---

# Think Before You Segment: An Object-aware Reasoning Agent for Referring Audio-Visual Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04418" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04418v1</a>
  <a href="https://arxiv.org/pdf/2508.04418.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04418v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04418v1', 'Think Before You Segment: An Object-aware Reasoning Agent for Referring Audio-Visual Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinxing Zhou, Yanghao Zhou, Mingfei Han, Tong Wang, Xiaojun Chang, Hisham Cholakkal, Rao Muhammad Anwer

**分类**: cs.MM, cs.CV, cs.MA, cs.SD, eess.AS

**发布日期**: 2025-08-06

**备注**: Project page: https://github.com/jasongief/TGS-Agent

**🔗 代码/项目**: [GITHUB](https://github.com/jasongief/TGS-Agent)

---

## 💡 一句话要点

**提出TGS-Agent以解决音频视觉分割中的对象理解问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频视觉分割` `多模态分析` `对象识别` `推理模型` `数据集构建` `模型泛化` `深度学习`

## 📋 核心要点

1. 现有的Ref-AVS方法依赖于强像素级监督，缺乏可解释性，难以有效理解和分割目标对象。
2. 本文提出TGS-Agent，通过Think-Ground-Segment过程模拟人类推理，使用Ref-Thinker进行多模态分析，提升对象识别与分割的准确性。
3. 在标准Ref-AVSBench和新提出的R²-AVSBench上，TGS-Agent均取得了最先进的性能，展示了其优越的模型泛化能力。

## 📝 摘要（中文）

Referring Audio-Visual Segmentation (Ref-AVS)旨在根据给定的参考表达在可听视频中分割目标对象。现有方法通常依赖于多模态融合学习潜在嵌入，促使可调的SAM/SAM2解码器进行分割，这需要强大的像素级监督且缺乏可解释性。本文提出TGS-Agent，从明确的参考理解角度出发，将任务分解为Think-Ground-Segment过程，模拟人类推理过程，首先通过多模态分析识别所指对象，然后进行粗粒度定位和精确分割。我们还构建了一个包含明确对象感知思维-回答链的指令调优数据集，以对Ref-Thinker进行微调。我们的方案在标准Ref-AVSBench和新提出的R²-AVSBench上均取得了最先进的结果。

## 🔬 方法详解

**问题定义**：本文旨在解决Ref-AVS中的对象理解问题，现有方法依赖于像素级监督，导致可解释性不足和效果受限。

**核心思路**：提出TGS-Agent，通过Think-Ground-Segment过程，首先进行多模态分析以识别目标对象，然后进行粗粒度定位和精确分割，模拟人类的推理过程。

**技术框架**：整体架构包括三个主要模块：Ref-Thinker（多模态语言模型）、Grounding-DINO和SAM2。Ref-Thinker负责推理，Grounding-DINO和SAM2则进行定位和分割。

**关键创新**：最重要的创新在于Ref-Thinker的引入，它能够在文本、视觉和听觉线索上进行推理，显著提升了对象识别的准确性，而不再依赖于传统的像素级监督。

**关键设计**：构建了一个包含明确对象感知思维-回答链的指令调优数据集，以对Ref-Thinker进行微调，确保其能够有效推理并生成准确的对象描述。

## 📊 实验亮点

TGS-Agent在标准Ref-AVSBench和新提出的R²-AVSBench上均取得了最先进的结果，展示了其在对象识别和分割任务中的优越性能，具体提升幅度未知。

## 🎯 应用场景

该研究在视频理解、智能监控和人机交互等领域具有广泛的应用潜力。通过提升音频视觉分割的准确性，TGS-Agent能够帮助实现更智能的视觉分析系统，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Referring Audio-Visual Segmentation (Ref-AVS) aims to segment target objects in audible videos based on given reference expressions. Prior works typically rely on learning latent embeddings via multimodal fusion to prompt a tunable SAM/SAM2 decoder for segmentation, which requires strong pixel-level supervision and lacks interpretability. From a novel perspective of explicit reference understanding, we propose TGS-Agent, which decomposes the task into a Think-Ground-Segment process, mimicking the human reasoning procedure by first identifying the referred object through multimodal analysis, followed by coarse-grained grounding and precise segmentation. To this end, we first propose Ref-Thinker, a multimodal language model capable of reasoning over textual, visual, and auditory cues. We construct an instruction-tuning dataset with explicit object-aware think-answer chains for Ref-Thinker fine-tuning. The object description inferred by Ref-Thinker is used as an explicit prompt for Grounding-DINO and SAM2, which perform grounding and segmentation without relying on pixel-level supervision. Additionally, we introduce R\textsuperscript{2}-AVSBench, a new benchmark with linguistically diverse and reasoning-intensive references for better evaluating model generalization. Our approach achieves state-of-the-art results on both standard Ref-AVSBench and proposed R\textsuperscript{2}-AVSBench. Code will be available at https://github.com/jasongief/TGS-Agent.

