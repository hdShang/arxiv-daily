---
layout: default
title: "LABELING COPILOT: A Deep Research Agent for Automated Data Curation in Computer Vision"
---

# LABELING COPILOT: A Deep Research Agent for Automated Data Curation in Computer Vision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22631" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22631v1</a>
  <a href="https://arxiv.org/pdf/2509.22631.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22631v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22631v1', 'LABELING COPILOT: A Deep Research Agent for Automated Data Curation in Computer Vision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Debargha Ganguly, Sumit Kumar, Ishwar Balappanawar, Weicong Chen, Shashank Kambhatla, Srinivasan Iyengar, Shivkumar Kalyanaraman, Ponnurangam Kumaraguru, Vipin Chaudhary

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出Labeling Copilot，用于计算机视觉中自动化数据标注的深度研究Agent。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据标注` `计算机视觉` `深度学习` `Agent` `主动学习` `多模态学习` `目标检测`

## 📋 核心要点

1. 高质量、特定领域数据集的标注是部署鲁棒视觉系统的主要瓶颈，需要在数据质量、多样性和成本之间进行权衡。
2. Labeling Copilot通过多模态大语言模型驱动的Agent，协调校准发现、可控合成和共识标注三个模块，实现自动化数据标注。
3. 实验表明，Labeling Copilot在COCO和Open Images数据集上表现出色，并在计算效率方面优于现有方法。

## 📝 摘要（中文）

本文介绍Labeling Copilot，这是首个用于计算机视觉的数据标注深度研究Agent。该Agent由大型多模态语言模型驱动的中心协调器组成，通过多步骤推理来执行跨三个核心功能的专用工具：（1）校准发现：从大型存储库中获取相关的、分布内的数据；（2）可控合成：为罕见场景生成具有鲁棒过滤的新数据；（3）共识标注：通过结合非极大值抑制和投票的新型共识机制，协调多个基础模型以产生准确的标签。大规模验证证明了Labeling Copilot组件的有效性。共识标注模块擅长目标发现：在密集的COCO数据集上，它平均每张图像产生14.2个候选提议，几乎是7.4个真实目标的二倍，最终标注的mAP达到37.1%。在网络规模的Open Images数据集上，它克服了极端的类别不平衡，发现了903个新的边界框类别，将其能力扩展到超过1500个。同时，我们的校准发现工具在1000万样本规模下进行了测试，其主动学习策略比具有同等样本效率的替代方案计算效率高出40倍。这些实验验证了具有优化、可扩展工具的Agent工作流程为标注工业规模数据集提供了强大的基础。

## 🔬 方法详解

**问题定义**：论文旨在解决计算机视觉领域中，大规模无标注数据集中高效、高质量数据标注的问题。现有方法通常面临数据质量不高、标注成本过高、难以处理长尾分布等挑战。

**核心思路**：论文的核心思路是构建一个基于Agent的自动化数据标注系统，该系统能够像研究人员一样，通过多步骤推理和工具调用，自主地完成数据发现、数据生成和数据标注等任务。这种Agentic的方法旨在提高标注效率、降低标注成本，并提升标注质量。

**技术框架**：Labeling Copilot的整体架构包含一个中心协调器Agent和三个核心模块：校准发现（Calibrated Discovery）、可控合成（Controllable Synthesis）和共识标注（Consensus Annotation）。中心协调器Agent负责任务分解、工具选择和结果整合。校准发现模块从大型数据集中筛选出相关的数据样本。可控合成模块生成罕见场景下的数据样本，以增强数据集的多样性。共识标注模块通过集成多个基础模型的预测结果，生成高质量的标注。

**关键创新**：论文的关键创新在于提出了一个完整的、可扩展的Agentic数据标注框架，并针对每个模块设计了专门的优化策略。共识标注模块采用了一种新颖的共识机制，结合了非极大值抑制和投票策略，能够有效地提高标注的准确性。校准发现模块采用主动学习策略，显著提高了样本效率。

**关键设计**：在共识标注模块中，论文采用了非极大值抑制（NMS）来减少冗余的候选框，并使用投票策略来集成不同模型的预测结果。在校准发现模块中，论文设计了一种主动学习策略，通过选择信息量最大的样本进行标注，从而提高样本效率。具体的参数设置和损失函数等技术细节在论文正文中进行了详细描述。

## 📊 实验亮点

实验结果表明，Labeling Copilot在COCO数据集上实现了37.1%的mAP，并且在Open Images数据集上发现了903个新的边界框类别。校准发现模块的主动学习策略比其他方法计算效率高出40倍。这些结果验证了Labeling Copilot在数据标注方面的有效性和效率。

## 🎯 应用场景

Labeling Copilot可应用于各种计算机视觉任务，例如目标检测、图像分割和图像分类。它可以帮助研究人员和工程师快速构建高质量的训练数据集，从而加速视觉系统的开发和部署。该系统尤其适用于需要处理大规模、长尾分布数据的场景，例如自动驾驶、智能安防和医疗影像分析等。

## 📄 摘要（原文）

> Curating high-quality, domain-specific datasets is a major bottleneck for deploying robust vision systems, requiring complex trade-offs between data quality, diversity, and cost when researching vast, unlabeled data lakes. We introduce Labeling Copilot, the first data curation deep research agent for computer vision. A central orchestrator agent, powered by a large multimodal language model, uses multi-step reasoning to execute specialized tools across three core capabilities: (1) Calibrated Discovery sources relevant, in-distribution data from large repositories; (2) Controllable Synthesis generates novel data for rare scenarios with robust filtering; and (3) Consensus Annotation produces accurate labels by orchestrating multiple foundation models via a novel consensus mechanism incorporating non-maximum suppression and voting. Our large-scale validation proves the effectiveness of Labeling Copilot's components. The Consensus Annotation module excels at object discovery: on the dense COCO dataset, it averages 14.2 candidate proposals per image-nearly double the 7.4 ground-truth objects-achieving a final annotation mAP of 37.1%. On the web-scale Open Images dataset, it navigated extreme class imbalance to discover 903 new bounding box categories, expanding its capability to over 1500 total. Concurrently, our Calibrated Discovery tool, tested at a 10-million sample scale, features an active learning strategy that is up to 40x more computationally efficient than alternatives with equivalent sample efficiency. These experiments validate that an agentic workflow with optimized, scalable tools provides a robust foundation for curating industrial-scale datasets.

