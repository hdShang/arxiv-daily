---
layout: default
title: "MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes"
---

# MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24945" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24945v2</a>
  <a href="https://arxiv.org/pdf/2509.24945.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24945v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24945v2', 'MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changsheng Zhao, Ernie Chang, Zechun Liu, Chia-Jung Chang, Wei Wen, Chen Lai, Sheng Cao, Yuandong Tian, Raghuraman Krishnamoorthi, Yangyang Shi, Vikas Chandra

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29 (更新: 2025-09-30)

**备注**: Model: https://huggingface.co/collections/facebook/mobilellm-r1-68c4597b104fac45f28f448e

---

## 💡 一句话要点

**MobileLLM-R1：通过开放训练方案探索十亿参数以下语言模型推理能力的极限**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小型语言模型` `推理能力` `数据重采样` `开源训练` `知识蒸馏`

## 📋 核心要点

1. 现有大型语言模型通常依赖于庞大的数据集（>10T tokens）进行训练，以获得强大的推理能力，这限制了小型模型的发展。
2. MobileLLM-R1通过精心策划和重采样开源数据集，证明了仅需约2T tokens的高质量数据即可训练出具有强大推理能力的十亿参数以下模型。
3. 实验结果表明，MobileLLM-R1-950M在多个推理基准测试中，性能优于或匹配了使用更多数据训练的更大模型，如Qwen3-0.6B。

## 📝 摘要（中文）

大型语言模型（LLM）的范式转变，从本能反应到思维链（CoT）推理，引发了两个普遍假设：（1）推理能力只出现在足够大的模型中；（2）这种能力需要在海量数据集上进行训练。虽然第一个假设已经受到最近的十亿参数以下推理模型（如Qwen3-0.6B和DeepSeek蒸馏变体）的挑战，但第二个假设在很大程度上仍未受到质疑。在这项工作中，我们重新审视了扩展到极其庞大的语料库（>10T tokens）对于推理能力出现的必要性。通过仔细策划和重新采样我们认为在设计的指标下有益的开源数据集，我们证明了强大的推理能力可以用更少的数据出现。具体来说，我们表明，只有约2T tokens的高质量数据就足够了，并且在从这些约2T tokens重新采样的数据集上进行4.2T tokens的预训练，然后进行既定的后训练程序，就可以开发MobileLLM-R1，这是一系列十亿参数以下的推理模型，其性能大大优于之前在完全开源数据上训练的模型。例如，MobileLLM-R1-950M的AIME得分达到15.5，而OLMo-2-1.48B仅为0.6，SmolLM-2-1.7B仅为0.3。值得注意的是，尽管与Qwen3用于预训练的36T-token专有语料库相比，MobileLLM-R1-950M仅在11.7%的tokens上进行了训练，但它在多个推理基准测试中与Qwen3-0.6B相匹配或超过了Qwen3-0.6B。为了促进这方面的进一步研究，我们发布了完整的训练方案、数据来源、数据混合比例和模型检查点，以及整个研究过程中获得的关键见解。

## 🔬 方法详解

**问题定义**：现有的大型语言模型通常需要使用超过10T tokens的数据进行训练才能获得较好的推理能力，这导致训练成本高昂，并且限制了小型模型的发展。因此，如何使用更少的数据训练出具有强大推理能力的小型语言模型是一个重要的研究问题。

**核心思路**：论文的核心思路是通过精心挑选和重采样开源数据集，构建一个高质量的小规模训练数据集。作者认为，并非所有数据都对推理能力的提升有益，因此需要对数据进行筛选和优化。通过这种方式，可以在使用较少数据的情况下，训练出具有竞争力的模型。

**技术框架**：MobileLLM-R1的训练流程主要包括以下几个阶段：1) 数据集构建：从开源数据集中选择有益于推理能力提升的数据，并进行重采样，构建一个规模约为2T tokens的高质量数据集。2) 预训练：使用构建的数据集进行4.2T tokens的预训练。3) 后训练：采用既定的后训练程序，进一步提升模型的性能。

**关键创新**：论文的关键创新在于提出了一个有效的数据选择和重采样策略，证明了高质量的小规模数据集可以替代大规模数据集，从而降低了训练成本，并使得小型模型也能具备强大的推理能力。与现有方法相比，该方法更加注重数据的质量而非数量。

**关键设计**：论文公开了完整的数据集构建细节，包括数据来源、数据混合比例等。此外，论文还公开了模型的训练方案和模型检查点，方便其他研究者进行复现和进一步研究。具体的参数设置、损失函数和网络结构等细节可能参考了已有的工作，论文重点在于数据处理和训练流程的优化。

## 📊 实验亮点

MobileLLM-R1-950M在AIME测试中取得了15.5的得分，显著优于OLMo-2-1.48B（0.6）和SmolLM-2-1.7B（0.3）。更重要的是，尽管MobileLLM-R1-950M仅使用了Qwen3预训练数据量的11.7%，但在多个推理基准测试中，其性能与Qwen3-0.6B相匹配甚至超越了Qwen3-0.6B，证明了高质量小规模数据集的有效性。

## 🎯 应用场景

MobileLLM-R1的研究成果可应用于资源受限的场景，例如移动设备、嵌入式系统等。该研究降低了训练和部署语言模型的成本，使得更多用户可以使用高性能的AI服务。未来，该研究可以推动小型语言模型在各个领域的应用，例如智能助手、自动问答、文本生成等。

## 📄 摘要（原文）

> The paradigm shift in large language models (LLMs) from instinctive responses to chain-of-thought (CoT) reasoning has fueled two prevailing assumptions: (1) reasoning capabilities only emerge in sufficiently large models, and (2) such capabilities require training on massive datasets. While the first assumption has already been challenged by recent sub-billion-parameter reasoning models such as Qwen3-0.6B and DeepSeek distilled variants, the second remains largely unquestioned. In this work, we revisit the necessity of scaling to extremely large corpora (>10T tokens) for reasoning emergence. By carefully curating and resampling open-source datasets that we identify as beneficial under our designed metrics, we demonstrate that strong reasoning abilities can emerge with far less data. Specifically, we show that only ~2T tokens of high-quality data are sufficient, and pre-training with 4.2T tokens on the dataset resampled from these ~2T tokens, followed by a established post-training procedure, enables the development of MobileLLM-R1, a series of sub-billion-parameter reasoning models that substantially outperform prior models trained on fully open-sourced data. For example, MobileLLM-R1-950M achieves an AIME score of 15.5, compared to just 0.6 for OLMo-2-1.48B and 0.3 for SmolLM-2-1.7B. Remarkably, despite being trained on only 11.7% of the tokens compared to Qwen3's proprietary 36T-token corpus for pretraining, MobileLLM-R1-950M matches or surpasses Qwen3-0.6B across multiple reasoning benchmarks. To facilitate further research in this direction, we have released the complete training recipe, data sources, data mixing ratio, and model checkpoints, together with the key insights obtained throughout this study.

