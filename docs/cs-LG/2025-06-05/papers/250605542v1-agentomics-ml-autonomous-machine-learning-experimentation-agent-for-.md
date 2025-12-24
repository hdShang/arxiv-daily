---
layout: default
title: "Agentomics-ML: Autonomous Machine Learning Experimentation Agent for Genomic and Transcriptomic Data"
---

# Agentomics-ML: Autonomous Machine Learning Experimentation Agent for Genomic and Transcriptomic Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05542" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05542v1</a>
  <a href="https://arxiv.org/pdf/2506.05542.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05542v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05542v1', 'Agentomics-ML: Autonomous Machine Learning Experimentation Agent for Genomic and Transcriptomic Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vlastimil Martinek, Andrea Gariboldi, Dimosthenis Tzimotoudis, Aitor Alberdi Escudero, Edward Blake, David Cechak, Luke Cassar, Alessandro Balestrucci, Panagiotis Alexiou

**分类**: cs.LG, cs.MA

**发布日期**: 2025-06-05

**🔗 代码/项目**: [GITHUB](https://github.com/BioGeMT/Agentomics-ML)

---

## 💡 一句话要点

**提出Agentomics-ML以解决生物数据自动化建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器学习` `生物数据` `自动化建模` `基因组学` `转录组学` `反馈机制` `自主代理` `性能优化`

## 📋 核心要点

1. 现有的机器学习方法在处理异质计算生物数据集时，面临着泛化能力不足和成功率低的问题。
2. Agentomics-ML通过自主交互和反馈机制，自动化整个机器学习实验过程，从而提高模型的泛化能力和成功率。
3. 在多个基准数据集上评估后，Agentomics-ML在泛化和成功率上均优于现有的最先进方法，并在某些数据集上达到了最先进的性能。

## 📝 摘要（中文）

机器学习和深度学习方法的应用已在分子医学领域引发了革命，尤其是在基因组学、转录组学、药物发现和生物系统建模方面。生物数据集的数量、模态和异质性不断增加，迫切需要能够生成可推广预测模型的自动化方法。本文提出了Agentomics-ML，一个完全自主的基于代理的系统，旨在生成分类模型及其可重复训练和推理所需的文件。该方法遵循预定义的机器学习实验过程，通过Bash与文件系统反复交互以完成各个步骤。实验结果表明，Agentomics-ML在多个基因组和转录组基准数据集上优于现有的代理方法，尽管领域专家构建的最先进模型在绝对性能上仍占优势，但Agentomics-ML缩小了完全自主系统的差距。

## 🔬 方法详解

**问题定义**：本文旨在解决现有机器学习方法在处理异质生物数据集时的泛化能力不足和成功率低的问题。现有方法在面对复杂的生物数据时，往往无法有效生成可推广的模型。

**核心思路**：Agentomics-ML的核心思路是通过自主代理系统自动化整个机器学习实验过程，利用反馈机制不断优化模型的训练和验证步骤，从而提高模型的性能和泛化能力。

**技术框架**：该方法的整体架构包括多个模块：首先是数据准备和预处理模块，然后是模型训练和验证模块，最后是反馈和调整模块。系统通过Bash脚本与文件系统交互，完成各个步骤的自动化。

**关键创新**：Agentomics-ML的主要创新在于其完全自主的实验过程和反馈机制，能够在每次实验后提供可操作的建议，从而不断改进模型的表现。这种设计使得系统在处理复杂的生物数据时，能够更好地适应不同的数据特性。

**关键设计**：在技术细节上，Agentomics-ML使用了特定的损失函数和超参数设置，以优化模型的训练过程。同时，系统设计了反思步骤，通过分析训练和验证指标，识别过拟合等问题，并生成相应的调整建议。

## 📊 实验亮点

在多个基准数据集上的实验结果显示，Agentomics-ML在泛化能力和成功率上均优于现有的最先进代理方法，尤其在某一基准数据集上达到了最先进的性能。这表明该系统在完全自主的机器学习实验中具有显著的优势，缩小了与领域专家构建模型之间的性能差距。

## 🎯 应用场景

Agentomics-ML的潜在应用领域包括基因组学、转录组学和药物发现等生物医学研究。其自动化建模能力可以大大提高研究效率，降低对领域专家的依赖，从而加速生物数据分析和新药研发的进程。未来，该系统有望在更广泛的生物信息学领域中得到应用，推动个性化医疗和精准医学的发展。

## 📄 摘要（原文）

> The adoption of machine learning (ML) and deep learning methods has revolutionized molecular medicine by driving breakthroughs in genomics, transcriptomics, drug discovery, and biological systems modeling. The increasing quantity, multimodality, and heterogeneity of biological datasets demand automated methods that can produce generalizable predictive models. Recent developments in large language model-based agents have shown promise for automating end-to-end ML experimentation on structured benchmarks. However, when applied to heterogeneous computational biology datasets, these methods struggle with generalization and success rates. Here, we introduce Agentomics-ML, a fully autonomous agent-based system designed to produce a classification model and the necessary files for reproducible training and inference. Our method follows predefined steps of an ML experimentation process, repeatedly interacting with the file system through Bash to complete individual steps. Once an ML model is produced, training and validation metrics provide scalar feedback to a reflection step to identify issues such as overfitting. This step then creates verbal feedback for future iterations, suggesting adjustments to steps such as data representation, model architecture, and hyperparameter choices. We have evaluated Agentomics-ML on several established genomic and transcriptomic benchmark datasets and show that it outperforms existing state-of-the-art agent-based methods in both generalization and success rates. While state-of-the-art models built by domain experts still lead in absolute performance on the majority of the computational biology datasets used in this work, Agentomics-ML narrows the gap for fully autonomous systems and achieves state-of-the-art performance on one of the used benchmark datasets. The code is available at https://github.com/BioGeMT/Agentomics-ML.

