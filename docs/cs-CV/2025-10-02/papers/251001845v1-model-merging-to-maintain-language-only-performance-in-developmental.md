---
layout: default
title: Model Merging to Maintain Language-Only Performance in Developmentally Plausible Multimodal Models
---

# Model Merging to Maintain Language-Only Performance in Developmentally Plausible Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01845" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01845v1</a>
  <a href="https://arxiv.org/pdf/2510.01845.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01845v1" onclick="toggleFavorite(this, '2510.01845v1', 'Model Merging to Maintain Language-Only Performance in Developmentally Plausible Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ece Takmaz, Lisa Bylinina, Jakub Dotlacil

**分类**: cs.CL, cs.CV

**发布日期**: 2025-10-02

**备注**: Accepted to the EMNLP 2025 workshop BabyLM: Accelerating language modeling research with cognitively plausible datasets

---

## 💡 一句话要点

**提出模型融合方法，提升多模态模型在语言任务中的性能表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `模型融合` `语言模型` `BabyLM` `低资源学习`

## 📋 核心要点

1. 多模态模型在纯语言任务中表现不佳是一个挑战，尤其是在资源受限和模拟儿童学习的场景下。
2. 论文提出模型融合方法，通过融合多模态模型和纯语言模型的参数，提升多模态模型在语言任务中的性能。
3. 实验结果表明，模型融合能够有效提升多模态模型在纯语言任务上的表现，同时保持其多模态性能。

## 📝 摘要（中文）

本文针对BabyLM挑战赛的多模态赛道，提出了一种在低资源环境下构建符合儿童发展规律的多模态模型的方法。该方法旨在解决多模态模型在纯语言任务中表现不佳的问题。通过使用加权线性插值融合多模态模型和纯语言模型的参数，即模型融合，来提升多模态模型在语言任务上的性能。实验结果表明，多模态模型在侧重语法的纯语言基准测试中表现确实较差，而与纯文本模型进行模型融合可以在一定程度上缓解这个问题，同时保持多模态性能。

## 🔬 方法详解

**问题定义**：现有的大型视觉-语言模型参数众多，训练数据量巨大，远超儿童语言习得过程中接触到的语言数据量。此外，多模态模型在纯语言任务上的表现往往不如纯语言模型，尤其是在语法相关的任务上。因此，论文要解决的问题是如何在资源受限的情况下，构建既能处理多模态信息，又能保持良好语言能力的模型。

**核心思路**：论文的核心思路是通过模型融合，将多模态模型和纯语言模型的优势结合起来。具体来说，就是将训练好的多模态模型和纯语言模型的参数进行加权平均，从而使融合后的模型既能利用视觉信息，又能保持较强的语言能力。这样设计的目的是为了缓解多模态模型在纯语言任务上的性能下降问题。

**技术框架**：论文采用的模型融合框架主要包含以下几个步骤：1) 分别训练一个多模态模型和一个纯语言模型；2) 使用加权线性插值方法，将两个模型的参数进行融合。融合后的模型可以同时处理视觉和语言信息，并且在纯语言任务上具有较好的性能。

**关键创新**：论文的关键创新在于将模型融合技术应用于多模态学习领域，并验证了其在提升多模态模型语言能力方面的有效性。与传统的训练方法相比，模型融合能够更有效地利用已有的纯语言模型，从而在资源受限的情况下获得更好的性能。

**关键设计**：论文采用加权线性插值作为模型融合的具体方法。具体公式为：θ_merged = α * θ_multimodal + (1 - α) * θ_language，其中θ_merged是融合后的模型参数，θ_multimodal是多模态模型参数，θ_language是纯语言模型参数，α是权重系数，控制着多模态模型和纯语言模型在融合后的模型中的贡献比例。α的选择是一个关键的设计参数，需要根据具体的任务和数据集进行调整。

## 📊 实验亮点

实验结果表明，多模态模型在纯语言基准测试中表现确实较差，尤其是在侧重语法的任务上。通过与纯文本模型进行模型融合，可以在一定程度上缓解这个问题，同时保持多模态性能。具体的性能提升幅度取决于权重系数α的选择，需要根据具体任务进行调整。

## 🎯 应用场景

该研究成果可应用于开发更符合儿童认知发展规律的多模态学习系统，例如儿童教育机器人、智能玩具等。通过模型融合，可以提升这些系统在理解和生成自然语言方面的能力，从而更好地与儿童进行互动和交流。此外，该方法也可以推广到其他资源受限的多模态学习场景。

## 📄 摘要（原文）

> State-of-the-art vision-and-language models consist of many parameters and learn from enormous datasets, surpassing the amounts of linguistic data that children are exposed to as they acquire a language. This paper presents our approach to the multimodal track of the BabyLM challenge addressing this discrepancy. We develop language-only and multimodal models in low-resource settings using developmentally plausible datasets, with our multimodal models outperforming previous BabyLM baselines. One finding in the multimodal language model literature is that these models tend to underperform in \textit{language-only} tasks. Therefore, we focus on maintaining language-only abilities in multimodal models. To this end, we experiment with \textit{model merging}, where we fuse the parameters of multimodal models with those of language-only models using weighted linear interpolation. Our results corroborate the findings that multimodal models underperform in language-only benchmarks that focus on grammar, and model merging with text-only models can help alleviate this problem to some extent, while maintaining multimodal performance.

