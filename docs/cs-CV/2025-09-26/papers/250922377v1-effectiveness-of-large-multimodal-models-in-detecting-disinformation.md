---
layout: default
title: "Effectiveness of Large Multimodal Models in Detecting Disinformation: Experimental Results"
---

# Effectiveness of Large Multimodal Models in Detecting Disinformation: Experimental Results

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22377" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22377v1</a>
  <a href="https://arxiv.org/pdf/2509.22377.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22377v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22377v1', 'Effectiveness of Large Multimodal Models in Detecting Disinformation: Experimental Results')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yasmina Kheddache, Marc Lalonde

**分类**: cs.CV

**发布日期**: 2025-09-26

**备注**: 9 pages

---

## 💡 一句话要点

**利用GPT-4o模型，结合优化Prompt工程，解决多模态信息伪造检测难题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `虚假信息检测` `GPT-4o` `Prompt工程` `自然语言处理` `计算机视觉` `深度学习`

## 📋 核心要点

1. 多模态虚假信息检测面临挑战，现有方法难以有效应对文本和图像结合的复杂情况。
2. 利用GPT-4o模型，结合Prompt工程，构建多模态分析框架，实现细粒度的内容分类。
3. 在多个数据集上进行实验，分析GPT-4o模型的优势和局限性，评估预测的稳定性和可靠性。

## 📝 摘要（中文）

本研究旨在探索大型多模态模型（LMMs）在检测和缓解虚假信息方面的潜力，尤其是在文本和图像结合的多模态语境下。我们利用GPT-4o模型，通过优化Prompt工程技术，实现精确和一致的评估。研究贡献包括：开发优化的Prompt，构建多模态分析框架（包含图像和文本预处理），定义六个细粒度的评估标准和置信度自评估机制，在Gossipcop、Politifact、Fakeddit、MMFakeBench和AMMEBA等数据集上进行全面的性能分析，评估模型预测的稳定性和可靠性，并引入基于置信度和变异性的评估方法。本研究为自动多模态虚假信息分析提供了一个稳健且可复现的方法框架。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态虚假信息检测问题，即如何有效地识别和减轻包含文本和图像的虚假信息。现有方法在处理复杂的多模态数据时，往往缺乏足够的准确性和鲁棒性，难以有效应对各种伪造手段。

**核心思路**：论文的核心思路是利用大型多模态模型GPT-4o的强大能力，通过精心设计的Prompt工程，引导模型进行准确和一致的评估。通过将文本和图像信息整合，并结合细粒度的评估标准，提高虚假信息检测的准确性和可靠性。

**技术框架**：整体框架包括以下几个主要阶段：1) 数据预处理：对图像和文本数据进行预处理，以符合GPT-4o模型的token限制。2) Prompt构建：设计优化的Prompt，引导模型进行评估。3) 模型评估：使用六个评估标准对内容进行细粒度分类，并进行置信度自评估。4) 性能分析：在多个数据集上评估模型的性能，并分析其优势和局限性。5) 稳定性评估：通过重复测试评估模型预测的稳定性和可靠性。

**关键创新**：最重要的技术创新点在于Prompt工程的优化和细粒度评估标准的引入。通过优化Prompt，可以更有效地引导模型进行评估，提高检测的准确性。细粒度评估标准可以更全面地评估内容的真实性，并提供更详细的分类结果。

**关键设计**：关键设计包括：1) 图像和文本的预处理方法，确保数据能够被GPT-4o模型有效处理。2) Prompt的设计，包括如何引导模型进行评估，以及如何整合文本和图像信息。3) 六个评估标准的定义，包括内容真实性、来源可靠性、上下文一致性等。4) 置信度自评估机制，用于评估模型对自身预测的信心程度。

## 📊 实验亮点

该研究通过在多个数据集（Gossipcop、Politifact、Fakeddit、MMFakeBench和AMMEBA）上进行实验，全面评估了GPT-4o模型在多模态虚假信息检测方面的性能。实验结果表明，GPT-4o模型在一定程度上能够有效识别虚假信息，但同时也存在一些局限性，例如对某些类型的伪造信息识别能力较弱。研究还通过重复测试评估了模型预测的稳定性和可靠性。

## 🎯 应用场景

该研究成果可应用于社交媒体平台、新闻媒体机构等，用于自动检测和过滤虚假信息，提高信息传播的真实性和可靠性。有助于减少虚假信息对社会的影响，维护公共利益，并为未来的多模态信息处理研究提供参考。

## 📄 摘要（原文）

> The proliferation of disinformation, particularly in multimodal contexts combining text and images, presents a significant challenge across digital platforms. This study investigates the potential of large multimodal models (LMMs) in detecting and mitigating false information. We propose to approach multimodal disinformation detection by leveraging the advanced capabilities of the GPT-4o model. Our contributions include: (1) the development of an optimized prompt incorporating advanced prompt engineering techniques to ensure precise and consistent evaluations; (2) the implementation of a structured framework for multimodal analysis, including a preprocessing methodology for images and text to comply with the model's token limitations; (3) the definition of six specific evaluation criteria that enable a fine-grained classification of content, complemented by a self-assessment mechanism based on confidence levels; (4) a comprehensive performance analysis of the model across multiple heterogeneous datasets Gossipcop, Politifact, Fakeddit, MMFakeBench, and AMMEBA highlighting GPT-4o's strengths and limitations in disinformation detection; (5) an investigation of prediction variability through repeated testing, evaluating the stability and reliability of the model's classifications; and (6) the introduction of confidence-level and variability-based evaluation methods. These contributions provide a robust and reproducible methodological framework for automated multimodal disinformation analysis.

