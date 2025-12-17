---
layout: default
title: TIBSTC-CoT: A Multi-Domain Instruction Dataset for Chain-of-Thought Reasoning in Language Models
---

# TIBSTC-CoT: A Multi-Domain Instruction Dataset for Chain-of-Thought Reasoning in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01977" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01977</a>
  <a href="https://arxiv.org/pdf/2508.01977.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01977" onclick="toggleFavorite(this, '2508.01977', 'TIBSTC-CoT: A Multi-Domain Instruction Dataset for Chain-of-Thought Reasoning in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fan Gao, Cheng Huang, Nyima Tashi, Yutong Liu, Xiangxiang Wang, Thupten Tsering, Ban Ma-bao, Renzeg Duojie, Gadeng Luosang, Rinchen Dongrub, Dorje Tashi, Xiao Feng, Hao Wang, Yongbin Yu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出TIBSTC-CoT藏语数据集，并训练Sunshine-thinking系列LLM，提升低资源藏语的CoT推理能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `藏语` `低资源语言` `大型语言模型` `思维链` `数据集构建`

## 📋 核心要点

1. 藏语作为低资源语言，面临数据稀缺的挑战，阻碍了藏语自然语言处理技术的发展。
2. 论文提出利用大型语言模型（LLM）的思维链提示，自动构建大规模多领域的藏语数据集TIBSTC-CoT。
3. 基于TIBSTC-CoT训练的Sunshine-thinking LLM系列，在推理和生成性能上可与SOTA多语言LLM媲美。

## 📝 摘要（中文）

为了解决藏语（一种拥有超过六百万使用者的低资源语言）中严重的数据稀缺问题，我们推出了TIBSTC-CoT，这是一个大规模、多领域的藏语数据集，它通过大型语言模型（LLM）的思维链提示自动构建。TIBSTC-CoT为低资源环境下的数据集创建建立了一个可扩展和可复现的框架，涵盖了语言理解和生成所必需的各种领域和推理模式。基于此数据集，我们开发了Sunshine-thinking LLM系列，这是一系列以藏语为中心的、具备思维链能力的LLM。Sunshine-thinking完全在TIBSTC-CoT上训练，已经展示出强大的推理和生成性能，可与最先进（SOTA）的多语言LLM相媲美。我们的工作通过资源创建和模型创新，为实现包容性人工智能迈出了重要一步，从而实现了高质量的藏语语言处理。所有数据均可用。

## 🔬 方法详解

**问题定义**：论文旨在解决低资源语言（特别是藏语）数据稀缺的问题，这限制了大型语言模型在藏语环境下的应用，尤其是在需要复杂推理的任务中。现有方法要么依赖少量人工标注数据，要么直接使用其他语言的模型进行迁移，效果不佳。缺乏大规模、高质量的藏语数据集是主要痛点。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的强大生成能力，通过思维链（Chain-of-Thought, CoT）提示自动生成大规模的藏语数据集。CoT提示能够引导LLM逐步推理，生成包含中间推理步骤的文本，从而提高数据的质量和多样性。这种方法避免了大量的人工标注工作，降低了数据获取的成本。

**技术框架**：整体框架包括以下几个主要阶段：1) 确定数据集的领域和任务类型；2) 设计合适的CoT提示模板，引导LLM生成包含推理步骤的藏语文本；3) 使用LLM进行数据生成，得到初始的TIBSTC-CoT数据集；4) 对生成的数据进行清洗和过滤，去除低质量或不符合要求的样本；5) 使用TIBSTC-CoT数据集训练Sunshine-thinking LLM系列。

**关键创新**：论文的关键创新在于提出了一种可扩展和可复现的低资源语言数据集自动构建框架。该框架利用CoT提示，有效地利用了现有LLM的知识，生成了高质量的藏语数据集。此外，论文还提出了Sunshine-thinking LLM系列，证明了该数据集的有效性。与现有方法相比，该方法能够以较低的成本获取大规模的藏语数据，并显著提升藏语LLM的性能。

**关键设计**：CoT提示模板的设计是关键。论文可能针对不同的领域和任务类型，设计了不同的提示模板，以引导LLM生成符合要求的推理过程。具体参数设置和损失函数等技术细节在摘要中未提及，属于未知信息。网络结构也属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2508.01977/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2508.01977/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2508.01977/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文构建了大规模多领域的藏语数据集TIBSTC-CoT，并基于此数据集训练了Sunshine-thinking LLM系列。实验结果表明，Sunshine-thinking LLM在推理和生成性能上可与SOTA多语言LLM媲美，证明了该数据集的有效性和该方法的优越性。具体的性能数据和提升幅度在摘要中未提及，属于未知信息。

## 🎯 应用场景

该研究成果可应用于藏语信息处理的多个领域，如机器翻译、智能问答、文本摘要、情感分析等。通过提升藏语LLM的性能，可以促进藏语文化传承和信息交流，为藏族人民提供更便捷的智能化服务。未来，该方法可以推广到其他低资源语言，助力实现更包容的人工智能。

## 📄 摘要（原文）

> To address the severe data scarcity in Tibetan, a low-resource language spoken by over six million people, we introduce TIBSTC-CoT, the large-scale, multi-domain Tibetan dataset automatically constructed via chain-of-thought prompting with large language models (LLMs). TIBSTC-CoT establishes a scalable and reproducible framework for dataset creation in low-resource settings, covering diverse domains and reasoning patterns essential for language understanding and generation. Building on this dataset, we develop the Sunshine-thinking LLM family, a series of Tibetan-centric LLMs equipped with chain-of-thought capabilities. Trained entirely on TIBSTC-CoT, Sunshine-thinking has demonstrated strong reasoning and generation performance, comparable to state-of-the-art (SOTA) multilingual LLMs. Our work marks a significant step toward inclusive AI by enabling high-quality Tibetan language processing through both resource creation and model innovation. All data are available:this https URL.

