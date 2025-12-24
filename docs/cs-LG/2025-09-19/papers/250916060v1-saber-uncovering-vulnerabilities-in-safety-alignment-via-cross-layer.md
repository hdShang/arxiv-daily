---
layout: default
title: "SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection"
---

# SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16060" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16060v1</a>
  <a href="https://arxiv.org/pdf/2509.16060.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16060v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16060v1', 'SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maithili Joshi, Palash Nandi, Tanmoy Chakraborty

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-19

**备注**: Accepted in EMNLP'25 Main

**🔗 代码/项目**: [GITHUB](https://github.com/PalGitts/SABER)

---

## 💡 一句话要点

**SABER：通过跨层残差连接揭示安全对齐大语言模型的脆弱性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全对齐` `越狱攻击` `残差连接` `白盒攻击`

## 📋 核心要点

1. 大型语言模型虽然经过安全对齐训练，但仍存在被恶意用户利用的越狱攻击风险，使其产生有害输出。
2. SABER方法的核心思想是利用LLM中安全机制主要存在于中后层的特性，通过跨层残差连接绕过安全对齐。
3. 实验结果表明，SABER方法在HarmBench测试集上比最佳基线提高了51%的攻击成功率，且对模型困惑度的影响很小。

## 📝 摘要（中文）

具有安全对齐训练的大型语言模型（LLMs）是强大的工具，具有强大的语言理解能力。这些模型通常经过细致的对齐程序，涉及人工反馈，以确保接受安全输入，同时拒绝有害或不安全的输入。然而，尽管它们规模庞大且进行了对齐工作，但LLMs仍然容易受到越狱攻击，恶意用户会操纵模型以产生其明确训练要避免的有害输出。在这项研究中，我们发现LLMs中的安全机制主要嵌入在中层到后层。基于这一见解，我们引入了一种新颖的白盒越狱方法SABER（通过额外残差的安全对齐绕过），该方法通过残差连接连接两个中间层$s$和$e$，使得$s < e$。我们的方法在HarmBench测试集上实现了比最佳基线高51%的改进。此外，在HarmBench验证集上评估时，SABER仅引起了困惑度的边际变化。源代码可在https://github.com/PalGitts/SABER上公开获得。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）的安全对齐漏洞问题。尽管LLMs经过了严格的安全对齐训练，但仍然容易受到越狱攻击，攻击者可以诱导模型生成有害或不安全的输出。现有方法难以有效绕过LLMs的安全机制，并且可能对模型的性能产生较大影响。

**核心思路**：SABER的核心思路是利用LLMs的安全机制主要嵌入在中层到后层的特性，通过在两个中间层之间建立残差连接来绕过这些安全机制。通过这种方式，攻击者可以更容易地操纵模型的输出，使其产生有害内容。

**技术框架**：SABER方法的技术框架主要包括以下几个步骤：1) 选择两个中间层$s$和$e$，其中$s < e$；2) 在这两个层之间建立残差连接，将层$s$的输出添加到层$e$的输入中；3) 使用修改后的模型生成输出，并评估其是否成功绕过了安全对齐。

**关键创新**：SABER的关键创新在于它是一种白盒越狱方法，利用了LLMs内部结构的特性，特别是安全机制在不同层之间的分布。与传统的黑盒攻击方法相比，SABER可以更有效地绕过安全对齐，并且对模型的性能影响较小。

**关键设计**：SABER的关键设计包括选择合适的中间层$s$和$e$。论文中可能探讨了不同层组合对攻击效果的影响。此外，残差连接的权重可能也需要进行调整，以平衡攻击成功率和模型性能。具体的损失函数和网络结构细节可能与原始LLM保持一致，SABER主要是在现有模型的基础上添加额外的残差连接。

## 📊 实验亮点

SABER方法在HarmBench测试集上取得了显著的成果，相较于最佳基线，攻击成功率提高了51%。同时，SABER对模型的困惑度影响很小，表明其在绕过安全对齐的同时，对模型的语言生成能力影响有限。这一结果表明SABER是一种有效且高效的白盒越狱方法。

## 🎯 应用场景

SABER的研究成果可以应用于评估和改进大型语言模型的安全性。通过识别和修复LLMs中的安全漏洞，可以提高其在各种应用场景中的可靠性和安全性，例如智能客服、内容生成和决策支持等。此外，该研究还可以促进对LLMs内部机制的理解，为开发更安全、更可靠的人工智能系统提供指导。

## 📄 摘要（原文）

> Large Language Models (LLMs) with safe-alignment training are powerful instruments with robust language comprehension capabilities. These models typically undergo meticulous alignment procedures involving human feedback to ensure the acceptance of safe inputs while rejecting harmful or unsafe ones. However, despite their massive scale and alignment efforts, LLMs remain vulnerable to jailbreak attacks, where malicious users manipulate the model to produce harmful outputs that it was explicitly trained to avoid. In this study, we find that the safety mechanisms in LLMs are predominantly embedded in the middle-to-late layers. Building on this insight, we introduce a novel white-box jailbreak method, SABER (Safety Alignment Bypass via Extra Residuals), which connects two intermediate layers $s$ and $e$ such that $s < e$, through a residual connection. Our approach achieves a 51% improvement over the best-performing baseline on the HarmBench test set. Furthermore, SABER induces only a marginal shift in perplexity when evaluated on the HarmBench validation set. The source code is publicly available at https://github.com/PalGitts/SABER.

