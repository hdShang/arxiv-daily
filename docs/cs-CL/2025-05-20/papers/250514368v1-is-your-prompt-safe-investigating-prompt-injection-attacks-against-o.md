---
layout: default
title: Is Your Prompt Safe? Investigating Prompt Injection Attacks Against Open-Source LLMs
---

# Is Your Prompt Safe? Investigating Prompt Injection Attacks Against Open-Source LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14368" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14368v1</a>
  <a href="https://arxiv.org/pdf/2505.14368.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14368v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14368v1', 'Is Your Prompt Safe? Investigating Prompt Injection Attacks Against Open-Source LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiawen Wang, Pritha Gupta, Ivan Habernal, Eyke Hüllermeier

**分类**: cs.CR, cs.CL

**发布日期**: 2025-05-20

**备注**: 8 pages, 3 figures, EMNLP 2025 under review

---

## 💡 一句话要点

**提出有效的提示注入攻击以评估开源LLM的安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `提示注入攻击` `大型语言模型` `安全性评估` `攻击成功概率` `开源模型`

## 📋 核心要点

1. 现有研究对开源LLM的提示注入攻击关注不足，导致其安全性评估不全面。
2. 提出了一种新的攻击成功概率（ASP）指标，能够更好地捕捉模型响应的不确定性。
3. 实验结果显示，催眠攻击和忽略前缀攻击在多个开源LLM上均表现出高效的攻击成功率。

## 📝 摘要（中文）

近期研究表明，大型语言模型（LLMs）易受不同的基于提示的攻击，可能生成有害内容或敏感信息。本文研究了针对14种流行开源LLM的有效提示注入攻击，提出了一种新的攻击成功概率（ASP）指标，能够反映模型响应的不确定性。通过全面分析提示注入攻击的有效性，提出了一种简单有效的催眠攻击，结果显示该攻击使得多个对齐的语言模型生成不当行为，ASP达到约90%。此外，忽略前缀攻击能够突破所有14种开源LLM，在多类别数据集上实现超过60%的ASP，发现中等知名度的LLM对提示注入攻击的脆弱性更高，强调了公众意识提升和有效缓解策略的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决开源大型语言模型（LLMs）在提示注入攻击下的脆弱性，现有方法仅关注攻击成功率，未考虑模型响应的不确定性。

**核心思路**：提出攻击成功概率（ASP）作为新的评估指标，能够反映攻击的可行性和模型的响应模糊性，同时设计催眠攻击和忽略前缀攻击以提高攻击效果。

**技术框架**：研究通过五个攻击基准对14种开源LLM进行评估，主要模块包括攻击设计、模型响应分析和成功率计算。

**关键创新**：引入ASP指标，综合考虑攻击成功率和模型响应的不确定性，提供更全面的安全评估。催眠攻击和忽略前缀攻击是本文的主要创新，能够有效突破多种开源LLM的防御。

**关键设计**：在实验中，催眠攻击实现了约90%的ASP，而忽略前缀攻击在多类别数据集上超过60%的ASP，显示出对不同模型的广泛适用性。

## 📊 实验亮点

实验结果表明，催眠攻击在多个对齐的语言模型上实现了约90%的攻击成功概率，而忽略前缀攻击在所有14种开源LLM上均突破了60%的成功率，显示出显著的攻击效果和广泛的适用性。

## 🎯 应用场景

该研究的潜在应用领域包括安全性评估、模型防御机制设计以及开源LLM的安全性提升。通过识别和缓解提示注入攻击，能够增强模型在实际应用中的可靠性，保护用户数据和隐私。

## 📄 摘要（原文）

> Recent studies demonstrate that Large Language Models (LLMs) are vulnerable to different prompt-based attacks, generating harmful content or sensitive information. Both closed-source and open-source LLMs are underinvestigated for these attacks. This paper studies effective prompt injection attacks against the $\mathbf{14}$ most popular open-source LLMs on five attack benchmarks. Current metrics only consider successful attacks, whereas our proposed Attack Success Probability (ASP) also captures uncertainty in the model's response, reflecting ambiguity in attack feasibility. By comprehensively analyzing the effectiveness of prompt injection attacks, we propose a simple and effective hypnotism attack; results show that this attack causes aligned language models, including Stablelm2, Mistral, Openchat, and Vicuna, to generate objectionable behaviors, achieving around $90$% ASP. They also indicate that our ignore prefix attacks can break all $\mathbf{14}$ open-source LLMs, achieving over $60$% ASP on a multi-categorical dataset. We find that moderately well-known LLMs exhibit higher vulnerability to prompt injection attacks, highlighting the need to raise public awareness and prioritize efficient mitigation strategies.

