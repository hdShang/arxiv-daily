---
layout: default
title: "MUCAR: Benchmarking Multilingual Cross-Modal Ambiguity Resolution for Multimodal Large Language Models"
---

# MUCAR: Benchmarking Multilingual Cross-Modal Ambiguity Resolution for Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17046" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17046v2</a>
  <a href="https://arxiv.org/pdf/2506.17046.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17046v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17046v2', 'MUCAR: Benchmarking Multilingual Cross-Modal Ambiguity Resolution for Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaolong Wang, Zhaolu Kang, Wangyuxuan Zhai, Xinyue Lou, Yunghwei Lai, Ziyue Wang, Yawen Wang, Kaiyu Huang, Yile Wang, Peng Li, Yang Liu

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-20 (更新: 2025-09-26)

---

## 💡 一句话要点

**提出MUCAR以解决多模态语言模型中的模糊性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大型语言模型` `模糊性解决` `跨模态理解` `多语言数据集` `双模糊数据集` `消歧方法` `视觉-语言任务`

## 📋 核心要点

1. 现有多模态基准忽视语言和视觉的模糊性，主要依赖单模态上下文进行消歧，导致效果不佳。
2. MUCAR基准通过构建多语言数据集和双模糊数据集，旨在评估和解决多模态场景中的模糊性问题。
3. 对19个最先进的多模态模型的评估结果显示，与人类表现相比，模型在模糊性理解上仍有显著差距。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）在视觉-语言任务中取得了显著进展，但在处理现实世界中的语言和视觉上下文的固有模糊性时仍面临挑战。现有的多模态基准通常忽视语言和视觉的模糊性，主要依赖单模态上下文进行消歧，未能充分利用模态间的相互澄清潜力。为此，本文提出了MUCAR，一个专门用于评估多语言和跨模态场景下模糊性解决的新基准。MUCAR包含一个多语言数据集，通过相应的视觉上下文唯一解决模糊的文本表达，以及一个双模糊数据集，系统性地将模糊图像与模糊文本上下文配对，以实现通过相互消歧得到单一清晰解释的目标。对19个最先进的多模态模型的广泛评估显示，与人类水平表现相比，仍存在显著差距，强调了未来在跨模态模糊理解方法上的研究需求。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大型语言模型在处理语言和视觉上下文中的模糊性问题。现有方法往往忽视模态间的相互作用，导致消歧效果不理想。

**核心思路**：MUCAR基准通过引入多语言和双模糊数据集，利用视觉上下文来唯一解析模糊的文本表达，促进模态间的相互澄清。

**技术框架**：MUCAR的整体架构包括两个主要模块：多语言数据集和双模糊数据集。多语言数据集提供了通过视觉上下文解析的模糊文本，而双模糊数据集则系统性地将模糊图像与模糊文本配对。

**关键创新**：MUCAR的创新之处在于其系统性地构建了双模糊数据集，使得每一对模糊图像和文本都能通过相互消歧得到清晰的解释，这在现有方法中尚属首次。

**关键设计**：在数据集构建中，采用了精心设计的配对策略，确保每个模糊组合都能通过视觉和文本的相互作用实现清晰的理解。

## 📊 实验亮点

实验结果显示，19个最先进的多模态模型在MUCAR基准上的表现与人类水平存在显著差距，强调了当前模型在跨模态模糊理解方面的不足。这一发现为未来的研究指明了方向，推动了更复杂的消歧方法的发展。

## 🎯 应用场景

该研究的潜在应用领域包括多模态信息检索、智能助手、自动内容生成等。通过提高多模态模型在模糊性理解方面的能力，MUCAR有助于推动更智能的交互系统的发展，提升用户体验和信息获取的准确性。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated significant advances across numerous vision-language tasks. MLLMs have shown promising capability in aligning visual and textual modalities, allowing them to process image-text pairs with clear and explicit meanings. However, resolving the inherent ambiguities present in real-world language and visual contexts remains a challenge. Existing multimodal benchmarks typically overlook linguistic and visual ambiguities, relying mainly on unimodal context for disambiguation and thus failing to exploit the mutual clarification potential between modalities. To bridge this gap, we introduce MUCAR, a novel and challenging benchmark designed explicitly for evaluating multimodal ambiguity resolution across multilingual and cross-modal scenarios. MUCAR includes first a multilingual dataset where ambiguous textual expressions are uniquely resolved by corresponding visual contexts, and second a dual-ambiguity dataset that systematically pairs ambiguous images with ambiguous textual contexts, with each combination carefully constructed to yield a single, clear interpretation through mutual disambiguation. Extensive evaluations involving 19 state-of-the-art multimodal models--encompassing both open-source and proprietary architectures--reveal substantial gaps compared to human-level performance, highlighting the need for future research into more sophisticated cross-modal ambiguity comprehension methods, further pushing the boundaries of multimodal reasoning.

