---
layout: default
title: DynaStride: Dynamic Stride Windowing with MMCoT for Instructional Multi-Scene Captioning
---

# DynaStride: Dynamic Stride Windowing with MMCoT for Instructional Multi-Scene Captioning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23907" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23907v2</a>
  <a href="https://arxiv.org/pdf/2510.23907.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23907v2" onclick="toggleFavorite(this, '2510.23907v2', 'DynaStride: Dynamic Stride Windowing with MMCoT for Instructional Multi-Scene Captioning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eddison Pham, Prisha Priyadarshini, Adrian Maliackel, Kanishk Bandi, Cristian Meo, Kevin Zhu

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-10-27 (更新: 2025-11-30)

**备注**: 16 pages, 15 figures, 5 Tables, Accepted at NeurIPS 7HVU Workshop, Accepted at AAAI AI4ED Workshop

---

## 💡 一句话要点

**DynaStride：结合MMCoT的动态步长窗口化方法，用于生成教学视频的多场景字幕。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `教学视频字幕生成` `多模态学习` `动态窗口选择` `链式思考` `场景理解` `时间推理` `自适应采样`

## 📋 核心要点

1. 现有的场景级字幕生成方法难以捕捉教学视频中的时间结构和视觉线索，导致字幕缺乏连贯性和质量。
2. DynaStride通过动态步长窗口化和多模态链式思考，自适应地平衡时间上下文和冗余，生成更连贯和信息丰富的字幕。
3. 实验结果表明，DynaStride在多个指标上优于现有基线模型，证明了其在教学视频字幕生成方面的有效性。

## 📝 摘要（中文）

本文提出DynaStride，一个用于生成连贯的场景级字幕的流程，无需手动场景分割，旨在提升教学视频的理解。DynaStride通过自适应帧采样和多模态窗口化来捕捉每个场景内的关键过渡。然后，它采用多模态链式思考过程来生成多个动作-对象对，并使用动态步长窗口选择算法进行提炼和融合，该算法自适应地平衡时间上下文和冗余。最终的场景级字幕将视觉语义和时间推理整合到一个教学字幕中。在YouCookII数据集上的实验结果表明，DynaStride在基于N-gram的指标（BLEU、METEOR）和语义相似性度量（BERTScore、CLIPScore）上均优于包括VLLaMA3和GPT-4o在内的强大基线。定性分析进一步表明，DynaStride生成的字幕在时间上更连贯且信息量更大，为改进AI驱动的教学内容生成提供了一个有希望的方向。

## 🔬 方法详解

**问题定义**：论文旨在解决教学视频中场景级字幕生成的问题。现有方法通常无法充分捕捉视频中的时间结构和视觉线索，导致生成的字幕缺乏连贯性和信息量，难以有效支持用户的学习过程。手动分割场景成本高昂，限制了应用范围。

**核心思路**：DynaStride的核心思路是通过自适应地选择关键帧和利用多模态信息，来捕捉场景内的关键过渡和动作-对象关系。动态步长窗口选择算法能够平衡时间上下文和冗余，确保生成的字幕既全面又简洁。多模态链式思考过程则用于提取更准确的动作-对象对。

**技术框架**：DynaStride的整体流程包括以下几个主要阶段：1) 自适应帧采样：根据场景内容动态选择关键帧。2) 多模态窗口化：利用视觉和文本信息构建窗口，捕捉场景内的过渡。3) 多模态链式思考：生成多个动作-对象对。4) 动态步长窗口选择：根据时间上下文和冗余度，选择最佳的动作-对象对组合。5) 字幕生成：将选择的动作-对象对融合为最终的场景级字幕。

**关键创新**：DynaStride的关键创新在于动态步长窗口选择算法和多模态链式思考过程的结合。动态步长窗口选择算法能够自适应地调整窗口大小，平衡时间上下文和冗余，从而生成更连贯的字幕。多模态链式思考过程则能够更准确地提取动作-对象对，提高字幕的信息量。

**关键设计**：动态步长窗口选择算法通过评估不同窗口大小的字幕质量，选择最佳的窗口大小。具体而言，它会考虑窗口内帧之间的相似度、窗口内动作-对象对的一致性等因素。多模态链式思考过程则利用视觉和文本信息，逐步推导出动作-对象对。具体而言，它会首先识别场景中的主要对象，然后根据对象的动作推断出相应的动作。

## 📊 实验亮点

DynaStride在YouCookII数据集上进行了评估，实验结果表明，DynaStride在BLEU、METEOR、BERTScore和CLIPScore等指标上均优于包括VLLaMA3和GPT-4o在内的强大基线。定性分析表明，DynaStride生成的字幕在时间上更连贯且信息量更大，能够更好地支持用户的学习过程。

## 🎯 应用场景

DynaStride可应用于大规模在线教育平台，自动生成教学视频的场景级字幕，提升学习体验。该技术还可用于视频内容分析、智能剪辑等领域，提高视频处理效率和智能化水平。未来，DynaStride有望扩展到其他类型的视频，如体育赛事、新闻报道等。

## 📄 摘要（原文）

> Scene-level captioning in instructional videos can enhance learning by requiring an understanding of both visual cues and temporal structure. By aligning visual cues with textual guidance, this understanding supports procedural learning and multimodal reasoning, providing a richer context for skill acquisition. However, captions that fail to capture this structure may lack coherence and quality, which can create confusion and undermine the video's educational intent. To address this gap, we introduce DynaStride, a pipeline to generate coherent, scene-level captions without requiring manual scene segmentation. Using the YouCookII dataset's scene annotations, DynaStride performs adaptive frame sampling and multimodal windowing to capture key transitions within each scene. It then employs a multimodal chain-of-thought process to produce multiple action-object pairs, which are refined and fused using a dynamic stride window selection algorithm that adaptively balances temporal context and redundancy. The final scene-level caption integrates visual semantics and temporal reasoning in a single instructional caption. Empirical evaluations against strong baselines, including VLLaMA3 and GPT-4o, demonstrate consistent gains on both N-gram-based metrics (BLEU, METEOR) and semantic similarity measures (BERTScore, CLIPScore). Qualitative analyses further show that DynaStride produces captions that are more temporally coherent and informative, suggesting a promising direction for improving AI-powered instructional content generation.

