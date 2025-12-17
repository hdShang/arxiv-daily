---
layout: default
title: TaP: A Taxonomy-Guided Framework for Automated and Scalable Preference Data Generation
---

# TaP: A Taxonomy-Guided Framework for Automated and Scalable Preference Data Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23979" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23979</a>
  <a href="https://arxiv.org/pdf/2506.23979.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23979" onclick="toggleFavorite(this, '2506.23979', 'TaP: A Taxonomy-Guided Framework for Automated and Scalable Preference Data Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Renren Jin, Tianhao Shen, Xinwei Wu, Dan Shi, Haoran Sun, Yuqi Ren, Wuwei Huang, Quandong Wang, Wei Liu, Jian Luan, Bin Wang, Deyi Xiong

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**TaP：一种基于分类法的自动化、可扩展的偏好数据生成框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `偏好学习` `数据生成` `大型语言模型` `分类法` `自动化` `多语言` `指令微调`

## 📋 核心要点

1. 现有LLM微调数据集构建成本高昂，且多为英文，限制了多语言LLM的发展。
2. TaP框架利用结构化分类法，实现对数据集组成的细粒度控制，保证数据多样性和覆盖率。
3. 实验表明，使用TaP生成的数据集训练的LLM，性能超越了使用更大规模开源数据集训练的LLM。

## 📝 摘要（中文）

为了提升大型语言模型（LLMs）遵循指令和与人类偏好及价值观对齐的能力，需要在其上进行有监督微调和偏好微调，这需要高质量的数据集。然而，构建此类数据集需要耗费大量资源，并且大多数可用的有监督和偏好微调数据集都是英文的。为了解决这些挑战，我们提出了基于分类法的偏好数据生成（TaP）框架，该框架有助于跨各种语言自动且可扩展地构建偏好数据集。TaP基于结构化的分类法，可以对数据集的组成进行细粒度控制，从而确保多样性和全面的覆盖。我们使用TaP生成的数据集对各种LLM进行有监督和偏好微调。实验结果表明，在TaP生成的数据集上训练的LLM优于在现有开源数据集上训练的LLM。值得注意的是，在TaP生成的数据集上训练的LLM的性能超过了在规模大180倍的开源数据集上训练的LLM。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）的有监督微调和偏好微调所需的高质量数据集的构建问题。现有方法主要面临两个痛点：一是数据集构建成本高昂，需要大量人工标注；二是现有数据集大多为英文，缺乏对多语言的支持。

**核心思路**：论文的核心思路是利用一个结构化的分类法（Taxonomy）来指导偏好数据的自动生成。通过分类法，可以对生成的数据集进行细粒度控制，从而保证数据集的多样性和覆盖率，同时降低人工标注的成本。

**技术框架**：TaP框架包含以下主要模块：1) 分类法构建模块：定义数据集的结构化分类体系，例如主题、风格、难度等；2) 数据生成模块：基于分类法，利用LLM自动生成候选数据；3) 偏好排序模块：对生成的数据进行排序，选出符合人类偏好的数据；4) 数据集构建模块：将排序后的数据构建成最终的偏好数据集。整个流程旨在自动化生成高质量、多语言的偏好数据集。

**关键创新**：TaP框架的关键创新在于引入了分类法来指导偏好数据的生成。与以往随机生成或人工标注的方法相比，TaP能够更有效地控制数据集的质量和多样性，并显著降低了数据构建的成本。

**关键设计**：分类法的具体设计是关键。例如，可以根据不同的应用场景定义不同的分类维度，并为每个维度设置不同的取值范围。数据生成模块可以使用不同的LLM和生成策略，偏好排序模块可以使用人工标注或自动评估指标。具体参数设置和损失函数的使用取决于具体的实现细节，论文中可能未详细说明。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2506.23979/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2506.23979/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2506.23979/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，使用TaP生成的数据集训练的LLM，性能显著优于使用现有开源数据集训练的LLM。更令人瞩目的是，使用TaP生成的数据集训练的LLM，其性能甚至超过了使用规模大180倍的开源数据集训练的LLM，这充分证明了TaP框架的有效性和效率。

## 🎯 应用场景

TaP框架可广泛应用于各种语言的大型语言模型的微调，尤其是在资源有限的情况下。通过自动化生成高质量的偏好数据集，可以显著降低LLM训练的成本，并提升其在特定任务上的性能。该框架还有助于构建更符合人类价值观和偏好的LLM，促进人机协作。

## 📄 摘要（原文）

> Conducting supervised fine-tuning and preference fine-tuning on large language models (LLMs) requires high-quality datasets to improve their ability to follow instructions and align with human preferences and values. However, constructing such datasets is resource-intensive, and most available datasets for supervised and preference fine-tuning are in English. To address these challenges, we propose the \underline{\textbf{Ta}}xonomy-Guided \underline{\textbf{P}}reference Data Generation (TaP) framework, which facilitates automated and scalable construction of preference datasets across various languages. TaP is grounded in a structured taxonomy that allows fine-grained control over dataset composition, thereby ensuring both diversity and comprehensive coverage. We employ TaP-generated datasets to perform supervised and preference fine-tuning on various LLMs. Experimental results demonstrate that LLMs trained on TaP-generated datasets outperform those trained on existing open-source datasets. Remarkably, LLMs trained on TaP-generated datasets surpass the performance of those trained on an open-source dataset that is 180 times larger.

