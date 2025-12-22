---
layout: default
title: Auxiliary Descriptive Knowledge for Few-Shot Adaptation of Vision-Language Model
---

# Auxiliary Descriptive Knowledge for Few-Shot Adaptation of Vision-Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17313" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17313v1</a>
  <a href="https://arxiv.org/pdf/2512.17313.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17313v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17313v1', 'Auxiliary Descriptive Knowledge for Few-Shot Adaptation of Vision-Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: SuBeen Lee, GilHan Park, WonJun Moon, Hyun Seok Seong, Jae-Pil Heo

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出辅助描述知识ADK，提升视觉-语言模型在少样本迁移学习中的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `少样本学习` `迁移学习` `参数高效微调` `辅助知识`

## 📋 核心要点

1. 现有VLM的少样本迁移学习方法依赖手工提示，难以充分理解类别语义，限制了模型性能。
2. 提出辅助描述知识(ADK)框架，利用大型语言模型生成丰富的类别描述，增强文本表示。
3. 实验表明，ADK能显著提升现有PEFT方法的性能，并在多个场景中达到新的state-of-the-art。

## 📝 摘要（中文）

尽管视觉-语言模型(VLM)具有令人印象深刻的零样本能力，但它们在下游任务中，当数据分布与预训练数据存在差异时，表现往往不佳。少样本迁移学习(FSA-VLM)已成为一个关键解决方案，通常使用参数高效微调(PEFT)来以最少的数据调整模型。然而，这些PEFT方法受到其对固定、手工制作提示的依赖的限制，这些提示通常不足以理解类别的语义。虽然一些研究提出了利用图像诱导提示来为分类提供额外的线索，但它们在推理时引入了过高的计算开销。因此，我们引入了辅助描述知识(ADK)，这是一个新颖的框架，可以有效地丰富文本表示，而不会影响效率。ADK首先利用大型语言模型离线生成每个类别的丰富描述性提示集。然后以两种方式部署这些预先计算的特征：(1)作为组合知识，一种平均表示，提供丰富的语义，尤其是在类名模糊或VLM不熟悉时；(2)作为实例特定知识，其中轻量级、非参数注意力机制动态地选择给定图像最相关的描述。这种方法提供了手工制作提示之外的两种额外类型的知识，从而有助于跨各种领域的类别区分。此外，ADK充当无参数、即插即用的组件，可增强现有的PEFT方法。大量的实验表明，ADK始终提高多个PEFT基线的性能，在各种场景中设置了新的最先进水平。

## 🔬 方法详解

**问题定义**：现有的视觉-语言模型在少样本迁移学习任务中，依赖于手工设计的文本提示，这些提示往往无法充分表达类别的语义信息，导致模型在面对分布偏移时性能下降。此外，一些利用图像生成提示的方法虽然可以提供额外信息，但计算成本过高，不适用于实际应用。

**核心思路**：论文的核心思路是利用大型语言模型(LLM)生成丰富的类别描述，作为辅助知识来增强视觉-语言模型的文本表示。通过预先计算并存储这些描述，可以在推理阶段高效地利用这些知识，而无需引入额外的计算负担。

**技术框架**：ADK框架包含两个主要组成部分：离线描述生成和在线知识融合。首先，利用LLM为每个类别生成多个描述性提示。然后，这些预计算的描述被用于两种方式：组合知识和实例特定知识。组合知识是对所有描述进行平均，提供类别的整体语义信息。实例特定知识则使用一个轻量级的非参数注意力机制，根据输入图像动态地选择最相关的描述。

**关键创新**：ADK的关键创新在于其高效的知识融合方式。通过预先计算描述并使用注意力机制动态选择相关描述，ADK能够在不引入额外计算负担的情况下，显著提升模型的性能。此外，ADK作为一个即插即用的模块，可以方便地集成到现有的PEFT方法中。

**关键设计**：ADK的关键设计包括：1) 使用LLM生成多样化的类别描述；2) 使用平均池化生成组合知识，提供类别的整体语义；3) 使用非参数注意力机制，根据图像特征动态选择实例相关的描述。具体来说，注意力机制的权重是基于图像特征和描述特征之间的相似度计算的。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17313v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17313v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17313v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ADK能够显著提升现有PEFT方法在少样本迁移学习任务中的性能。例如，在多个数据集上，ADK将CoOp、Tip-Adapter等基线的性能提升了多个百分点，并在多个场景中取得了state-of-the-art的结果。这证明了ADK能够有效地利用辅助知识来增强视觉-语言模型的文本表示，从而提升模型的泛化能力。

## 🎯 应用场景

该研究成果可广泛应用于图像分类、目标检测、图像检索等视觉-语言任务中，尤其是在数据稀缺或类别语义复杂的场景下。例如，在医学图像分析中，可以利用ADK来辅助医生诊断罕见疾病，或在自动驾驶领域，提升模型对复杂交通场景的理解能力。该方法具有很强的通用性和可扩展性，有望推动视觉-语言模型在实际应用中的发展。

## 📄 摘要（原文）

> Despite the impressive zero-shot capabilities of Vision-Language Models (VLMs), they often struggle in downstream tasks with distribution shifts from the pre-training data. Few-Shot Adaptation (FSA-VLM) has emerged as a key solution, typically using Parameter-Efficient Fine-Tuning (PEFT) to adapt models with minimal data. However, these PEFT methods are constrained by their reliance on fixed, handcrafted prompts, which are often insufficient to understand the semantics of classes. While some studies have proposed leveraging image-induced prompts to provide additional clues for classification, they introduce prohibitive computational overhead at inference. Therefore, we introduce Auxiliary Descriptive Knowledge (ADK), a novel framework that efficiently enriches text representations without compromising efficiency. ADK first leverages a Large Language Model to generate a rich set of descriptive prompts for each class offline. These pre-computed features are then deployed in two ways: (1) as Compositional Knowledge, an averaged representation that provides rich semantics, especially beneficial when class names are ambiguous or unfamiliar to the VLM; and (2) as Instance-Specific Knowledge, where a lightweight, non-parametric attention mechanism dynamically selects the most relevant descriptions for a given image. This approach provides two additional types of knowledge alongside the handcrafted prompt, thereby facilitating category distinction across various domains. Also, ADK acts as a parameter-free, plug-and-play component that enhances existing PEFT methods. Extensive experiments demonstrate that ADK consistently boosts the performance of multiple PEFT baselines, setting a new state-of-the-art across various scenarios.

