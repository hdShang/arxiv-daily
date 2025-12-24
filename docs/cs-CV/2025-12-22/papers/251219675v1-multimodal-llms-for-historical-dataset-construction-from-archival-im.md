---
layout: default
title: "Multimodal LLMs for Historical Dataset Construction from Archival Image Scans: German Patents (1877-1918)"
---

# Multimodal LLMs for Historical Dataset Construction from Archival Image Scans: German Patents (1877-1918)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19675" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19675v1</a>
  <a href="https://arxiv.org/pdf/2512.19675.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19675v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19675v1', 'Multimodal LLMs for Historical Dataset Construction from Archival Image Scans: German Patents (1877-1918)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Niclas Griesshaber, Jochen Streb

**分类**: econ.GN, cs.CV, cs.DL

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**利用多模态LLM从档案图像扫描件构建德国专利历史数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `大型语言模型` `历史文档` `数据集构建` `图像识别` `经济史` `专利数据`

## 📋 核心要点

1. 经济史研究中，历史档案图像数据蕴含丰富信息，但人工标注成本高、效率低，阻碍了大规模数据集的构建。
2. 论文提出了一种基于多模态LLM的自动化数据管道，利用LLM强大的图像理解和文本处理能力，高效提取专利信息。
3. 实验表明，该方法在数据集构建速度和成本上远超人工，且数据质量更高，为经济史研究提供了一种新的数据获取途径。

## 📝 摘要（中文）

本文利用多模态大型语言模型（LLM），具体而言是Gemini-2.5-Pro和Gemini-2.5-Flash-Lite，构建了一个包含306,070项德国专利（1877-1918）的数据集，数据来源于9,562份档案图像扫描件。基准测试初步表明，多模态LLM能够创建比研究助理更高质量的数据集，同时在从图像语料库构建专利数据集时，速度提高了795倍以上，成本降低了205倍。每页嵌入约20到50个专利条目，以双栏格式排列，并以哥特体和罗马字体印刷。主要来源材料的字体和布局复杂性表明，多模态LLM是经济史中数据集构建方式的范式转变。我们开源了基准测试和专利数据集以及基于LLM的数据管道，该管道可以使用LLM辅助编码工具轻松地适应其他图像语料库，从而降低了技术水平较低的研究人员的门槛。最后，我们解释了部署LLM进行历史数据集构建的经济学原理，并推测了对经济史领域的潜在影响。

## 🔬 方法详解

**问题定义**：论文旨在解决从大量历史档案图像扫描件中高效、低成本地提取结构化专利数据的问题。现有方法依赖人工标注，耗时耗力，难以处理大规模数据集。此外，历史文档的字体复杂、排版不规范，进一步增加了人工标注的难度。

**核心思路**：论文的核心思路是利用多模态LLM的强大能力，将图像理解和文本处理相结合，自动化地从图像中提取专利信息。通过训练LLM识别历史文档的布局、字体和内容，实现高效的数据抽取和结构化。

**技术框架**：论文构建了一个基于LLM的数据管道，主要包含以下几个阶段：1) 图像预处理：对档案图像进行清洗、校正等预处理操作，提高图像质量。2) LLM推理：使用多模态LLM（Gemini-2.5-Pro和Gemini-2.5-Flash-Lite）对图像进行分析，识别专利条目，提取关键信息。3) 数据结构化：将提取的信息进行结构化处理，构建专利数据集。4) 数据验证：对提取的数据进行验证和校对，确保数据质量。

**关键创新**：论文的关键创新在于将多模态LLM应用于历史档案图像数据的处理，实现了自动化、高效的数据集构建。与传统OCR方法相比，LLM具有更强的图像理解和文本处理能力，能够更好地处理复杂字体和排版。此外，论文还开源了数据管道和数据集，降低了其他研究人员的使用门槛。

**关键设计**：论文使用了Gemini-2.5-Pro和Gemini-2.5-Flash-Lite两种LLM模型，并针对历史文档的特点进行了微调。具体的技术细节，例如损失函数、网络结构等，论文中没有详细描述，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19675v1/figure-representative-page.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19675v1/figure-patent-entry.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19675v1/figure-RA-interface.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于多模态LLM的数据管道在构建德国专利数据集时，速度比人工提高了795倍以上，成本降低了205倍，并且数据质量更高。这些数据充分证明了多模态LLM在历史数据集构建方面的巨大潜力。

## 🎯 应用场景

该研究成果可广泛应用于历史文献数字化、档案管理、知识图谱构建等领域。通过自动化提取历史文献中的信息，可以加速历史研究进程，为经济史、社会史等领域提供更丰富的数据支持。此外，该方法还可以应用于其他类型的图像数据处理，例如医学影像分析、遥感图像解译等。

## 📄 摘要（原文）

> We leverage multimodal large language models (LLMs) to construct a dataset of 306,070 German patents (1877-1918) from 9,562 archival image scans using our LLM-based pipeline powered by Gemini-2.5-Pro and Gemini-2.5-Flash-Lite. Our benchmarking exercise provides tentative evidence that multimodal LLMs can create higher quality datasets than our research assistants, while also being more than 795 times faster and 205 times cheaper in constructing the patent dataset from our image corpus. About 20 to 50 patent entries are embedded on each page, arranged in a double-column format and printed in Gothic and Roman fonts. The font and layout complexity of our primary source material suggests to us that multimodal LLMs are a paradigm shift in how datasets are constructed in economic history. We open-source our benchmarking and patent datasets as well as our LLM-based data pipeline, which can be easily adapted to other image corpora using LLM-assisted coding tools, lowering the barriers for less technical researchers. Finally, we explain the economics of deploying LLMs for historical dataset construction and conclude by speculating on the potential implications for the field of economic history.

