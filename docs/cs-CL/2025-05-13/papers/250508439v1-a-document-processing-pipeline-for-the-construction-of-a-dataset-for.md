---
layout: default
title: A document processing pipeline for the construction of a dataset for topic modeling based on the judgments of the Italian Supreme Court
---

# A document processing pipeline for the construction of a dataset for topic modeling based on the judgments of the Italian Supreme Court

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08439" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08439v1</a>
  <a href="https://arxiv.org/pdf/2505.08439.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08439v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08439v1', 'A document processing pipeline for the construction of a dataset for topic modeling based on the judgments of the Italian Supreme Court')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matteo Marulli, Glauco Panattoni, Marco Bertini

**分类**: cs.CL

**发布日期**: 2025-05-13

**备注**: 51 pages

---

## 💡 一句话要点

**提出文档处理管道以构建意大利最高法院判决主题建模数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `主题建模` `法律文本分析` `光学字符识别` `文档处理` `数据集构建` `深度学习` `自然语言处理`

## 📋 核心要点

1. 现有的意大利法律研究缺乏公共数据集，限制了对最高法院判决的主题分析。
2. 本文提出了一种文档处理管道，集成了文档布局分析、光学字符识别和文本匿名化，优化了数据集的构建。
3. 实验结果显示，所提方法在主题建模的多样性和一致性得分上显著优于传统OCR方法。

## 📝 摘要（中文）

意大利法律研究中的主题建模受到缺乏公共数据集的限制，影响了对最高法院判决法律主题的分析。为了解决这一问题，本文开发了一种文档处理管道，生成了优化用于主题建模的匿名数据集。该管道集成了文档布局分析（YOLOv8x）、光学字符识别（OCR）和文本匿名化。实验结果显示，DLA模块在mAP@50上达到了0.964，OCR检测器在mAP@50-95上达到了0.9022，文本识别器（TrOCR）的字符错误率为0.0047，单词错误率为0.0248。与仅使用OCR的方法相比，我们的数据集在多样性得分和一致性得分上分别提高至0.6198和0.6638。我们应用BERTopic提取主题，并使用大型语言模型生成标签和摘要，输出结果经过领域专家的评估。Claude Sonnet 3.7在标签生成和摘要方面分别达到了0.8119和0.9130的BERTScore F1值。

## 🔬 方法详解

**问题定义**：本文旨在解决意大利法律研究中缺乏公共数据集的问题，现有方法无法有效支持对最高法院判决的主题建模分析。

**核心思路**：通过开发一个文档处理管道，集成多种技术以生成优化的匿名数据集，从而提高主题建模的效果。

**技术框架**：该管道包括三个主要模块：文档布局分析（使用YOLOv8x）、光学字符识别（OCR）和文本匿名化。文档首先经过布局分析，提取文本区域，然后进行OCR处理，最后对识别出的文本进行匿名化处理。

**关键创新**：最重要的创新在于将文档布局分析与OCR和文本匿名化结合，形成一个高效的处理管道，显著提高了数据集的质量和主题建模的效果。

**关键设计**：在DLA模块中，mAP@50达到0.964，OCR检测器的mAP@50-95为0.9022，文本识别器TrOCR的字符错误率为0.0047，单词错误率为0.0248，这些参数设置确保了高精度的文本提取和识别。

## 📊 实验亮点

实验结果显示，所提文档处理管道在主题建模方面显著优于传统OCR方法，数据集的多样性得分为0.6198，一致性得分为0.6638。Claude Sonnet 3.7在标签生成和摘要方面分别达到了0.8119和0.9130的BERTScore F1值，表明该方法在实际应用中具有良好的效果。

## 🎯 应用场景

该研究的潜在应用领域包括法律研究、司法分析和人工智能辅助决策等。通过提供高质量的法律文本数据集，研究者和法律从业者可以更深入地分析法律主题，推动法律科技的发展，并为未来的法律智能系统奠定基础。

## 📄 摘要（原文）

> Topic modeling in Italian legal research is hindered by the lack of public datasets, limiting the analysis of legal themes in Supreme Court judgments. To address this, we developed a document processing pipeline that produces an anonymized dataset optimized for topic modeling.
>   The pipeline integrates document layout analysis (YOLOv8x), optical character recognition, and text anonymization. The DLA module achieved a mAP@50 of 0.964 and a mAP@50-95 of 0.800. The OCR detector reached a mAP@50-95 of 0.9022, and the text recognizer (TrOCR) obtained a character error rate of 0.0047 and a word error rate of 0.0248. Compared to OCR-only methods, our dataset improved topic modeling with a diversity score of 0.6198 and a coherence score of 0.6638.
>   We applied BERTopic to extract topics and used large language models to generate labels and summaries. Outputs were evaluated against domain expert interpretations. Claude Sonnet 3.7 achieved a BERTScore F1 of 0.8119 for labeling and 0.9130 for summarization.

