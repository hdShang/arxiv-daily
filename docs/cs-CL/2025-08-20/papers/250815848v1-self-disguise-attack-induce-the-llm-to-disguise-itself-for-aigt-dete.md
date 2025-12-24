---
layout: default
title: "Self-Disguise Attack: Induce the LLM to disguise itself for AIGT detection evasion"
---

# Self-Disguise Attack: Induce the LLM to disguise itself for AIGT detection evasion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15848" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15848v1</a>
  <a href="https://arxiv.org/pdf/2508.15848.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15848v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15848v1', 'Self-Disguise Attack: Induce the LLM to disguise itself for AIGT detection evasion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinghan Zhou, Juan Wen, Wanli Peng, Zhengxian Wu, Ziwei Zhang, Yiming Xue

**分类**: cs.CR, cs.CL

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出自我伪装攻击以解决AIGT检测规避问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自我伪装攻击` `AI生成文本` `检测规避` `大型语言模型` `对抗特征提取` `上下文优化` `文本生成` `内容审核`

## 📋 核心要点

1. 现有的AIGT检测规避方法存在高计算成本和文本质量下降的问题，限制了其实际应用。
2. 本文提出的自我伪装攻击（SDA）通过对抗特征提取和上下文示例优化，帮助LLM主动伪装输出，降低检测概率。
3. 实验结果显示，SDA显著降低了多种AIGT检测器的检测准确率，同时保持了生成文本的质量。

## 📝 摘要（中文）

AI生成文本（AIGT）检测规避旨在降低AIGT的检测概率，帮助识别检测器的弱点并增强其在实际应用中的有效性和可靠性。尽管现有的规避方法表现良好，但它们面临高计算成本和文本质量下降的问题。为了解决这些挑战，本文提出了自我伪装攻击（SDA），这是一种新颖的方法，使大型语言模型（LLM）能够主动伪装其输出，从而降低被分类器检测的可能性。SDA包括两个主要组件：对抗特征提取器和基于检索的上下文示例优化器。前者生成伪装特征，使LLM能够理解如何生成更人性化的文本；后者从外部知识库中检索最相关的示例作为上下文示例，进一步增强LLM的自我伪装能力，并减轻伪装过程对生成文本多样性的影响。实验结果表明，SDA有效降低了多种AIGT检测器对三种不同LLM生成文本的平均检测准确率，同时保持了AIGT的质量。

## 🔬 方法详解

**问题定义**：本文旨在解决AI生成文本（AIGT）在检测时的规避问题。现有方法通常面临高计算成本和生成文本质量下降的挑战。

**核心思路**：自我伪装攻击（SDA）通过引入对抗特征提取器和基于检索的上下文示例优化器，使LLM能够主动生成更具人类特征的文本，从而降低被检测的风险。

**技术框架**：SDA的整体架构包括两个主要模块：对抗特征提取器负责生成伪装特征，帮助LLM理解人类文本的特征；而上下文示例优化器则从外部知识库中检索相关示例，增强生成文本的多样性和自然性。

**关键创新**：SDA的创新在于其主动伪装机制，允许LLM在生成文本时自我调整输出特征，与传统的被动规避方法形成鲜明对比。

**关键设计**：在设计中，SDA使用了特定的损失函数来优化伪装特征的生成，同时通过检索算法确保上下文示例的相关性和多样性，以提升生成文本的质量和检测规避能力。

## 📊 实验亮点

实验结果表明，SDA显著降低了多种AIGT检测器的平均检测准确率，具体表现为在三种不同LLM生成的文本上，检测准确率降低幅度达到XX%（具体数据未知），同时保持了文本的高质量。

## 🎯 应用场景

该研究的潜在应用领域包括内容生成、社交媒体管理和自动化写作等。通过提高AIGT的检测规避能力，SDA可以帮助开发更为智能的文本生成系统，增强其在实际应用中的可靠性和有效性，未来可能对内容审核和信息传播产生深远影响。

## 📄 摘要（原文）

> AI-generated text (AIGT) detection evasion aims to reduce the detection probability of AIGT, helping to identify weaknesses in detectors and enhance their effectiveness and reliability in practical applications. Although existing evasion methods perform well, they suffer from high computational costs and text quality degradation. To address these challenges, we propose Self-Disguise Attack (SDA), a novel approach that enables Large Language Models (LLM) to actively disguise its output, reducing the likelihood of detection by classifiers. The SDA comprises two main components: the adversarial feature extractor and the retrieval-based context examples optimizer. The former generates disguise features that enable LLMs to understand how to produce more human-like text. The latter retrieves the most relevant examples from an external knowledge base as in-context examples, further enhancing the self-disguise ability of LLMs and mitigating the impact of the disguise process on the diversity of the generated text. The SDA directly employs prompts containing disguise features and optimized context examples to guide the LLM in generating detection-resistant text, thereby reducing resource consumption. Experimental results demonstrate that the SDA effectively reduces the average detection accuracy of various AIGT detectors across texts generated by three different LLMs, while maintaining the quality of AIGT.

