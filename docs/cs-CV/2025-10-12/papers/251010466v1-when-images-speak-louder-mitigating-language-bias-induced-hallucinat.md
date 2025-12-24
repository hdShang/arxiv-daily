---
layout: default
title: "When Images Speak Louder: Mitigating Language Bias-induced Hallucinations in VLMs through Cross-Modal Guidance"
---

# When Images Speak Louder: Mitigating Language Bias-induced Hallucinations in VLMs through Cross-Modal Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10466" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10466v1</a>
  <a href="https://arxiv.org/pdf/2510.10466.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10466v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10466v1', 'When Images Speak Louder: Mitigating Language Bias-induced Hallucinations in VLMs through Cross-Modal Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinjin Cao, Zhiyang Chen, Zijun Wang, Liyuan Ma, Weijian Luo, Guojun Qi

**分类**: cs.CV

**发布日期**: 2025-10-12

---

## 💡 一句话要点

**提出跨模态引导（CMG）方法，缓解视觉语言模型中的语言偏见导致的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `语言偏见` `幻觉问题` `跨模态引导` `注意力机制`

## 📋 核心要点

1. 现有VLM易产生与图像无关但语言流畅的幻觉，源于语言偏见。
2. 提出跨模态引导（CMG）方法，通过退化视觉-语言注意力来降低语言偏见。
3. 实验表明CMG能有效提升VLM在幻觉基准上的性能，且无需额外训练。

## 📝 摘要（中文）

视觉语言模型(VLM)在视觉和语言上下文的多模态理解方面表现出强大的能力。然而，现有的VLM常常面临严重的幻觉挑战，即VLM倾向于生成在语言上流畅但与先前上下文中的图像无关的响应。为了解决这个问题，我们分析了语言偏见如何导致幻觉，并引入了跨模态引导(CMG)，这是一种无需训练的解码方法，通过利用原始模型的输出分布与视觉-语言注意力退化后的模型的输出分布之间的差异来解决幻觉问题。在实践中，我们自适应地屏蔽选定的Transformer层中最具影响力的图像token的注意力权重，以破坏视觉-语言感知，作为一种具体的退化方式。这种退化诱导的解码强调了对视觉上下文的感知，因此显著降低了语言偏见，而不会损害VLM的能力。在实验部分，我们进行了全面的研究。所有结果都证明了CMG的优越性，无需额外的条件或训练成本。我们还定量地表明，CMG可以提高不同VLM在特定于幻觉的基准测试中的性能，并有效地泛化。

## 🔬 方法详解

**问题定义**：现有视觉语言模型（VLM）在多模态理解方面表现出色，但容易产生幻觉，即生成语言流畅但与图像内容无关的回复。这种幻觉问题主要源于模型对语言的过度依赖，而忽略了视觉信息，导致语言偏见。现有方法难以有效缓解这种语言偏见，从而限制了VLM的可靠性和应用范围。

**核心思路**：本文的核心思路是通过引入跨模态引导（CMG）来降低VLM中的语言偏见。CMG的核心思想是，通过对比原始VLM的输出分布和经过视觉-语言注意力退化后的VLM的输出分布，来引导模型更多地关注视觉信息。这种方法基于一个假设：如果模型过度依赖语言，那么在视觉信息被部分移除后，其输出分布会发生显著变化。

**技术框架**：CMG是一种训练自由的解码方法，不需要额外的训练过程。其主要流程如下：1) 使用原始VLM生成一个输出分布。2) 通过自适应地屏蔽选定的Transformer层中最具影响力的图像token的注意力权重，来退化视觉-语言注意力。3) 使用退化后的VLM生成另一个输出分布。4) 计算两个输出分布之间的差异，并利用该差异来调整原始VLM的输出，从而引导模型更多地关注视觉信息。

**关键创新**：CMG的关键创新在于其无需训练的特性，以及通过对比原始模型和退化模型的输出分布来引导模型关注视觉信息。与需要额外训练或微调的方法不同，CMG可以直接应用于现有的VLM，而无需修改模型结构或参数。此外，CMG通过自适应地选择需要屏蔽的图像token，可以更有效地破坏视觉-语言注意力，从而更好地降低语言偏见。

**关键设计**：CMG的关键设计包括：1) 自适应地选择需要屏蔽的图像token。具体来说，选择在视觉-语言注意力权重中具有最高值的token，因为这些token被认为是对模型输出影响最大的视觉信息。2) 选择合适的Transformer层进行注意力屏蔽。论文中提到选择特定的Transformer层可以更有效地破坏视觉-语言注意力。3) 使用合适的距离度量来计算原始模型和退化模型输出分布之间的差异。论文中可能使用了KL散度或其他类似的距离度量。

## 📊 实验亮点

实验结果表明，CMG方法在多个幻觉相关的基准测试中显著提高了VLM的性能，且无需任何额外的训练成本。具体来说，CMG能够有效地降低VLM生成的回复中与图像内容无关的信息，从而提高回复的准确性和相关性。此外，CMG还具有良好的泛化能力，可以应用于不同的VLM模型。

## 🎯 应用场景

该研究成果可广泛应用于各种需要可靠视觉语言理解的场景，例如图像描述生成、视觉问答、多模态对话系统等。通过降低语言偏见和减少幻觉，可以提高VLM在这些应用中的准确性和可靠性，从而提升用户体验和应用价值。未来，该方法可以进一步扩展到其他多模态任务和模型中。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have shown solid ability for multimodal understanding of both visual and language contexts. However, existing VLMs often face severe challenges of hallucinations, meaning that VLMs tend to generate responses that are only fluent in the language but irrelevant to images in previous contexts. To address this issue, we analyze how language bias contributes to hallucinations and then introduce Cross-Modal Guidance(CMG), a training-free decoding method that addresses the hallucinations by leveraging the difference between the output distributions of the original model and the one with degraded visual-language attention. In practice, we adaptively mask the attention weight of the most influential image tokens in selected transformer layers to corrupt the visual-language perception as a concrete type of degradation. Such a degradation-induced decoding emphasizes the perception of visual contexts and therefore significantly reduces language bias without harming the ability of VLMs. In experiment sections, we conduct comprehensive studies. All results demonstrate the superior advantages of CMG with neither additional conditions nor training costs. We also quantitatively show CMG can improve different VLM's performance on hallucination-specific benchmarks and generalize effectively.

