---
layout: default
title: Localizing Persona Representations in LLMs
---

# Localizing Persona Representations in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24539" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24539v3</a>
  <a href="https://arxiv.org/pdf/2505.24539.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24539v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24539v3', 'Localizing Persona Representations in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Celia Cintas, Miriam Rateike, Erik Miehling, Elizabeth Daly, Skyler Speakman

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-09-08)

**备注**: To appear in the AAAI/ACM Conference on AI, Ethics, and Society (AIES) 2025

---

## 💡 一句话要点

**研究如何在大型语言模型中定位个性化表征**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化表征` `大型语言模型` `伦理观点` `政治意识形态` `模式识别` `降维技术`

## 📋 核心要点

1. 现有大型语言模型在个性化特征的表示上存在不均匀性，难以准确捕捉不同人类特征的编码方式。
2. 本研究通过降维和模式识别方法，分析LLMs中个性化表征的编码层次及其相对关系，揭示其内部结构。
3. 实验结果表明，个性化表征的差异主要集中在解码器的最后三分之一层，且不同伦理和政治观点的表示存在显著差异。

## 📝 摘要（中文）

本研究探讨了个性化特征（包括人类特征、价值观和信念）在大型语言模型（LLMs）表示空间中的编码方式和位置。通过多种降维和模式识别方法，我们识别出在编码这些表征时，模型层之间的显著差异。分析结果显示，在多个预训练的解码器LLMs中，个性化表征的差异主要集中在解码器层的最后三分之一。此外，我们观察到特定伦理观点（如道德虚无主义和功利主义）之间存在重叠激活，而政治意识形态（如保守主义和自由主义）则在更为独特的区域中表现。这些发现有助于深化对LLMs内部信息表示的理解，并为未来在LLM输出中调节特定人类特征提供指导。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型中个性化特征编码的模糊性和不均匀性，现有方法未能有效识别不同特征的表示差异。

**核心思路**：通过多种降维和模式识别技术，识别出模型中个性化表征的编码层，并分析其激活情况，以揭示不同特征之间的关系。

**技术框架**：研究首先使用降维方法识别出重要的模型层，然后在选定层中分析激活，比较不同个性化特征的嵌入空间。

**关键创新**：本研究的创新在于系统性地分析了多个预训练解码器LLMs中个性化特征的表示差异，尤其是在解码器的最后三分之一层，揭示了伦理和政治观点的重叠与区分。

**关键设计**：采用了多种降维技术（如主成分分析）和模式识别方法，重点分析了模型层的激活情况，确保了对个性化特征的准确捕捉。实验中还考虑了不同伦理和政治观点的样本激活情况。

## 📊 实验亮点

实验结果显示，在多个预训练解码器LLMs中，个性化表征的差异主要集中在解码器的最后三分之一层，且伦理观点（如道德虚无主义和功利主义）之间存在重叠激活，而政治意识形态（如保守主义和自由主义）则表现出明显的区域区分。这一发现为理解LLMs的内部信息表示提供了新的视角。

## 🎯 应用场景

该研究的结果可以应用于改善大型语言模型在生成文本时对个性化特征的调节能力，尤其是在需要体现特定人类特征的场景中，如个性化对话系统、情感分析和社会影响评估等领域。未来，研究成果可能推动更具人性化的AI交互设计。

## 📄 摘要（原文）

> We present a study on how and where personas -- defined by distinct sets of human characteristics, values, and beliefs -- are encoded in the representation space of large language models (LLMs). Using a range of dimension reduction and pattern recognition methods, we first identify the model layers that show the greatest divergence in encoding these representations. We then analyze the activations within a selected layer to examine how specific personas are encoded relative to others, including their shared and distinct embedding spaces. We find that, across multiple pre-trained decoder-only LLMs, the analyzed personas show large differences in representation space only within the final third of the decoder layers. We observe overlapping activations for specific ethical perspectives -- such as moral nihilism and utilitarianism -- suggesting a degree of polysemy. In contrast, political ideologies like conservatism and liberalism appear to be represented in more distinct regions. These findings help to improve our understanding of how LLMs internally represent information and can inform future efforts in refining the modulation of specific human traits in LLM outputs. Warning: This paper includes potentially offensive sample statements.

