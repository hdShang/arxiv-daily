---
layout: default
title: "Aya Vision: Advancing the Frontier of Multilingual Multimodality"
---

# Aya Vision: Advancing the Frontier of Multilingual Multimodality

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08751" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08751v1</a>
  <a href="https://arxiv.org/pdf/2505.08751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08751v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08751v1', 'Aya Vision: Advancing the Frontier of Multilingual Multimodality')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saurabh Dash, Yiyang Nan, John Dang, Arash Ahmadian, Shivalika Singh, Madeline Smith, Bharat Venkitesh, Vlad Shmyhlo, Viraat Aryabumi, Walter Beller-Morales, Jeremy Pekmez, Jason Ozuzu, Pierre Richemond, Acyr Locatelli, Nick Frosst, Phil Blunsom, Aidan Gomez, Ivan Zhang, Marzieh Fadaee, Manoj Govindassamy, Sudip Roy, Matthias Gallé, Beyza Ermis, Ahmet Üstün, Sara Hooker

**分类**: cs.CL, cs.CV, cs.LG

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出Aya Vision以解决多语言多模态模型构建中的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `多语言处理` `合成注释` `跨模态合并` `灾难性遗忘` `生成模型` `数据稀缺` `机器翻译`

## 📋 核心要点

1. 核心问题：现有多模态语言模型在多语言环境中面临数据稀缺、翻译失真和灾难性遗忘等挑战。
2. 方法要点：提出合成注释框架以获取高质量多语言多模态数据，并引入跨模态模型合并技术以减轻灾难性遗忘。
3. 实验或效果：Aya-Vision-8B和Aya-Vision-32B在多模态生成性能上超越了多种强大模型，展示了显著的性能提升。

## 📝 摘要（中文）

构建多模态语言模型面临诸多挑战，包括视觉与语言模态的对齐、高质量指令数据的获取，以及在引入视觉信息后避免现有文本能力的退化。在多语言环境中，这些困难更加突出，数据稀缺、机器翻译失真和灾难性遗忘问题更加明显。为此，本文提出了一种合成注释框架，旨在策划高质量、多样化的多语言多模态指令数据，使Aya Vision模型能够对多模态输入生成自然且人类偏好的响应。此外，提出的跨模态模型合并技术有效缓解了灾难性遗忘，保留了文本能力，同时提升了多模态生成性能。Aya-Vision-8B在与其他强大的多模态模型比较中表现出色，Aya-Vision-32B更是超越了体量超过其两倍的模型，推动了多语言多模态领域的进展。

## 🔬 方法详解

**问题定义**：本文旨在解决多语言多模态模型构建中的挑战，特别是数据稀缺、机器翻译失真及灾难性遗忘等问题。现有方法在引入视觉信息后，常常导致文本能力的退化。

**核心思路**：提出合成注释框架以策划高质量的多语言多模态指令数据，同时引入跨模态模型合并技术，以有效保留文本能力并提升多模态生成性能。

**技术框架**：整体架构包括两个主要模块：合成注释框架用于数据收集和处理，跨模态模型合并技术用于模型训练和优化。数据模块负责生成多样化的多模态指令数据，而模型模块则通过合并技术实现能力的保留与提升。

**关键创新**：最重要的创新在于合成注释框架的设计与跨模态模型合并技术的结合，这一设计有效解决了数据稀缺和灾难性遗忘问题，与现有方法相比，显著提升了模型的多模态生成能力。

**关键设计**：在参数设置上，采用了多语言数据集进行训练，损失函数设计考虑了多模态输入的特性，网络结构则结合了视觉和文本特征的融合机制，以实现更好的生成效果。

## 📊 实验亮点

实验结果显示，Aya-Vision-8B在与Qwen-2.5-VL-7B、Pixtral-12B等强大多模态模型的比较中表现优异，Aya-Vision-32B更是超越了体量超过其两倍的Molmo-72B和LLaMA-3.2-90B-Vision，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括多语言翻译、跨文化交流、智能助手等。通过提升多模态生成能力，Aya Vision能够在多种语言环境中提供更自然的交互体验，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Building multimodal language models is fundamentally challenging: it requires aligning vision and language modalities, curating high-quality instruction data, and avoiding the degradation of existing text-only capabilities once vision is introduced. These difficulties are further magnified in the multilingual setting, where the need for multimodal data in different languages exacerbates existing data scarcity, machine translation often distorts meaning, and catastrophic forgetting is more pronounced. To address the aforementioned challenges, we introduce novel techniques spanning both data and modeling. First, we develop a synthetic annotation framework that curates high-quality, diverse multilingual multimodal instruction data, enabling Aya Vision models to produce natural, human-preferred responses to multimodal inputs across many languages. Complementing this, we propose a cross-modal model merging technique that mitigates catastrophic forgetting, effectively preserving text-only capabilities while simultaneously enhancing multimodal generative performance. Aya-Vision-8B achieves best-in-class performance compared to strong multimodal models such as Qwen-2.5-VL-7B, Pixtral-12B, and even much larger Llama-3.2-90B-Vision. We further scale this approach with Aya-Vision-32B, which outperforms models more than twice its size, such as Molmo-72B and LLaMA-3.2-90B-Vision. Our work advances multilingual progress on the multi-modal frontier, and provides insights into techniques that effectively bend the need for compute while delivering extremely high performance.

