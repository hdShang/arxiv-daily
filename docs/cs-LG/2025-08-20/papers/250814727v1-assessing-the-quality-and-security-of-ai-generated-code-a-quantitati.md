---
layout: default
title: "Assessing the Quality and Security of AI-Generated Code: A Quantitative Analysis"
---

# Assessing the Quality and Security of AI-Generated Code: A Quantitative Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14727" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14727v1</a>
  <a href="https://arxiv.org/pdf/2508.14727.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14727v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14727v1', 'Assessing the Quality and Security of AI-Generated Code: A Quantitative Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abbas Sabra, Olivier Schmitt, Joseph Tyler

**分类**: cs.SE, cs.LG

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**量化评估AI生成代码的质量与安全性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI生成代码` `代码质量评估` `安全漏洞检测` `静态分析` `大型语言模型` `软件开发` `SonarQube`

## 📋 核心要点

1. 现有的LLM生成代码虽然功能性强，但在质量和安全性上存在显著缺陷，亟需评估与改进。
2. 本研究通过静态分析工具SonarQube对LLM生成的代码进行全面评估，揭示其潜在的安全隐患与质量问题。
3. 研究结果显示，所有评估模型存在共同的弱点，强调了静态分析在软件开发中的重要性与必要性。

## 📝 摘要（中文）

本研究对五种主要的大型语言模型（LLMs）生成的代码质量和安全性进行了量化评估，包括Claude Sonnet 4、Claude 3.7 Sonnet、GPT-4o、Llama 3.2 90B和OpenCoder 8B。尽管先前研究评估了LLM生成代码的功能性能，但本研究通过SonarQube对4,442个Java编码作业的输出进行了全面的静态分析。结果表明，LLM虽然能够生成功能性代码，但也引入了多种软件缺陷，包括错误、安全漏洞和代码异味。这些缺陷并非孤立存在，而是可能源于当前LLM代码生成方法的系统性局限性。研究发现，功能性能（通过单元测试的Pass@1率衡量）与生成代码的整体质量和安全性（通过SonarQube问题数量衡量）之间没有直接相关性，表明功能基准性能得分并不是整体代码质量和安全性的良好指标。

## 🔬 方法详解

**问题定义**：本研究旨在解决LLM生成代码的质量与安全性评估问题，现有方法未能充分揭示代码中的潜在缺陷与安全漏洞。

**核心思路**：通过对LLM生成的代码进行静态分析，识别和量化代码中的缺陷，强调功能性能与代码质量之间的脱节。

**技术框架**：研究使用SonarQube对4,442个Java编码作业进行静态分析，评估生成代码的质量和安全性，主要模块包括代码缺陷检测和安全漏洞识别。

**关键创新**：本研究的创新在于系统性地评估LLM生成代码的质量与安全性，揭示了功能性能与代码质量之间的无关性，强调了静态分析的重要性。

**关键设计**：采用SonarQube作为静态分析工具，设置了多种代码质量指标，关注安全漏洞（如硬编码密码和路径遍历漏洞）及代码异味的检测。

## 📊 实验亮点

实验结果显示，尽管LLM生成的代码在功能性上表现良好，但在SonarQube分析中发现了多种缺陷，尤其是安全漏洞，如硬编码密码和路径遍历问题。这些发现强调了功能性能与代码质量之间的脱节，表明LLM生成的代码在生产环境中需要经过严格的验证。

## 🎯 应用场景

该研究的结果对软件开发领域具有重要的实际价值，尤其是在使用AI生成代码的场景中。通过识别和修复潜在的安全漏洞，企业可以提高软件的安全性和可靠性，降低风险。此外，静态分析工具的应用可以成为开发流程中的标准实践，促进代码质量的提升。

## 📄 摘要（原文）

> This study presents a quantitative evaluation of the code quality and security of five prominent Large Language Models (LLMs): Claude Sonnet 4, Claude 3.7 Sonnet, GPT-4o, Llama 3.2 90B, and OpenCoder 8B. While prior research has assessed the functional performance of LLM-generated code, this research tested LLM output from 4,442 Java coding assignments through comprehensive static analysis using SonarQube. The findings suggest that although LLMs can generate functional code, they also introduce a range of software defects, including bugs, security vulnerabilities, and code smells. These defects do not appear to be isolated; rather, they may represent shared weaknesses stemming from systemic limitations within current LLM code generation methods. In particular, critically severe issues, such as hard-coded passwords and path traversal vulnerabilities, were observed across multiple models. These results indicate that LLM-generated code requires verification in order to be considered production-ready. This study found no direct correlation between a model's functional performance (measured by Pass@1 rate of unit tests) and the overall quality and security of its generated code, measured by the number of SonarQube issues in benchmark solutions that passed the functional tests. This suggests that functional benchmark performance score is not a good indicator of overall code quality and security. The goal of this study is not to rank LLM performance but to highlight that all evaluated models appear to share certain weaknesses. Consequently, these findings support the view that static analysis can be a valuable instrument for detecting latent defects and an important safeguard for organizations that deploy AI in software development.

