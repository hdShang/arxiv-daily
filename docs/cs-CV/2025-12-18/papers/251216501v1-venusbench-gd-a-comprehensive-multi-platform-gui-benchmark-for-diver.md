---
layout: default
title: "VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks"
---

# VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16501" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16501v1</a>
  <a href="https://arxiv.org/pdf/2512.16501.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16501v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16501v1', 'VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Beitong Zhou, Zhexiao Huang, Yuan Guo, Zhangxuan Gu, Tianyu Xia, Zichen Luo, Fei Tang, Dehan Kong, Yanyi Shang, Suling Ou, Zhenlin Guo, Changhua Meng, Shuheng Shen

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出VenusBench-GD，一个全面的多平台GUI基准，用于评估多样化的Grounding任务。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GUI grounding` `多平台基准` `用户界面` `多模态学习` `分层任务` `数据集构建` `人机交互`

## 📋 核心要点

1. 现有GUI grounding基准数据量不足、领域覆盖窄，或过度关注单一平台，限制了GUI代理的开发。
2. VenusBench-GD构建大规模跨平台GUI基准，包含丰富的UI元素和标注数据，并提出分层任务分类法。
3. 实验表明通用多模态模型在基础任务上表现优异，但高级任务仍需GUI专用模型，存在过拟合问题。

## 📝 摘要（中文）

GUI grounding是构建强大GUI代理的关键组成部分。然而，现有的grounding基准存在显著的局限性：它们要么提供的数据量不足且领域覆盖范围狭窄，要么过度关注单一平台并需要高度专业的领域知识。本文提出了VenusBench-GD，这是一个全面的、双语的GUI grounding基准，涵盖多个平台，能够对真实世界的应用程序进行分层评估。VenusBench-GD的贡献如下：（i）引入了一个大规模、跨平台的基准，具有广泛的应用程序覆盖、多样的UI元素和丰富的标注数据；（ii）建立了一个高质量的数据构建流程，用于grounding任务，实现了比现有基准更高的标注准确率；（iii）通过提出一个分层任务分类法，扩展了元素grounding的范围，该分类法将grounding分为基本和高级类别，包含六个不同的子任务，旨在从互补的角度评估模型。实验结果揭示了关键的见解：通用多模态模型现在在基本grounding任务上与专门的GUI模型相匹配甚至超越。相比之下，高级任务仍然偏爱GUI专用模型，尽管它们表现出显著的过拟合和较差的鲁棒性。这些结果强调了全面、多层评估框架的必要性。

## 🔬 方法详解

**问题定义**：论文旨在解决现有GUI grounding基准数据集不足、领域覆盖范围有限以及平台单一的问题。现有方法难以有效评估和提升GUI代理在真实世界应用中的grounding能力，尤其是在跨平台和复杂交互场景下。现有基准的标注质量也存在问题，影响了模型训练和评估的可靠性。

**核心思路**：论文的核心思路是构建一个大规模、跨平台、高质量的GUI grounding基准数据集，并提出一个分层的任务分类体系，从而更全面地评估模型的grounding能力。通过引入多样化的UI元素和应用场景，以及高质量的人工标注，提高数据集的代表性和可靠性。分层任务分类法旨在区分模型在基础和高级grounding任务上的表现，从而更深入地了解模型的优势和不足。

**技术框架**：VenusBench-GD的构建流程主要包括以下几个阶段：1) 数据收集：从多个平台（例如Android、iOS、Web）收集GUI应用程序的截图和UI元素信息。2) 数据标注：对UI元素进行详细的标注，包括元素类型、位置、文本内容等。采用高质量的标注流程，确保标注的准确性和一致性。3) 任务定义：将grounding任务分为基本和高级类别，并定义六个不同的子任务，例如元素定位、关系推理等。4) 基准测试：在VenusBench-GD上评估现有模型的性能，并分析实验结果。

**关键创新**：VenusBench-GD的关键创新点在于：1) 大规模跨平台数据集：提供了比现有基准更广泛的应用程序覆盖和更多样化的UI元素。2) 高质量数据构建流程：通过严格的标注流程和质量控制，提高了数据集的标注准确率。3) 分层任务分类法：将grounding任务分为基本和高级类别，从而更全面地评估模型的grounding能力。

**关键设计**：VenusBench-GD的数据集包含多种类型的UI元素，例如按钮、文本框、图像等。标注信息包括元素的类型、位置、文本内容、父子关系等。分层任务分类法包括以下六个子任务：1) 元素定位：根据文本描述定位UI元素。2) 属性识别：识别UI元素的属性，例如颜色、大小等。3) 关系推理：推理UI元素之间的关系，例如包含、相邻等。4) 状态理解：理解UI元素的状态，例如激活、禁用等。5) 动作预测：预测用户在GUI上的下一步动作。6) 复杂交互：处理涉及多个UI元素的复杂交互。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16501v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16501v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16501v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，通用多模态模型在基本grounding任务上与GUI专用模型性能相当甚至超越，但在高级任务上，GUI专用模型仍然更胜一筹，但存在过拟合和鲁棒性问题。VenusBench-GD的评估结果揭示了现有模型在不同类型grounding任务上的优缺点，为未来的研究方向提供了指导。

## 🎯 应用场景

VenusBench-GD可应用于开发更智能、更强大的GUI代理，例如自动化测试工具、辅助技术和人机交互系统。该基准能够促进跨平台GUI理解和交互的研究，帮助提升用户体验，并为残疾人士提供更好的辅助功能。未来，该研究可扩展到更复杂的GUI环境，并支持更高级的交互任务。

## 📄 摘要（原文）

> GUI grounding is a critical component in building capable GUI agents. However, existing grounding benchmarks suffer from significant limitations: they either provide insufficient data volume and narrow domain coverage, or focus excessively on a single platform and require highly specialized domain knowledge. In this work, we present VenusBench-GD, a comprehensive, bilingual benchmark for GUI grounding that spans multiple platforms, enabling hierarchical evaluation for real-word applications. VenusBench-GD contributes as follows: (i) we introduce a large-scale, cross-platform benchmark with extensive coverage of applications, diverse UI elements, and rich annotated data, (ii) we establish a high-quality data construction pipeline for grounding tasks, achieving higher annotation accuracy than existing benchmarks, and (iii) we extend the scope of element grounding by proposing a hierarchical task taxonomy that divides grounding into basic and advanced categories, encompassing six distinct subtasks designed to evaluate models from complementary perspectives. Our experimental findings reveal critical insights: general-purpose multimodal models now match or even surpass specialized GUI models on basic grounding tasks. In contrast, advanced tasks, still favor GUI-specialized models, though they exhibit significant overfitting and poor robustness. These results underscore the necessity of comprehensive, multi-tiered evaluation frameworks.

