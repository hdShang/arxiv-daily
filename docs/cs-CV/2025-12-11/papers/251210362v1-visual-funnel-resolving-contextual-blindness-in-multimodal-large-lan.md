---
layout: default
title: Visual Funnel: Resolving Contextual Blindness in Multimodal Large Language Models
---

# Visual Funnel: Resolving Contextual Blindness in Multimodal Large Language Models

**arXiv**: [2512.10362v1](https://arxiv.org/abs/2512.10362) | [PDF](https://arxiv.org/pdf/2512.10362.pdf)

**作者**: Woojun Jung, Jaehoon Go, Mingyu Jeon, Sunjae Yoon, Junyeong Kim

---

## 💡 一句话要点

**提出Visual Funnel以解决多模态大语言模型中的上下文盲区问题**

**关键词**: `多模态大语言模型` `上下文盲区` `视觉细节感知` `无训练方法` `层次化上下文` `注意力熵`

## 📋 核心要点

1. 核心问题：多模态大语言模型在精细视觉细节感知上存在不足，导致上下文盲区，影响高精度任务应用。
2. 方法要点：采用无训练的两步法，通过上下文锚定和熵缩放组合构建层次化上下文，动态确定裁剪大小和中心。
3. 实验或效果：在实验中显著优于单裁剪和非结构化多裁剪基线，验证层次化结构对解决上下文盲区的关键作用。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) demonstrate impressive reasoning capabilities, but often fail to perceive fine-grained visual details, limiting their applicability in precision-demanding tasks. While methods that crop salient regions of an image offer a partial solution, we identify a critical limitation they introduce: "Contextual Blindness". This failure occurs due to structural disconnect between high-fidelity details (from the crop) and the broader global context (from the original image), even when all necessary visual information is present. We argue that this limitation stems not from a lack of information 'Quantity', but from a lack of 'Structural Diversity' in the model's input. To resolve this, we propose Visual Funnel, a training-free, two-step approach. Visual Funnel first performs Contextual Anchoring to identify the region of interest in a single forward pass. It then constructs an Entropy-Scaled Portfolio that preserves the hierarchical context - ranging from focal detail to broader surroundings - by dynamically determining crop sizes based on attention entropy and refining crop centers. Through extensive experiments, we demonstrate that Visual Funnel significantly outperforms naive single-crop and unstructured multi-crop baselines. Our results further validate that simply adding more unstructured crops provides limited or even detrimental benefits, confirming that the hierarchical structure of our portfolio is key to resolving Contextual Blindness.

