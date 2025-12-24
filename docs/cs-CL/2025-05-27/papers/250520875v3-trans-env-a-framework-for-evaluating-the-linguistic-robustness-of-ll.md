---
layout: default
title: "Trans-EnV: A Framework for Evaluating the Linguistic Robustness of LLMs Against English Varieties"
---

# Trans-EnV: A Framework for Evaluating the Linguistic Robustness of LLMs Against English Varieties

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20875" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20875v3</a>
  <a href="https://arxiv.org/pdf/2505.20875.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20875v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20875v3', 'Trans-EnV: A Framework for Evaluating the Linguistic Robustness of LLMs Against English Varieties')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiyoung Lee, Seungho Kim, Jieun Han, Jun-Min Lee, Kitaek Kim, Alice Oh, Edward Choi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-27 (更新: 2025-10-09)

**备注**: NeurIPS 2025 Track on Datasets and Benchmarks (27 pages, 6 figures, 16 tables)

**🔗 代码/项目**: [GITHUB](https://github.com/jiyounglee-0523/TransEnV) | [HUGGINGFACE](https://huggingface.co/collections/jiyounglee0523)

---

## 💡 一句话要点

**提出Trans-EnV框架以评估LLMs对英语变体的语言鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `语言鲁棒性` `英语变体` `公平性评估` `自然语言处理` `跨文化交流`

## 📋 核心要点

1. 现有方法主要集中在标准美式英语上，忽视了全球英语变体，导致公平性问题。
2. 论文提出Trans-EnV框架，通过自动转换SAE数据集为多种英语变体，评估LLMs的语言鲁棒性。
3. 实验结果显示，七个LLMs在非标准变体上的准确率下降高达46.3%，揭示了性能差异的严重性。

## 📝 摘要（中文）

大型语言模型（LLMs）主要在标准美式英语（SAE）上进行评估，常常忽视全球英语变体的多样性。这种狭隘的关注可能引发公平性问题，因为在非标准变体上的性能下降可能导致全球用户受益不均。因此，全面评估LLMs在多种非标准英语变体上的语言鲁棒性至关重要。我们提出了Trans-EnV框架，该框架自动将SAE数据集转换为多种英语变体，以评估语言鲁棒性。我们的框架结合了语言学专家知识和LLM基础的转换，确保了语言有效性和可扩展性。通过Trans-EnV，我们将六个基准数据集转换为38种英语变体，并评估了七个最先进的LLMs，结果显示在非标准变体上的准确率下降高达46.3%。这些发现突显了在多样化英语变体中进行全面语言鲁棒性评估的重要性。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在非标准英语变体上的评估不足问题。现有方法主要集中于标准美式英语，导致模型在多样化语言环境中的表现不均衡，可能引发公平性问题。

**核心思路**：论文的核心思路是构建Trans-EnV框架，通过结合语言学专家知识和LLM基础的转换技术，自动将标准美式英语数据集转换为多种英语变体，从而全面评估模型的语言鲁棒性。

**技术框架**：Trans-EnV框架包括两个主要模块：一是基于语言学文献和语料库的变体特征和转换指南的策划，二是利用LLM进行语言有效性和可扩展性的转换。整体流程为：数据集选择→特征提取→变体转换→模型评估。

**关键创新**：最重要的技术创新点在于将语言学知识与LLM技术相结合，形成一种新的评估框架。这种方法不仅提高了评估的全面性，还确保了转换的语言有效性。

**关键设计**：在关键设计上，框架中涉及的参数设置和转换规则经过严格的统计测试和语言学专家的咨询，以确保其有效性和可靠性。

## 📊 实验亮点

实验结果显示，七个最先进的LLMs在非标准英语变体上的准确率下降高达46.3%，揭示了模型在多样性语言环境中的显著性能差异。这一发现强调了在多样化英语变体中进行全面评估的重要性，为未来的研究提供了重要的参考。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、教育技术和跨文化交流等。通过提高LLMs在多样化英语变体上的表现，能够为全球用户提供更公平的语言服务，促进不同文化背景下的沟通与理解。未来，该框架还可以扩展到其他语言和方言的评估中，进一步推动语言模型的公平性和鲁棒性研究。

## 📄 摘要（原文）

> Large Language Models (LLMs) are predominantly evaluated on Standard American English (SAE), often overlooking the diversity of global English varieties. This narrow focus may raise fairness concerns as degraded performance on non-standard varieties can lead to unequal benefits for users worldwide. Therefore, it is critical to extensively evaluate the linguistic robustness of LLMs on multiple non-standard English varieties. We introduce Trans-EnV, a framework that automatically transforms SAE datasets into multiple English varieties to evaluate the linguistic robustness. Our framework combines (1) linguistics expert knowledge to curate variety-specific features and transformation guidelines from linguistic literature and corpora, and (2) LLM-based transformations to ensure both linguistic validity and scalability. Using Trans-EnV, we transform six benchmark datasets into 38 English varieties and evaluate seven state-of-the-art LLMs. Our results reveal significant performance disparities, with accuracy decreasing by up to 46.3% on non-standard varieties. These findings highlight the importance of comprehensive linguistic robustness evaluation across diverse English varieties. Each construction of Trans-EnV was validated through rigorous statistical testing and consultation with a researcher in the field of second language acquisition, ensuring its linguistic validity. Our code and datasets are publicly available at https://github.com/jiyounglee-0523/TransEnV and https://huggingface.co/collections/jiyounglee0523/transenv-681eadb3c0c8cf363b363fb1.

