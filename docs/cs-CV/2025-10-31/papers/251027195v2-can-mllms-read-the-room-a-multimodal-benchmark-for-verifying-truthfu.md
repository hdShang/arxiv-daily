---
layout: default
title: Can MLLMs Read the Room? A Multimodal Benchmark for Verifying Truthfulness in Multi-Party Social Interactions
---

# Can MLLMs Read the Room? A Multimodal Benchmark for Verifying Truthfulness in Multi-Party Social Interactions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27195" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27195v2</a>
  <a href="https://arxiv.org/pdf/2510.27195.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27195v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27195v2', 'Can MLLMs Read the Room? A Multimodal Benchmark for Verifying Truthfulness in Multi-Party Social Interactions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Caixin Kang, Yifei Huang, Liangyang Ouyang, Mingfang Zhang, Yoichi Sato

**分类**: cs.CV, cs.CL, cs.SI

**发布日期**: 2025-10-31 (更新: 2025-11-04)

**备注**: ICCV2025 Workshop

---

## 💡 一句话要点

**提出MIVA基准，评估多模态大语言模型在多人社交互动中识别谎言的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `谎言识别` `社交智能` `大语言模型` `多方交互` `真实性评估` `狼人杀` `视觉语言理解`

## 📋 核心要点

1. 现有方法难以在动态多人对话中进行欺骗检测，缺乏对语言和非语言线索的有效融合。
2. 提出多模态交互真实性评估（MIVA）任务，并构建基于“狼人杀”游戏的多模态数据集。
3. 实验表明，即使是GPT-4o等先进MLLM也难以可靠区分真假，存在显著性能差距。

## 📝 摘要（中文）

随着人工智能系统日益融入人类生活，赋予它们强大的社交智能已成为一个关键前沿。这种智能的一个关键方面是辨别真假，这是人类互动中普遍存在的要素，通过口头语言和非语言视觉线索的复杂相互作用来传达。然而，在动态的多方对话中自动进行欺骗检测仍然是一个重大挑战。最近强大的多模态大语言模型（MLLM）的兴起，凭借其在视觉和文本理解方面的卓越能力，使其成为这项任务的天然候选者。因此，它们在这个关键领域的能力在很大程度上是未量化的。为了弥补这一差距，我们引入了一项新任务，即多模态交互真实性评估（MIVA），并提出了一个源自社交推理游戏“狼人杀”的新型多模态数据集。该数据集为每个陈述提供同步的视频、文本以及可验证的真实标签。我们建立了一个全面的基准，评估最先进的MLLM，揭示了一个显著的性能差距：即使是像GPT-4o这样强大的模型也难以可靠地区分真假。我们对失败模式的分析表明，这些模型未能有效地将语言扎根于视觉社交线索中，并且可能在对齐方面过于保守，突显了迫切需要新的方法来构建更具洞察力和值得信赖的AI系统。

## 🔬 方法详解

**问题定义**：论文旨在解决多方社交互动场景下的谎言识别问题。现有方法在处理动态对话和融合多模态信息方面存在不足，难以有效捕捉语言和非语言线索之间的复杂关系。特别是在多人互动中，欺骗行为往往更加隐蔽，需要更强的推理能力和对社交环境的理解。

**核心思路**：论文的核心思路是利用多模态大语言模型（MLLM）的强大视觉和文本理解能力，通过分析参与者的语言表达和非语言行为（如面部表情、肢体动作）来判断其陈述的真实性。通过构建一个包含同步视频、文本和真实标签的数据集，为MLLM提供学习和评估的平台。

**技术框架**：论文构建了一个多模态交互真实性评估（MIVA）框架，该框架主要包含以下几个阶段：1) 数据收集与标注：从“狼人杀”游戏中收集视频和文本数据，并为每个陈述标注真实标签。2) 特征提取：利用MLLM提取视频和文本的特征表示。3) 真实性预测：基于提取的特征，利用分类器预测陈述的真实性。4) 性能评估：使用准确率、精确率、召回率等指标评估MLLM的性能。

**关键创新**：论文的主要创新点在于：1) 提出了多模态交互真实性评估（MIVA）任务，填补了多方社交互动场景下谎言识别研究的空白。2) 构建了一个基于“狼人杀”游戏的新型多模态数据集，为MLLM的学习和评估提供了数据基础。3) 对比评估了多种先进的MLLM在MIVA任务上的性能，揭示了现有模型在理解和融合多模态社交线索方面的不足。

**关键设计**：论文的关键设计包括：1) 数据集的构建：精心设计了数据收集和标注流程，保证了数据的质量和多样性。2) 特征提取方法：选择了合适的MLLM来提取视频和文本的特征表示，并探索了不同的特征融合策略。3) 评估指标：采用了多种评估指标来全面评估MLLM的性能。

## 📊 实验亮点

实验结果表明，即使是GPT-4o等先进的MLLM在MIVA数据集上的表现也远低于人类水平，准确率仅为未知百分比。这表明现有模型在理解和融合多模态社交线索方面存在显著不足，需要进一步的研究和改进。

## 🎯 应用场景

该研究成果可应用于智能客服、在线教育、招聘面试等领域，帮助系统识别用户或参与者的欺骗行为，提高交互的真实性和可靠性。未来可进一步扩展到社交媒体内容审核、金融风险评估等领域，构建更值得信赖的人工智能系统。

## 📄 摘要（原文）

> As AI systems become increasingly integrated into human lives, endowing them with robust social intelligence has emerged as a critical frontier. A key aspect of this intelligence is discerning truth from deception, a ubiquitous element of human interaction that is conveyed through a complex interplay of verbal language and non-verbal visual cues. However, automatic deception detection in dynamic, multi-party conversations remains a significant challenge. The recent rise of powerful Multimodal Large Language Models (MLLMs), with their impressive abilities in visual and textual understanding, makes them natural candidates for this task. Consequently, their capabilities in this crucial domain are mostly unquantified. To address this gap, we introduce a new task, Multimodal Interactive Veracity Assessment (MIVA), and present a novel multimodal dataset derived from the social deduction game Werewolf. This dataset provides synchronized video, text, with verifiable ground-truth labels for every statement. We establish a comprehensive benchmark evaluating state-of-the-art MLLMs, revealing a significant performance gap: even powerful models like GPT-4o struggle to distinguish truth from falsehood reliably. Our analysis of failure modes indicates that these models fail to ground language in visual social cues effectively and may be overly conservative in their alignment, highlighting the urgent need for novel approaches to building more perceptive and trustworthy AI systems.

