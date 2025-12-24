---
layout: default
title: "Do Retrieval Augmented Language Models Know When They Don't Know?"
---

# Do Retrieval Augmented Language Models Know When They Don't Know?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01476" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01476v3</a>
  <a href="https://arxiv.org/pdf/2509.01476.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01476v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01476v3', 'Do Retrieval Augmented Language Models Know When They Don\'t Know?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youchao Zhou, Heyan Huang, Yicheng Liu, Rui Dai, Xinglin Wang, Xingchen Zhang, Shumin Shi, Yang Deng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-01 (更新: 2025-11-18)

**备注**: AAAI 2026 camera ready version. Extended version with Appendix is coming soon

---

## 💡 一句话要点

**研究检索增强语言模型（RALM）的拒识能力，并提出改进方案。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强语言模型` `拒识能力` `校准` `幻觉` `不确定性估计` `上下文微调` `知识状态`

## 📋 核心要点

1. 现有检索增强语言模型（RALM）存在幻觉问题，且缺乏对其拒识能力的充分评估。
2. 研究核心在于评估RALM在不同知识状态下的校准情况，并探究其拒识能力与校准质量的关系。
3. 通过上下文微调缓解过度拒绝问题，并结合不确定性估计改进RALM的整体回答质量。

## 📝 摘要（中文）

现有的大型语言模型（LLM）有时会生成看似合理但实际上不正确的回复，即幻觉。缓解幻觉主要有两种方法：检索增强语言模型（RALM）和拒绝后训练。然而，目前的研究主要集中于它们各自的有效性，而忽略了对RALM的拒绝能力的评估。理想情况下，如果RALM知道它们不知道什么，它们应该拒绝回答。本研究探讨了一个基本问题：RALM是否知道它们不知道什么？具体来说，我们研究了三个问题。首先，RALM在不同的内部和外部知识状态下是否校准良好？我们考察了各种因素的影响。与预期相反，当所有检索到的文档都不相关时，RALM仍然倾向于拒绝它们本可以正确回答的问题。其次，鉴于模型明显的	extbf{过度拒绝}行为，我们提出了第二个问题：RALM的拒绝能力与其校准质量如何一致？我们的结果表明，过度拒绝问题可以通过上下文微调来缓解。然而，我们观察到，改进的拒绝行为并不一定意味着更好的校准或更高的总体准确性。最后，我们问：我们能否将具有拒绝意识的RALM与基于不确定性的答案回避相结合，以减轻过度拒绝？我们为拒绝后训练的RALM开发了一种简单而有效的拒绝机制，通过平衡拒绝和正确答案来提高它们的整体答案质量。我们的研究提供了对影响RALM行为的因素的更全面的理解。同时，我们强调，RALM的不确定性估计仍然是一个值得深入研究的开放问题。

## 🔬 方法详解

**问题定义**：论文旨在解决检索增强语言模型（RALM）在面对未知信息时，无法有效拒绝回答，从而产生幻觉的问题。现有方法主要关注提升RALM的检索和生成能力，而忽略了对其拒识能力的评估，导致模型在缺乏相关知识时仍然会给出错误答案。

**核心思路**：论文的核心思路是评估RALM在不同知识状态下的校准情况，即模型对其自身知识的置信度是否与其回答的正确性相符。通过分析RALM在检索到无关文档时的行为，以及拒识能力与校准质量之间的关系，来深入理解影响RALM拒识能力的因素。

**技术框架**：论文的研究框架主要包括以下几个阶段：1) 评估RALM在不同知识状态下的校准情况，包括检索到相关文档、无关文档以及没有检索到文档等情况。2) 分析RALM的拒识能力，特别是过度拒绝现象，即模型拒绝回答其本可以正确回答的问题。3) 通过上下文微调等方法来缓解过度拒绝问题，并评估其对校准质量和总体准确性的影响。4) 提出一种基于不确定性的拒绝机制，结合拒绝后训练的RALM，以进一步提高模型的回答质量。

**关键创新**：论文的关键创新在于对RALM的拒识能力进行了系统性的评估，并揭示了其与校准质量之间的复杂关系。此外，论文还提出了一种简单而有效的拒绝机制，通过平衡拒绝和正确答案来提高RALM的整体回答质量。

**关键设计**：论文的关键设计包括：1) 使用不同的数据集和评估指标来评估RALM的校准情况和拒识能力。2) 通过上下文微调来调整RALM的拒识阈值，以缓解过度拒绝问题。3) 设计一种基于不确定性的拒绝机制，利用模型输出的置信度来判断是否应该拒绝回答。

## 📊 实验亮点

实验结果表明，当检索到的文档不相关时，RALM倾向于拒绝回答，即使它们本可以正确回答。通过上下文微调可以缓解过度拒绝问题，但改进的拒绝行为并不一定意味着更好的校准或更高的总体准确性。提出的拒绝机制能够有效平衡拒绝和正确答案，提高RALM的整体回答质量。

## 🎯 应用场景

该研究成果可应用于各种需要可靠信息检索和问答的场景，例如智能客服、知识库问答、医疗诊断辅助等。通过提高RALM的拒识能力，可以减少错误信息的传播，提高用户对系统的信任度，并最终提升用户体验。

## 📄 摘要（原文）

> Existing large language models (LLMs) occasionally generate plausible yet factually incorrect responses, known as hallucinations. Two main approaches have been proposed to mitigate hallucinations: retrieval-augmented language models (RALMs) and refusal post-training. However, current research predominantly focuses on their individual effectiveness while overlooking the evaluation of the refusal capability of RALMs. Ideally, if RALMs know when they do not know, they should refuse to answer.In this study, we ask the fundamental question: Do RALMs know when they don't know? Specifically, we investigate three questions. First, are RALMs well calibrated with respect to different internal and external knowledge states? We examine the influence of various factors. Contrary to expectations, when all retrieved documents are irrelevant, RALMs still tend to refuse questions they could have answered correctly. Next, given the model's pronounced \textbf{over-refusal} behavior, we raise a second question: How does a RALM's refusal ability align with its calibration quality? Our results show that the over-refusal problem can be mitigated through in-context fine-tuning. However, we observe that improved refusal behavior does not necessarily imply better calibration or higher overall accuracy. Finally, we ask: Can we combine refusal-aware RALMs with uncertainty-based answer abstention to mitigate over-refusal? We develop a simple yet effective refusal mechanism for refusal-post-trained RALMs that improves their overall answer quality by balancing refusal and correct answers. Our study provides a more comprehensive understanding of the factors influencing RALM behavior. Meanwhile, we emphasize that uncertainty estimation for RALMs remains an open problem deserving deeper investigation.

