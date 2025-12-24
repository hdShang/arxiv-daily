---
layout: default
title: "ASCD: Attention-Steerable Contrastive Decoding for Reducing Hallucination in MLLM"
---

# ASCD: Attention-Steerable Contrastive Decoding for Reducing Hallucination in MLLM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14766" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14766v2</a>
  <a href="https://arxiv.org/pdf/2506.14766.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14766v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14766v2', 'ASCD: Attention-Steerable Contrastive Decoding for Reducing Hallucination in MLLM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yujun Wang, Aniri, Jinhe Bi, Soeren Pirk, Yunpu Ma

**分类**: cs.CV, cs.CL

**发布日期**: 2025-06-17 (更新: 2025-10-19)

**备注**: 14 pages, 8 figures

---

## 💡 一句话要点

**提出ASCD以减少多模态大语言模型中的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `幻觉现象` `对比解码` `注意力机制` `生成模型` `视觉理解` `自然语言处理`

## 📋 核心要点

1. 现有的多模态大语言模型在处理视觉信息时，常常会受到虚假线索的影响，导致生成不准确的内容。
2. 本文提出的注意力可引导对比解码（ASCD）方法，通过引导注意力分数来减少幻觉现象，结合正向和负向引导策略。
3. ASCD在五个MLLM骨干和三种解码方案上，减少了幻觉现象最多38.2%，同时在标准VQA基准上提高了准确性。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）常常因过度依赖虚假视觉线索而产生幻觉。以往的解决方案如视觉和指令对比解码（VCD, ICD）虽然有所改善，但其机制仍不明确。本文首次实证表明，这些方法的改进与跨模态注意力的重新分配系统性相关。基于此，提出了注意力可引导对比解码（ASCD），该方法直接在解码过程中引导注意力分数。ASCD结合了正向引导和负向引导，前者增强了模型内部稳定且跨领域鲁棒的文本中心头部，后者则抑制了实时识别的关键视觉标记。该方法在运行时和内存开销上几乎没有影响，并且无需额外训练。实验结果显示，ASCD在多个MLLM骨干和解码方案上，减少了POPE、CHAIR和MMHal-Bench上的幻觉现象，提升了标准VQA基准的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型（MLLMs）在生成过程中因虚假视觉线索而产生的幻觉问题。现有的解决方案如VCD和ICD虽然有所改善，但其机制不够透明，难以理解其效果来源。

**核心思路**：论文提出的ASCD方法通过直接引导解码过程中的注意力分数，来减少幻觉现象。该方法结合了正向引导（增强文本中心头部）和负向引导（抑制关键视觉标记），从而实现更准确的多模态生成。

**技术框架**：ASCD的整体架构包括两个主要模块：正向引导模块和负向引导模块。正向引导模块自动挖掘并放大文本中心的注意力头，而负向引导模块则实时识别并抑制不必要的视觉标记。

**关键创新**：ASCD的创新在于其注意力引导机制，能够在解码过程中动态调整注意力分数，区别于以往静态的对比解码方法。这种设计使得模型在不同领域和任务中都能保持鲁棒性。

**关键设计**：ASCD在实现过程中，采用了轻量级的参数设置，确保在运行时和内存开销上几乎没有影响。此外，该方法不需要额外的训练，便于在现有模型上直接应用。

## 📊 实验亮点

ASCD在五个不同的多模态大语言模型骨干和三种解码方案上表现出色，减少幻觉现象最多达到38.2%。同时，该方法在标准VQA基准测试中提高了准确性，展示了其在多模态生成任务中的有效性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括多模态生成任务，如图像描述、视频理解和人机交互等。通过减少幻觉现象，ASCD能够提升生成内容的准确性和可信度，具有重要的实际价值。未来，该方法可能会影响多模态大语言模型的设计和应用，推动更安全和可靠的AI系统发展。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) frequently hallucinate by over-committing to spurious visual cues. Prior remedies-Visual and Instruction Contrastive Decoding (VCD, ICD)-mitigate this issue, yet the mechanism remains opaque. We first empirically show that their improvements systematically coincide with redistributions of cross-modal attention. Building on this insight, we propose Attention-Steerable Contrastive Decoding (ASCD), which directly steers the attention scores during decoding. ASCD combines (i) positive steering, which amplifies automatically mined text-centric heads-stable within a model and robust across domains-with (ii) negative steering, which dampens on-the-fly identified critical visual tokens. The method incurs negligible runtime and memory overhead and requires no additional training. Across five MLLM backbones and three decoding schemes, ASCD reduces hallucination on POPE, CHAIR, and MMHal-Bench by up to 38.2 percent while improving accuracy on standard VQA benchmarks, including MMMU, MM-VET, ScienceQA, TextVQA, and GQA. These results position attention steering as a simple, model-agnostic, and principled route to safer, more faithful multimodal generation.

