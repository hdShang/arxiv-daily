---
layout: default
title: "On the Faithfulness of Visual Thinking: Measurement and Enhancement"
---

# On the Faithfulness of Visual Thinking: Measurement and Enhancement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23482" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23482v1</a>
  <a href="https://arxiv.org/pdf/2510.23482.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23482v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.23482v1', 'On the Faithfulness of Visual Thinking: Measurement and Enhancement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zujing Liu, Junwen Pan, Qi She, Yuan Gao, Guisong Xia

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-27

**🔗 代码/项目**: [GITHUB](https://github.com/EugeneLiu01/Faithful_Thinking_with_Image)

---

## 💡 一句话要点

**提出SCCM学习策略，提升视觉语言模型多模态推理中视觉信息的可靠性和充分性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `多模态推理` `思维链` `强化学习` `视觉真实性`

## 📋 核心要点

1. 现有视觉语言模型的多模态思维链(MCoT)推理过程缺乏真实性，视觉信息常被忽略。
2. 提出充分组件因果模型(SCCM)学习策略，鼓励MCoT生成充分且最小的视觉组件以实现独立推理。
3. 实验表明，SCCM能显著提升模型在细粒度感知和推理任务中的视觉真实性。

## 📝 摘要（中文）

当前的大型视觉语言模型(LVLMs)在经过强化微调(RFT)后，能够生成视觉-文本多模态思维链(MCoT)。然而，我们观察到MCoT中包含的视觉信息通常是不准确的，尽管仍然可以产生正确的答案，这表明MCoT推理过程缺乏真实性。我们将这种不真实性归因于RFT中的强化学习奖励，它仅仅激励交错的视觉-文本提示的格式，即它鼓励模型将视觉信息纳入其文本推理步骤，而不考虑视觉信息的正确性。在本文中，我们首先通过测量当其视觉和文本思想受到干预时预测的变化程度来探测MCoT的真实性。令人惊讶的是，模型的预测在视觉干预下几乎保持不变，但在文本干预下发生显著变化，表明视觉证据在很大程度上被忽略。为了进一步分析视觉信息，我们引入了一种基于LVLM的自动评估指标，该指标从可靠性和充分性两个角度量化视觉线索的真实性。我们的评估表明，当前MCoT轨迹中的视觉信息同时是不可靠和不充分的。为了解决这个问题，我们提出了一种新的MCoT学习策略，称为充分组件因果模型(SCCM)学习。这种方法鼓励MCoT生成充分但最小的视觉组件，这些组件能够独立地导致正确的答案。我们注意到，所提出的SCCM是无标注的，并且可以以即插即用的方式与各种用于MCoT的RFT兼容。经验结果表明，SCCM持续提高了在一系列细粒度感知和推理基准上的视觉真实性。

## 🔬 方法详解

**问题定义**：现有大型视觉语言模型（LVLMs）通过强化学习微调（RFT）生成多模态思维链（MCoT），但MCoT中视觉信息的准确性不足，模型倾向于依赖文本信息进行推理，忽略视觉证据。现有RFT方法只关注视觉信息是否被使用，而忽略了视觉信息的正确性，导致视觉信息不可靠且不充分。

**核心思路**：论文的核心思路是鼓励模型生成“充分且最小”的视觉组件，这些组件能够独立地支持正确的答案。通过这种方式，模型不再仅仅将视觉信息作为文本推理的辅助，而是将其作为独立推理的依据，从而提高视觉信息的可靠性和充分性。

**技术框架**：SCCM学习策略可以与现有的RFT方法结合使用，作为一个即插即用的模块。整体流程包括：1）使用LVLM生成MCoT；2）使用SCCM学习策略优化MCoT，鼓励生成充分且最小的视觉组件；3）使用RFT进行微调。

**关键创新**：关键创新在于提出了“充分组件因果模型（SCCM）”的概念，并设计了相应的学习策略。与现有方法不同，SCCM不依赖于额外的标注数据，而是通过自监督的方式学习视觉信息的因果关系，从而提高视觉信息的质量。

**关键设计**：SCCM学习策略的关键在于如何定义和衡量视觉组件的“充分性”和“最小性”。论文中可能使用了特定的损失函数来鼓励模型生成既能独立支持答案，又尽可能简洁的视觉组件。具体的技术细节（如损失函数的具体形式、网络结构的调整等）需要在论文中进一步查找。

## 📊 实验亮点

实验结果表明，SCCM学习策略能够显著提高模型在细粒度感知和推理基准上的视觉真实性。具体性能数据和提升幅度需要在论文中查找。该方法无需额外标注，且能与现有RFT方法兼容，具有较强的实用性。

## 🎯 应用场景

该研究成果可应用于需要高度视觉信息可信度的场景，例如自动驾驶、医疗影像诊断、安防监控等。通过提高视觉信息的可靠性和充分性，可以提升模型在这些领域的决策能力和安全性，并为未来的视觉语言模型研究提供新的思路。

## 📄 摘要（原文）

> Recent large vision-language models (LVLMs) can generate vision-text multimodal chain-of-thought (MCoT) traces after reinforcement fine-tuning (RFT). However, we observe that the visual information incorporated in MCoT is often inaccurate, though still yield correct answers, indicating a lack of faithfulness in the MCoT reasoning process. We attribute this unfaithfulness to the RL reward in RFT, which solely incentivizes the format of interleaved vision-text cues, ie, it encourages the model to incorporate visual information into its text reasoning steps without considering the correctness of the visual information. In this paper, we first probe the faithfulness of MCoT by measuring how much the prediction changes when its visual and textual thoughts are intervened. Surprisingly, the model's predictions remain nearly unchanged under visual intervention but change significantly under textual intervention, indicating that the visual evidence is largely ignored. To further analyze visual information, we introduce an automated LVLM-based evaluation metric that quantifies the faithfulness of visual cues from two perspectives: reliability and sufficiency. Our evaluation reveals that the visual information in current MCoT traces is simultaneously unreliable and insufficient. To address this issue, we propose a novel MCoT learning strategy termed Sufficient-Component Cause Model (SCCM) learning. This approach encourages the MCoT to generate sufficient yet minimal visual components that are independently capable of leading to correct answers. We note that the proposed SCCM is annotation-free and compatible with various RFT for MCoT in a plug-and-play manner. Empirical results demonstrate that SCCM consistently improves the visual faithfulness across a suite of fine-grained perception and reasoning benchmarks. Code is available at https://github.com/EugeneLiu01/Faithful_Thinking_with_Image.

