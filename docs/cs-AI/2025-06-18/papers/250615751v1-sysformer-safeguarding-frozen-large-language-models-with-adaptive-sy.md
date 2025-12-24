---
layout: default
title: "Sysformer: Safeguarding Frozen Large Language Models with Adaptive System Prompts"
---

# Sysformer: Safeguarding Frozen Large Language Models with Adaptive System Prompts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15751" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15751v1</a>
  <a href="https://arxiv.org/pdf/2506.15751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15751v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15751v1', 'Sysformer: Safeguarding Frozen Large Language Models with Adaptive System Prompts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kartik Sharma, Yiqiao Jin, Vineeth Rakesh, Yingtong Dou, Menghai Pan, Mahashweta Das, Srijan Kumar

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出Sysformer以解决大语言模型安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `安全性` `系统提示` `鲁棒性` `适应性学习` `模型训练` `深度学习`

## 📋 核心要点

1. 现有方法在确保大语言模型安全性方面存在不足，常依赖昂贵的微调或次优的启发式技术。
2. 本文提出Sysformer，通过在保持模型参数不变的情况下，适应性地调整系统提示以提高安全性。
3. 实验表明，Sysformer在拒绝有害提示的能力上提升了80%，在遵循安全提示的合规性上提升了90%。

## 📝 摘要（中文）

随着大语言模型（LLMs）在安全关键环境中的应用，确保其响应符合安全标准变得至关重要。研究表明，LLMs常常无法理解安全行为，导致对无害提示的无端拒绝或生成有害内容。现有防御方法通常依赖于昂贵的模型参数微调或使用次优的启发式技术。本文提出了一种新方法，通过学习适应系统提示来保护LLMs。我们提出的Sysformer模型在保持LLM参数不变的情况下，能够根据用户输入调整系统提示，从而显著提高LLMs的鲁棒性。实验结果表明，Sysformer在拒绝有害提示的能力上提升了80%，在遵循安全提示的合规性上提升了90%。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在安全性方面的不足，现有方法往往依赖昂贵的微调或启发式技术，难以有效应对有害提示。

**核心思路**：Sysformer通过在保持LLM参数不变的情况下，学习适应性地调整系统提示，以提高模型对用户输入的响应安全性。

**技术框架**：Sysformer模型的整体架构包括输入嵌入空间中的初始系统提示和经过调整的系统提示，模型在训练过程中关注用户提示，确保对有害提示的拒绝和对安全提示的响应。

**关键创新**：Sysformer的主要创新在于其能够在不改变LLM参数的情况下，通过动态调整系统提示来增强模型的安全性，这与传统的微调方法本质上不同。

**关键设计**：在模型训练中，Sysformer使用特定的损失函数来优化对有害提示的拒绝率，同时确保对安全提示的高合规性，设计了有效的网络结构以实现这一目标。

## 📊 实验亮点

实验结果显示，Sysformer在拒绝有害提示的能力上提升了80%，在遵循安全提示的合规性上提升了90%。此外，Sysformer对复杂的越狱攻击表现出良好的鲁棒性，使得模型在不同攻击策略下的安全性提升达到100%。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融和自动驾驶等安全关键场景，能够有效提升大语言模型在这些领域的安全性和可靠性。未来，Sysformer的设计理念可能激励更多关于可变系统提示的研究，推动大语言模型的安全应用。

## 📄 摘要（原文）

> As large language models (LLMs) are deployed in safety-critical settings, it is essential to ensure that their responses comply with safety standards. Prior research has revealed that LLMs often fail to grasp the notion of safe behaviors, resulting in either unjustified refusals to harmless prompts or the generation of harmful content. While substantial efforts have been made to improve their robustness, existing defenses often rely on costly fine-tuning of model parameters or employ suboptimal heuristic techniques. In this work, we take a novel approach to safeguard LLMs by learning to adapt the system prompts in instruction-tuned LLMs. While LLMs are typically pre-trained to follow a fixed system prompt, we investigate the impact of tailoring the system prompt to each specific user input on the safety of the responses. To this end, we propose $\textbf{Sysformer}$, a trans$\textbf{former}$ model that updates an initial $\textbf{sys}$tem prompt to a more robust system prompt in the LLM input embedding space while attending to the user prompt. While keeping the LLM parameters frozen, the Sysformer is trained to refuse to respond to a set of harmful prompts while responding ideally to a set of safe ones. Through extensive experiments on $5$ LLMs from different families and $2$ recent benchmarks, we demonstrate that Sysformer can significantly enhance the robustness of LLMs, leading to upto $80\%$ gain in the refusal rate on harmful prompts while enhancing the compliance with the safe prompts by upto $90\%$. Results also generalize well to sophisticated jailbreaking attacks, making LLMs upto $100\%$ more robust against different attack strategies. We hope our findings lead to cheaper safeguarding of LLMs and motivate future investigations into designing variable system prompts.

