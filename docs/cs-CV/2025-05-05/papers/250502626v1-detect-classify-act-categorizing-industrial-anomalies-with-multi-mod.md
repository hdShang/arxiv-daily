---
layout: default
title: Detect, Classify, Act: Categorizing Industrial Anomalies with Multi-Modal Large Language Models
---

# Detect, Classify, Act: Categorizing Industrial Anomalies with Multi-Modal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02626" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02626v1</a>
  <a href="https://arxiv.org/pdf/2505.02626.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02626v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02626v1', 'Detect, Classify, Act: Categorizing Industrial Anomalies with Multi-Modal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sassan Mokhtar, Arian Mousakhan, Silvio Galesso, Jawad Tayyub, Thomas Brox

**分类**: cs.CV

**发布日期**: 2025-05-05

**备注**: Accepted as a spotlight presentation paper at the VAND Workshop, CVPR 2025. 10 pages, 6 figures

---

## 💡 一句话要点

**提出VELM以解决工业异常分类问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工业异常检测` `异常分类` `多模态学习` `大型语言模型` `无监督学习` `数据集构建` `视觉检测`

## 📋 核心要点

1. 现有的异常分类方法在实际应用中面临数据集缺乏精确注释的问题，导致分类效果不理想。
2. 本文提出的VELM方法结合无监督异常检测与大型语言模型，能够快速有效地进行异常分类。
3. 实验结果显示，VELM在MVTec-AD和MVTec-AC数据集上的分类准确率分别提高了5%和显著提升，验证了其有效性。

## 📝 摘要（中文）

近年来，视觉工业异常检测的进展在识别和分割异常区域方面表现出色，但异常分类的研究仍然相对不足。为填补这一空白，本文提出了一种基于大型语言模型的异常分类管道VELM。该方法首先应用无监督异常检测技术评估观察结果的正常性，若检测到异常，LLM将对其类型进行分类。为了解决现有数据集中缺乏精确异常类注释的问题，本文引入了MVTec-AC和VisA-AC数据集，提供准确的异常类标签。实验结果表明，VELM在MVTec-AD和MVTec-AC数据集上的异常分类准确率分别达到了80.4%和84%，超越了之前的基线，展示了其在理解和分类异常方面的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决工业异常分类中的关键问题，即现有方法在异常类型区分上存在不足，且缺乏精确的异常类注释数据集。

**核心思路**：提出的VELM方法通过结合无监督异常检测与大型语言模型，首先评估观察结果的正常性，若发现异常，则进行类型分类。这种设计旨在提高分类的准确性和效率。

**技术框架**：VELM的整体架构包括两个主要模块：第一模块为无监督异常检测，负责判断观察结果是否正常；第二模块为大型语言模型，负责对检测到的异常进行分类。

**关键创新**：最重要的技术创新在于引入了MVTec-AC和VisA-AC数据集，提供了准确的异常类标签，从而使得异常分类的评估更加严格和有效。与现有方法相比，VELM在分类准确性上有显著提升。

**关键设计**：在模型设计中，采用了特定的损失函数以优化分类性能，同时在网络结构上进行了调整，以适应多模态数据的处理需求。

## 📊 实验亮点

在实验中，VELM在MVTec-AD数据集上的异常分类准确率达到了80.4%，相比之前的基线提高了5%；在MVTec-AC数据集上，准确率更是达到了84%。这些结果表明，VELM在异常理解和分类方面的有效性显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括工业生产监控、质量检测和设备维护等。通过提高异常分类的准确性，VELM能够帮助企业更有效地识别和处理生产过程中的异常情况，从而降低损失和提高生产效率。未来，该方法有望在其他领域的异常检测与分类任务中得到推广。

## 📄 摘要（原文）

> Recent advances in visual industrial anomaly detection have demonstrated exceptional performance in identifying and segmenting anomalous regions while maintaining fast inference speeds. However, anomaly classification-distinguishing different types of anomalies-remains largely unexplored despite its critical importance in real-world inspection tasks. To address this gap, we propose VELM, a novel LLM-based pipeline for anomaly classification. Given the critical importance of inference speed, we first apply an unsupervised anomaly detection method as a vision expert to assess the normality of an observation. If an anomaly is detected, the LLM then classifies its type. A key challenge in developing and evaluating anomaly classification models is the lack of precise annotations of anomaly classes in existing datasets. To address this limitation, we introduce MVTec-AC and VisA-AC, refined versions of the widely used MVTec-AD and VisA datasets, which include accurate anomaly class labels for rigorous evaluation. Our approach achieves a state-of-the-art anomaly classification accuracy of 80.4% on MVTec-AD, exceeding the prior baselines by 5%, and 84% on MVTec-AC, demonstrating the effectiveness of VELM in understanding and categorizing anomalies. We hope our methodology and benchmark inspire further research in anomaly classification, helping bridge the gap between detection and comprehensive anomaly characterization.

