---
layout: default
title: AprielGuard
---

# AprielGuard

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20293" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20293v1</a>
  <a href="https://arxiv.org/pdf/2512.20293.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20293v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20293v1', 'AprielGuard')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaykumar Kasundra, Anjaneya Praharaj, Sourabh Surana, Lakshmi Sirisha Chodisetty, Sourav Sharma, Abhigya Verma, Abhishek Bhardwaj, Debasish Kanhar, Aakash Bhagat, Khalil Slimi, Seganrasan Subramanian, Sathwik Tejaswi Madhusudhan, Ranga Prasad Chenna, Srinivas Sunkara

**分类**: cs.CL

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出AprielGuard，统一安全风险与对抗威胁，提升LLM安全防护能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型安全` `对抗攻击防御` `安全风险检测` `统一安全框架` `可解释性AI` `LLM安全防护` `多轮对话安全` `代理安全`

## 📋 核心要点

1. 现有LLM安全防护方法将安全风险和对抗威胁视为独立问题，缺乏统一性和鲁棒性。
2. AprielGuard通过统一的分类框架和学习范式，整合安全风险与对抗威胁，提升防护能力。
3. 实验表明，AprielGuard在检测有害内容和对抗攻击方面优于现有开源模型，尤其在复杂场景下。

## 📝 摘要（中文）

随着大型语言模型（LLMs）越来越多地部署在对话和代理环境中，保护它们免受不安全或对抗行为的影响至关重要。现有的审核工具通常将安全风险（如毒性、偏见）和对抗性威胁（如提示注入、越狱）视为独立的问题，限制了它们的鲁棒性和泛化能力。我们介绍了AprielGuard，一个80亿参数的安全防护模型，它在一个统一的分类和学习框架内整合了这些维度。AprielGuard在包含独立提示、多轮对话和代理工作流的各种开放和合成数据上进行训练，并辅以结构化的推理轨迹以提高可解释性。在多个公共和专有基准测试中，AprielGuard在检测有害内容和对抗性操纵方面表现出色，优于现有的开源防护模型，如Llama-Guard和Granite Guardian，尤其是在多步骤和推理密集型场景中。通过发布该模型，我们旨在推进关于LLM可靠安全防护的透明和可复现的研究。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLMs）安全防护方法通常将安全风险（如毒性、偏见）和对抗性威胁（如提示注入、越狱）视为两个独立的问题来处理。这种分离的处理方式导致了防护系统的鲁棒性和泛化能力受限，无法有效地应对复杂和多变的安全挑战。现有的开源防护模型在多步骤推理和复杂对话场景下的表现也存在不足。

**核心思路**：AprielGuard的核心思路是将安全风险和对抗性威胁统一到一个共同的分类和学习框架中。通过这种统一，模型能够更好地理解和识别不同类型的安全问题，并采取相应的防护措施。此外，AprielGuard还利用结构化的推理轨迹来提高模型的可解释性，使其能够更好地解释其决策过程。

**技术框架**：AprielGuard是一个基于Transformer架构的80亿参数模型。其训练流程包括以下几个主要步骤：首先，收集和构建一个包含各种安全风险和对抗性威胁的混合数据集，包括开放数据和合成数据。其次，使用该数据集对模型进行训练，使其能够识别和分类不同类型的安全问题。第三，利用结构化的推理轨迹来增强模型的可解释性。最后，在多个公共和专有基准测试中评估模型的性能。

**关键创新**：AprielGuard最重要的技术创新点在于其统一的安全风险和对抗性威胁处理框架。与现有方法不同，AprielGuard不是将安全风险和对抗性威胁视为独立的问题，而是将它们整合到一个共同的框架中。这种统一的处理方式使得模型能够更好地理解和识别不同类型的安全问题，并采取相应的防护措施。此外，利用结构化的推理轨迹来提高模型的可解释性也是一个重要的创新点。

**关键设计**：AprielGuard的关键设计包括以下几个方面：1) 使用80亿参数的Transformer模型，以获得强大的表示学习能力。2) 构建一个包含各种安全风险和对抗性威胁的混合数据集，以提高模型的泛化能力。3) 利用结构化的推理轨迹来增强模型的可解释性。4) 使用合适的损失函数和优化算法来训练模型，以获得最佳的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20293v1/data_generation.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20293v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20293v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

AprielGuard在多个公共和专有基准测试中表现出色，优于现有的开源防护模型，如Llama-Guard和Granite Guardian。尤其是在多步骤和推理密集型场景中，AprielGuard的性能提升更为显著，表明其在复杂安全挑战面前具有更强的鲁棒性。具体性能数据未在摘要中给出，但强调了其超越现有开源模型的优势。

## 🎯 应用场景

AprielGuard可应用于各种需要安全防护的大型语言模型应用场景，例如聊天机器人、智能助手、内容生成平台等。它可以有效地检测和阻止有害内容和对抗性攻击，保护用户免受不良信息的侵害，并维护平台的安全和稳定。该研究的成果有助于提升LLM在实际应用中的可靠性和安全性，促进LLM技术的健康发展。

## 📄 摘要（原文）

> Safeguarding large language models (LLMs) against unsafe or adversarial behavior is critical as they are increasingly deployed in conversational and agentic settings. Existing moderation tools often treat safety risks (e.g. toxicity, bias) and adversarial threats (e.g. prompt injections, jailbreaks) as separate problems, limiting their robustness and generalizability. We introduce AprielGuard, an 8B parameter safeguard model that unify these dimensions within a single taxonomy and learning framework. AprielGuard is trained on a diverse mix of open and synthetic data covering standalone prompts, multi-turn conversations, and agentic workflows, augmented with structured reasoning traces to improve interpretability. Across multiple public and proprietary benchmarks, AprielGuard achieves strong performance in detecting harmful content and adversarial manipulations, outperforming existing opensource guardrails such as Llama-Guard and Granite Guardian, particularly in multi-step and reasoning intensive scenarios. By releasing the model, we aim to advance transparent and reproducible research on reliable safeguards for LLMs.

