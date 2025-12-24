---
layout: default
title: "MME-SCI: A Comprehensive and Challenging Science Benchmark for Multimodal Large Language Models"
---

# MME-SCI: A Comprehensive and Challenging Science Benchmark for Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13938" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13938v1</a>
  <a href="https://arxiv.org/pdf/2508.13938.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13938v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13938v1', 'MME-SCI: A Comprehensive and Challenging Science Benchmark for Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiacheng Ruan, Dan Jiang, Xian Gao, Ting Liu, Yuzhuo Fu, Yangyang Kang

**分类**: cs.CL, cs.CV

**发布日期**: 2025-08-19

**备注**: 9 pages, 6 figures, work in progress

**🔗 代码/项目**: [GITHUB](https://github.com/JCruan519/MME-SCI)

---

## 💡 一句话要点

**提出MME-SCI以解决多模态大语言模型评估中的关键挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `科学评估` `推理能力` `多语言支持` `知识点注释`

## 📋 核心要点

1. 现有科学领域的评估基准在多语言推理能力、模态覆盖和知识点注释方面存在不足。
2. 本文提出MME-SCI基准，通过收集高质量问答对，覆盖多个学科和语言，提升评估的全面性和挑战性。
3. 在对16个开源模型和4个闭源模型的实验中，MME-SCI显示出显著的挑战性，模型在各学科的准确率普遍较低。

## 📝 摘要（中文）

近年来，多模态大语言模型（MLLMs）在各个领域取得了显著进展，相应的评估基准也在不断完善。然而，现有基准在科学领域评估模型推理能力时面临三大挑战：1）多语言场景下模型推理能力评估不足；2）对MLLMs的综合模态覆盖评估不够；3）科学知识点缺乏细粒度注释。为了解决这些问题，本文提出了MME-SCI，一个全面且具有挑战性的基准，收集了1,019对高质量的问答对，涵盖数学、物理、化学和生物四个学科，并支持中文、英文、法文、西班牙文和日文五种语言。实验结果表明，MME-SCI对现有MLLMs具有广泛的挑战性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态大语言模型评估基准在多语言推理、模态覆盖和科学知识细粒度注释方面的不足。现有方法未能全面评估模型的推理能力和知识掌握情况。

**核心思路**：提出MME-SCI基准，通过精心收集多学科的高质量问答对，涵盖多种语言，旨在提供一个更具挑战性的评估框架，以全面评估MLLMs的能力。

**技术框架**：MME-SCI基准包含三个评估模式，涉及数学、物理、化学和生物四个学科，支持中文、英文、法文、西班牙文和日文五种语言。整体流程包括数据收集、问答对构建和模型评估三个主要阶段。

**关键创新**：MME-SCI的创新在于其多语言支持和细粒度知识点注释，使得评估更具深度和广度，能够揭示模型在特定领域的弱点。与现有基准相比，MME-SCI提供了更高的挑战性和更全面的评估视角。

**关键设计**：在问答对的构建中，采用了高质量的科学知识点，并确保覆盖不同语言的表达方式。评估过程中，使用了多种模型进行对比，确保结果的可靠性和有效性。实验中还考虑了不同学科的难度差异，确保评估的公平性。

## 📊 实验亮点

在对16个开源模型和4个闭源模型的实验中，MME-SCI显示出显著的挑战性。例如，在图像仅评估模式下，o4-mini在数学、物理、化学和生物的准确率分别仅为52.11%、24.73%、36.57%和29.80%，显示出相比现有基准更高的难度水平。

## 🎯 应用场景

MME-SCI基准的提出为多模态大语言模型在科学领域的应用提供了新的评估工具，能够帮助研究人员更好地理解模型的推理能力和知识掌握情况。未来，该基准有望推动科学教育、智能问答系统和跨语言信息检索等领域的发展。

## 📄 摘要（原文）

> Recently, multimodal large language models (MLLMs) have achieved significant advancements across various domains, and corresponding evaluation benchmarks have been continuously refined and improved. In this process, benchmarks in the scientific domain have played an important role in assessing the reasoning capabilities of MLLMs. However, existing benchmarks still face three key challenges: 1) Insufficient evaluation of models' reasoning abilities in multilingual scenarios; 2) Inadequate assessment of MLLMs' comprehensive modality coverage; 3) Lack of fine-grained annotation of scientific knowledge points. To address these gaps, we propose MME-SCI, a comprehensive and challenging benchmark. We carefully collected 1,019 high-quality question-answer pairs, which involve 3 distinct evaluation modes. These pairs cover four subjects, namely mathematics, physics, chemistry, and biology, and support five languages: Chinese, English, French, Spanish, and Japanese. We conducted extensive experiments on 16 open-source models and 4 closed-source models, and the results demonstrate that MME-SCI is widely challenging for existing MLLMs. For instance, under the Image-only evaluation mode, o4-mini achieved accuracy of only 52.11%, 24.73%, 36.57%, and 29.80% in mathematics, physics, chemistry, and biology, respectively, indicating a significantly higher difficulty level compared to existing benchmarks. More importantly, using MME-SCI's multilingual and fine-grained knowledge attributes, we analyzed existing models' performance in depth and identified their weaknesses in specific domains. The Data and Evaluation Code are available at https://github.com/JCruan519/MME-SCI.

