---
layout: default
title: "E-THER: A Multimodal Dataset for Empathic AI -- Towards Emotional Mismatch Awareness"
---

# E-THER: A Multimodal Dataset for Empathic AI -- Towards Emotional Mismatch Awareness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02100" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02100v2</a>
  <a href="https://arxiv.org/pdf/2509.02100.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02100v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02100v2', 'E-THER: A Multimodal Dataset for Empathic AI -- Towards Emotional Mismatch Awareness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sharjeel Tahir, Judith Johnson, Jumana Abu-Khalaf, Syed Afaq Ali Shah

**分类**: cs.HC, cs.CL

**发布日期**: 2025-09-02 (更新: 2025-09-08)

**备注**: 15 pages, 4 figures. Preprint

---

## 💡 一句话要点

**提出E-THER多模态数据集，用于提升AI在识别言语-视觉情感不一致方面的能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `共情AI` `多模态数据集` `情感不一致` `人本主义治疗` `视觉-语言模型`

## 📋 核心要点

1. 现有共情AI系统缺乏识别言语与情感状态不一致的能力，阻碍了其真正共情能力的提升。
2. E-THER数据集通过提供言语-视觉不一致的多维标注，旨在训练AI识别和理解深层情感。
3. 实验表明，使用E-THER训练的视觉-语言模型在共情对话质量和治疗参与度方面均有显著提升。

## 📝 摘要（中文）

当前共情AI系统的一个普遍缺陷是无法识别言语表达可能无法完全反映潜在情感状态的情况。这是因为现有数据集侧重于表面层面的情感识别，而没有解决对共情理解有用的复杂言语-视觉不一致（不匹配）模式。本文提出了E-THER，这是第一个基于以人为中心的治疗的多模态数据集，具有用于言语-视觉不一致检测的多维注释，从而能够训练AI系统，使其发展真正的而非表演性的共情能力。数据集中包含的注释来自人本主义方法，即识别客户-咨询师互动中的言语-视觉情感错位，从而形成训练和评估AI在共情任务上的框架。额外的参与度评分提供了用于研究应用的 behavioral 注释。在使用基于共情和治疗原则的评估指标时，在最先进的视觉-语言模型（VLM）中，例如IDEFICS和VideoLLAVA，观察到共情和治疗对话质量的显着提高。实证研究结果表明，我们经过不一致训练的模型在关键特征方面优于通用模型，例如维持治疗参与度，最大限度地减少人为或夸张的语言模式，以及保持对PCT理论框架的忠实性。

## 🔬 方法详解

**问题定义**：现有共情AI系统主要依赖于表面层面的情感识别，忽略了言语表达与实际情感状态可能存在的不一致性。这种不一致性是人类共情理解的关键组成部分，现有方法无法有效捕捉和利用，导致AI系统难以产生真正的共情能力。

**核心思路**：E-THER数据集的核心思路是提供包含言语和视觉信息的多模态数据，并对其中的情感不一致性进行标注。通过训练AI模型识别和理解这些不一致性，使其能够更准确地推断个体的情感状态，从而提升共情能力。这种方法借鉴了以人为中心的治疗（Person-Centered Therapy, PCT）的理论框架。

**技术框架**：E-THER数据集的构建流程主要包括数据收集、多维标注和模型训练评估三个阶段。数据收集阶段主要收集客户-咨询师的互动视频和文本记录。多维标注阶段则由专业人员对数据进行标注，标注内容包括情感状态、言语表达、视觉表现以及言语-视觉情感不一致性。模型训练评估阶段则使用标注好的数据训练视觉-语言模型，并使用基于共情和治疗原则的评估指标进行评估。

**关键创新**：E-THER数据集的关键创新在于其对言语-视觉情感不一致性的标注。这是首个专门针对这一问题构建的多模态数据集，为研究人员提供了一个新的视角和工具，用于开发更具共情能力的AI系统。此外，该数据集还采用了以人为中心的治疗理论框架，为AI共情能力的建模提供了理论基础。

**关键设计**：E-THER数据集的关键设计包括：1) 采用多模态数据，包含言语和视觉信息；2) 对言语-视觉情感不一致性进行多维标注；3) 基于以人为中心的治疗理论框架进行标注；4) 提供额外的参与度评分，用于行为分析；5) 使用基于共情和治疗原则的评估指标进行模型评估。具体参数设置、损失函数和网络结构的选择取决于所使用的视觉-语言模型，例如IDEFICS和VideoLLAVA。

## 📊 实验亮点

使用E-THER数据集训练的视觉-语言模型（如IDEFICS和VideoLLAVA）在共情和治疗对话质量方面取得了显著提升。实验结果表明，经过不一致训练的模型在维持治疗参与度、减少人为语言模式以及保持对PCT理论框架的忠实性方面优于通用模型。具体性能数据未知，但整体提升趋势明显。

## 🎯 应用场景

E-THER数据集及其训练方法可应用于心理咨询、客户服务、人机交互等领域。通过提升AI的共情能力，可以改善心理咨询的效果，提高客户服务的满意度，并使人机交互更加自然和流畅。未来，该研究可以扩展到其他情感相关的领域，例如教育和医疗保健。

## 📄 摘要（原文）

> A prevalent shortfall among current empathic AI systems is their inability to recognize when verbal expressions may not fully reflect underlying emotional states. This is because the existing datasets, used for the training of these systems, focus on surface-level emotion recognition without addressing the complex verbal-visual incongruence (mismatch) patterns useful for empathic understanding. In this paper, we present E-THER, the first Person-Centered Therapy-grounded multimodal dataset with multidimensional annotations for verbal-visual incongruence detection, enabling training of AI systems that develop genuine rather than performative empathic capabilities. The annotations included in the dataset are drawn from humanistic approach, i.e., identifying verbal-visual emotional misalignment in client-counsellor interactions - forming a framework for training and evaluating AI on empathy tasks. Additional engagement scores provide behavioral annotations for research applications. Notable gains in empathic and therapeutic conversational qualities are observed in state-of-the-art vision-language models (VLMs), such as IDEFICS and VideoLLAVA, using evaluation metrics grounded in empathic and therapeutic principles. Empirical findings indicate that our incongruence-trained models outperform general-purpose models in critical traits, such as sustaining therapeutic engagement, minimizing artificial or exaggerated linguistic patterns, and maintaining fidelity to PCT theoretical framework.

