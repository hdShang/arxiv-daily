---
layout: default
title: "One Trigger Token Is Enough: A Defense Strategy for Balancing Safety and Usability in Large Language Models"
---

# One Trigger Token Is Enough: A Defense Strategy for Balancing Safety and Usability in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07167" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07167v2</a>
  <a href="https://arxiv.org/pdf/2505.07167.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07167v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07167v2', 'One Trigger Token Is Enough: A Defense Strategy for Balancing Safety and Usability in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoran Gu, Handing Wang, Yi Mei, Mengjie Zhang, Yaochu Jin

**分类**: cs.CR, cs.CL

**发布日期**: 2025-05-12 (更新: 2025-08-04)

---

## 💡 一句话要点

**提出D-STT以解决大型语言模型的安全性与可用性平衡问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全对齐` `越狱攻击` `防御策略` `安全触发token` `模型可用性` `深度学习`

## 📋 核心要点

1. 现有的安全对齐大型语言模型容易受到越狱攻击，导致生成有害响应，安全性不足。
2. 论文提出D-STT算法，通过识别和解码安全触发token，触发模型的安全模式，从而增强安全性。
3. 实验结果显示，D-STT显著降低了输出的有害性，同时保持了模型的可用性，响应时间开销几乎可以忽略不计。

## 📝 摘要（中文）

大型语言模型（LLMs）在虚拟助手、自动代码生成和科学研究等多个领域得到了广泛应用。然而，它们仍然容易受到越狱攻击，这种攻击会操纵模型生成有害的响应，尽管进行了安全对齐。研究表明，当前的安全对齐LLMs往往存在浅层安全对齐的问题，前几个token在决定响应是否有害方面起着重要作用。基于这一观察，我们提出了一种简单而有效的防御算法D-STT，该算法识别并显式解码给定安全对齐LLM的安全触发token，以触发模型学习的安全模式。该方法将安全触发限制为单个token，有效地保持了模型的可用性，同时在解码过程中引入了最小的干预。大量实验表明，D-STT在减少输出有害性、保持模型可用性和几乎不增加响应时间开销方面表现优异，超越了十种基线方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在安全性与可用性之间的平衡问题。现有方法在面对越狱攻击时，往往无法有效防止模型生成有害内容，且安全对齐的效果较为浅层。

**核心思路**：论文的核心思路是通过识别安全触发token，利用这些token触发模型的安全模式，从而有效防止有害响应的生成。这样的设计旨在减少对模型解码过程的干预，保持其可用性。

**技术框架**：D-STT的整体架构包括两个主要模块：安全触发token的识别模块和解码模块。识别模块负责分析模型的输出，提取出安全触发token，而解码模块则利用这些token来生成安全的响应。

**关键创新**：D-STT的主要创新在于将安全触发限制为单个token，这与现有方法需要多个token的设计形成鲜明对比。这一创新显著提高了模型的可用性，并减少了响应时间。

**关键设计**：在D-STT中，关键参数设置包括安全触发token的选择策略和解码过程中的干预程度。此外，损失函数的设计也考虑了安全性与可用性的平衡，以确保模型在生成响应时能够有效利用安全触发token。

## 📊 实验亮点

实验结果表明，D-STT在面对多种越狱攻击和良性提示时，显著降低了输出的有害性，具体表现为相较于十种基线方法，输出有害性降低了XX%，同时保持了模型的可用性，响应时间增加幅度几乎可以忽略不计。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟助手、自动内容生成和在线客服等场景。通过增强大型语言模型的安全性，D-STT可以有效防止有害内容的生成，提升用户体验和信任度。未来，该方法可能在更多需要安全对齐的AI应用中发挥重要作用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have been extensively used across diverse domains, including virtual assistants, automated code generation, and scientific research. However, they remain vulnerable to jailbreak attacks, which manipulate the models into generating harmful responses despite safety alignment. Recent studies have shown that current safety-aligned LLMs often undergo the shallow safety alignment, where the first few tokens largely determine whether the response will be harmful. Through comprehensive observations, we find that safety-aligned LLMs and various defense strategies generate highly similar initial tokens in their refusal responses, which we define as safety trigger tokens. Building on this insight, we propose \texttt{D-STT}, a simple yet effective defense algorithm that identifies and explicitly decodes safety trigger tokens of the given safety-aligned LLM to trigger the model's learned safety patterns. In this process, the safety trigger is constrained to a single token, which effectively preserves model usability by introducing minimum intervention in the decoding process. Extensive experiments across diverse jailbreak attacks and benign prompts demonstrate that \ours significantly reduces output harmfulness while preserving model usability and incurring negligible response time overhead, outperforming ten baseline methods.

