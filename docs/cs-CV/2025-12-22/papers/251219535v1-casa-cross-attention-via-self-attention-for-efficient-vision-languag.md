---
layout: default
title: "CASA: Cross-Attention via Self-Attention for Efficient Vision-Language Fusion"
---

# CASA: Cross-Attention via Self-Attention for Efficient Vision-Language Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19535" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19535v1</a>
  <a href="https://arxiv.org/pdf/2512.19535.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19535v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19535v1', 'CASA: Cross-Attention via Self-Attention for Efficient Vision-Language Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Moritz Böhle, Amélie Royer, Juliette Marrie, Edouard Grave, Patrick Pérez

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出CASA：通过自注意力实现的跨注意力，用于高效的视觉-语言融合**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `跨注意力` `自注意力` `多模态融合` `长上下文` `图像理解` `视频字幕`

## 📋 核心要点

1. 现有视觉-语言模型在高分辨率图像等场景下，直接插入图像tokens导致计算和内存成本过高。
2. CASA通过自注意力实现跨注意力，在跨注意力层中加入局部文本交互，提升模型性能。
3. CASA在图像理解任务上缩小了与token插入的差距，并在长上下文多模态任务中保持了可扩展性。

## 📝 摘要（中文）

视觉-语言模型（VLMs）通常通过将预训练视觉编码器的图像tokens插入到语言模型的文本流中进行训练。这使得文本和图像信息能够在模型内部充分地相互关注，但对于高分辨率图像、长对话或流媒体视频来说，无论在内存还是计算方面，成本都非常高昂。利用跨注意力的VLMs是token插入的一种有效替代方案，但在性能上存在明显的差距，尤其是在涉及细粒度视觉细节的任务中。我们发现，改进此类模型的关键在于在专用的跨注意力层中启用局部文本到文本的交互。在此基础上，我们提出了CASA，即通过自注意力实现的跨注意力，这是一种简单而有效的范例，它大大缩小了在常见图像理解基准测试中与完全token插入的差距，同时在应用于长上下文多模态任务（如流媒体视频字幕）时，具有与跨注意力模型相同的可扩展性。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型（VLMs）在处理高分辨率图像、长对话或流媒体视频等长上下文多模态任务时，直接将图像tokens插入到语言模型的文本流中，导致计算和内存成本显著增加。虽然基于跨注意力的VLMs可以降低计算成本，但其性能，尤其是在需要细粒度视觉信息的任务上，与token插入方法相比存在明显差距。

**核心思路**：CASA的核心思路是通过自注意力机制来增强跨注意力模块，从而在降低计算成本的同时，提升模型对细粒度视觉信息的理解能力。具体来说，CASA在跨注意力层中引入局部文本到文本的交互，使得文本信息在与图像信息交互之前，能够更好地理解上下文信息，从而提高跨注意力机制的效率和准确性。

**技术框架**：CASA的整体框架是在现有的跨注意力VLM架构基础上，修改了跨注意力模块。该模块接收文本和图像特征作为输入，首先使用自注意力机制对文本特征进行局部上下文建模，然后将处理后的文本特征与图像特征进行跨注意力交互，最后输出融合后的特征表示。整个过程可以看作是先通过自注意力增强文本表示，再利用增强后的文本表示进行跨注意力。

**关键创新**：CASA的关键创新在于利用自注意力机制来增强跨注意力模块，从而在不显著增加计算成本的前提下，提升了模型对细粒度视觉信息的理解能力。与传统的跨注意力模型相比，CASA通过引入局部文本到文本的交互，使得文本信息在与图像信息交互之前，能够更好地理解上下文信息，从而提高了跨注意力机制的效率和准确性。

**关键设计**：CASA的关键设计包括：1) 使用标准的自注意力模块进行局部文本上下文建模；2) 将自注意力模块集成到现有的跨注意力模块中，保持整体架构的简洁性；3) 通过实验验证了不同自注意力参数设置（如注意力头数、隐藏层维度）对模型性能的影响，并选择了最优的参数配置。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19535v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19535v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19535v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

CASA在常见的图像理解基准测试中，显著缩小了与完全token插入方法的性能差距，同时保持了与跨注意力模型相当的计算效率。实验结果表明，CASA在处理细粒度视觉信息方面具有优势，能够有效提升视觉-语言模型的性能。具体性能数据和对比基线信息在论文中详细给出。

## 🎯 应用场景

CASA具有广泛的应用前景，包括但不限于：流媒体视频字幕、视频问答、图像描述、视觉对话等。其高效的计算特性使其特别适用于资源受限的场景，如移动设备或边缘计算平台。此外，CASA还可以应用于长上下文多模态任务，如长时间视频分析和理解，为智能监控、自动驾驶等领域提供技术支持。

## 📄 摘要（原文）

> Vision-language models (VLMs) are commonly trained by inserting image tokens from a pretrained vision encoder into the textual stream of a language model. This allows text and image information to fully attend to one another within the model, but becomes extremely costly for high-resolution images, long conversations, or streaming videos, both in memory and compute. VLMs leveraging cross-attention are an efficient alternative to token insertion but exhibit a clear performance gap, in particular on tasks involving fine-grained visual details. We find that a key to improving such models is to also enable local text-to-text interaction in the dedicated cross-attention layers. Building on this, we propose CASA, Cross-Attention via Self-Attention, a simple and efficient paradigm which substantially reduces the gap with full token insertion on common image understanding benchmarks, while enjoying the same scalability as cross-attention models when applied to long-context multimodal tasks such as streaming video captioning. For samples and code, please see our project page at https://kyutai.org/casa .

