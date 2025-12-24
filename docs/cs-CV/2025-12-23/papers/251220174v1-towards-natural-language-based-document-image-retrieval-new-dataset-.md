---
layout: default
title: Towards Natural Language-Based Document Image Retrieval: New Dataset and Benchmark
---

# Towards Natural Language-Based Document Image Retrieval: New Dataset and Benchmark

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20174" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20174v1</a>
  <a href="https://arxiv.org/pdf/2512.20174.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20174v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20174v1', 'Towards Natural Language-Based Document Image Retrieval: New Dataset and Benchmark')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Guo, Xugong Qin, Jun Jie Ou Yang, Peng Zhang, Gangyan Zeng, Yubo Li, Hailun Lin

**分类**: cs.CV, cs.CL, cs.IR

**发布日期**: 2025-12-23

**备注**: CVPR 2025

---

## 💡 一句话要点

**提出NL-DIR基准数据集，用于解决自然语言描述的文档图像检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文档图像检索` `自然语言查询` `视觉语言模型` `NL-DIR数据集` `两阶段检索`

## 📋 核心要点

1. 现有文档图像检索方法难以处理实际场景中细粒度语义的文本查询。
2. 提出NL-DIR基准数据集，使用自然语言描述作为查询，促进更精细的文档图像检索。
3. 通过零样本和微调实验，验证了现有模型在NL-DIR上的性能，并探索了两阶段检索方法。

## 📝 摘要（中文）

文档图像检索（DIR）旨在根据给定的查询从图库中检索文档图像。现有的DIR方法主要基于图像查询，检索语义类别粗略相同的文档，例如报纸或收据。然而，在实际场景中，通常提供具有细粒度语义的文本查询，这些方法难以有效检索文档图像。为了弥合这一差距，我们引入了一个新的基于自然语言的文档图像检索（NL-DIR）基准，并提出了相应的评估指标。在这项工作中，自然语言描述作为DIR任务的语义丰富的查询。NL-DIR数据集包含4.1万张真实的文档图像，每张图像都配有五个高质量、细粒度的语义查询，这些查询通过大型语言模型生成并评估，并结合人工验证。我们对现有的主流对比视觉-语言模型和无OCR的视觉文档理解（VDU）模型进行了零样本和微调评估。进一步研究了一种两阶段检索方法，以提高性能，同时实现时间和空间效率。我们希望提出的NL-DIR基准能够为VDU社区带来新的机遇并促进研究。数据集和代码将在huggingface.co/datasets/nianbing/NL-DIR上公开。

## 🔬 方法详解

**问题定义**：论文旨在解决基于自然语言描述的文档图像检索问题。现有文档图像检索方法主要依赖图像查询，只能检索粗粒度语义类别相同的文档，无法有效处理实际应用中常见的、具有细粒度语义的文本查询。这限制了文档图像检索在更广泛场景中的应用，例如根据用户输入的具体问题查找相关文档。

**核心思路**：论文的核心思路是构建一个高质量的、包含自然语言描述的文档图像数据集，并以此为基础评估和改进现有视觉-语言模型在文档图像检索任务中的性能。通过引入自然语言描述作为查询，可以实现更精细、更灵活的文档图像检索，从而更好地满足用户的实际需求。

**技术框架**：论文主要包含以下几个阶段：1) 构建NL-DIR数据集，包括收集文档图像，并使用大型语言模型生成和人工验证自然语言描述；2) 对现有主流的对比视觉-语言模型和无OCR的视觉文档理解模型进行零样本和微调评估；3) 探索两阶段检索方法，以提高检索性能和效率。整体框架围绕NL-DIR数据集展开，旨在评估现有模型并探索更有效的检索方法。

**关键创新**：论文的关键创新在于构建了NL-DIR数据集，该数据集包含4.1万张真实的文档图像，每张图像都配有五个高质量、细粒度的自然语言描述。与现有数据集相比，NL-DIR数据集更贴近实际应用场景，并且提供了更丰富的语义信息，为研究基于自然语言的文档图像检索提供了新的平台。此外，论文还探索了一种两阶段检索方法，在提高性能的同时兼顾了时间和空间效率。

**关键设计**：NL-DIR数据集的关键设计在于使用大型语言模型生成自然语言描述，并结合人工验证，以保证描述的质量和准确性。两阶段检索方法的关键设计在于首先使用粗粒度的图像特征进行快速检索，然后使用细粒度的文本特征进行精确排序，从而实现性能和效率的平衡。具体的模型选择、损失函数和网络结构等细节，论文中没有详细描述，属于模型选择和调优的范畴。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20174v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20174v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20174v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文构建的NL-DIR数据集包含4.1万张文档图像，并配有高质量的自然语言描述，为相关研究提供了宝贵资源。实验结果表明，现有视觉-语言模型在NL-DIR数据集上仍有提升空间。论文提出的两阶段检索方法在提高检索性能的同时，兼顾了时间和空间效率，具有一定的实用价值。

## 🎯 应用场景

该研究成果可应用于智能文档管理、信息检索、法律咨询、金融分析等领域。例如，用户可以通过自然语言描述快速找到所需的合同、发票、报告等文档图像。未来，该研究有望推动文档图像检索技术的发展，实现更智能、更高效的文档处理和信息服务。

## 📄 摘要（原文）

> Document image retrieval (DIR) aims to retrieve document images from a gallery according to a given query. Existing DIR methods are primarily based on image queries that retrieve documents within the same coarse semantic category, e.g., newspapers or receipts. However, these methods struggle to effectively retrieve document images in real-world scenarios where textual queries with fine-grained semantics are usually provided. To bridge this gap, we introduce a new Natural Language-based Document Image Retrieval (NL-DIR) benchmark with corresponding evaluation metrics. In this work, natural language descriptions serve as semantically rich queries for the DIR task. The NL-DIR dataset contains 41K authentic document images, each paired with five high-quality, fine-grained semantic queries generated and evaluated through large language models in conjunction with manual verification. We perform zero-shot and fine-tuning evaluations of existing mainstream contrastive vision-language models and OCR-free visual document understanding (VDU) models. A two-stage retrieval method is further investigated for performance improvement while achieving both time and space efficiency. We hope the proposed NL-DIR benchmark can bring new opportunities and facilitate research for the VDU community. Datasets and codes will be publicly available at huggingface.co/datasets/nianbing/NL-DIR.

