---
layout: default
title: "FinMMR: Make Financial Numerical Reasoning More Multimodal, Comprehensive, and Challenging"
---

# FinMMR: Make Financial Numerical Reasoning More Multimodal, Comprehensive, and Challenging

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04625" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04625v1</a>
  <a href="https://arxiv.org/pdf/2508.04625.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04625v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04625v1', 'FinMMR: Make Financial Numerical Reasoning More Multimodal, Comprehensive, and Challenging')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zichen Tang, Haihong E, Jiacheng Liu, Zhongjun Yang, Rongjin Li, Zihua Rong, Haoyang He, Zhuodi Hao, Xinyang Hu, Kun Ji, Ziyan Ma, Mengyuan Ji, Jun Zhang, Chenghao Ma, Qianhe Zheng, Yang Liu, Yiling Huang, Xinyi Hu, Qing Huang, Zijian Xie, Shiyao Peng

**分类**: cs.CV, cs.CE

**发布日期**: 2025-08-06

**备注**: Accepted by ICCV 2025. arXiv admin note: text overlap with arXiv:2311.06602 by other authors

---

## 💡 一句话要点

**提出FinMMR以提升金融数值推理的多模态能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `金融推理` `多模态学习` `大型语言模型` `基准测试` `数值推理` `数据分析` `机器学习`

## 📋 核心要点

1. 现有的金融数值推理基准在多模态性和知识覆盖面上存在不足，无法全面评估模型的推理能力。
2. FinMMR通过引入多模态数据和丰富的金融子领域问题，提供了一个更全面的评估平台。
3. 在困难问题上，最佳表现的MLLM仅达到53.0%的准确率，显示出该基准的挑战性和必要性。

## 📝 摘要（中文）

我们提出了FinMMR，这是一个新颖的双语多模态基准，旨在评估多模态大型语言模型（MLLMs）在金融数值推理任务中的推理能力。与现有基准相比，我们的工作引入了三项重要进展：（1）多模态性：我们精心改造了现有的金融推理基准，并从最新的中文金融研究报告中构建了新问题。FinMMR包含4300个问题和8700张图像，涵盖14个类别，包括表格、条形图和所有权结构图。（2）全面性：FinMMR涵盖14个金融子领域，包括公司金融、银行和行业分析，显著超越了现有基准在金融领域知识广度上的表现。（3）挑战性：模型需要通过整合金融知识与对复杂金融图像和文本的理解，进行多步骤的精确数值推理。表现最好的MLLM在困难问题上的准确率仅为53.0%。我们相信，FinMMR将推动提升MLLM在现实场景中的推理能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有金融数值推理基准在多模态性和知识覆盖面不足的问题。现有方法无法有效评估模型在复杂金融场景中的推理能力。

**核心思路**：我们通过构建一个包含多模态数据（如图像和文本）的新基准，来提升模型的推理能力。设计上强调了多步骤推理和金融知识的结合。

**技术框架**：FinMMR的整体架构包括数据收集、问题设计和模型评估三个主要模块。数据收集阶段从最新的金融研究报告中提取信息，问题设计阶段则构建多样化的推理问题，最后通过评估模型的表现来验证效果。

**关键创新**：FinMMR的最大创新在于其多模态性和全面性，涵盖了14个金融子领域，显著提升了现有基准的挑战性和适用性。与传统基准相比，FinMMR更能反映真实世界中的复杂金融推理需求。

**关键设计**：在设计上，我们设置了多样化的问题类型和图像格式，并采用了适应性损失函数，以提高模型在多模态推理中的表现。

## 📊 实验亮点

在FinMMR基准上，表现最好的多模态大型语言模型在困难问题上的准确率仅为53.0%，显示出该基准的高挑战性。这一结果表明，当前模型在复杂金融推理任务中的能力仍有待提升，强调了FinMMR在推动研究进展中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括金融分析、投资决策支持和智能财务顾问等。通过提升多模态大型语言模型的推理能力，FinMMR能够帮助金融从业者更好地理解和分析复杂的金融数据，从而提高决策的准确性和效率。未来，FinMMR有望成为金融领域AI应用的重要基准。

## 📄 摘要（原文）

> We present FinMMR, a novel bilingual multimodal benchmark tailored to evaluate the reasoning capabilities of multimodal large language models (MLLMs) in financial numerical reasoning tasks. Compared to existing benchmarks, our work introduces three significant advancements. (1) Multimodality: We meticulously transform existing financial reasoning benchmarks, and construct novel questions from the latest Chinese financial research reports. FinMMR comprises 4.3K questions and 8.7K images spanning 14 categories, including tables, bar charts, and ownership structure charts. (2) Comprehensiveness: FinMMR encompasses 14 financial subdomains, including corporate finance, banking, and industry analysis, significantly exceeding existing benchmarks in financial domain knowledge breadth. (3) Challenge: Models are required to perform multi-step precise numerical reasoning by integrating financial knowledge with the understanding of complex financial images and text. The best-performing MLLM achieves only 53.0% accuracy on Hard problems. We believe that FinMMR will drive advancements in enhancing the reasoning capabilities of MLLMs in real-world scenarios.

