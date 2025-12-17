---
layout: default
title: VisJudge-Bench: Aesthetics and Quality Assessment of Visualizations
---

# VisJudge-Bench: Aesthetics and Quality Assessment of Visualizations

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22373" target="_blank" class="toolbar-btn">arXiv: 2510.22373v1</a>
    <a href="https://arxiv.org/pdf/2510.22373.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22373v1" 
            onclick="toggleFavorite(this, '2510.22373v1', 'VisJudge-Bench: Aesthetics and Quality Assessment of Visualizations')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yupeng Xie, Zhiyang Zhang, Yifan Wu, Sirong Lu, Jiayi Zhang, Zhaoyang Yu, Jinlin Wang, Sirui Hong, Bang Liu, Chenglin Wu, Yuyu Luo

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-10-25

**备注**: 53 pages, 26 figures, 5 tables

**🔗 代码/项目**: [GITHUB](https://github.com/HKUSTDial/VisJudgeBench)

---

## 💡 一句话要点

**提出VisJudge-Bench，用于评估MLLM在可视化美学和质量评估中的性能，并提出VisJudge模型。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可视化评估` `多模态大语言模型` `基准数据集` `美学评估` `质量评估` `VisJudge-Bench` `VisJudge` `自动化评估`

## 📋 核心要点

1. 现有方法缺乏针对可视化美学和质量评估的系统性基准，难以有效评估多模态大语言模型（MLLM）在此领域的性能。
2. 论文提出VisJudge-Bench基准数据集，并设计VisJudge模型，专门用于提升可视化美学和质量的自动评估能力。
3. 实验表明，VisJudge模型在VisJudge-Bench上显著优于现有MLLM，在MAE和一致性方面均有大幅提升，更接近人类专家水平。

## 📝 摘要（中文）

可视化是一种将复杂数据集转化为直观见解的有效方式，其价值取决于数据是否被忠实地表示、清晰地传达以及美观地设计。然而，评估可视化质量具有挑战性，因为它需要同时判断数据编码的准确性、信息表达的有效性和视觉美学。尽管多模态大型语言模型（MLLM）在自然图像的美学评估中表现出良好的性能，但目前还没有系统的基准来衡量它们在评估可视化方面的能力。为了解决这个问题，我们提出了VisJudge-Bench，这是第一个用于评估MLLM在可视化美学和质量评估中性能的综合基准。它包含来自真实场景的3090个专家标注样本，涵盖32种图表类型的单个可视化、多个可视化和仪表板。对该基准的系统测试表明，即使是最先进的MLLM（如GPT-5）在判断方面与人类专家相比仍然存在显著差距，平均绝对误差（MAE）为0.551，与人类评分的相关性仅为0.429。为了解决这个问题，我们提出了VisJudge，一个专门为可视化美学和质量评估设计的模型。实验结果表明，与GPT-5相比，VisJudge显著缩小了与人类判断的差距，将MAE降低到0.442（降低了19.8%），并将与人类专家的一致性提高到0.681（提高了58.7%）。该基准可在https://github.com/HKUSTDial/VisJudgeBench上获得。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）在可视化美学和质量评估方面表现不足的问题。现有方法缺乏专门针对可视化设计的评估基准，无法有效衡量MLLM在此领域的性能。同时，通用MLLM在处理可视化特有的数据编码、信息表达和视觉美学等复杂因素时存在困难，导致评估结果与人类专家存在较大差距。

**核心思路**：论文的核心思路是构建一个高质量的可视化评估基准（VisJudge-Bench），并在此基础上训练一个专门针对可视化评估的模型（VisJudge）。通过高质量的数据和针对性的模型设计，提升MLLM在可视化美学和质量评估方面的准确性和一致性。

**技术框架**：VisJudge-Bench包含3090个专家标注的可视化样本，涵盖32种图表类型，包括单个可视化、多个可视化和仪表板。VisJudge模型基于现有的MLLM架构进行改进，可能包括针对可视化特征提取的特定模块，以及针对评估任务的优化训练策略。整体流程为：首先，使用VisJudge-Bench对现有MLLM进行评估，发现其不足；然后，基于VisJudge-Bench训练VisJudge模型；最后，对比VisJudge和现有MLLM在VisJudge-Bench上的性能。

**关键创新**：论文的关键创新在于：1) 提出了VisJudge-Bench，这是第一个专门针对可视化美学和质量评估的综合基准；2) 设计了VisJudge模型，该模型针对可视化评估任务进行了优化，能够更准确地评估可视化的质量。与现有方法相比，VisJudge-Bench提供了更具针对性的评估数据，VisJudge模型则提供了更有效的评估方法。

**关键设计**：具体的技术细节（如VisJudge模型的网络结构、损失函数、训练策略等）在论文中可能没有详细描述，属于未知信息。可能涉及的关键设计包括：针对不同图表类型的特征提取模块、用于融合数据编码、信息表达和视觉美学信息的注意力机制、以及用于优化评估结果与人类专家一致性的损失函数。

## 📊 实验亮点

实验结果表明，VisJudge模型在VisJudge-Bench上显著优于现有MLLM，将平均绝对误差（MAE）从GPT-5的0.551降低到0.442（降低了19.8%），并将与人类专家的一致性从0.429提高到0.681（提高了58.7%）。这些结果表明，VisJudge模型能够更准确地评估可视化的美学和质量，更接近人类专家的判断。

## 🎯 应用场景

该研究成果可应用于自动化可视化质量评估、可视化设计辅助、以及可视化教学等领域。通过自动评估可视化质量，可以帮助用户快速发现和改进可视化设计中的问题，提升数据呈现的有效性和美观性。此外，该研究还可以为可视化教学提供客观的评估标准，帮助学生更好地掌握可视化设计原则。

## 📄 摘要（原文）

> Visualization, a domain-specific yet widely used form of imagery, is an effective way to turn complex datasets into intuitive insights, and its value depends on whether data are faithfully represented, clearly communicated, and aesthetically designed. However, evaluating visualization quality is challenging: unlike natural images, it requires simultaneous judgment across data encoding accuracy, information expressiveness, and visual aesthetics. Although multimodal large language models (MLLMs) have shown promising performance in aesthetic assessment of natural images, no systematic benchmark exists for measuring their capabilities in evaluating visualizations. To address this, we propose VisJudge-Bench, the first comprehensive benchmark for evaluating MLLMs' performance in assessing visualization aesthetics and quality. It contains 3,090 expert-annotated samples from real-world scenarios, covering single visualizations, multiple visualizations, and dashboards across 32 chart types. Systematic testing on this benchmark reveals that even the most advanced MLLMs (such as GPT-5) still exhibit significant gaps compared to human experts in judgment, with a Mean Absolute Error (MAE) of 0.551 and a correlation with human ratings of only 0.429. To address this issue, we propose VisJudge, a model specifically designed for visualization aesthetics and quality assessment. Experimental results demonstrate that VisJudge significantly narrows the gap with human judgment, reducing the MAE to 0.442 (a 19.8% reduction) and increasing the consistency with human experts to 0.681 (a 58.7% improvement) compared to GPT-5. The benchmark is available at https://github.com/HKUSTDial/VisJudgeBench.

