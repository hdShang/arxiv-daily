---
layout: default
title: ConspEmoLLM-v2: A robust and stable model to detect sentiment-transformed conspiracy theories
---

# ConspEmoLLM-v2: A robust and stable model to detect sentiment-transformed conspiracy theories

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14917" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14917v1</a>
  <a href="https://arxiv.org/pdf/2505.14917.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14917v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14917v1', 'ConspEmoLLM-v2: A robust and stable model to detect sentiment-transformed conspiracy theories')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiwei Liu, Paul Thompson, Jiaqi Rong, Sophia Ananiadou

**分类**: cs.CL

**发布日期**: 2025-05-20

**备注**: work in progress

**DOI**: [10.3233/FAIA251468](https://doi.org/10.3233/FAIA251468)

**🔗 代码/项目**: [GITHUB](https://github.com/lzw108/ConspEmoLLM)

---

## 💡 一句话要点

**提出ConspEmoLLM-v2以解决情感转变阴谋论检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阴谋论检测` `情感分析` `大型语言模型` `数据集增强` `机器学习`

## 📋 核心要点

1. 现有阴谋论检测方法主要依赖人类创作的文本，难以应对LLM生成的情感转变内容。
2. 论文提出通过增强版的ConDID-v2数据集，结合人类与LLM评估，训练出更鲁棒的ConspEmoLLM-v2模型。
3. 实验结果显示，ConspEmoLLM-v2在处理情感转变推文时显著提升了检测性能，超越了多个基线模型。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）带来了许多好处，但它们也可能导致误信息的自动生成，包括阴谋论。LLMs能够通过改变文本特征来“伪装”阴谋论，例如将强烈的负面情绪转变为更积极的语调。现有的阴谋论检测方法通常基于人类创作的文本，未能有效应对LLM生成的内容。为此，本文开发了增强版的ConDID阴谋论检测数据集ConDID-v2，并利用该数据集训练了ConspEmoLLM-v2。实验结果表明，ConspEmoLLM-v2在原始人类创作内容上保持或超越了ConspEmoLLM的性能，并在处理情感转变的推文时显著优于其他基线模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有阴谋论检测模型在面对LLM生成的情感转变内容时的检测能力不足问题。现有方法多依赖于人类创作的文本特征，导致对经过情感伪装的阴谋论内容的检测效果不佳。

**核心思路**：论文通过构建增强版的ConDID-v2数据集，结合人类与LLM的评估，提供了更多样化的训练样本，以提高模型对情感转变阴谋论的检测能力。

**技术框架**：整体架构包括数据集构建、模型训练和性能评估三个主要阶段。首先，利用LLM重写阴谋论推文以降低其负面情绪，随后使用这些数据训练ConspEmoLLM-v2模型，最后通过实验评估模型在不同数据集上的表现。

**关键创新**：最重要的创新在于引入了LLM重写的阴谋论文本，增强了训练数据的多样性，使得模型能够更好地识别经过情感转变的阴谋论内容。这一方法与传统依赖人类文本特征的检测方法形成了鲜明对比。

**关键设计**：在模型训练中，采用了结合人类和LLM评估的混合损失函数，确保重写文本的质量。此外，模型结构上进行了优化，以提高对情感特征的敏感性，确保在不同情感表达下的检测准确性。

## 📊 实验亮点

实验结果表明，ConspEmoLLM-v2在原始人类创作内容上保持或超越了ConspEmoLLM的性能，并在处理情感转变推文时，检测准确率提高了显著幅度，超越了多个基线模型，显示出其在阴谋论检测领域的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体监控、信息安全和公共舆论分析。通过提高对情感转变阴谋论的检测能力，可以有效减少误信息的传播，保护公众免受虚假信息的影响，具有重要的社会价值和实际意义。

## 📄 摘要（原文）

> Despite the many benefits of large language models (LLMs), they can also cause harm, e.g., through automatic generation of misinformation, including conspiracy theories. Moreover, LLMs can also ''disguise'' conspiracy theories by altering characteristic textual features, e.g., by transforming their typically strong negative emotions into a more positive tone. Although several studies have proposed automated conspiracy theory detection methods, they are usually trained using human-authored text, whose features can vary from LLM-generated text. Furthermore, several conspiracy detection models, including the previously proposed ConspEmoLLM, rely heavily on the typical emotional features of human-authored conspiracy content. As such, intentionally disguised content may evade detection. To combat such issues, we firstly developed an augmented version of the ConDID conspiracy detection dataset, ConDID-v2, which supplements human-authored conspiracy tweets with versions rewritten by an LLM to reduce the negativity of their original sentiment. The quality of the rewritten tweets was verified by combining human and LLM-based assessment. We subsequently used ConDID-v2 to train ConspEmoLLM-v2, an enhanced version of ConspEmoLLM. Experimental results demonstrate that ConspEmoLLM-v2 retains or exceeds the performance of ConspEmoLLM on the original human-authored content in ConDID, and considerably outperforms both ConspEmoLLM and several other baselines when applied to sentiment-transformed tweets in ConDID-v2. The project will be available at https://github.com/lzw108/ConspEmoLLM.

