---
layout: default
title: "DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm"
---

# DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15550" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15550v2</a>
  <a href="https://arxiv.org/pdf/2509.15550.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15550v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15550v2', 'DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaowei Zhu, Yubing Ren, Fang Fang, Qingfeng Tan, Shi Wang, Yanan Cao

**分类**: cs.CL

**发布日期**: 2025-09-19 (更新: 2025-10-09)

**备注**: NeurIPS 2025 Spotlight

**🔗 代码/项目**: [GITHUB](https://github.com/Xiaoweizhu57/DNA-DetectLLM)

---

## 💡 一句话要点

**提出DNA-DetectLLM，利用DNA修复机制实现零样本AI生成文本检测。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI生成文本检测` `零样本学习` `DNA修复机制` `可解释性` `对抗攻击` `鲁棒性` `自然语言处理`

## 📋 核心要点

1. 现有AI生成文本检测方法难以区分人类撰写和AI生成文本，因为二者特征分布高度重叠，分类边界模糊。
2. DNA-DetectLLM受DNA修复机制启发，通过迭代修复非最优token，量化修复工作量，从而区分二者。
3. 实验表明，DNA-DetectLLM在多个数据集上取得了SOTA性能，AUROC相对提升5.55%，F1分数相对提升2.08%。

## 📝 摘要（中文）

大型语言模型（LLMs）的快速发展模糊了AI生成文本和人类撰写文本之间的界限。这种进步带来了诸如错误信息、作者身份模糊和知识产权问题等社会风险，突显了对可靠的AI生成文本检测方法的迫切需求。然而，生成语言建模的最新进展导致人类撰写文本和AI生成文本的特征分布之间存在显著重叠，模糊了分类边界，使得准确检测变得越来越具有挑战性。为了解决上述挑战，我们提出了一种受DNA启发的视角，利用基于修复的过程来直接且可解释地捕获人类撰写文本和AI生成文本之间的内在差异。在此基础上，我们引入了DNA-DetectLLM，一种用于区分AI生成文本和人类撰写文本的零样本检测方法。该方法为每个输入构建一个理想的AI生成序列，迭代地修复非最优token，并将累积的修复工作量量化为可解释的检测信号。经验评估表明，我们的方法实现了最先进的检测性能，并对各种对抗性攻击和输入长度表现出强大的鲁棒性。具体而言，DNA-DetectLLM在多个公共基准数据集上实现了AUROC相对提升5.55%，F1分数相对提升2.08%。代码和数据可在https://github.com/Xiaoweizhu57/DNA-DetectLLM获取。

## 🔬 方法详解

**问题定义**：论文旨在解决AI生成文本检测问题。现有方法难以有效区分人类撰写文本和AI生成文本，因为随着生成模型的发展，二者的特征分布越来越接近，导致检测准确率下降。此外，现有方法缺乏可解释性，难以理解其判断依据。

**核心思路**：论文的核心思路是借鉴DNA的修复机制。假设AI生成的文本存在“缺陷”，可以通过迭代修复使其更接近“理想”的AI生成文本。修复过程中的“修复工作量”可以作为区分AI生成文本和人类撰写文本的指标。人类撰写文本通常更自然，需要的修复工作量较小。

**技术框架**：DNA-DetectLLM的整体流程如下：1) 输入一段文本；2) 为该文本构建一个“理想”的AI生成序列；3) 迭代地修复输入文本中的非最优token，使其更接近“理想”序列；4) 量化累积的修复工作量；5) 根据修复工作量判断输入文本是AI生成还是人类撰写。

**关键创新**：该方法最重要的创新点在于将DNA修复机制引入AI生成文本检测领域，并提出了一种可解释的检测信号——修复工作量。与现有方法相比，DNA-DetectLLM不需要训练，具有零样本检测能力，并且能够提供可解释的判断依据。

**关键设计**：关键设计包括：1) 如何构建“理想”的AI生成序列（例如，使用大型语言模型生成）；2) 如何定义和量化“修复工作量”（例如，使用token替换的概率变化）；3) 迭代修复的停止条件（例如，达到最大迭代次数或修复工作量低于阈值）。具体参数设置和损失函数细节论文中未明确说明，属于未知信息。

## 📊 实验亮点

DNA-DetectLLM在多个公共基准数据集上取得了显著的性能提升。具体而言，AUROC指标相对提升了5.55%，F1分数相对提升了2.08%。实验结果表明，该方法具有较强的鲁棒性，能够有效抵抗各种对抗性攻击，并且对不同长度的输入文本具有良好的适应性。这些结果证明了DNA-DetectLLM在AI生成文本检测领域的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于检测虚假新闻、防止学术抄袭、识别AI生成的恶意评论等领域。通过提高AI生成文本的检测能力，有助于维护网络信息安全，保护知识产权，并促进人工智能技术的健康发展。未来，该方法可以进一步扩展到其他类型的AI生成内容检测，例如图像和音频。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has blurred the line between AI-generated and human-written text. This progress brings societal risks such as misinformation, authorship ambiguity, and intellectual property concerns, highlighting the urgent need for reliable AI-generated text detection methods. However, recent advances in generative language modeling have resulted in significant overlap between the feature distributions of human-written and AI-generated text, blurring classification boundaries and making accurate detection increasingly challenging. To address the above challenges, we propose a DNA-inspired perspective, leveraging a repair-based process to directly and interpretably capture the intrinsic differences between human-written and AI-generated text. Building on this perspective, we introduce DNA-DetectLLM, a zero-shot detection method for distinguishing AI-generated and human-written text. The method constructs an ideal AI-generated sequence for each input, iteratively repairs non-optimal tokens, and quantifies the cumulative repair effort as an interpretable detection signal. Empirical evaluations demonstrate that our method achieves state-of-the-art detection performance and exhibits strong robustness against various adversarial attacks and input lengths. Specifically, DNA-DetectLLM achieves relative improvements of 5.55% in AUROC and 2.08% in F1 score across multiple public benchmark datasets. Code and data are available at https://github.com/Xiaoweizhu57/DNA-DetectLLM.

