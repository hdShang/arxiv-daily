---
layout: default
title: "Beyond Token Limits: Assessing Language Model Performance on Long Text Classification"
---

# Beyond Token Limits: Assessing Language Model Performance on Long Text Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10199" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10199v3</a>
  <a href="https://arxiv.org/pdf/2509.10199.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10199v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10199v3', 'Beyond Token Limits: Assessing Language Model Performance on Long Text Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Miklós Sebők, Viktor Kovács, Martin Bánóczy, Daniel Møller Eriksen, Nathalie Neptune, Philippe Roussille

**分类**: cs.CL

**发布日期**: 2025-09-12 (更新: 2025-09-26)

---

## 💡 一句话要点

**评估语言模型在长文本分类任务上的性能，发现长文本专用模型并无明显优势。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本分类` `语言模型` `Longformer` `XLM-RoBERTa` `GPT-3.5` `GPT-4` `政策分析` `多语言`

## 📋 核心要点

1. 现有BERT等模型在处理长文本分类任务时受限于输入长度，无法直接应用于法律等长文档。
2. 该研究对比了XLM-RoBERTa、Longformer、GPT等模型在长文本分类任务上的性能表现。
3. 实验结果表明，专门为长文本设计的Longformer模型并未展现出显著优势，开源模型表现更佳。

## 📝 摘要（中文）

社交科学领域广泛使用的大型语言模型（如BERT及其衍生模型RoBERTa）在处理长文本输入时存在长度限制。这对于需要处理长文本的分类任务（例如法律和草案）来说是一个严峻的问题，因为这些文本可能长达数百页，超出模型可处理的token数量（例如512个）。本文使用XLM-RoBERTa、Longformer、GPT-3.5和GPT-4模型，针对比较议程项目（Comparative Agendas Project）的多类别分类任务（包含从教育到医疗保健的21个政策主题标签）进行了五种语言的实验。结果表明，专门为处理长输入而预训练的Longformer模型并没有表现出明显的优势。GPT模型与表现最佳的开源模型相比，后者更胜一筹。对类别层面因素的分析表明，在处理长文本输入时，特定类别之间的支持和实质性重叠非常重要。

## 🔬 方法详解

**问题定义**：该论文旨在解决大型语言模型在长文本分类任务中的应用问题，特别是针对法律、草案等篇幅较长的文档。现有方法如BERT等模型受限于输入长度，无法直接处理这些长文本。虽然有Longformer等专门为长文本设计的模型，但其性能优势尚不明确。

**核心思路**：该论文的核心思路是通过实验对比不同类型的语言模型（包括通用模型和长文本专用模型）在长文本分类任务上的性能，从而评估它们在处理长文本时的能力。通过分析模型在不同类别上的表现，探究影响长文本分类性能的关键因素。

**技术框架**：该研究采用比较议程项目（Comparative Agendas Project）的多类别分类任务作为实验平台。该任务包含21个政策主题标签，涵盖从教育到医疗保健等领域。研究使用了XLM-RoBERTa、Longformer、GPT-3.5和GPT-4等模型，并对五种语言的数据进行了实验。

**关键创新**：该研究的关键创新在于对长文本专用模型Longformer的性能进行了评估，并发现其在特定任务上并没有表现出明显的优势。此外，该研究还分析了类别层面的因素，揭示了类别之间的支持和实质性重叠对长文本分类性能的影响。

**关键设计**：该研究使用了XLM-RoBERTa作为基线模型，并与Longformer和GPT系列模型进行了对比。实验中，研究人员使用了比较议程项目提供的多语言数据集，并针对不同的模型进行了适当的参数调整。具体的损失函数和网络结构细节取决于所使用的模型。

## 📊 实验亮点

实验结果表明，专门为处理长输入而预训练的Longformer模型并没有表现出明显的优势。在比较议程项目的多类别分类任务中，表现最佳的开源模型优于GPT模型。类别层面的分析表明，类别之间的支持和实质性重叠是影响长文本分类性能的重要因素。

## 🎯 应用场景

该研究成果可应用于法律文本分析、政策文件分类、社会科学研究等领域。通过选择合适的语言模型，可以提高长文本分类的准确性和效率，为相关领域的决策提供支持。未来的研究可以进一步探索如何优化模型结构和训练方法，以更好地处理长文本数据。

## 📄 摘要（原文）

> The most widely used large language models in the social sciences (such as BERT, and its derivatives, e.g. RoBERTa) have a limitation on the input text length that they can process to produce predictions. This is a particularly pressing issue for some classification tasks, where the aim is to handle long input texts. One such area deals with laws and draft laws (bills), which can have a length of multiple hundred pages and, therefore, are not particularly amenable for processing with models that can only handle e.g. 512 tokens. In this paper, we show results from experiments covering 5 languages with XLM-RoBERTa, Longformer, GPT-3.5, GPT-4 models for the multiclass classification task of the Comparative Agendas Project, which has a codebook of 21 policy topic labels from education to health care. Results show no particular advantage for the Longformer model, pre-trained specifically for the purposes of handling long inputs. The comparison between the GPT variants and the best-performing open model yielded an edge for the latter. An analysis of class-level factors points to the importance of support and substance overlaps between specific categories when it comes to performance on long text inputs.

