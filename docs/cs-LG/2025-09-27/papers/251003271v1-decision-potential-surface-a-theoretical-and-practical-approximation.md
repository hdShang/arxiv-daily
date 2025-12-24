---
layout: default
title: "Decision Potential Surface: A Theoretical and Practical Approximation of LLM's Decision Boundary"
---

# Decision Potential Surface: A Theoretical and Practical Approximation of LLM's Decision Boundary

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03271" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03271v1</a>
  <a href="https://arxiv.org/pdf/2510.03271.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03271v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03271v1', 'Decision Potential Surface: A Theoretical and Practical Approximation of LLM\'s Decision Boundary')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zi Liang, Zhiyao Wu, Haoyang Shang, Yulin Jin, Qingqing Ye, Huadi Zheng, Peizhao Hu, Haibo Hu

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-27

**备注**: Source code: https://github.com/liangzid/DPS

---

## 💡 一句话要点

**提出决策势面(DPS)以近似大语言模型(LLM)的决策边界**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `决策边界` `决策势面` `模型分析` `可解释性` `安全性` `近似算法`

## 📋 核心要点

1. 现有方法难以在大规模LLM中构建决策边界，因为计算量巨大且LLM具有自回归特性。
2. 论文提出决策势面(DPS)的概念，通过分析不同采样序列的置信度来捕捉决策边界的潜力。
3. 论文提出K-DPS算法，通过有限次采样近似LLM的决策边界，并从理论上证明了误差界限。

## 📝 摘要（中文）

决策边界是机器学习模型中一个关键概念，它代表了模型对不同类别赋予相同分类概率的输入子空间，对于揭示模型的核心属性和解释其行为至关重要。虽然分析大型语言模型（LLM）的决策边界近年来受到越来越多的关注，但由于LLM巨大的词汇序列规模和自回归特性，为主流LLM构建决策边界在计算上仍然是不可行的。为了解决这个问题，本文提出了一种新的分析LLM决策边界的概念——决策势面（Decision Potential Surface, DPS）。DPS定义在区分每个输入的各种采样序列的置信度上，自然地捕捉了决策边界的潜力。我们证明了DPS中的零高度等值面等价于LLM的决策边界，封闭区域代表决策区域。通过利用DPS，我们在文献中首次提出了一种近似决策边界构建算法，即K-DPS，它只需要K次有限的序列采样，就可以用可忽略的误差来近似LLM的决策边界。我们从理论上推导了K-DPS与理想DPS之间的绝对误差、期望误差和误差集中度的上界，证明了这些误差可以通过采样次数进行权衡。我们的结果通过各种LLM和语料库的广泛实验得到了经验验证。

## 🔬 方法详解

**问题定义**：现有方法难以有效地分析和构建大型语言模型（LLM）的决策边界。由于LLM的词汇量巨大，序列长度很长，以及自回归的特性，直接计算其决策边界在计算上是不可行的。这限制了我们对LLM行为的理解和解释，阻碍了模型改进和安全部署。

**核心思路**：论文的核心思路是引入“决策势面”（Decision Potential Surface, DPS）的概念，它基于模型对不同采样序列的置信度来定义。DPS能够捕捉决策边界的潜力，并且可以通过有限次采样进行近似。通过分析DPS，可以间接推断LLM的决策边界，从而避免直接计算的复杂性。这种方法利用了LLM生成序列的概率分布，将决策边界的分析转化为对概率势能的分析。

**技术框架**：该方法主要包含以下几个阶段：
1. **定义决策势面 (DPS)**：对于给定的输入，计算LLM生成不同序列的置信度，并基于这些置信度定义DPS。
2. **K-DPS算法**：通过K次有限的序列采样，近似计算DPS。采样策略旨在覆盖可能的决策区域。
3. **决策边界推断**：通过找到DPS的零高度等值面，推断LLM的决策边界。封闭区域代表不同的决策区域。
4. **误差分析**：从理论上分析K-DPS与理想DPS之间的误差，并推导出误差上界。

**关键创新**：该论文的关键创新在于提出了决策势面（DPS）的概念，并将其与LLM的决策边界联系起来。与直接计算决策边界不同，DPS提供了一种基于采样和置信度的近似方法，大大降低了计算复杂度。此外，论文还提供了理论上的误差分析，保证了近似的精度。

**关键设计**：K-DPS算法的关键设计包括：
1. **采样策略**：如何选择K个采样序列，以尽可能覆盖决策区域，影响着近似的精度。
2. **置信度计算**：如何准确计算LLM对每个采样序列的置信度，需要考虑LLM的自回归特性。
3. **误差界限**：理论误差界限的推导，依赖于对LLM概率分布的假设和分析。

## 📊 实验亮点

论文提出了K-DPS算法，通过有限次采样近似LLM的决策边界，并在理论上推导了K-DPS与理想DPS之间的绝对误差、期望误差和误差集中度的上界。实验结果表明，K-DPS能够以可忽略的误差近似LLM的决策边界，并且误差可以通过采样次数进行权衡。该方法在各种LLM和语料库上进行了验证。

## 🎯 应用场景

该研究成果可应用于LLM的安全性和可靠性评估。通过近似LLM的决策边界，可以更好地理解模型的行为，发现潜在的漏洞和偏见。此外，该方法还可以用于提高LLM的可解释性，帮助用户理解模型做出决策的原因。未来，该技术有望应用于对抗攻击防御、模型校准和公平性评估等领域。

## 📄 摘要（原文）

> Decision boundary, the subspace of inputs where a machine learning model assigns equal classification probabilities to two classes, is pivotal in revealing core model properties and interpreting behaviors. While analyzing the decision boundary of large language models (LLMs) has raised increasing attention recently, constructing it for mainstream LLMs remains computationally infeasible due to the enormous vocabulary-sequence sizes and the auto-regressive nature of LLMs. To address this issue, in this paper we propose Decision Potential Surface (DPS), a new notion for analyzing LLM decision boundary. DPS is defined on the confidences in distinguishing different sampling sequences for each input, which naturally captures the potential of decision boundary. We prove that the zero-height isohypse in DPS is equivalent to the decision boundary of an LLM, with enclosed regions representing decision regions. By leveraging DPS, for the first time in the literature, we propose an approximate decision boundary construction algorithm, namely $K$-DPS, which only requires K-finite times of sequence sampling to approximate an LLM's decision boundary with negligible error. We theoretically derive the upper bounds for the absolute error, expected error, and the error concentration between K-DPS and the ideal DPS, demonstrating that such errors can be trade-off with sampling times. Our results are empirically validated by extensive experiments across various LLMs and corpora.

