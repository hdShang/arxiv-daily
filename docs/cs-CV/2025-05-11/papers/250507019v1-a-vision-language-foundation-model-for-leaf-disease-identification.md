---
layout: default
title: A Vision-Language Foundation Model for Leaf Disease Identification
---

# A Vision-Language Foundation Model for Leaf Disease Identification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07019" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07019v1</a>
  <a href="https://arxiv.org/pdf/2505.07019.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07019v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07019v1', 'A Vision-Language Foundation Model for Leaf Disease Identification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Khang Nguyen Quoc, Lan Le Thi Thu, Luyl-Da Quach

**分类**: cs.CV

**发布日期**: 2025-05-11

**DOI**: [10.1016/j.eswa.2025.130084](https://doi.org/10.1016/j.eswa.2025.130084)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/enalis/scold)

---

## 💡 一句话要点

**提出SCOLD模型以解决植物叶片疾病识别问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `植物疾病识别` `视觉-语言模型` `对比学习` `智能农业` `多模态融合`

## 📋 核心要点

1. 现有的植物叶片疾病识别方法在图像与文本模态的整合上存在不足，且常依赖于缺乏领域特定信息的数据集。
2. SCOLD模型通过上下文感知的对比学习，利用平滑标签来提高模型的泛化能力和鲁棒性，解决了现有方法的局限性。
3. 实验结果显示，SCOLD在零-shot和少-shot分类、图像-文本检索等任务上均优于现有模型，且参数量保持竞争力。

## 📝 摘要（中文）

植物叶片疾病识别在智能农业中至关重要。然而，许多现有研究在图像和文本模态的整合上仍面临挑战，且常依赖于缺乏领域特定信息的预训练数据集。为此，本文提出了SCOLD（Soft-target COntrastive learning for Leaf Disease identification），这是一个针对农业任务的上下文感知视觉-语言基础模型。SCOLD使用超过186,000对图像-描述的多样语料库进行任务无关的预训练，通过平滑标签来减轻对比学习中的过度自信，从而提高模型在细粒度分类任务上的泛化能力和鲁棒性。实验结果表明，SCOLD在多个基准测试中超越了现有的视觉-语言模型，如OpenAI-CLIP-L、BioCLIP和SigLIP2，同时保持了竞争力的参数规模。

## 🔬 方法详解

**问题定义**：本文旨在解决植物叶片疾病识别中的图像与文本模态整合不足的问题。现有方法多依赖于缺乏领域特定信息的预训练数据集，导致模型在实际应用中的效果不佳。

**核心思路**：SCOLD模型通过上下文感知的对比学习，使用平滑标签来减轻对比学习中的过度自信，从而提升模型在细粒度分类任务中的表现。这样的设计旨在提高模型的泛化能力和鲁棒性，特别是在农业领域的应用中。

**技术框架**：SCOLD的整体架构包括数据预处理、任务无关的预训练和模型微调三个主要阶段。模型通过对186,000对图像-描述的多样语料库进行训练，确保了其在不同任务上的适应性。

**关键创新**：SCOLD的主要创新在于引入了上下文感知的软目标对比学习方法，这与传统的硬标签对比学习方法形成了鲜明对比。通过平滑标签，SCOLD有效地减轻了模型的过度自信，从而提高了分类精度。

**关键设计**：在模型设计中，SCOLD采用了特定的损失函数来实现软目标对比学习，并在网络结构上进行了优化，以确保在保持较小参数量的同时，提升模型的性能。

## 📊 实验亮点

实验结果表明，SCOLD在多个基准测试中超越了OpenAI-CLIP-L、BioCLIP和SigLIP2等现有视觉-语言模型，尤其在零-shot和少-shot分类任务中表现突出，提升幅度显著，且保持了较小的参数规模。

## 🎯 应用场景

SCOLD模型在智能农业中的潜在应用广泛，能够有效识别植物叶片的疾病，帮助农民及时采取措施，减少作物损失。未来，该模型还可扩展到其他多模态系统中，为植物疾病诊断提供更智能的解决方案。

## 📄 摘要（原文）

> Leaf disease identification plays a pivotal role in smart agriculture. However, many existing studies still struggle to integrate image and textual modalities to compensate for each other's limitations. Furthermore, many of these approaches rely on pretraining with constrained datasets such as ImageNet, which lack domain-specific information. We propose SCOLD (Soft-target COntrastive learning for Leaf Disease identification), a context-aware vision-language foundation model tailored to address these challenges for agricultural tasks. SCOLD is developed using a diverse corpus of plant leaf images and corresponding symptom descriptions, comprising over 186,000 image-caption pairs aligned with 97 unique concepts. Through task-agnostic pretraining, SCOLD leverages contextual soft targets to mitigate overconfidence in contrastive learning by smoothing labels, thereby improving model generalization and robustness on fine-grained classification tasks. Experimental results demonstrate that SCOLD outperforms existing vision-language models such as OpenAI-CLIP-L, BioCLIP, and SigLIP2 across several benchmarks, including zero-shot and few-shot classification, image-text retrieval, and image classification, while maintaining a competitive parameter footprint. Ablation studies further highlight SCOLD's effectiveness in contrast to its counterparts. The proposed approach significantly advances the agricultural vision-language foundation model, offering strong performance with minimal or no supervised fine-tuning. This work lays a solid groundwork for future research on models trained with long-form and simplified contexts, tasks involving class ambiguity, and multi-modal systems for intelligent plant disease diagnostics. The code for this study is available at https://huggingface.co/enalis/scold

