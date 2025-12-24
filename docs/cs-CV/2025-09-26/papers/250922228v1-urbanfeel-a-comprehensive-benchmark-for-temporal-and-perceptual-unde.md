---
layout: default
title: "UrbanFeel: A Comprehensive Benchmark for Temporal and Perceptual Understanding of City Scenes through Human Perspective"
---

# UrbanFeel: A Comprehensive Benchmark for Temporal and Perceptual Understanding of City Scenes through Human Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22228" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22228v1</a>
  <a href="https://arxiv.org/pdf/2509.22228.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22228v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22228v1', 'UrbanFeel: A Comprehensive Benchmark for Temporal and Perceptual Understanding of City Scenes through Human Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun He, Yi Lin, Zilong Huang, Jiacong Yin, Junyan Ye, Yuchuan Zhou, Weijia Li, Xiang Zhang

**分类**: cs.CV

**发布日期**: 2025-09-26

**备注**: 13 pages, 6 figures

---

## 💡 一句话要点

**UrbanFeel：提出一个综合性城市街景理解benchmark，关注时序变化和人类感知。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市理解` `多模态学习` `benchmark` `时间推理` `主观感知` `街景图像` `视觉问答`

## 📋 核心要点

1. 现有城市环境理解benchmark缺乏对时间演变和主观感知的系统探索，无法全面评估MLLM的城市理解能力。
2. UrbanFeel通过构建包含静态场景、时间变化和主观感知的多维度benchmark，系统评估MLLM在城市理解方面的能力。
3. 实验表明，Gemini-2.5 Pro在UrbanFeel上表现最佳，但在时间推理和主观感知方面仍有提升空间。

## 📝 摘要（中文）

城市发展影响着全球一半以上的人口，对城市结构和感知变化进行以人为本的理解对于可持续发展至关重要。尽管多模态大型语言模型（MLLM）在各个领域都表现出了卓越的能力，但现有的探索其在城市环境中性能的benchmark仍然有限，缺乏对城市环境的时间演变和主观感知的系统探索，而这些与人类感知密切相关。为了解决这些局限性，我们提出了UrbanFeel，这是一个综合性的benchmark，旨在评估MLLM在城市发展理解和主观环境感知方面的性能。UrbanFeel包含14.3K个精心构建的视觉问题，涵盖三个认知递进的维度：静态场景感知、时间变化理解和主观环境感知。我们从全球11个代表性城市收集了多时相的单视角和全景街景图像，并通过空间聚类、基于规则的生成、模型辅助提示和人工标注的混合流程生成高质量的问答对。通过对20个最先进的MLLM的广泛评估，我们观察到Gemini-2.5 Pro实现了最佳的整体性能，其准确率接近人类专家水平，平均差距仅为1.5%。大多数模型在基于场景理解的任务中表现良好。特别地，一些模型甚至在像素级变化检测方面超过了人类标注者。然而，在需要对城市发展进行时间推理的任务中，性能显著下降。此外，在主观感知维度中，一些模型在评估美丽和安全等维度时达到了人类水平甚至更高的一致性。

## 🔬 方法详解

**问题定义**：现有方法在评估多模态大语言模型（MLLM）对城市环境的理解能力时，缺乏对城市环境随时间变化以及人类主观感知的系统性评估。这导致无法全面衡量模型在理解城市发展和人类体验方面的能力。现有benchmark主要关注静态场景的理解，忽略了城市动态变化和人类情感的复杂性。

**核心思路**：UrbanFeel的核心思路是构建一个综合性的benchmark，包含静态场景感知、时间变化理解和主观环境感知三个认知递进的维度。通过多时相的街景图像和精心设计的问答对，系统性地评估MLLM在不同认知层次上的城市理解能力。这种多维度的方法旨在更全面地反映人类对城市环境的理解方式。

**技术框架**：UrbanFeel的构建流程主要包括以下几个阶段：1) 数据收集：从全球11个代表性城市收集多时相的单视角和全景街景图像。2) 问题生成：采用空间聚类、基于规则的生成、模型辅助提示和人工标注的混合流程生成高质量的问答对。3) 模型评估：使用生成的benchmark评估20个最先进的MLLM在不同维度上的性能。4) 结果分析：分析模型的优势和不足，为未来的研究提供指导。

**关键创新**：UrbanFeel的关键创新在于其综合性的多维度评估体系，涵盖了静态场景感知、时间变化理解和主观环境感知三个方面。这种设计能够更全面地评估MLLM对城市环境的理解能力，并揭示模型在不同认知层次上的表现差异。此外，混合式问答对生成方法结合了自动化和人工标注的优点，保证了benchmark的质量和多样性。

**关键设计**：在问答对生成方面，采用了空间聚类方法来选择具有代表性的场景，并使用基于规则的生成方法来生成基础问题。为了提高问题的复杂性和多样性，采用了模型辅助提示的方法，利用大型语言模型生成更具挑战性的问题。最后，通过人工标注来保证问答对的质量和准确性。在模型评估方面，采用了准确率、一致性等指标来衡量模型的性能。

## 📊 实验亮点

Gemini-2.5 Pro在UrbanFeel上取得了最佳的整体性能，其准确率接近人类专家水平，平均差距仅为1.5%。一些模型在像素级变化检测方面甚至超过了人类标注者。然而，在需要进行时间推理的任务中，模型的性能显著下降，表明模型在理解城市发展的时间演变方面仍有提升空间。

## 🎯 应用场景

UrbanFeel可用于评估和提升多模态大语言模型在智慧城市、城市规划、自动驾驶、环境监测等领域的应用能力。通过更全面地理解城市环境，可以为城市可持续发展提供更智能的解决方案，改善居民的生活质量。

## 📄 摘要（原文）

> Urban development impacts over half of the global population, making human-centered understanding of its structural and perceptual changes essential for sustainable development. While Multimodal Large Language Models (MLLMs) have shown remarkable capabilities across various domains, existing benchmarks that explore their performance in urban environments remain limited, lacking systematic exploration of temporal evolution and subjective perception of urban environment that aligns with human perception. To address these limitations, we propose UrbanFeel, a comprehensive benchmark designed to evaluate the performance of MLLMs in urban development understanding and subjective environmental perception. UrbanFeel comprises 14.3K carefully constructed visual questions spanning three cognitively progressive dimensions: Static Scene Perception, Temporal Change Understanding, and Subjective Environmental Perception. We collect multi-temporal single-view and panoramic street-view images from 11 representative cities worldwide, and generate high-quality question-answer pairs through a hybrid pipeline of spatial clustering, rule-based generation, model-assisted prompting, and manual annotation. Through extensive evaluation of 20 state-of-the-art MLLMs, we observe that Gemini-2.5 Pro achieves the best overall performance, with its accuracy approaching human expert levels and narrowing the average gap to just 1.5\%. Most models perform well on tasks grounded in scene understanding. In particular, some models even surpass human annotators in pixel-level change detection. However, performance drops notably in tasks requiring temporal reasoning over urban development. Additionally, in the subjective perception dimension, several models reach human-level or even higher consistency in evaluating dimension such as beautiful and safety.

