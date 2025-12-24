---
layout: default
title: "Learning to See Before Seeing: Demystifying LLM Visual Priors from Language Pre-training"
---

# Learning to See Before Seeing: Demystifying LLM Visual Priors from Language Pre-training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26625" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26625v1</a>
  <a href="https://arxiv.org/pdf/2509.26625.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26625v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26625v1', 'Learning to See Before Seeing: Demystifying LLM Visual Priors from Language Pre-training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junlin Han, Shengbang Tong, David Fan, Yufan Ren, Koustuv Sinha, Philip Torr, Filippos Kokkinos

**分类**: cs.LG, cs.AI, cs.CV, cs.MM

**发布日期**: 2025-09-30

**备注**: Project page: https://junlinhan.github.io/projects/lsbs/

---

## 💡 一句话要点

**揭示LLM视觉先验：通过语言预训练学习视觉感知与推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `视觉先验` `多模态学习` `预训练` `视觉推理` `视觉感知` `数据驱动` `MLLM`

## 📋 核心要点

1. 现有方法难以有效利用LLM在语言预训练中获得的视觉先验知识，限制了多模态LLM的性能。
2. 论文提出一种数据驱动的方法，通过控制预训练数据类型，有意识地培养LLM的视觉感知和推理能力。
3. 实验表明，该方法能够有效提升LLM的视觉能力，并在大规模预训练中得到验证，为多模态LLM发展提供新思路。

## 📝 摘要（中文）

大型语言模型（LLM）仅通过文本训练，却出人意料地发展出丰富的视觉先验知识。这些先验知识使得潜在的视觉能力能够通过相对少量的多模态数据被解锁，用于视觉任务，在某些情况下，甚至可以在没有见过图像的情况下执行视觉任务。通过系统分析，我们揭示了视觉先验——在语言预训练期间获得的关于视觉世界的隐式、涌现的知识——由可分离的感知和推理先验组成，它们具有独特的缩放趋势和起源。我们表明，LLM的潜在视觉推理能力主要通过以推理为中心的数据（例如，代码、数学、学术）的预训练来发展，并逐步扩展。这种从语言预训练中获得的推理先验是可转移的，并且普遍适用于视觉推理。相比之下，感知先验更分散地从广泛的语料库中涌现出来，并且感知能力对视觉编码器和视觉指令调整数据更敏感。同时，描述视觉世界的文本被证明至关重要，尽管其性能影响迅速饱和。利用这些见解，我们提出了一种以数据为中心的预训练视觉感知LLM的方案，并在1T token规模的预训练中验证了它。我们的发现基于超过100个受控实验，消耗了500,000 GPU-hours，涵盖了完整的MLLM构建流程——从LLM预训练到视觉对齐和监督多模态微调——跨越五个模型规模，各种数据类别和混合，以及多种适应设置。除了我们的主要发现，我们提出并研究了几个假设，并引入了多层次存在基准（MLE-Bench）。总之，这项工作提供了一种有意识地从语言预训练中培养视觉先验的新方法，为下一代多模态LLM铺平了道路。

## 🔬 方法详解

**问题定义**：论文旨在解决如何有效利用大型语言模型（LLM）在纯文本预训练过程中获得的视觉先验知识，从而提升多模态LLM的性能。现有方法通常依赖于大量的多模态数据进行微调，但忽略了LLM本身已经具备的潜在视觉能力。如何解耦和利用这些视觉先验，是当前研究的痛点。

**核心思路**：论文的核心思路是将LLM的视觉先验分解为感知先验和推理先验，并研究它们各自的来源和缩放规律。通过控制预训练数据的类型和规模，有针对性地培养LLM的视觉感知和推理能力。这种数据驱动的方法旨在最大限度地利用LLM的内在视觉知识，减少对大规模多模态数据的依赖。

**技术框架**：论文的研究框架主要包括以下几个阶段：1) LLM预训练：在不同类型和规模的文本数据上预训练LLM；2) 视觉对齐：将LLM与视觉编码器对齐，使其能够处理图像输入；3) 多模态微调：使用少量多模态数据对齐后的LLM进行微调，以适应特定的视觉任务；4) 评估：使用多种视觉任务和基准测试评估LLM的视觉能力。论文还提出了Multi-Level Existence Bench (MLE-Bench)用于更细粒度的评估。

**关键创新**：论文最重要的技术创新点在于揭示了LLM视觉先验的组成和来源，并提出了有针对性的数据驱动的预训练方法。与现有方法相比，该方法更加注重利用LLM本身已经具备的视觉知识，而不是仅仅依赖于大规模的多模态数据。此外，论文还提出了MLE-Bench，为更深入地评估LLM的视觉能力提供了新的工具。

**关键设计**：论文的关键设计包括：1) 控制预训练数据的类型和比例，例如增加代码、数学和学术数据的比例，以提升推理能力；2) 设计合适的视觉编码器和对齐方法，以确保LLM能够有效地处理图像输入；3) 使用多种视觉任务和基准测试进行评估，以全面了解LLM的视觉能力；4) 探索不同的模型规模和训练策略，以研究视觉先验的缩放规律。

## 📊 实验亮点

实验结果表明，通过控制预训练数据类型，可以显著提升LLM的视觉推理能力。例如，增加推理相关数据的比例可以使LLM在视觉推理任务上取得显著提升。此外，论文还发现感知能力对视觉编码器和视觉指令调整数据更敏感。该研究在五个模型规模和多种数据混合上进行了验证，消耗了500,000 GPU-hours。

## 🎯 应用场景

该研究成果可应用于开发更高效、更强大的多模态LLM，减少对大规模多模态数据的依赖。潜在应用领域包括智能助手、图像理解、视觉推理、机器人导航等。通过更好地利用LLM的内在视觉知识，可以降低模型训练成本，提升模型泛化能力，并推动多模态人工智能的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs), despite being trained on text alone, surprisingly develop rich visual priors. These priors allow latent visual capabilities to be unlocked for vision tasks with a relatively small amount of multimodal data, and in some cases, to perform visual tasks without ever having seen an image. Through systematic analysis, we reveal that visual priors-the implicit, emergent knowledge about the visual world acquired during language pre-training-are composed of separable perception and reasoning priors with unique scaling trends and origins. We show that an LLM's latent visual reasoning ability is predominantly developed by pre-training on reasoning-centric data (e.g., code, math, academia) and scales progressively. This reasoning prior acquired from language pre-training is transferable and universally applicable to visual reasoning. In contrast, a perception prior emerges more diffusely from broad corpora, and perception ability is more sensitive to the vision encoder and visual instruction tuning data. In parallel, text describing the visual world proves crucial, though its performance impact saturates rapidly. Leveraging these insights, we propose a data-centric recipe for pre-training vision-aware LLMs and verify it in 1T token scale pre-training. Our findings are grounded in over 100 controlled experiments consuming 500,000 GPU-hours, spanning the full MLLM construction pipeline-from LLM pre-training to visual alignment and supervised multimodal fine-tuning-across five model scales, a wide range of data categories and mixtures, and multiple adaptation setups. Along with our main findings, we propose and investigate several hypotheses, and introduce the Multi-Level Existence Bench (MLE-Bench). Together, this work provides a new way of deliberately cultivating visual priors from language pre-training, paving the way for the next generation of multimodal LLMs.

