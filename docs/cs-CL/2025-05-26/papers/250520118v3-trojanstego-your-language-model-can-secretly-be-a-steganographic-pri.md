---
layout: default
title: TrojanStego: Your Language Model Can Secretly Be A Steganographic Privacy Leaking Agent
---

# TrojanStego: Your Language Model Can Secretly Be A Steganographic Privacy Leaking Agent

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20118" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20118v3</a>
  <a href="https://arxiv.org/pdf/2505.20118.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20118v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20118v3', 'TrojanStego: Your Language Model Can Secretly Be A Steganographic Privacy Leaking Agent')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dominik Meier, Jan Philip Wahle, Paul Röttger, Terry Ruas, Bela Gipp

**分类**: cs.CL, cs.CR

**发布日期**: 2025-05-26 (更新: 2025-09-29)

**备注**: 9 pages, 5 figures To be presented in the Conference on Empirical Methods in Natural Language Processing, 2025

---

## 💡 一句话要点

**提出TrojanStego以解决语言模型隐私泄露问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `隐写术` `信息安全` `数据隐私` `机器学习` `攻击模型` `微调技术`

## 📋 核心要点

1. 现有大型语言模型在敏感应用中存在信息泄露的风险，尤其是在缺乏控制的情况下。
2. TrojanStego通过微调语言模型，利用语言隐写术将敏感信息嵌入自然输出，避免显式控制输入。
3. 实验表明，被攻陷的模型在传输秘密时准确率高达87%，并通过多数投票可提升至97%以上，且保持高效性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在敏感工作流程中的应用，关于其泄露机密信息的潜在风险日益增加。本文提出了TrojanStego，一种新型威胁模型，攻击者通过微调LLM，将敏感上下文信息嵌入自然语言输出中，且无需对推理输入进行显式控制。我们引入了一种分类法，概述了被攻陷LLM的风险因素，并利用该分类法评估威胁的风险特征。实验结果显示，被攻陷的模型在保留高效性的同时，能够以87%的准确率可靠地传输32位秘密，经过三次生成的多数投票后准确率超过97%。这些结果突显了一类新的LLM数据外泄攻击，具有被动、隐蔽、实用和危险的特征。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在敏感工作流程中可能导致的隐私泄露问题。现有方法通常缺乏对输入的控制，容易被攻击者利用。

**核心思路**：TrojanStego的核心思路是通过微调语言模型，使其能够在自然语言输出中嵌入敏感信息，而不需要对输入进行显式控制。这种方法利用了语言隐写术的特性。

**技术框架**：整体架构包括对语言模型的微调过程，采用词汇分区的编码方案，使模型能够学习如何在输出中嵌入秘密信息。主要模块包括数据准备、模型训练和信息提取。

**关键创新**：最重要的技术创新在于提出了一种新的威胁模型和编码方案，使得语言模型能够在不被察觉的情况下传输敏感信息。这与传统的隐写方法有本质区别。

**关键设计**：在参数设置上，模型通过词汇分区进行编码，损失函数设计为优化信息嵌入的准确性。网络结构上，微调的模型能够在多次生成中保持信息的连贯性和隐蔽性。

## 📊 实验亮点

实验结果显示，TrojanStego在传输32位秘密时的准确率达到87%，通过三次生成的多数投票，准确率提升至97%以上。这表明该方法在隐蔽性和有效性方面具有显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括信息安全、数据隐私保护和自然语言处理等。TrojanStego的技术可以用于保护敏感信息在传输过程中的安全性，防止信息泄露，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> As large language models (LLMs) become integrated into sensitive workflows, concerns grow over their potential to leak confidential information. We propose TrojanStego, a novel threat model in which an adversary fine-tunes an LLM to embed sensitive context information into natural-looking outputs via linguistic steganography, without requiring explicit control over inference inputs. We introduce a taxonomy outlining risk factors for compromised LLMs, and use it to evaluate the risk profile of the threat. To implement TrojanStego, we propose a practical encoding scheme based on vocabulary partitioning learnable by LLMs via fine-tuning. Experimental results show that compromised models reliably transmit 32-bit secrets with 87% accuracy on held-out prompts, reaching over 97% accuracy using majority voting across three generations. Further, they maintain high utility, can evade human detection, and preserve coherence. These results highlight a new class of LLM data exfiltration attacks that are passive, covert, practical, and dangerous.

