---
layout: default
title: VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks
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

**关键词**: `GUI grounding` `基准数据集` `多平台` `多模态学习` `分层任务` `用户界面` `人工智能`

## 📋 核心要点

1. 现有GUI grounding基准数据集规模小、领域窄，或过于关注单平台，限制了GUI代理的发展。
2. VenusBench-GD构建了一个大规模、跨平台、双语的GUI grounding基准，并设计了分层任务分类法。
3. 实验表明，通用多模态模型在基本任务上表现出色，但高级任务仍需专用模型，且存在过拟合问题。

## 📝 摘要（中文）

GUI grounding是构建强大GUI代理的关键组成部分。然而，现有的grounding基准存在显著局限性：它们要么提供的数据量不足且领域覆盖范围狭窄，要么过度关注单一平台并需要高度专业化的领域知识。本文提出了VenusBench-GD，这是一个全面的、双语的GUI grounding基准，跨越多个平台，能够对真实应用进行分层评估。VenusBench-GD的贡献如下：（i）引入了一个大规模、跨平台的基准，具有广泛的应用覆盖、多样的UI元素和丰富的标注数据；（ii）建立了一个高质量的数据构建流程，用于grounding任务，实现了比现有基准更高的标注准确率；（iii）通过提出一个分层任务分类法扩展了元素grounding的范围，该分类法将grounding分为基本和高级类别，包含六个不同的子任务，旨在从互补的角度评估模型。实验结果揭示了关键见解：通用多模态模型现在在基本grounding任务上与专用GUI模型相匹配甚至超越。相比之下，高级任务仍然偏爱GUI专用模型，尽管它们表现出显著的过拟合和较差的鲁棒性。这些结果强调了全面、多层评估框架的必要性。

## 🔬 方法详解

**问题定义**：论文旨在解决现有GUI grounding基准数据集不足的问题，包括数据量小、领域覆盖范围窄、平台单一以及标注质量不高等问题。现有方法难以全面评估GUI代理的grounding能力，并且容易过拟合特定平台或任务。

**核心思路**：论文的核心思路是构建一个大规模、跨平台、高质量的GUI grounding基准数据集，并设计一个分层的任务分类体系，从而能够更全面、更准确地评估GUI代理的grounding能力。通过引入多样化的应用场景和UI元素，以及高质量的人工标注，提高数据集的泛化性和可靠性。

**技术框架**：VenusBench-GD的构建流程主要包含以下几个阶段：1) 数据收集：从多个平台收集GUI应用数据；2) 数据清洗：对收集到的数据进行清洗和过滤，去除噪声和冗余信息；3) 数据标注：对UI元素进行标注，包括位置、类型、文本等信息；4) 任务划分：将grounding任务划分为基本和高级类别，并设计六个不同的子任务；5) 数据集发布：将构建好的数据集发布，供研究人员使用。

**关键创新**：该论文的关键创新在于：1) 构建了一个大规模、跨平台的GUI grounding基准数据集，覆盖了更广泛的应用场景和UI元素；2) 提出了一个分层的任务分类体系，能够更全面地评估GUI代理的grounding能力；3) 实现了比现有基准更高的标注准确率，提高了数据集的可靠性。

**关键设计**：论文中关于数据集构建和任务划分的具体技术细节未详细描述，例如，数据收集的具体平台和应用类型、数据清洗的具体方法、标注的具体规范、任务划分的具体标准以及六个子任务的具体定义等。这些细节对于复现和进一步研究至关重要，但文中未提供足够的信息。

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

实验结果表明，通用多模态模型在基本grounding任务上与专用GUI模型相匹配甚至超越，但在高级任务上，GUI专用模型仍然更胜一筹，但存在显著的过拟合和较差的鲁棒性。这表明需要更全面、多层次的评估框架来推动GUI grounding技术的发展。

## 🎯 应用场景

VenusBench-GD可用于训练和评估各种GUI代理，例如自动化测试工具、辅助技术和智能助手。该基准数据集能够促进GUI grounding技术的发展，提高GUI代理的智能化水平，从而改善用户体验并提高工作效率。未来，该研究可以扩展到更多平台和应用领域，并探索更复杂的grounding任务。

## 📄 摘要（原文）

> GUI grounding is a critical component in building capable GUI agents. However, existing grounding benchmarks suffer from significant limitations: they either provide insufficient data volume and narrow domain coverage, or focus excessively on a single platform and require highly specialized domain knowledge. In this work, we present VenusBench-GD, a comprehensive, bilingual benchmark for GUI grounding that spans multiple platforms, enabling hierarchical evaluation for real-word applications. VenusBench-GD contributes as follows: (i) we introduce a large-scale, cross-platform benchmark with extensive coverage of applications, diverse UI elements, and rich annotated data, (ii) we establish a high-quality data construction pipeline for grounding tasks, achieving higher annotation accuracy than existing benchmarks, and (iii) we extend the scope of element grounding by proposing a hierarchical task taxonomy that divides grounding into basic and advanced categories, encompassing six distinct subtasks designed to evaluate models from complementary perspectives. Our experimental findings reveal critical insights: general-purpose multimodal models now match or even surpass specialized GUI models on basic grounding tasks. In contrast, advanced tasks, still favor GUI-specialized models, though they exhibit significant overfitting and poor robustness. These results underscore the necessity of comprehensive, multi-tiered evaluation frameworks.

