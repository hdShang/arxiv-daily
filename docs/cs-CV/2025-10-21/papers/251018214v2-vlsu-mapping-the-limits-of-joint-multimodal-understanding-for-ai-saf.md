---
layout: default
title: VLSU: Mapping the Limits of Joint Multimodal Understanding for AI Safety
---

# VLSU: Mapping the Limits of Joint Multimodal Understanding for AI Safety

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.18214" class="toolbar-btn" target="_blank">📄 arXiv: 2510.18214v2</a>
  <a href="https://arxiv.org/pdf/2510.18214.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.18214v2" onclick="toggleFavorite(this, '2510.18214v2', 'VLSU: Mapping the Limits of Joint Multimodal Understanding for AI Safety')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shruti Palaskar, Leon Gatys, Mona Abdelrahman, Mar Jacobo, Larry Lindsey, Rutika Moharir, Gunnar Lund, Yang Xu, Navid Shiee, Jeffrey Bigham, Charles Maalouf, Joseph Yitan Cheng

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-10-21 (更新: 2025-12-03)

**备注**: 10 pages, 5 figures, 4 tables, detailed appendix. Under review

---

## 💡 一句话要点

**VLSU：构建多模态AI安全评估框架，揭示视觉-语言联合理解的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态安全` `视觉-语言理解` `AI安全评估` `组合推理` `基准数据集`

## 📋 核心要点

1. 现有方法在评估多模态模型安全性时，通常独立处理视觉和语言输入，忽略了联合理解可能带来的风险。
2. VLSU框架通过细粒度的严重程度分类和组合分析，系统性地评估多模态AI的安全性，并构建大规模基准。
3. 实验表明，现有模型在联合图像-文本推理方面存在显著缺陷，尤其是在需要组合推理时性能大幅下降。

## 📝 摘要（中文）

本文提出了视觉-语言安全理解（VLSU）框架，旨在系统性地评估多模态AI的安全性，通过细粒度的严重程度分类和跨17种不同安全模式的组合分析。该框架利用真实世界的图像和人工标注，构建了一个包含8187个样本的大规模基准，涵盖15个危害类别。对11个先进模型的评估表明，模型在联合理解方面存在系统性缺陷：在清晰的单模态安全信号上，模型准确率超过90%，但当需要联合图像-文本推理来确定安全标签时，性能显著下降到20-55%。更关键的是，34%的联合图像-文本安全分类错误发生在各个模态都被正确分类的情况下，进一步表明模型缺乏组合推理能力。此外，模型难以平衡拒绝不安全内容与响应边缘案例。例如，指令框架可以将Gemini-1.5在边缘内容上的过度屏蔽率从62.4%降低到10.4%，但代价是降低了对不安全内容的拒绝率，从90.8%降至53.9%。总而言之，该框架揭示了当前模型在联合图像-文本理解方面的弱点和对齐差距，并为鲁棒的视觉-语言安全研究提供了关键的测试平台。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态AI安全评估中存在的不足，即现有方法未能充分考虑视觉和语言信息联合理解带来的安全风险，并且无法有效区分明确不安全内容和边缘案例，导致过度屏蔽或未能拒绝有害内容。现有方法主要关注单模态的安全评估，忽略了模态之间的相互作用，无法准确评估模型的整体安全性。

**核心思路**：论文的核心思路是构建一个全面的多模态安全评估框架，该框架能够系统性地评估模型在处理视觉和语言信息时的安全性，并能够区分不同严重程度的安全问题。通过构建一个包含多种安全模式和危害类别的大规模基准，可以更全面地评估模型的安全性能。

**技术框架**：VLSU框架包含一个多阶段的流水线，包括数据收集、人工标注和模型评估。首先，收集真实世界的图像和文本数据，并进行人工标注，标注内容包括安全类别和严重程度。然后，利用这些标注数据构建一个大规模的基准数据集。最后，使用该基准数据集评估现有模型的安全性能，并分析模型的错误类型和原因。

**关键创新**：VLSU框架的关键创新在于其全面性和细粒度。它不仅考虑了多种安全模式和危害类别，还对安全问题进行了细粒度的严重程度分类。此外，该框架还强调了联合图像-文本推理的重要性，并揭示了现有模型在组合推理方面的不足。

**关键设计**：VLSU框架的关键设计包括：1）使用真实世界的图像和文本数据，以确保评估的真实性和可靠性；2）采用人工标注，以确保标注的准确性和一致性；3）构建一个包含多种安全模式和危害类别的大规模基准数据集，以确保评估的全面性；4）对安全问题进行细粒度的严重程度分类，以便更准确地评估模型的安全性能。

## 📊 实验亮点

实验结果表明，现有模型在联合图像-文本推理方面存在显著缺陷。在清晰的单模态安全信号上，模型准确率超过90%，但当需要联合图像-文本推理时，性能下降到20-55%。更重要的是，34%的联合图像-文本安全分类错误发生在各个模态都被正确分类的情况下。此外，指令框架可以降低Gemini-1.5在边缘内容上的过度屏蔽率，但代价是降低了对不安全内容的拒绝率。

## 🎯 应用场景

该研究成果可应用于提升多模态AI系统的安全性，例如图像-文本生成模型、视觉问答系统等。通过使用VLSU框架进行安全评估，可以发现并修复模型中存在的安全漏洞，从而降低模型被恶意利用的风险。此外，该研究还可以促进多模态安全领域的研究，推动更安全、更可靠的AI系统的发展。

## 📄 摘要（原文）

> Safety evaluation of multimodal foundation models often treats vision and language inputs separately, missing risks from joint interpretation where benign content becomes harmful in combination. Existing approaches also fail to distinguish clearly unsafe content from borderline cases, leading to problematic over-blocking or under-refusal of genuinely harmful content. We present Vision Language Safety Understanding (VLSU), a comprehensive framework to systematically evaluate multimodal safety through fine-grained severity classification and combinatorial analysis across 17 distinct safety patterns. Using a multi-stage pipeline with real-world images and human annotation, we construct a large-scale benchmark of 8,187 samples spanning 15 harm categories. Our evaluation of eleven state-of-the-art models reveals systematic joint understanding failures: while models achieve 90%-plus accuracy on clear unimodal safety signals, performance degrades substantially to 20-55% when joint image-text reasoning is required to determine the safety label. Most critically, 34% of errors in joint image-text safety classification occur despite correct classification of the individual modalities, further demonstrating absent compositional reasoning capabilities. Additionally, we find that models struggle to balance refusing unsafe content while still responding to borderline cases that deserve engagement. For example, we find that instruction framing can reduce the over-blocking rate on borderline content from 62.4% to 10.4% in Gemini-1.5, but only at the cost of under-refusing on unsafe content with refusal rate dropping from 90.8% to 53.9%. Overall, our framework exposes weaknesses in joint image-text understanding and alignment gaps in current models, and provides a critical test bed to enable the next milestones in research on robust vision-language safety.

