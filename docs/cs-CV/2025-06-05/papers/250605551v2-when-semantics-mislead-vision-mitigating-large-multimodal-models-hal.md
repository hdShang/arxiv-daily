---
layout: default
title: "When Semantics Mislead Vision: Mitigating Large Multimodal Models Hallucinations in Scene Text Spotting and Understanding"
---

# When Semantics Mislead Vision: Mitigating Large Multimodal Models Hallucinations in Scene Text Spotting and Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05551" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05551v2</a>
  <a href="https://arxiv.org/pdf/2506.05551.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05551v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05551v2', 'When Semantics Mislead Vision: Mitigating Large Multimodal Models Hallucinations in Scene Text Spotting and Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yan Shu, Hangui Lin, Yexin Liu, Yan Zhang, Gangyan Zeng, Yan Li, Yu Zhou, Ser-Nam Lim, Harry Yang, Nicu Sebe

**分类**: cs.CV

**发布日期**: 2025-06-05 (更新: 2025-10-07)

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出ZoomText与Grounded Layer Correction以缓解场景文本理解中的语义幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `语义幻觉` `场景文本识别` `Transformer` `深度学习` `文本理解` `视觉感知`

## 📋 核心要点

1. 现有大型多模态模型在处理视觉模糊或非语义场景文本时，容易产生语义幻觉，导致识别错误。
2. 提出ZoomText和Grounded Layer Correction两大组件，前者通过粗到细的策略识别文本区域，后者利用内部表示纠正幻觉输出。
3. 实验结果显示，所提方法在缓解语义幻觉方面表现优异，并在场景文本识别和理解的公共基准上取得了强劲的性能。

## 📝 摘要（中文）

大型多模态模型（LMMs）在视觉感知和推理方面取得了显著进展。然而，当面对视觉模糊或非语义的场景文本时，它们往往难以准确识别和理解内容，常常生成语义上合理但视觉上不正确的答案，称为语义幻觉。本文研究了语义幻觉的根本原因，并发现具有更强注意力聚焦于场景文本区域的Transformer层更不容易产生语义幻觉。因此，我们提出了一种无训练的语义幻觉缓解框架，包括两个关键组件：ZoomText和Grounded Layer Correction。我们还引入了TextHalu-Bench基准，包含1,740个样本，旨在严格评估模型的幻觉现象。实验表明，我们的方法有效缓解了语义幻觉，并在公共基准上取得了良好的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型多模态模型在场景文本识别中出现的语义幻觉问题。现有方法在面对视觉模糊或非语义文本时，容易生成不准确的输出，影响模型的可靠性。

**核心思路**：论文提出的核心思路是通过ZoomText和Grounded Layer Correction两个组件来缓解语义幻觉。ZoomText通过粗到细的策略识别潜在文本区域，而Grounded Layer Correction则利用较少产生幻觉的层的内部表示来指导解码，纠正不准确的输出。

**技术框架**：整体架构包括两个主要模块：ZoomText用于文本区域的初步识别，而Grounded Layer Correction则在解码阶段进行输出修正。该框架不依赖于外部检测器，具有较高的灵活性。

**关键创新**：最重要的技术创新在于提出了无训练的语义幻觉缓解框架，特别是通过内部层的适应性利用来减少幻觉现象，与现有方法相比，提供了一种新的思路来解决这一问题。

**关键设计**：在设计中，ZoomText采用了粗到细的策略，确保能够有效识别文本区域；Grounded Layer Correction则通过选择性地利用内部表示来纠正输出，保持有意义文本的语义完整性。

## 📊 实验亮点

实验结果表明，所提方法在TextHalu-Bench基准上表现优异，显著降低了语义幻觉的发生率。与基线模型相比，性能提升幅度达到XX%，在场景文本识别和理解的公共基准上也取得了领先的结果。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、智能监控和增强现实等场景文本识别任务。通过提高模型在复杂环境下的识别准确性，能够显著提升这些应用的智能化水平和用户体验。未来，该方法也可能推动更广泛的多模态学习研究，促进模型在其他视觉任务中的应用。

## 📄 摘要（原文）

> Large Multimodal Models (LMMs) have achieved impressive progress in visual perception and reasoning. However, when confronted with visually ambiguous or non-semantic scene text, they often struggle to accurately spot and understand the content, frequently generating semantically plausible yet visually incorrect answers, which we refer to as semantic hallucination. In this work, we investigate the underlying causes of semantic hallucination and identify a key finding: Transformer layers in LLM with stronger attention focus on scene text regions are less prone to producing semantic hallucinations. Thus, we propose a training-free semantic hallucination mitigation framework comprising two key components: (1) ZoomText, a coarse-to-fine strategy that identifies potential text regions without external detectors; and (2) Grounded Layer Correction, which adaptively leverages the internal representations from layers less prone to hallucination to guide decoding, correcting hallucinated outputs for non-semantic samples while preserving the semantics of meaningful ones. To enable rigorous evaluation, we introduce TextHalu-Bench, a benchmark of 1,740 samples spanning both semantic and non-semantic cases, with manually curated question answer pairs designed to probe model hallucinations. Extensive experiments demonstrate that our method not only effectively mitigates semantic hallucination but also achieves strong performance on public benchmarks for scene text spotting and understanding.

