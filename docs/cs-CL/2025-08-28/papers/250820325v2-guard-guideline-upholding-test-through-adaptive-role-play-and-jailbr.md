---
layout: default
title: "GUARD: Guideline Upholding Test through Adaptive Role-play and Jailbreak Diagnostics for LLMs"
---

# GUARD: Guideline Upholding Test through Adaptive Role-play and Jailbreak Diagnostics for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20325" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20325v2</a>
  <a href="https://arxiv.org/pdf/2508.20325.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20325v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20325v2', 'GUARD: Guideline Upholding Test through Adaptive Role-play and Jailbreak Diagnostics for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haibo Jin, Ruoxi Chen, Peiyan Zhang, Andy Zhou, Haohan Wang

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-08-28 (更新: 2025-11-07)

**备注**: 54 pages

---

## 💡 一句话要点

**提出GUARD以解决大型语言模型合规性测试问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `合规性测试` `伦理指南` `越狱诊断` `自动生成问题` `安全性评估` `可信AI` `模型评估`

## 📋 核心要点

1. 现有方法在将伦理指南转化为可操作的测试问题方面存在明显不足，导致大型语言模型的合规性难以验证。
2. GUARD方法通过自动生成违反指南的问题和越狱情境，旨在有效评估大型语言模型的合规性和安全性。
3. 在对七个大型语言模型进行实证验证后，GUARD展示了其在合规性测试和越狱诊断方面的有效性，提升了模型的安全性。

## 📝 摘要（中文）

随着大型语言模型在各领域的广泛应用，其生成有害响应的潜力引发了社会和监管方面的重大关注。为此，政府发布了伦理指南以促进可信AI的发展。然而，这些指南通常是对开发者和测试者的高层次要求，缺乏将其转化为可操作的测试问题以验证大型语言模型合规性的具体方法。为了解决这一挑战，本文提出了GUARD（通过自适应角色扮演和越狱诊断进行指南维护测试），该测试方法旨在将指南转化为具体的违反指南的问题，以评估大型语言模型的遵循情况。GUARD通过自动生成违反指南的问题来测试响应是否符合这些指南，并在响应直接违反指南时报告不一致。此外，GUARD还整合了“越狱”概念，创建情境以激发不道德或违反指南的响应，从而有效识别可能绕过内置安全机制的潜在场景。最后，GUARD生成合规报告，详细说明遵循程度并突出任何违规行为。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在遵循伦理指南方面的合规性测试问题。现有方法缺乏将高层次伦理要求转化为具体可操作的测试问题，导致合规性验证困难。

**核心思路**：GUARD通过自动生成违反指南的问题，结合越狱情境的设计，能够有效评估大型语言模型的合规性和潜在的安全漏洞。这样的设计使得测试过程更加系统化和全面。

**技术框架**：GUARD的整体架构包括两个主要模块：一是自动生成违反指南的问题，二是越狱诊断模块（GUARD-JD），后者通过创建特定情境来诱导模型产生不当响应。

**关键创新**：GUARD的主要创新在于将伦理指南转化为具体的测试问题，并通过越狱情境的设计来识别潜在的安全风险。这一方法与传统的合规性测试方法相比，更加注重实际应用中的安全性评估。

**关键设计**：在实现过程中，GUARD采用了特定的参数设置和生成算法，以确保生成的问题具有代表性和挑战性。同时，越狱情境的设计也考虑了多种可能的模型响应，以全面评估模型的安全性。

## 📊 实验亮点

GUARD在对七个大型语言模型进行测试时，成功识别了多种违反伦理指南的响应，并在越狱诊断中发现了潜在的安全漏洞。实验结果表明，GUARD能够显著提高合规性测试的有效性，确保模型在实际应用中的安全性。

## 🎯 应用场景

GUARD的研究成果具有广泛的应用潜力，尤其在大型语言模型的合规性测试和安全性评估领域。其方法可以被应用于政府、企业和研究机构，以确保AI系统的安全性和伦理性，促进可信AI的实际应用。未来，GUARD的框架可能扩展到其他类型的模型和应用场景，进一步推动AI技术的健康发展。

## 📄 摘要（原文）

> As Large Language Models become increasingly integral to various domains, their potential to generate harmful responses has prompted significant societal and regulatory concerns. In response, governments have issued ethics guidelines to promote the development of trustworthy AI. However, these guidelines are typically high-level demands for developers and testers, leaving a gap in translating them into actionable testing questions to verify LLM compliance.
>   To address this challenge, we introduce GUARD (\textbf{G}uideline \textbf{U}pholding Test through \textbf{A}daptive \textbf{R}ole-play and Jailbreak \textbf{D}iagnostics), a testing method designed to operationalize guidelines into specific guideline-violating questions that assess LLM adherence. To implement this, GUARD uses automated generation of guideline-violating questions based on government-issued guidelines, thereby testing whether responses comply with these guidelines. When responses directly violate guidelines, GUARD reports inconsistencies. Furthermore, for responses that do not directly violate guidelines, GUARD integrates the concept of ``jailbreaks'' to diagnostics, named GUARD-JD, which creates scenarios that provoke unethical or guideline-violating responses, effectively identifying potential scenarios that could bypass built-in safety mechanisms. Our method finally culminates in a compliance report, delineating the extent of adherence and highlighting any violations.
>   We have empirically validated the effectiveness of GUARD on seven LLMs, including Vicuna-13B, LongChat-7B, Llama2-7B, Llama-3-8B, GPT-3.5, GPT-4, GPT-4o, and Claude-3.7, by testing compliance under three government-issued guidelines and conducting jailbreak diagnostics. Additionally, GUARD-JD can transfer jailbreak diagnostics to vision-language models, demonstrating its usage in promoting reliable LLM-based applications.

