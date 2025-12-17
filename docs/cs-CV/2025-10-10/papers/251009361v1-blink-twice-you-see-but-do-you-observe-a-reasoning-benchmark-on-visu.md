---
layout: default
title: BLINK-Twice: You see, but do you observe? A Reasoning Benchmark on Visual Perception
---

# BLINK-Twice: You see, but do you observe? A Reasoning Benchmark on Visual Perception

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.09361" target="_blank" class="toolbar-btn">arXiv: 2510.09361v1</a>
    <a href="https://arxiv.org/pdf/2510.09361.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09361v1" 
            onclick="toggleFavorite(this, '2510.09361v1', 'BLINK-Twice: You see, but do you observe? A Reasoning Benchmark on Visual Perception')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Junyan Ye, Dongzhi Jiang, Jun He, Baichuan Zhou, Zilong Huang, Zhiyuan Yan, Hongsheng Li, Conghui He, Weijia Li

**分类**: cs.CV

**发布日期**: 2025-10-10

**备注**: Accepted to 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Track on Datasets and Benchmarks

**🔗 代码/项目**: [GITHUB](https://github.com/PicoTrex/BLINK-Twice)

---

## 💡 一句话要点

**BLINK-Twice：提出视觉感知推理基准，强调细粒度观察与分析，挑战多模态大语言模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉推理` `多模态学习` `大语言模型` `视觉感知` `推理基准`

## 📋 核心要点

1. 现有推理基准侧重于语言推理，忽略了视觉感知的细粒度推理能力，无法有效评估多模态模型的视觉理解深度。
2. BLINK-Twice基准通过视觉挑战、对抗图像和推理链，迫使模型从视觉内容推理，并提供细粒度的推理过程评估。
3. 实验表明，现有MLLM在BLINK-Twice上表现不佳，重复观察图像和主动视觉交互能提升性能，揭示了视觉推理的新方向。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在推理能力方面取得了快速进展。然而，现有的推理基准主要评估基于语言的推理，通常将视觉输入视为可替换的上下文。为了解决这一差距，我们引入了BLINK-Twice，这是一个以视觉为中心的推理基准，它基于具有挑战性的感知任务。我们的任务不需要依赖外部知识，而是要求模型仅从视觉内容进行推理，从而将重点从基于语言的推理转移到基于图像的推理。与之前的感知基准相比，它超越了浅层感知（“看”），需要细粒度的观察和分析推理（“观察”）。BLINK-Twice集成了三个核心组件：七种用于测试视觉推理的视觉挑战类型，强制依赖视觉内容的自然对抗图像对，以及用于对推理过程进行细粒度评估（而不仅仅是最终答案）的带注释的推理链。我们评估了20个领先的MLLM，包括12个基础模型和8个推理增强模型。BLINK-Twice对当前模型提出了重大挑战。虽然语言空间中现有的推理策略（如思维链或自我批评）可以提高性能，但它们通常会导致不稳定和冗余的推理。我们观察到，重复的图像观察可以提高模型的性能，而主动的视觉交互（如o3模型所展示的）突出了对视觉推理新范式的需求。该数据集可在https://github.com/PicoTrex/BLINK-Twice公开获取。

## 🔬 方法详解

**问题定义**：现有的大部分多模态学习benchmark主要关注语言推理能力，将视觉信息作为辅助信息，缺乏对模型视觉感知和推理能力的深入评估。现有方法难以区分模型是真正理解了图像内容，还是仅仅依赖于语言知识进行推断。因此，需要一个更侧重于视觉的推理基准，来评估模型从视觉信息中进行细粒度观察和分析推理的能力。

**核心思路**：BLINK-Twice的核心思路是构建一个以视觉为中心的推理基准，通过设计具有挑战性的视觉任务、对抗性图像对和推理链，迫使模型依赖视觉内容进行推理，并提供细粒度的推理过程评估。通过这种方式，可以更准确地评估模型在视觉感知和推理方面的能力。

**技术框架**：BLINK-Twice基准包含以下三个核心组件：
1. **视觉挑战类型**：包含七种不同的视觉挑战，用于测试模型的视觉推理能力。
2. **自然对抗图像对**：这些图像对旨在强制模型依赖视觉内容，而不是外部知识。
3. **带注释的推理链**：提供细粒度的推理过程评估，而不仅仅是最终答案。

**关键创新**：BLINK-Twice的关键创新在于其以视觉为中心的推理设计，它强调细粒度的观察和分析推理，而不是依赖外部知识或语言信息。此外，该基准还引入了自然对抗图像对和带注释的推理链，以提供更全面和细致的评估。

**关键设计**：在数据集构建方面，作者精心设计了七种视觉挑战类型，包括计数、比较、空间关系推理等。对抗图像对的设计旨在通过细微的视觉差异来迷惑模型，迫使其进行更深入的视觉分析。推理链的标注则提供了模型推理过程的中间步骤，方便进行更细粒度的评估和分析。具体参数设置和网络结构取决于被评估的MLLM模型。

## 📊 实验亮点

对20个领先MLLM的评估表明，BLINK-Twice对现有模型提出了重大挑战。虽然思维链等语言推理策略可以提高性能，但效果不稳定且存在冗余。重复图像观察能提升模型性能，主动视觉交互（如o3模型）表明视觉推理需要新范式。这些结果突出了当前模型在视觉推理方面的局限性，并为未来的研究方向提供了启示。

## 🎯 应用场景

BLINK-Twice基准的潜在应用领域包括机器人视觉、自动驾驶、智能监控等。通过提高模型在视觉感知和推理方面的能力，可以提升这些应用在复杂环境中的性能和可靠性。该研究有助于推动多模态大语言模型在实际场景中的应用，并促进视觉推理领域的发展。

## 📄 摘要（原文）

> Recently, Multimodal Large Language Models (MLLMs) have made rapid progress, particularly in enhancing their reasoning capabilities. However, existing reasoning benchmarks still primarily assess language-based reasoning, often treating visual input as replaceable context. To address this gap, we introduce BLINK-Twice, a vision-centric reasoning benchmark grounded in challenging perceptual tasks. Instead of relying on external knowledge, our tasks require models to reason from visual content alone, shifting the focus from language-based to image-grounded reasoning. Compared to prior perception benchmarks, it moves beyond shallow perception ("see") and requires fine-grained observation and analytical reasoning ("observe"). BLINK-Twice integrates three core components: seven types of visual challenges for testing visual reasoning, natural adversarial image pairs that enforce reliance on visual content, and annotated reasoning chains for fine-grained evaluation of the reasoning process rather than final answers alone. We evaluate 20 leading MLLMs, including 12 foundation models and 8 reasoning-enhanced models. BLINK-Twice poses a significant challenge to current models. While existing reasoning strategies in the language space-such as chain-of-thought or self-criticism can improve performance, they often result in unstable and redundant reasoning. We observe that repeated image observation improves performance across models, and active visual interaction, as demonstrated by models like o3, highlights the need for a new paradigm for vision reasoning. The dataset is publicly available at https://github.com/PicoTrex/BLINK-Twice

