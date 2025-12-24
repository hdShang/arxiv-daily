---
layout: default
title: "Context Misleads LLMs: The Role of Context Filtering in Maintaining Safe Alignment of LLMs"
---

# Context Misleads LLMs: The Role of Context Filtering in Maintaining Safe Alignment of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10031" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10031v1</a>
  <a href="https://arxiv.org/pdf/2508.10031.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10031v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10031v1', 'Context Misleads LLMs: The Role of Context Filtering in Maintaining Safe Alignment of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinhwa Kim, Ian G. Harris

**分类**: cs.CR, cs.AI, cs.CL

**发布日期**: 2025-08-09

**备注**: 13 pages, 2 figures

---

## 💡 一句话要点

**提出上下文过滤模型以解决大型语言模型的安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `上下文过滤` `安全性` `越狱攻击` `输入预处理` `用户意图识别` `深度学习`

## 📋 核心要点

1. 现有大型语言模型在安全性上面临越狱攻击的挑战，恶意上下文可能导致模型生成有害内容。
2. 论文提出的上下文过滤模型通过预处理输入，过滤不可信的上下文，识别真实用户意图，从而提高模型的安全性。
3. 实验结果显示，该模型在防御越狱攻击时，攻击成功率降低了88%，同时保持了模型的原始性能，展现出卓越的安全性和实用性。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在性能上取得了显著进展，但各种越狱攻击带来了日益严重的安全和伦理风险。恶意用户常常利用对抗性上下文来欺骗LLMs，使其生成对有害查询的响应。本研究提出了一种新的防御机制——上下文过滤模型，这是一种输入预处理方法，旨在过滤掉不可信和不可靠的上下文，同时识别包含真实用户意图的主要提示，以揭示隐藏的恶意意图。我们的模型在防御越狱攻击方面表现出色，能够将攻击成功率降低多达88%，同时保持LLMs的原始性能。该模型为即插即用，适用于所有LLMs，包括白盒和黑盒模型，增强其安全性而无需对模型进行微调。我们将公开该模型以供研究使用。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在面对恶意上下文时的安全性问题。现有方法往往无法有效识别和过滤这些不可信的上下文，导致模型生成有害内容。

**核心思路**：论文提出的上下文过滤模型通过对输入进行预处理，过滤掉不可靠的上下文信息，确保模型能够专注于真实的用户意图，从而降低被欺骗的风险。

**技术框架**：该模型的整体架构包括输入预处理模块、上下文过滤模块和用户意图识别模块。输入预处理模块负责接收用户输入并进行初步处理，过滤模块则根据设定的标准筛选上下文，最后用户意图识别模块提取主要提示。

**关键创新**：该模型的最大创新在于其即插即用的特性，能够适用于所有大型语言模型，无论是白盒还是黑盒模型，且无需对模型进行微调。这一设计使得安全性提升变得更加灵活和高效。

**关键设计**：模型在上下文过滤过程中采用了特定的参数设置和损失函数，以确保过滤的准确性和效率。网络结构方面，模型结合了多种深度学习技术，以增强其对上下文的理解和处理能力。

## 📊 实验亮点

实验结果表明，上下文过滤模型在防御越狱攻击方面表现优异，攻击成功率降低了高达88%。与现有最先进的防御机制相比，该模型在安全性和有用性方面均取得了显著提升，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体、在线客服和内容生成等场景，能够有效提升大型语言模型在实际应用中的安全性，减少恶意内容生成的风险。未来，该模型的广泛应用可能会推动更安全的人工智能系统的开发，增强用户信任。

## 📄 摘要（原文）

> While Large Language Models (LLMs) have shown significant advancements in performance, various jailbreak attacks have posed growing safety and ethical risks. Malicious users often exploit adversarial context to deceive LLMs, prompting them to generate responses to harmful queries. In this study, we propose a new defense mechanism called Context Filtering model, an input pre-processing method designed to filter out untrustworthy and unreliable context while identifying the primary prompts containing the real user intent to uncover concealed malicious intent. Given that enhancing the safety of LLMs often compromises their helpfulness, potentially affecting the experience of benign users, our method aims to improve the safety of the LLMs while preserving their original performance. We evaluate the effectiveness of our model in defending against jailbreak attacks through comparative analysis, comparing our approach with state-of-the-art defense mechanisms against six different attacks and assessing the helpfulness of LLMs under these defenses. Our model demonstrates its ability to reduce the Attack Success Rates of jailbreak attacks by up to 88% while maintaining the original LLMs' performance, achieving state-of-the-art Safety and Helpfulness Product results. Notably, our model is a plug-and-play method that can be applied to all LLMs, including both white-box and black-box models, to enhance their safety without requiring any fine-tuning of the models themselves. We will make our model publicly available for research purposes.

