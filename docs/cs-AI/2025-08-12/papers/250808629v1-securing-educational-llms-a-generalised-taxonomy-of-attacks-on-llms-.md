---
layout: default
title: "Securing Educational LLMs: A Generalised Taxonomy of Attacks on LLMs and DREAD Risk Assessment"
---

# Securing Educational LLMs: A Generalised Taxonomy of Attacks on LLMs and DREAD Risk Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08629" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08629v1</a>
  <a href="https://arxiv.org/pdf/2508.08629.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08629v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08629v1', 'Securing Educational LLMs: A Generalised Taxonomy of Attacks on LLMs and DREAD Risk Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Farzana Zahid, Anjalika Sewwandi, Lee Brandon, Vimal Kumar, Roopak Sinha

**分类**: cs.CY, cs.AI

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出教育领域LLM安全攻击分类与DREAD风险评估方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `教育技术` `安全性评估` `攻击分类` `DREAD框架` `风险管理` `对抗性攻击`

## 📋 核心要点

1. 现有的教育领域LLMs在安全性方面面临严重挑战，缺乏对攻击方式的全面了解。
2. 本文提出了一种通用的攻击分类法，系统性地识别和分类针对LLMs的攻击，帮助评估其风险。
3. 通过DREAD框架的风险评估，识别出对教育LLMs的关键攻击，为安全防护提供了依据。

## 📝 摘要（中文）

随着教育领域对大型语言模型（LLMs）的广泛应用，安全性问题日益突出。本文提出了一种针对LLMs的攻击分类法，涵盖了50种攻击方式，并将其分为针对模型和基础设施的攻击。通过DREAD风险评估框架，评估了这些攻击在教育环境中的严重性，发现令牌走私、对抗性提示、直接注入和多步越狱是对教育LLMs的关键攻击。这一分类法及其在教育环境中的应用将帮助学术和工业界构建更具韧性的解决方案，以保护学习者和教育机构。

## 🔬 方法详解

**问题定义**：本文旨在解决教育领域LLMs的安全性问题，现有方法缺乏对攻击方式的全面分类和评估，导致难以有效防护。

**核心思路**：提出一种通用的攻击分类法，将50种攻击方式系统性地分类，并使用DREAD风险评估框架评估其在教育环境中的影响。

**技术框架**：整体架构包括攻击分类模块和风险评估模块，前者负责识别和分类攻击，后者使用DREAD框架评估攻击的严重性。

**关键创新**：最重要的创新在于提出了针对教育LLMs的攻击通用分类法，填补了现有研究的空白，提供了系统的风险评估方法。

**关键设计**：在分类过程中，考虑了攻击的目标（模型或基础设施）和攻击手段的多样性，确保分类的全面性和准确性。

## 📊 实验亮点

实验结果表明，使用DREAD框架评估后，发现令牌走私、对抗性提示、直接注入和多步越狱是对教育LLMs的四种关键攻击。这些攻击的识别和评估为教育领域的安全防护提供了重要依据。

## 🎯 应用场景

该研究的潜在应用领域包括教育机构、在线学习平台和教育技术公司。通过识别和评估LLMs的安全风险，能够帮助这些组织构建更安全的教学和学习环境，提升教育质量和安全性。

## 📄 摘要（原文）

> Due to perceptions of efficiency and significant productivity gains, various organisations, including in education, are adopting Large Language Models (LLMs) into their workflows. Educator-facing, learner-facing, and institution-facing LLMs, collectively, Educational Large Language Models (eLLMs), complement and enhance the effectiveness of teaching, learning, and academic operations. However, their integration into an educational setting raises significant cybersecurity concerns. A comprehensive landscape of contemporary attacks on LLMs and their impact on the educational environment is missing. This study presents a generalised taxonomy of fifty attacks on LLMs, which are categorized as attacks targeting either models or their infrastructure. The severity of these attacks is evaluated in the educational sector using the DREAD risk assessment framework. Our risk assessment indicates that token smuggling, adversarial prompts, direct injection, and multi-step jailbreak are critical attacks on eLLMs. The proposed taxonomy, its application in the educational environment, and our risk assessment will help academic and industrial practitioners to build resilient solutions that protect learners and institutions.

