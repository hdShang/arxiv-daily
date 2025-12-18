---
layout: default
title: What "Not" to Detect: Negation-Aware VLMs via Structured Reasoning and Token Merging
---

# What "Not" to Detect: Negation-Aware VLMs via Structured Reasoning and Token Merging

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13232" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13232v1</a>
  <a href="https://arxiv.org/pdf/2510.13232.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13232v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.13232v1', 'What &quot;Not&quot; to Detect: Negation-Aware VLMs via Structured Reasoning and Token Merging')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Inha Kang, Youngsun Lim, Seonho Lee, Jiho Choi, Junsuk Choe, Hyunjung Shim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-15

**备注**: 38 pages

---

## 💡 一句话要点

**提出NegToMe模块和CoVAND数据集，提升VLM在否定描述对象检测中的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `否定理解` `对象检测` `思维链` `LoRA微调`

## 📋 核心要点

1. 现有VLM在否定理解方面存在不足，尤其是在描述对象检测任务中，容易产生肯定偏见。
2. 提出NegToMe模块，通过合并token的方式保留否定语义，并结合LoRA微调，提升模型对否定的理解能力。
3. 在CoVAND数据集和OVDEval基准测试上，该方法显著提升了性能，NMS-AP提升高达+10.8个点，并具备泛化能力。

## 📝 摘要（中文）

当前最先进的视觉-语言模型(VLM)在理解否定概念时存在严重缺陷，即所谓的肯定偏见，在描述对象检测(DOD)任务中尤为突出。为了解决这个问题，我们提出了两个主要贡献：(1)一个新的数据集构建流程；(2)一种新颖且轻量级的模型适配方法。首先，我们引入了CoVAND，这是一个通过系统的思维链(CoT)和基于VQA的流程构建的数据集，用于生成高质量、实例级别的否定数据。其次，我们提出了NegToMe，一种新颖的文本token合并模块，它直接解决了肯定偏见的架构原因。NegToMe从根本上解决了token化过程中否定线索的结构性丢失问题，将它们与属性组合成连贯的语义短语。它在输入层面保持了正确的极性，即使在数据有限的情况下也能实现鲁棒的否定理解。例如，为了防止模型将分散的token“not”和“girl”简单地视为“girl”，NegToMe将它们绑定到一个token中，其含义与单独的“girl”有明显区别。该模块与参数高效且具有策略性的LoRA微调方法相结合。我们的方法显著提高了具有挑战性的否定基准测试的性能，降低了假阳性率，在OVDEval上将NMS-AP提高了高达+10.8个点，并展示了对SoTA VLM的泛化能力。这项工作标志着在解决现实世界检测应用中的否定理解方面迈出了关键一步。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型（VLM）在处理否定描述对象检测（DOD）任务时，存在严重的“肯定偏见”，即无法准确理解和区分肯定与否定的描述。例如，模型可能将“没有戴帽子的女孩”错误地识别为“女孩”。现有方法的痛点在于token化过程会破坏否定词的语义信息，导致模型无法有效利用这些信息进行推理。

**核心思路**：论文的核心思路是通过在token化之后，将否定词与其修饰的属性词合并成一个token，从而保留否定语义。这样，模型在处理输入时，就能将“not girl”作为一个整体进行理解，而不是将其拆分为两个独立的token。这种方法旨在从根本上解决由于token化导致的否定信息丢失问题。

**技术框架**：整体框架包括两个主要部分：CoVAND数据集的构建和NegToMe模块的集成。CoVAND数据集通过思维链（CoT）和VQA方法生成高质量的否定描述数据。NegToMe模块则在VLM的文本编码器中插入，用于合并否定词和属性词的token。之后，使用LoRA（Low-Rank Adaptation）进行参数高效的微调。整体流程为：输入图像和文本描述 -> 文本token化 -> NegToMe模块进行token合并 -> VLM进行视觉-语言融合 -> 输出检测结果。

**关键创新**：最重要的技术创新点是NegToMe模块。与现有方法不同，NegToMe直接在token级别操作，通过合并token的方式显式地保留否定语义。这种方法避免了在模型训练过程中隐式地学习否定关系，从而提高了模型的泛化能力和鲁棒性。此外，CoVAND数据集的构建也为否定理解的研究提供了高质量的数据支持。

**关键设计**：NegToMe模块的关键设计在于如何确定哪些token需要合并。论文采用了一种基于规则的方法，例如将“not”与其后面的名词或形容词合并。LoRA微调采用了一种策略性的方法，只微调与NegToMe模块相关的参数，从而降低了计算成本并提高了训练效率。具体的损失函数和网络结构细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，NegToMe模块在OVDEval基准测试上显著提升了性能，NMS-AP提高了高达+10.8个点。此外，该方法还降低了假阳性率，表明模型能够更准确地识别否定描述的对象。实验还证明了该方法具有良好的泛化能力，可以应用于不同的SoTA VLM。

## 🎯 应用场景

该研究成果可应用于自动驾驶、智能监控、图像搜索等领域。例如，在自动驾驶中，模型需要准确识别“没有行人的斑马线”；在智能监控中，需要识别“没有携带武器的人员”。该研究提升了VLM在这些场景下的准确性和可靠性，具有重要的实际应用价值和潜在的社会影响。

## 📄 摘要（原文）

> State-of-the-art vision-language models (VLMs) suffer from a critical failure in understanding negation, often referred to as affirmative bias. This limitation is particularly severe in described object detection (DOD) tasks. To address this, we propose two primary contributions: (1) a new dataset pipeline and (2) a novel, lightweight adaptation recipe. First, we introduce CoVAND, a dataset constructed with a systematic chain-of-thought (CoT) and VQA-based pipeline to generate high-quality, instance-grounded negation data. Second, we propose NegToMe, a novel text token merging module that directly tackles the architectural cause of affirmative bias. NegToMe fundamentally addresses the structural loss of negation cues in tokenization, grouping them with attributes into coherent semantic phrases. It maintains correct polarity at the input level, enabling robust negation understanding even with limited data. For instance, to prevent a model from treating the fragmented tokens "not" and "girl" as simply "girl", NegToMe binds them into a single token whose meaning is correctly distinguished from that of "girl" alone. This module is integrated with a parameter-efficient and strategic LoRA fine-tuning approach. Our method significantly improves performance on challenging negation benchmarks with a lowered false positive rate, boosting NMS-AP by up to +10.8 points on OVDEval and demonstrating generalization to SoTA VLMs. This work marks a crucial step forward in addressing negation understanding for real-world detection applications.

